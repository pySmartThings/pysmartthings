"""Define the SmartThings Cloud API."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
import logging
from typing import TYPE_CHECKING, Any, Callable, Self

from aiohttp import ClientSession
from aiohttp.hdrs import METH_DELETE, METH_GET, METH_POST, METH_PUT
from aiosseclient import aiosseclient
from yarl import URL

from .const import API_BASE
from .exceptions import (
    SmartThingsAuthenticationFailedError,
    SmartThingsCommandError,
    SmartThingsConnectionError,
)
from .models import (
    BaseLocation,
    Device,
    DeviceEvent,
    DeviceResponse,
    DeviceStatus,
    ErrorResponse,
    Event,
    EventType,
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

_LOGGER = logging.getLogger(__package__)


@dataclass
class SmartThings:
    """Define a class for interacting with the SmartThings Cloud API."""

    request_timeout: int = 10
    _close_session: bool = False
    _token: str | None = None
    session: ClientSession | None = None
    refresh_token_function: Callable[[], Awaitable[str]] | None = None
    __capability_event_listeners: dict[
        tuple[str, str, Capability],
        list[Callable[[DeviceEvent], None]],
    ] = field(default_factory=dict)

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
            "version": "application/vnd.smartthings+json;v=20250122",
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
        ).joinpath(f"v1/{uri}")

        await self.refresh_token()

        headers = {
            "Accept": "application/json, text/plain, */*",
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

        text = await response.text()

        if response.status == 401:
            msg = "Authentication failed with SmartThings"
            raise SmartThingsAuthenticationFailedError(msg)

        if response.status == 422:
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
        resp = await self._get("locations")
        return LocationResponse.from_json(resp).items

    async def get_location(self, location_id: str) -> Location:
        """Retrieve a location with the specified ID."""
        resp = await self._get(f"locations/{location_id}")
        return Location.from_json(resp)

    async def get_rooms(self, location_id: str) -> list[Room]:
        """Retrieve a list of rooms for a location."""
        resp = await self._get(f"locations/{location_id}/rooms")
        return RoomResponse.from_json(resp).items

    async def get_room(self, location_id: str, room_id: str) -> Room:
        """Retrieve a specific room."""
        resp = await self._get(f"locations/{location_id}/rooms/{room_id}")
        return Room.from_json(resp)

    async def get_devices(
        self,
        *,
        capabilities: list[Capability] | None = None,
        location_ids: list[str] | None = None,
        device_ids: list[str] | None = None,
    ) -> list[Device]:
        """Retrieve SmartThings devices."""
        params = {}
        if capabilities:
            params["capability"] = ",".join(capabilities)
        if location_ids:
            params["locationId"] = ",".join(location_ids)
        if device_ids:
            params["deviceId"] = ",".join(device_ids)
        resp = await self._get("devices", params=params)
        return DeviceResponse.from_json(resp).items

    async def get_device(self, device_id: str) -> Device:
        """Retrieve a device with the specified ID."""
        resp = await self._get(f"devices/{device_id}")
        return Device.from_json(resp)

    async def get_scenes(self, location_id: str | None = None) -> list[Scene]:
        """Retrieve SmartThings scenes."""
        params = {}
        if location_id:
            params["locationId"] = location_id
        resp = await self._get("scenes", params=params)
        return SceneResponse.from_json(resp).items

    async def execute_scene(self, scene_id: str) -> None:
        """Execute the scene with the specified ID."""
        await self._post(f"scenes/{scene_id}/execute")

    async def get_device_status(
        self, device_id: str
    ) -> dict[str, dict[Capability, dict[Attribute, Status]]]:
        """Retrieve the status of a device."""
        resp = await self._get(f"devices/{device_id}/status")
        return DeviceStatus.from_json(resp).components

    async def get_capability(self, capability: Capability | str) -> str:
        """Retrieve the capability schema."""
        return await self._get(f"capabilities/{capability}/1")

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
        _LOGGER.debug("Executing command for device %s: %s", device_id, command_payload)
        response = await self._post(
            f"devices/{device_id}/commands",
            data={"commands": [command_payload]},
        )
        _LOGGER.debug("Command response: %s", response)

    def add_device_event_listener(
        self,
        device_id: str,
        component_id: str,
        capability: Capability,
        callback: Callable[[DeviceEvent], None],
    ) -> Callable[[], None]:
        """Add a listener for device events."""
        key = (device_id, component_id, capability)
        if key not in self.__capability_event_listeners:
            self.__capability_event_listeners[key] = []
        self.__capability_event_listeners[key].append(callback)
        return lambda: self.__capability_event_listeners[key].remove(callback)

    async def _create_subscription(
        self, location_id: str, installed_app_id: str
    ) -> Subscription:
        """Create a subscription."""
        resp = await self._post(
            "subscriptions",
            data={
                "name": "My Home Assistant sub",
                "version": 20250122,
                "clientDeviceId": f"iapp_{installed_app_id}",
                "subscriptionFilters": [
                    {
                        "type": "LOCATIONIDS",
                        "value": [location_id],
                        "eventType": [EventType.DEVICE_EVENT],
                    }
                ],
            },
        )
        return Subscription.from_json(resp)

    async def subscribe(self, location_id: str, installed_app_id: str) -> None:
        """Create a subscription."""
        retry_count = 0
        while True:
            try:
                subscription = await self._create_subscription(
                    location_id, installed_app_id
                )
                _LOGGER.debug("Subscription created: %s", subscription)
                retry_count = 0
                async for event in aiosseclient(
                    subscription.registration_url,
                    headers=self._get_headers(),
                ):
                    if event.event == EventType.DEVICE_EVENT:
                        _LOGGER.debug("Received event: %s", event.data)
                        event_type = Event.from_json(event.data)
                        device_event = event_type.device_event
                        key = (
                            device_event.device_id,
                            device_event.component_id,
                            device_event.capability,
                        )
                        if key in self.__capability_event_listeners:
                            for callback in self.__capability_event_listeners[key]:
                                callback(device_event)
                    else:
                        _LOGGER.debug("Received event: %s", event.data)
            except Exception:  # pylint: disable=broad-except  # noqa: PERF203
                msg = "Error occurred while subscribing to events"
                _LOGGER.exception(msg)
                await asyncio.sleep(2**retry_count)
                retry_count += 1

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
