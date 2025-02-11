"""Define the SmartThings Cloud API."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
import logging
from typing import Any, Self

from aiohttp import ClientSession
from aiohttp.hdrs import METH_DELETE, METH_GET, METH_POST, METH_PUT
from yarl import URL

from .const import API_BASE
from .exceptions import SmartThingsCommandError, SmartThingsConnectionError
from .models import (
    Attribute,
    BaseLocation,
    Capability,
    Command,
    Device,
    DeviceResponse,
    DeviceStatus,
    ErrorResponse,
    Location,
    LocationResponse,
    Room,
    RoomResponse,
    Scene,
    SceneResponse,
    Status,
)

_LOGGER = logging.getLogger(__name__)


@dataclass
class SmartThings:
    """Define a class for interacting with the SmartThings Cloud API."""

    token: str
    request_timeout: int = 10
    _close_session: bool = False
    session: ClientSession | None = None

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

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": f"Bearer {self.token}",
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

    async def execute_device_command(
        self,
        device_id: str,
        capability: Capability,
        command: Command,
        component: str = "main",
        argument: int | str | list | dict | None = None,
    ) -> None:
        """Execute a command on a device."""
        command_payload = {
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

    # async def location(self, location_id: str) -> LocationEntity:
    #     """Retrieve a location with the specified ID."""
    #     entity = await self._service.get_location(location_id)
    #     return LocationEntity(self._service, entity)
    #
    # async def rooms(self, location_id: str) -> list[RoomEntity]:
    #     """Retrieve a list of rooms for a location."""
    #     resp = await self._service.get_rooms(location_id)
    #     return [RoomEntity(self._service, entity) for entity in resp]
    #
    # async def room(self, location_id: str, room_id: str) -> RoomEntity:
    #     """Retrieve a specific room."""
    #     entity = await self._service.get_room(location_id, room_id)
    #     return RoomEntity(self._service, entity)
    #
    # async def create_room(self, room: Room) -> RoomEntity:
    #     """Create a room."""
    #     entity = await self._service.create_room(room.location_id, room.to_data())
    #     return RoomEntity(self._service, entity)
    #
    # async def update_room(self, room: Room) -> RoomEntity:
    #     """Update a room."""
    #     entity = await self._service.update_room(
    #         room.location_id, room.room_id, room.to_data()
    #     )
    #     return RoomEntity(self._service, entity)
    #
    # async def delete_room(self, location_id: str, room_id: str) -> bool:
    #     """Delete a room."""
    #     return await self._service.delete_room(location_id, room_id) == {}
    #
    # async def devices(
    #     self,
    #     *,
    #     location_ids: Sequence[str] | None = None,
    #     capabilities: Sequence[str] | None = None,
    #     device_ids: Sequence[str] | None = None,
    # ) -> list:
    #     """Retrieve SmartThings devices."""
    #     params = []
    #     if location_ids:
    #         params.extend([("locationId", lid) for lid in location_ids])
    #     if capabilities:
    #         params.extend([("capability", cap) for cap in capabilities])
    #     if device_ids:
    #         params.extend([("deviceId", did) for did in device_ids])
    #     resp = await self._service.get_devices(params)
    #     return [DeviceEntity(self._service, entity) for entity in resp]
    #
    # async def device(self, device_id: str) -> DeviceEntity:
    #     """Retrieve a device with the specified ID."""
    #     entity = await self._service.get_device(device_id)
    #     return DeviceEntity(self._service, entity)
    #
    # async def apps(self, *, app_type: str | None = None) -> list[AppEntity]:
    #     """Retrieve list of apps."""
    #     params = []
    #     if app_type:
    #         params.append(("appType", app_type))
    #     resp = await self._service.get_apps(params)
    #     return [AppEntity(self._service, entity) for entity in resp]
    #
    # async def app(self, app_id: str) -> AppEntity:
    #     """Retrieve an app with the specified ID."""
    #     entity = await self._service.get_app(app_id)
    #     return AppEntity(self._service, entity)
    #
    # async def create_app(self, app: App) -> (AppEntity, AppOAuthClient):
    #     """Create a new app."""
    #     entity = await self._service.create_app(app.to_data())
    #     return AppEntity(self._service, entity["app"]), AppOAuthClient(entity)
    #
    # async def delete_app(self, app_id: str) -> bool:
    #     """Delete an app."""
    #     return await self._service.delete_app(app_id) == {}
    #
    # async def app_settings(self, app_id: str) -> AppSettingsEntity:
    #     """Get an app's settings."""
    #     settings = await self._service.get_app_settings(app_id)
    #     return AppSettingsEntity(self._service, app_id, settings)
    #
    # async def update_app_settings(self, data: AppSettings) -> AppSettingsEntity:
    #     """Update an app's settings."""
    #     entity = await self._service.update_app_settings(data.app_id, data.to_data())
    #     return AppSettingsEntity(self._service, data.app_id, entity)
    #
    # async def app_oauth(self, app_id: str) -> AppOAuthEntity:
    #     """Get an app's OAuth settings."""
    #     oauth = await self._service.get_app_oauth(app_id)
    #     return AppOAuthEntity(self._service, app_id, oauth)
    #
    # async def update_app_oauth(self, data: AppOAuth) -> AppOAuthEntity:
    #     """Update an app's OAuth settings without having to retrieve it."""
    #     entity = await self._service.update_app_oauth(data.app_id, data.to_data())
    #     return AppOAuthEntity(self._service, data.app_id, entity)
    #
    # async def generate_app_oauth(self, data: AppOAuth) -> AppOAuthClientEntity:
    #     """Generate a new oauth client id and secret."""
    #     entity = await self._service.generate_app_oauth(data.app_id, data.to_data())
    #     return AppOAuthClientEntity(self._service, data.app_id, entity)
    #
    # async def installed_apps(
    #     self,
    #     *,
    #     location_id: str | None = None,
    #     installed_app_status: InstalledAppStatus | None = None,
    # ) -> list[InstalledAppEntity]:
    #     """Get a list of the installed applications."""
    #     params = []
    #     if location_id:
    #         params.append(("locationId", location_id))
    #     if installed_app_status:
    #         params.append(("installedAppStatus", installed_app_status.value))
    #     resp = await self._service.get_installed_apps(params)
    #     return [InstalledAppEntity(self._service, entity) for entity in resp]
    #
    # async def installed_app(self, installed_app_id: str) -> InstalledAppEntity:
    #     """Get an installedapp with the specified ID."""
    #     entity = await self._service.get_installed_app(installed_app_id)
    #     return InstalledAppEntity(self._service, entity)
    #
    # async def delete_installed_app(self, installed_app_id: str) -> bool:
    #     """Delete an installedapp."""
    #     result = await self._service.delete_installed_app(installed_app_id)
    #     return result == {"count": 1}
    #
    # async def subscriptions(self, installed_app_id: str) -> list[SubscriptionEntity]:
    #     """Get an installedapp's subscriptions."""
    #     resp = await self._service.get_subscriptions(installed_app_id)
    #     return [SubscriptionEntity(self._service, entity) for entity in resp]
    #
    # async def delete_subscriptions(self, installed_app_id: str) -> int:
    #     """Delete an installedapp's subscriptions."""
    #     resp = await self._service.delete_all_subscriptions(installed_app_id)
    #     return resp["count"]
    #
    # async def delete_subscription(
    #     self, installed_app_id: str, subscription_id: str
    # ) -> bool:
    #     """Delete an individual subscription."""
    #     return await self._service.delete_subscription(
    #         installed_app_id, subscription_id
    #     ) == {"count": 1}
    #
    # async def create_subscription(
    #     self, subscription: Subscription
    # ) -> SubscriptionEntity:
    #     """Create a new subscription for an installedapp."""
    #     entity = await self._service.create_subscription(
    #         subscription.installed_app_id, subscription.to_data()
    #     )
    #     return SubscriptionEntity(self._service, entity)
    #
    # async def scenes(self, *, location_id: str | None = None) -> list[SceneEntity]:
    #     """Get a list of scenes and optionally filter by location."""
    #     params = []
    #     if location_id:
    #         params.append(("locationId", location_id))
    #     resp = await self._service.get_scenes(params)
    #     return [SceneEntity(self._service, entity) for entity in resp]
    #
    # async def execute_scene(self, scene_id: str) -> bool:
    #     """Execute the scene with the specified id."""
    #     result = await self._service.execute_scene(scene_id)
    #     return result == {"status": "success"}
    #
    # async def generate_tokens(
    #     self, client_id: str, client_secret: str, refresh_token: str
    # ) -> OAuthToken:
    #     """Generate a new refresh/access token pair."""
    #     result = await self._service.generate_tokens(
    #         client_id, client_secret, refresh_token
    #     )
    #     return OAuthToken(self._service, result)

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
