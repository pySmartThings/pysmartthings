"""Models for SmartThings API."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin


class Capability(StrEnum):
    """Capability model."""

    BATTERY = "battery"
    CIRCADIAN_LIGHTING_EFFECT = "synthetic.lightingEffectCircadian"
    COLOR_CONTROL = "colorControl"
    COLOR_TEMPERATURE = "colorTemperature"
    FADE_LIGHTNING_EFFECT = "synthetic.lightingEffectFade"
    HEALTH_CHECK = "healthCheck"
    HUE_SYNC_MODE = "samsungim.hueSyncMode"
    MOTION_SENSOR = "motionSensor"
    REFRESH = "refresh"
    SWITCH = "switch"
    SWITCH_LEVEL = "switchLevel"


@dataclass
class BaseLocation(DataClassORJSONMixin):
    """Base location model."""

    location_id: str = field(metadata=field_options(alias="locationId"))
    name: str


@dataclass
class Location(BaseLocation):
    """Location model."""

    country_code: str = field(metadata=field_options(alias="countryCode"))
    latitude: float
    longitude: float
    region_radius: int = field(metadata=field_options(alias="regionRadius"))
    temperature_scale: str = field(metadata=field_options(alias="temperatureScale"))


@dataclass
class Room(DataClassORJSONMixin):
    """Room model."""

    room_id: str = field(metadata=field_options(alias="roomId"))
    location_id: str = field(metadata=field_options(alias="locationId"))
    name: str


class DeviceType(StrEnum):
    """Device type."""

    BLE = "BLE"
    BLE_D2D = "BLE_D2D"
    DTH = "DTH"
    ENDPOINT_APP = "ENDPOINT_APP"
    GROUP = "GROUP"
    HUB = "HUB"
    IR = "IR"
    IR_OCF = "IR_OCF"
    LAN = "LAN"
    MATTER = "MATTER"
    MOBILE = "MOBILE"
    MQTT = "MQTT"
    OCF = "OCF"
    PENGYOU = "PENGYOU"
    SHP = "SHP"
    VIDEO = "VIDEO"
    VIPER = "VIPER"
    VIRTUAL = "VIRTUAL"
    WATCH = "WATCH"
    ZIGBEE = "ZIGBEE"
    ZWAVE = "ZWAVE"
    EDGE_CHILD = "EDGE_CHILD"


class DeviceNetworkType(StrEnum):
    """Device network type."""

    ZWAVE = "ZWAVE"


@dataclass
class Component(DataClassORJSONMixin):
    """Component model."""

    id: str
    capabilities: list[Capability]
    label: str | None = None

    @classmethod
    def __pre_deserialize__(cls, d: dict[str, Any]) -> dict[str, Any]:
        """Pre deserialize hook."""
        d["capabilities"] = [c["id"] for c in d["capabilities"]]
        return d


@dataclass
class Device(DataClassORJSONMixin):
    """Device model."""

    device_id: str = field(metadata=field_options(alias="deviceId"))
    name: str
    label: str
    location_id: str = field(metadata=field_options(alias="locationId"))
    type: DeviceType
    components: list[Component]
    device_network_type: DeviceNetworkType | None = field(
        metadata=field_options(alias="deviceNetworkType"), default=None
    )
    device_type_id: str | None = field(
        metadata=field_options(alias="deviceTypeId"), default=None
    )
    device_type_name: str | None = field(
        metadata=field_options(alias="deviceTypeName"), default=None
    )
    device_manufacturer_code: str | None = field(
        metadata=field_options(alias="deviceManufacturerCode"), default=None
    )


@dataclass
class LocationResponse(DataClassORJSONMixin):
    """Location response model."""

    items: list[BaseLocation]


@dataclass
class RoomResponse(DataClassORJSONMixin):
    """Room response model."""

    items: list[Room]


@dataclass
class DeviceResponse(DataClassORJSONMixin):
    """Device response model."""

    items: list[Device]
