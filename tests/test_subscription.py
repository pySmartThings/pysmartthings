"""Tests for SmartThings SSE subscriptions."""

from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, MagicMock, patch

from aiohttp import ClientSession
from aiohttp.hdrs import METH_DELETE, METH_GET, METH_POST
from aiointercept import aiointercept
import orjson
import pytest

from pysmartthings import (
    Capability,
    Lifecycle,
    SmartThings,
    SmartThingsBlockedError,
    SmartThingsCommandError,
    SmartThingsRateLimitError,
    SmartThingsServerError,
    SmartThingsSinkError,
    Subscription,
)
from pysmartthings.const import DEFAULT_USER_AGENT

from . import load_fixture, load_json_fixture

from .const import HEADERS, MOCK_URL

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

LOCATION_ID = "88a3a314-f0c8-40b4-bb44-44ba06c9c42e"
SUBSCRIPTION_ID = "f5768ce8-c9e5-4507-9020-912c0c60e0ab"
REGISTRATION_URL = (
    "https://spigot-regional.api.smartthings.com/filters/"
    f"{SUBSCRIPTION_ID}/activate?filterRegion=eu-west-1"
)
SUBSCRIPTIONS_URL = f"{MOCK_URL}/v1/sse/subscriptions"
SUBSCRIPTION_URL = f"{SUBSCRIPTIONS_URL}/{SUBSCRIPTION_ID}"

GOODBYE = "event: CONTROL_EVENT\ndata: goodbye\n\n"


def sse_event(event_type: str, fixture: str) -> str:
    """Build a single-line SSE event from a JSON fixture."""
    data = orjson.dumps(load_json_fixture(fixture)).decode()  # pylint: disable=no-member
    return f"event: {event_type}\ndata: {data}\n\n"


def mock_create_subscription(responses: aiointercept) -> None:
    """Mock a successful subscription creation."""
    responses.post(
        SUBSCRIPTIONS_URL, status=200, body=load_fixture("sse_subscription.json")
    )


def mock_subscription_limit(responses: aiointercept) -> None:
    """Mock subscription creation failing on the limit, which ends subscribe()."""
    responses.post(
        SUBSCRIPTIONS_URL,
        status=422,
        body=load_fixture("sse_subscription_limit_error.json"),
    )


