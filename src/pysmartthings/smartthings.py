"""Define the SmartThings Cloud API."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable, Self, cast

from aiohttp import ClientConnectionError, ClientError, ClientSession, ClientTimeout
from aiohttp.hdrs import METH_DELETE, METH_GET, METH_POST, METH_PUT
from aiohttp_sse_client2.client import EventSource
import orjson
from yarl import URL

from .const import API_BASE, API_VERSION, LOGGER
from .exceptions import (
    SmartThingsAuthenticationFailedError,
    SmartThingsCommandError,
    SmartThingsConnectionError,
    SmartThingsForbiddenError,
    SmartThingsSinkError,
)
from .models import (
    BaseLocation,
    Device,
    DeviceEvent,
    DeviceEventRoot,
    DeviceHealth,
    DeviceHealthEvent,
    DeviceHealthEventRoot,
    DeviceLifecycleEventRoot,
    DeviceResponse,
    DeviceStatus,
    ErrorResponse,
    EventType,
    Lifecycle,
    Location,
    LocationResponse,
    Room,
    RoomResponse,
    Scene,
    SceneResponse,
    Status,
    Subscription,
)

if TYPE_CHECKING:
    from collections.abc import Awaitable

    from .attribute import Attribute
    from .capability import Capability
    from .command import Command


@dataclass
class SmartThings:
    """Define a class for interacting with the SmartThings Cloud API."""

    request_timeout: int = 10
    _close_session: bool = False
    _token: str | None = None
    session: ClientSession | None = None
    refresh_token_function: Callable[[], Awaitable[str]] | None = None
    new_subscription_id_callback: Callable[[str | None], None] | None = None
    max_connections_reached_callback: Callable[[], None] | None = None
    __capability_event_listeners: dict[
        tuple[str, str, Capability | str],
        list[Callable[[DeviceEvent], None]],
    ] = field(default_factory=dict)
    __unspecified_device_event_listeners: list[Callable[[DeviceEvent], None]] = field(
        default_factory=list
    )
    __device_event_listeners: dict[str, list[Callable[[DeviceEvent], None]]] = field(
        default_factory=dict
    )
    __device_availability_event_listeners: dict[
        str, list[Callable[[DeviceHealthEvent], None]]
    ] = field(default_factory=dict)
    __device_lifecycle_event_listeners: dict[Lifecycle, list[Callable[[str], None]]] = (
        field(default_factory=dict)
    )
    __retry_count: int = 0

    async def refresh_token(self) -> None:
        """Refresh token with provided function."""
        if self.refresh_token_function:
            self._token = await self.refresh_token_function()

    def authenticate(self, token: str) -> None:
        """Authenticate the user with a token."""
        self._token = token

    def _get_headers(self) -> dict[str, str]:
        """Get headers for requests."""
        return {
            "Authorization": f"Bearer {self._token}",
        }

    async def _request(
        self,
        method: str,
        uri: str,
        *,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> str:
        """Handle a request to SmartThings."""
        url = URL.build(
            scheme="https",
            host=API_BASE,
            port=443,
        ).joinpath(uri)

        await self.refresh_token()

        headers = {
            "Accept": f"application/vnd.smartthings+json;v={API_VERSION}",
            **self._get_headers(),
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        try:
            async with asyncio.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    headers=headers,
                    json=data,
                    params=params,
                )
        except asyncio.TimeoutError as exception:
            msg = "Timeout occurred while connecting to SmartThings"
            raise SmartThingsConnectionError(msg) from exception
        except ClientConnectionError as exception:
            msg = "Error occurred while connecting to SmartThings"
            raise SmartThingsConnectionError(msg) from exception

        text = await response.text()

        if response.status == 401:
            msg = "Authentication failed with SmartThings"
            raise SmartThingsAuthenticationFailedError(msg)

        if response.status == 403:
            msg = "Forbidden"
            raise SmartThingsForbiddenError(msg)

        if response.status in {409, 422}:
            raise SmartThingsCommandError(ErrorResponse.from_json(text))

        return text

    async def _get(self, uri: str, params: dict[str, Any] | None = None) -> str:
        """Handle a GET request to SmartThings."""
        return await self._request(METH_GET, uri, params=params)

    async def _post(
        self,
        uri: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> str:
        """Handle a POST request to SmartThings."""
        return await self._request(METH_POST, uri, data=data, params=params)

    async def _put(
        self,
        uri: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> str:
        """Handle a PUT request to SmartThings."""
        return await self._request(METH_PUT, uri, data=data, params=params)

    async def _delete(
        self,
        uri: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> str:
        """Handle a DELETE request to SmartThings."""
        return await self._request(METH_DELETE, uri, data=data, params=params)

    async def get_locations(self) -> list[BaseLocation]:
        """Retrieve SmartThings locations."""
        resp = await self._get("v1/locations")
        return LocationResponse.from_json(resp).items

    async def get_location(self, location_id: str) -> Location:
        """Retrieve a location with the specified ID."""
        resp = await self._get(f"v1/locations/{location_id}")
        return Location.from_json(resp)

    async def get_rooms(self, location_id: str) -> list[Room]:
        """Retrieve a list of rooms for a location."""
        resp = await self._get(f"v1/locations/{location_id}/rooms")
        return RoomResponse.from_json(resp).items

    async def get_room(self, location_id: str, room_id: str) -> Room:
        """Retrieve a specific room."""
        resp = await self._get(f"v1/locations/{location_id}/rooms/{room_id}")
        return Room.from_json(resp)

    async def _get_devices(
        self,
        *,
        capabilities: list[Capability] | None = None,
        location_ids: list[str] | None = None,
        device_ids: list[str] | None = None,
        max_results: int | None = None,
        page: int | None = None,
    ) -> str:
        """Retrieve SmartThings devices."""
        params: dict[str, Any] = {}
        if capabilities:
            params["capability"] = ",".join(capabilities)
        if location_ids:
            params["locationId"] = ",".join(location_ids)
        if device_ids:
            params["deviceId"] = ",".join(device_ids)
        if max_results:
            params["max"] = max_results
        if page:
            params["page"] = page
        return await self._get("v1/devices", params=params)

    async def get_devices(
        self,
        *,
        capabilities: list[Capability] | None = None,
        location_ids: list[str] | None = None,
        device_ids: list[str] | None = None,
    ) -> list[Device]:
        """Retrieve SmartThings devices."""
        devices = []
        resp = DeviceResponse.from_json(
            await self._get_devices(
                capabilities=capabilities,
                location_ids=location_ids,
                device_ids=device_ids,
            )
        )
        devices.extend(resp.items)
        while resp.next_link:
            url = URL(resp.next_link)
            resp = DeviceResponse.from_json(
                await self._get_devices(
                    capabilities=capabilities,
                    location_ids=location_ids,
                    device_ids=device_ids,
                    max_results=int(url.query["max"]),
                    page=int(url.query["page"]),
                )
            )
            devices.extend(resp.items)
        return devices

    async def get_raw_devices(self) -> list[dict[str, Any]]:
        """Retrieve SmartThings devices."""
        resp = orjson.loads(await self._get_devices())  # pylint: disable=no-member
        response = [resp]
        next_page_url = resp.get("_links", {}).get("next", {}).get("href")
        while next_page_url:
            url = URL(next_page_url)
            resp = orjson.loads(  # pylint: disable=no-member
                await self._get_devices(
                    max_results=int(url.query["max"]), page=int(url.query["page"])
                )
            )
            response.append(resp)
            next_page_url = resp.get("_links", {}).get("next", {}).get("href")
        return response

    async def _get_device(self, device_id: str) -> str:
        """Retrieve a device with the specified ID."""
        return await self._get(f"v1/devices/{device_id}")

    async def get_device(self, device_id: str) -> Device:
        """Retrieve a device with the specified ID."""
        resp = await self._get_device(device_id)
        return Device.from_json(resp)

    async def get_raw_device(self, device_id: str) -> dict[str, Any]:
        """Retrieve a device with the specified ID."""
        return cast("dict[str, Any]", orjson.loads(await self._get_device(device_id)))  # pylint: disable=no-member

    async def get_scenes(self, location_id: str | None = None) -> list[Scene]:
        """Retrieve SmartThings scenes."""
        params = {}
        if location_id:
            params["locationId"] = location_id
        resp = await self._get("v1/scenes", params=params)
        return SceneResponse.from_json(resp).items

    async def get_device_health(self, device_id: str) -> DeviceHealth:
        """Retrieve device health with the specified ID."""
        resp = await self._get(f"v1/devices/{device_id}/health")
        return DeviceHealth.from_json(resp)

    async def execute_scene(self, scene_id: str) -> None:
        """Execute the scene with the specified ID."""
        await self._post(f"v1/scenes/{scene_id}/execute")

    async def _get_device_status(self, device_id: str) -> str:
        """Retrieve the status of a device."""
        return await self._get(f"v1/devices/{device_id}/status")

    async def get_device_status(
        self, device_id: str
    ) -> dict[str, dict[Capability | str, dict[Attribute | str, Status]]]:
        """Retrieve the status of a device."""
        resp = await self._get_device_status(device_id)
        return DeviceStatus.from_json(resp).components

    async def get_raw_device_status(self, device_id: str) -> dict[str, Any]:
        """Retrieve the status of a device."""
        resp = await self._get_device_status(device_id)
        return cast("dict[str, Any]", orjson.loads(resp))  # pylint: disable=no-member

    async def get_capability(self, capability: Capability | str) -> str:
        """Retrieve the capability schema."""
        return await self._get(f"v1/capabilities/{capability}/1")

    async def execute_device_command(
        self,
        device_id: str,
        capability: Capability,
        command: Command,
        component: str = "main",
        argument: int | str | list[Any] | dict[str, Any] | None = None,
    ) -> None:
        """Execute a command on a device."""
        command_payload: dict[str, Any] = {
            "component": component,
            "capability": capability,
            "command": command,
        }
        if argument is not None:
            command_payload["arguments"] = (
                argument if isinstance(argument, list) else [argument]
            )
        LOGGER.debug("Executing command for device %s: %s", device_id, command_payload)
        response = await self._post(
            f"v1/devices/{device_id}/commands",
            data={"commands": [command_payload]},
        )
        LOGGER.debug("Command response: %s", response)

    def add_unspecified_device_event_listener(
        self, callback: Callable[[DeviceEvent], None]
    ) -> Callable[[], None]:
        """Add a listener for unspecified device events."""
        self.__unspecified_device_event_listeners.append(callback)
        return lambda: self.__unspecified_device_event_listeners.remove(callback)

    def add_device_lifecycle_event_listener(
        self, lifecycle_event: Lifecycle, callback: Callable[[str], None]
    ) -> Callable[[], None]:
        """Add a listener for device lifecycle events."""
        if lifecycle_event not in self.__device_lifecycle_event_listeners:
            self.__device_lifecycle_event_listeners[lifecycle_event] = []
        self.__device_lifecycle_event_listeners[lifecycle_event].append(callback)
        return lambda: self.__device_lifecycle_event_listeners[lifecycle_event].remove(
            callback
        )

    def add_device_capability_event_listener(
        self,
        device_id: str,
        component_id: str,
        capability: Capability | str,
        callback: Callable[[DeviceEvent], None],
    ) -> Callable[[], None]:
        """Add a listener for device events."""
        key = (device_id, component_id, capability)
        if key not in self.__capability_event_listeners:
            self.__capability_event_listeners[key] = []
        self.__capability_event_listeners[key].append(callback)
        return lambda: self.__capability_event_listeners[key].remove(callback)

    def add_device_event_listener(
        self, device_id: str, callback: Callable[[DeviceEvent], None]
    ) -> Callable[[], None]:
        """Add a listener for device events."""
        if device_id not in self.__device_event_listeners:
            self.__device_event_listeners[device_id] = []
        self.__device_event_listeners[device_id].append(callback)
        return lambda: self.__device_event_listeners[device_id].remove(callback)

    def add_device_availability_event_listener(
        self, device_id: str, callback: Callable[[DeviceHealthEvent], None]
    ) -> Callable[[], None]:
        """Add a listener for device availability events."""
        if device_id not in self.__device_availability_event_listeners:
            self.__device_availability_event_listeners[device_id] = []
        self.__device_availability_event_listeners[device_id].append(callback)
        return lambda: self.__device_availability_event_listeners[device_id].remove(
            callback
        )

    async def create_subscription(
        self, location_id: str, installed_app_id: str
    ) -> Subscription:
        """Create a subscription."""
        try:
            resp = await self._post(
                "subscriptions",
                data={
                    "name": "My Home Assistant sub",
                    "version": API_VERSION,
                    "clientDeviceId": f"iapp_{installed_app_id}",
                    "subscriptionFilters": [
                        {
                            "type": "LOCATIONIDS",
                            "value": [location_id],
                            "eventType": [
                                EventType.DEVICE_EVENT,
                                EventType.DEVICE_LIFECYCLE_EVENT,
                                EventType.DEVICE_HEALTH_EVENT,
                            ],
                        }
                    ],
                },
            )
        except SmartThingsCommandError as err:
            msg = "Reached limit of subscriptions"
            raise SmartThingsSinkError(msg) from err
        return Subscription.from_json(resp)

    async def _internal_subscribe(self, session: ClientSession, url: str) -> None:  # noqa: PLR0912
        """Subscribe to events."""
        await self.refresh_token()
        async with EventSource(
            url, session=session, headers=self._get_headers(), on_open=self.__on_open
        ) as event_source:
            async for event in event_source:
                LOGGER.debug("Received event: %s", event.data)
                if event.type == EventType.DEVICE_EVENT:
                    event_type = DeviceEventRoot.from_json(event.data)
                    device_event = event_type.device_event
                    try:
                        for callback in self.__unspecified_device_event_listeners:
                            callback(device_event)
                        if device_event.device_id in self.__device_event_listeners:
                            for callback in self.__device_event_listeners[
                                device_event.device_id
                            ]:
                                callback(device_event)
                        key = (
                            device_event.device_id,
                            device_event.component_id,
                            device_event.capability,
                        )
                        if key in self.__capability_event_listeners:
                            for callback in self.__capability_event_listeners[key]:
                                callback(device_event)
                    except Exception:  # pylint: disable=broad-except  # noqa: BLE001
                        LOGGER.exception(
                            "Error occurred while processing device event: %s",
                            device_event,
                        )
                elif event.type == EventType.DEVICE_LIFECYCLE_EVENT:
                    lifecycle_event = DeviceLifecycleEventRoot.from_json(event.data)
                    device_lifecycle_event = lifecycle_event.device_lifecycle_event
                    if (
                        device_lifecycle_event.lifecycle
                        in self.__device_lifecycle_event_listeners
                    ):
                        for dle_callback in self.__device_lifecycle_event_listeners[
                            device_lifecycle_event.lifecycle
                        ]:
                            dle_callback(device_lifecycle_event.device_id)
                elif event.type == EventType.DEVICE_HEALTH_EVENT:
                    device_health_event = DeviceHealthEventRoot.from_json(event.data)
                    if (
                        device_health_event.device_health_event.device_id
                        in self.__device_availability_event_listeners
                    ):
                        for dhe_callback in self.__device_availability_event_listeners[
                            device_health_event.device_health_event.device_id
                        ]:
                            dhe_callback(device_health_event.device_health_event)
                elif event.type == EventType.CONTROL_EVENT:
                    if event.data in {"goodbye", "goobye"}:
                        LOGGER.debug("Received goodbye event, closing connection")
                        break

    def __on_open(self) -> None:
        """Handle the opening of the connection."""
        LOGGER.debug("Connection opened")
        self.__retry_count = 0

    async def subscribe(  # noqa: PLR0915  # pylint: disable=too-many-statements
        self,
        location_id: str,
        installed_app_id: str,
        initial_subscription: Subscription | None = None,
    ) -> None:
        """Create a subscription."""
        self.__retry_count = 0
        using_initial = initial_subscription is not None
        timeout = ClientTimeout(
            total=None, connect=None, sock_connect=None, sock_read=120
        )
        async with ClientSession(timeout=timeout) as session:
            while True:
                try:
                    if using_initial:
                        assert initial_subscription is not None  # noqa: S101
                        LOGGER.debug(
                            "Using initial subscription: %s", initial_subscription
                        )
                        subscription_id = initial_subscription.subscription_id
                        subscription_url = initial_subscription.registration_url
                    else:
                        subscription = await self.create_subscription(
                            location_id, installed_app_id
                        )
                        subscription_id = subscription.subscription_id
                        subscription_url = subscription.registration_url
                        LOGGER.debug("Subscription created: %s", subscription)
                        if self.new_subscription_id_callback:
                            self.new_subscription_id_callback(subscription_id)
                    await self._internal_subscribe(session, subscription_url)
                    using_initial = False
                    await self.delete_subscription(subscription_id)
                except SmartThingsSinkError:  # noqa: PERF203
                    # This is only triggered by creating a new one
                    # So we don't have an active one and thus don't have to delete one
                    if self.max_connections_reached_callback:
                        self.max_connections_reached_callback()
                        break
                except (ClientError, ConnectionError):
                    msg = "Connection error occurred while subscribing to events"
                    LOGGER.exception(msg)
                    await asyncio.sleep(2**self.__retry_count)
                    self.__retry_count += 1
                    try:
                        await self.delete_subscription(subscription_id)
                    except SmartThingsConnectionError:
                        LOGGER.debug("Connection error while deleting subscription")
                        if self.max_connections_reached_callback:
                            self.max_connections_reached_callback()
                    using_initial = False
                except Exception:  # pylint: disable=broad-except  # noqa: BLE001
                    msg = "Error occurred while subscribing to events"
                    LOGGER.exception(msg)
                    await asyncio.sleep(2**self.__retry_count)
                    self.__retry_count += 1
                    try:
                        await self.delete_subscription(subscription_id)
                    except SmartThingsConnectionError:
                        LOGGER.debug("Unknown error while deleting subscription")
                        if self.max_connections_reached_callback:
                            self.max_connections_reached_callback()
                    using_initial = False

    async def delete_subscription(self, subscription_id: str) -> None:
        """Delete a subscription."""
        LOGGER.debug("Deleting subscription: %s", subscription_id)
        await self._delete(f"subscriptions/{subscription_id}")
        if self.new_subscription_id_callback:
            self.new_subscription_id_callback(None)

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> Self:
        """Async enter.

        Returns
        -------
            The SmartThings object.

        """
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.

        """
        await self.close()
