"""Models for SmartThings API."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime  # noqa: TC003
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
    RELATIVE_HUMIDITY_MEASUREMENT = "relativeHumidityMeasurement"
    SWITCH = "switch"
    SWITCH_LEVEL = "switchLevel"
    TEMPERATURE_MEASUREMENT = "temperatureMeasurement"
    THERMOSTAT_MODE = "thermostatMode"
    WINDOW_SHADE = "windowShade"


class Attribute(StrEnum):
    """Attribute model."""

    BATTERY = "battery"
    CHECK_INTERVAL = "checkInterval"
    CIRCADIAN = "circadian"
    COLOR = "color"
    COLOR_TEMPERATURE_RANGE = "colorTemperatureRange"
    COLOR_TEMPERATURE = "colorTemperature"
    DEVICE_WATCH_ENROLL = "DeviceWatch-Enroll"
    DEVICE_WATCH_DEVICE_STATUS = "DeviceWatch-DeviceStatus"
    FADE = "fade"
    HEALTH_STATUS = "healthStatus"
    HUE = "hue"
    HUMIDITY = "humidity"
    LEVEL = "level"
    LEVEL_RANGE = "levelRange"
    MODE = "mode"
    MOTION = "motion"
    QUANTITY = "quantity"
    SATURATION = "saturation"
    SUPPORTED_THERMOSTAT_MODES = "supportedThermostatModes"
    SUPPORTED_WINDOW_SHADE_COMMANDS = "supportedWindowShadeCommands"
    SWITCH = "switch"
    TEMPERATURE = "temperature"
    TEMPERATURE_RANGE = "temperatureRange"
    THERMOSTAT_MODE = "thermostatMode"
    TYPE = "type"
    WINDOW_SHADE = "windowShade"


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
class Scene(DataClassORJSONMixin):
    """Scene model."""

    scene_id: str = field(metadata=field_options(alias="sceneId"))
    name: str = field(metadata=field_options(alias="sceneName"))
    location_id: str = field(metadata=field_options(alias="locationId"))


@dataclass
class Status(DataClassORJSONMixin):
    """Status model."""

    value: str | int | dict[str, Any] | None
    unit: str | None = None
    data: dict[str, Any] | None = None
    timestamp: datetime | None = None


@dataclass
class DeviceStatus(DataClassORJSONMixin):
    """Device status model."""

    components: dict[str, dict[Capability, dict[Attribute, Status]]]


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


@dataclass
class SceneResponse(DataClassORJSONMixin):
    """Scene response model."""

    items: list[Scene]