async def test_create_subscription(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test creating a subscription."""
    mock_create_subscription(responses)
    assert await client.create_subscription(LOCATION_ID) == Subscription(
        subscription_id=SUBSCRIPTION_ID,
        registration_url=REGISTRATION_URL,
        name="My Home Assistant sub",
    )
    responses.assert_called_once_with(
        SUBSCRIPTIONS_URL,
        METH_POST,
        headers=HEADERS,
        params=None,
        json={
            "name": "My Home Assistant sub",
            "subscriptionFilters": [
                {
                    "type": "LOCATIONIDS",
                    "value": [LOCATION_ID],
                    "eventType": [
                        "DEVICE_EVENT",
                        "DEVICE_LIFECYCLE_EVENT",
                        "DEVICE_HEALTH_EVENT",
                    ],
                }
            ],
        },
    )


async def test_create_subscription_custom_user_agent(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test a configured user agent is sent instead of the default."""
    mock_create_subscription(responses)
    client.user_agent = "MyIntegration/1.0.0 (contact: dev@example.com)"
    await client.create_subscription(LOCATION_ID)
    responses.assert_called_once_with(
        SUBSCRIPTIONS_URL,
        METH_POST,
        headers={
            **HEADERS,
            "User-Agent": "MyIntegration/1.0.0 (contact: dev@example.com)",
        },
    )


async def test_create_subscription_session_user_agent(
    responses: aiointercept,
) -> None:
    """Test a user agent already set on the session is not overridden."""
    mock_create_subscription(responses)
    async with (
        ClientSession(headers={"User-Agent": "FromSession/1.0"}) as session,
        SmartThings(session=session) as client,
    ):
        client.authenticate("token")
        await client.create_subscription(LOCATION_ID)
    responses.assert_called_once_with(
        SUBSCRIPTIONS_URL,
        METH_POST,
        headers={**HEADERS, "User-Agent": "FromSession/1.0"},
    )


async def test_create_subscription_limit_reached(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test creating a subscription when the limit is reached."""
    mock_subscription_limit(responses)
    with pytest.raises(SmartThingsSinkError, match="Reached limit of subscriptions"):
        await client.create_subscription(LOCATION_ID)


async def test_create_subscription_other_command_error(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test a validation error is not mistaken for the subscription limit."""
    responses.post(
        SUBSCRIPTIONS_URL,
        status=422,
        body=orjson.dumps(  # pylint: disable=no-member
            {
                "requestId": "1",
                "error": {
                    "code": "ConstraintViolationError",
                    "message": "The request is malformed.",
                    "details": [
                        {
                            "code": "PatternError",
                            "target": "subscriptionFilters[0].value",
                            "message": "Invalid location ID",
                            "details": [],
                        }
                    ],
                },
            }
        ).decode(),
    )
    with pytest.raises(SmartThingsCommandError, match="PatternError"):
        await client.create_subscription(LOCATION_ID)


@pytest.mark.parametrize(
    ("status", "exception"),
    [
        (418, SmartThingsBlockedError),
        (429, SmartThingsRateLimitError),
        (500, SmartThingsServerError),
        (503, SmartThingsServerError),
    ],
)
async def test_create_subscription_error_status(
    client: SmartThings,
    responses: aiointercept,
    status: int,
    exception: type[Exception],
) -> None:
    """Test error statuses raise instead of returning the body."""
    responses.post(SUBSCRIPTIONS_URL, status=status)
    with pytest.raises(exception):
        await client.create_subscription(LOCATION_ID)


async def test_delete_subscription(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test deleting a subscription."""
    responses.delete(SUBSCRIPTION_URL, status=200)
    new_subscription_id_callback = MagicMock()
    client.new_subscription_id_callback = new_subscription_id_callback
    await client.delete_subscription(SUBSCRIPTION_ID)
    responses.assert_called_once_with(
        SUBSCRIPTION_URL,
        METH_DELETE,
        headers=HEADERS,
        params=None,
        json=None,
    )
    new_subscription_id_callback.assert_called_once_with(None)


async def test_subscribe_dispatches_events(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test events from the stream reach the matching listeners."""
    # The device event is pretty-printed, so it arrives as multiple data lines
    # that the parser has to join back together.
    multiline_device_event = "event: DEVICE_EVENT\n" + "".join(
        f"data: {line}\n" for line in load_fixture("event.json").splitlines()
    )
    stream = (
        ": keepalive\n\n"
        + multiline_device_event
        + "\n"
        + sse_event("DEVICE_LIFECYCLE_EVENT", "new_device_event.json")
        + sse_event("DEVICE_HEALTH_EVENT", "device_health_event.json")
        + GOODBYE
    )
    mock_create_subscription(responses)
    responses.get(REGISTRATION_URL, status=200, body=stream)
    responses.delete(SUBSCRIPTION_URL, status=200)
    mock_subscription_limit(responses)

    device_id = "440063de-a200-40b5-8a6b-f3399eaa0370"
    unspecified_listener = MagicMock()
    device_listener = MagicMock()
    capability_listener = MagicMock()
    other_capability_listener = MagicMock()
    lifecycle_listener = MagicMock()
    health_listener = MagicMock()
    client.add_unspecified_device_event_listener(unspecified_listener)
    client.add_device_event_listener(device_id, device_listener)
    client.add_device_capability_event_listener(
        device_id, "main", Capability.SWITCH, capability_listener
    )
    client.add_device_capability_event_listener(
        device_id, "main", Capability.SWITCH_LEVEL, other_capability_listener
    )
    client.add_device_lifecycle_event_listener(Lifecycle.CREATE, lifecycle_listener)
    client.add_device_availability_event_listener(
        "7905bc7a-0633-4d80-a95b-45d59f1393a5", health_listener
    )
    new_subscription_id_callback = MagicMock()
    max_connections_reached_callback = MagicMock()
    client.new_subscription_id_callback = new_subscription_id_callback
    client.max_connections_reached_callback = max_connections_reached_callback

    await client.subscribe(LOCATION_ID)

    unspecified_listener.assert_called_once()
    device_event = unspecified_listener.call_args.args[0]
    assert device_event.device_id == device_id
    assert device_event.capability == Capability.SWITCH
    assert device_event.value == "on"
    device_listener.assert_called_once_with(device_event)
    capability_listener.assert_called_once_with(device_event)
    other_capability_listener.assert_not_called()
    lifecycle_listener.assert_called_once_with("46b0958e-4a92-40f3-b531-eb60c5d1aa7a")
    health_listener.assert_called_once()
    assert health_listener.call_args.args[0].status == "ONLINE"

    responses.assert_called_with(
        REGISTRATION_URL,
        METH_GET,
        headers={
            "Authorization": "Bearer token",
            "User-Agent": DEFAULT_USER_AGENT,
            "Accept": "text/event-stream",
        },
    )
    assert [c.args for c in new_subscription_id_callback.call_args_list] == [
        (SUBSCRIPTION_ID,),
        (None,),
    ]
    max_connections_reached_callback.assert_called_once_with()


async def test_subscribe_with_initial_subscription(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test an initial subscription is used instead of creating a new one."""
    responses.get(REGISTRATION_URL, status=200, body=GOODBYE)
    responses.delete(SUBSCRIPTION_URL, status=200)
    mock_subscription_limit(responses)
    new_subscription_id_callback = MagicMock()
    client.new_subscription_id_callback = new_subscription_id_callback
    client.max_connections_reached_callback = MagicMock()

    await client.subscribe(
        LOCATION_ID,
        initial_subscription=Subscription(
            subscription_id=SUBSCRIPTION_ID,
            registration_url=REGISTRATION_URL,
            name="My Home Assistant sub",
        ),
    )

    # Only the delete reports a change; no new subscription ID was announced.
    new_subscription_id_callback.assert_called_once_with(None)
    responses.assert_any_call(SUBSCRIPTION_URL, METH_DELETE)


async def test_subscribe_reconnects_when_server_closes_stream(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test a stream closed without a goodbye still leads to a new subscription."""
    mock_create_subscription(responses)
    responses.get(
        REGISTRATION_URL,
        status=200,
        body=sse_event("DEVICE_EVENT", "event.json"),
    )
    responses.delete(SUBSCRIPTION_URL, status=200)
    mock_subscription_limit(responses)
    listener = MagicMock()
    client.add_unspecified_device_event_listener(listener)
    max_connections_reached_callback = MagicMock()
    client.max_connections_reached_callback = max_connections_reached_callback

    await client.subscribe(LOCATION_ID)

    listener.assert_called_once()
    responses.assert_any_call(SUBSCRIPTION_URL, METH_DELETE)
    max_connections_reached_callback.assert_called_once_with()


async def test_subscribe_reconnects_on_read_timeout(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test a silent, half-open stream is abandoned after the read timeout."""

    async def stalled_stream() -> AsyncIterator[bytes]:
        yield sse_event("DEVICE_EVENT", "event.json").encode()
        # Hold the connection open without sending anything.
        await asyncio.sleep(1)

    mock_create_subscription(responses)
    responses.get(REGISTRATION_URL, status=200, body=stalled_stream())
    responses.delete(SUBSCRIPTION_URL, status=200)
    mock_subscription_limit(responses)
    listener = MagicMock()
    client.add_unspecified_device_event_listener(listener)
    max_connections_reached_callback = MagicMock()
    client.max_connections_reached_callback = max_connections_reached_callback

    with patch("pysmartthings.smartthings.SSE_READ_TIMEOUT", 0.1):
        await client.subscribe(LOCATION_ID)

    listener.assert_called_once()
    responses.assert_any_call(SUBSCRIPTION_URL, METH_DELETE)
    max_connections_reached_callback.assert_called_once_with()


async def test_subscribe_retries_on_connection_error(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test a connection error backs off, cleans up and resubscribes."""
    mock_create_subscription(responses)
    responses.get(REGISTRATION_URL, exception=True)
    responses.delete(SUBSCRIPTION_URL, status=200)
    mock_subscription_limit(responses)
    max_connections_reached_callback = MagicMock()
    client.max_connections_reached_callback = max_connections_reached_callback

    with patch(
        "pysmartthings.smartthings.asyncio.sleep", new_callable=AsyncMock
    ) as mock_sleep:
        await client.subscribe(LOCATION_ID)

    mock_sleep.assert_awaited_once_with(1)
    responses.assert_any_call(SUBSCRIPTION_URL, METH_DELETE)
    max_connections_reached_callback.assert_called_once_with()


async def test_subscribe_retries_on_unexpected_error(
    client: SmartThings,
    responses: aiointercept,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test an unparsable event backs off, cleans up and resubscribes."""
    mock_create_subscription(responses)
    responses.get(
        REGISTRATION_URL,
        status=200,
        body="event: DEVICE_EVENT\ndata: not json\n\n",
    )
    responses.delete(SUBSCRIPTION_URL, status=200)
    mock_subscription_limit(responses)
    max_connections_reached_callback = MagicMock()
    client.max_connections_reached_callback = max_connections_reached_callback

    with (
        caplog.at_level(logging.ERROR),
        patch(
            "pysmartthings.smartthings.asyncio.sleep", new_callable=AsyncMock
        ) as mock_sleep,
    ):
        await client.subscribe(LOCATION_ID)

    assert "Error occurred while subscribing to events" in caplog.text
    mock_sleep.assert_awaited_once_with(1)
    responses.assert_any_call(SUBSCRIPTION_URL, METH_DELETE)
    max_connections_reached_callback.assert_called_once_with()


async def test_subscribe_listener_error_does_not_stop_stream(
    client: SmartThings,
    responses: aiointercept,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test a failing listener is logged and later events are still delivered."""
    mock_create_subscription(responses)
    responses.get(
        REGISTRATION_URL,
        status=200,
        body=sse_event("DEVICE_EVENT", "event.json")
        + sse_event("DEVICE_HEALTH_EVENT", "device_health_event.json")
        + GOODBYE,
    )
    responses.delete(SUBSCRIPTION_URL, status=200)
    mock_subscription_limit(responses)
    client.add_unspecified_device_event_listener(
        MagicMock(side_effect=ValueError("boom"))
    )
    health_listener = MagicMock()
    client.add_device_availability_event_listener(
        "7905bc7a-0633-4d80-a95b-45d59f1393a5", health_listener
    )
    client.max_connections_reached_callback = MagicMock()

    with caplog.at_level(logging.ERROR):
        await client.subscribe(LOCATION_ID)

    assert "Error occurred while processing device event" in caplog.text
    health_listener.assert_called_once()


async def test_removed_listener_is_not_called(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test the callable returned when adding a listener removes it."""
    mock_create_subscription(responses)
    responses.get(
        REGISTRATION_URL,
        status=200,
        body=sse_event("DEVICE_EVENT", "event.json") + GOODBYE,
    )
    responses.delete(SUBSCRIPTION_URL, status=200)
    mock_subscription_limit(responses)
    listener = MagicMock()
    remove_listener = client.add_unspecified_device_event_listener(listener)
    remove_listener()
    client.max_connections_reached_callback = MagicMock()

    await client.subscribe(LOCATION_ID)

    listener.assert_not_called()


async def test_subscribe_limit_without_callback_stops(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test reaching the limit ends subscribe() even without a callback."""
    mock_subscription_limit(responses)
    async with asyncio.timeout(1):
        await client.subscribe(LOCATION_ID)
    responses.assert_called_once_with(SUBSCRIPTIONS_URL, METH_POST)


@pytest.mark.parametrize("status", [403, 404])
async def test_subscribe_expired_initial_subscription(
    client: SmartThings,
    responses: aiointercept,
    status: int,
) -> None:
    """Test an expired initial subscription is dropped and a new one created."""
    responses.get(REGISTRATION_URL, status=403)
    responses.delete(SUBSCRIPTION_URL, status=status)
    mock_subscription_limit(responses)
    new_subscription_id_callback = MagicMock()
    max_connections_reached_callback = MagicMock()
    client.new_subscription_id_callback = new_subscription_id_callback
    client.max_connections_reached_callback = max_connections_reached_callback

    with patch("pysmartthings.smartthings.asyncio.sleep", new_callable=AsyncMock):
        await client.subscribe(
            LOCATION_ID,
            initial_subscription=Subscription(
                subscription_id=SUBSCRIPTION_ID,
                registration_url=REGISTRATION_URL,
                name="My Home Assistant sub",
            ),
        )

    new_subscription_id_callback.assert_called_once_with(None)
    responses.assert_any_call(SUBSCRIPTIONS_URL, METH_POST)
    max_connections_reached_callback.assert_called_once_with()


@pytest.mark.parametrize("status", [403, 404])
async def test_subscribe_subscription_expired_before_delete(
    client: SmartThings,
    responses: aiointercept,
    status: int,
) -> None:
    """Test a goodbye followed by a failed delete still resubscribes."""
    mock_create_subscription(responses)
    responses.get(REGISTRATION_URL, status=200, body=GOODBYE)
    responses.delete(SUBSCRIPTION_URL, status=status)
    mock_subscription_limit(responses)
    new_subscription_id_callback = MagicMock()
    max_connections_reached_callback = MagicMock()
    client.new_subscription_id_callback = new_subscription_id_callback
    client.max_connections_reached_callback = max_connections_reached_callback

    await client.subscribe(LOCATION_ID)

    assert [c.args for c in new_subscription_id_callback.call_args_list] == [
        (SUBSCRIPTION_ID,),
        (None,),
    ]
    max_connections_reached_callback.assert_called_once_with()


async def test_subscribe_blocked_client_raises(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test a client flagged as problematic stops instead of retrying."""
    responses.post(SUBSCRIPTIONS_URL, status=418)
    with pytest.raises(SmartThingsBlockedError):
        await client.subscribe(LOCATION_ID)
    responses.assert_called_once_with(SUBSCRIPTIONS_URL, METH_POST)


async def test_subscribe_create_error_does_not_delete(
    client: SmartThings,
    responses: aiointercept,
) -> None:
    """Test a failed create backs off without deleting a missing subscription."""
    responses.post(SUBSCRIPTIONS_URL, status=429)
    mock_subscription_limit(responses)
    client.max_connections_reached_callback = MagicMock()

    with patch(
        "pysmartthings.smartthings.asyncio.sleep", new_callable=AsyncMock
    ) as mock_sleep:
        await client.subscribe(LOCATION_ID)

    mock_sleep.assert_awaited_once_with(1)
    with pytest.raises(AssertionError):
        responses.assert_any_call(SUBSCRIPTION_URL, METH_DELETE)
