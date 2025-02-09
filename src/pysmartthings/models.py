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
    COLOR_CONTROL = "colorControl"
    COLOR_TEMPERATURE = "colorTemperature"
    EXECUTE = "execute"
    HEALTH_CHECK = "healthCheck"
    MOTION_SENSOR = "motionSensor"
    OCF = "ocf"
    OVEN_MODE = "ovenMode"
    OVEN_OPERATING_STATE = "ovenOperatingState"
    OVEN_SETPOINT = "ovenSetpoint"
    REFRESH = "refresh"
    RELATIVE_HUMIDITY_MEASUREMENT = "relativeHumidityMeasurement"
    REMOTE_CONTROL_STATUS = "remoteControlStatus"
    SWITCH = "switch"
    SWITCH_LEVEL = "switchLevel"
    TEMPERATURE_MEASUREMENT = "temperatureMeasurement"
    THERMOSTAT_MODE = "thermostatMode"
    WINDOW_SHADE = "windowShade"

    CUSTOM_COOKTOP_OPERATING_STATE = "custom.cooktopOperatingState"
    CUSTOM_DISABLED_CAPABILITIES = "custom.disabledCapabilities"
    CUSTOM_OVEN_CAVITY_STATUS = "custom.ovenCavityStatus"

    SAMSUNG_CE_CUSTOM_RECIPE = "samsungce.customRecipe"
    SAMSUNG_CE_DEVICE_IDENTIFICATION = "samsungce.deviceIdentification"
    SAMSUNG_CE_DOOR_STATE = "samsungce.doorState"
    SAMSUNG_CE_DRIVER_VERSION = "samsungce.driverVersion"
    SAMSUNG_CE_KIDS_LOCK = "samsungce.kidsLock"
    SAMSUNG_CE_KITCHEN_DEVICE_DEFAULTS = "samsungce.kitchenDeviceDefaults"
    SAMSUNG_CE_KITCHEN_DEVICE_IDENTIFICATION = "samsungce.kitchenDeviceIdentification"
    SAMSUNG_CE_KITCHEN_MODE_SPECIFICATION = "samsungce.kitchenModeSpecification"
    SAMSUNG_CE_LAMP = "samsungce.lamp"
    SAMSUNG_CE_MEAT_PROBE = "samsungce.meatProbe"
    SAMSUNG_CE_OVEN_MODE = "samsungce.ovenMode"
    SAMSUNG_CE_OVEN_OPERATING_STATE = "samsungce.ovenOperatingState"
    SAMSUNG_CE_SOFTWARE_UPDATE = "samsungce.softwareUpdate"

    SAMSUNG_IM_HUE_SYNC_MODE = "samsungim.hueSyncMode"

    SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT = "synthetic.lightingEffectCircadian"
    SYNTHETIC_FADE_LIGHTNING_EFFECT = "synthetic.lightingEffectFade"


class Attribute(StrEnum):
    """Attribute model."""

    AVAILABLE_MODULES = "availableModules"
    BATTERY = "battery"
    BINARY_ID = "binaryId"
    BRIGHTNESS_LEVEL = "brightnessLevel"
    CHECK_INTERVAL = "checkInterval"
    CIRCADIAN = "circadian"
    COLOR = "color"
    COLOR_TEMPERATURE = "colorTemperature"
    COLOR_TEMPERATURE_RANGE = "colorTemperatureRange"
    COMPLETION_TIME = "completionTime"
    COOKTOP_OPERATING_STATE = "cooktopOperatingState"
    DATA = "data"
    DATA_MODEL_VERSION = "dmv"
    DEFAULT_OPERATION_TIME = "defaultOperationTime"
    DEFAULT_OVEN_MODE = "defaultOvenMode"
    DEFAULT_OVEN_SETPOINT = "defaultOvenSetpoint"
    DESCRIPTION = "description"
    DEVICE_ID = "di"
    DEVICE_NAME = "n"
    DEVICE_WATCH_DEVICE_STATUS = "DeviceWatch-DeviceStatus"
    DEVICE_WATCH_ENROLL = "DeviceWatch-Enroll"
    DISABLED_CAPABILITIES = "disabledCapabilities"
    DOOR_STATE = "doorState"
    FADE = "fade"
    FIRMWARE_VERSION = "mnfv"
    FUEL = "fuel"
    HARDWARE_VERSION = "mnhw"
    HEALTH_STATUS = "healthStatus"
    HUE = "hue"
    HUMIDITY = "humidity"
    LAST_UPDATED_DATE = "lastUpdatedDate"
    LEVEL = "level"
    LEVEL_RANGE = "levelRange"
    LOCK_STATE = "lockState"
    MACHINE_STATE = "machineState"
    MANUFACTURER_DETAILS_LINK = "mnml"
    MANUFACTURER_NAME = "mnmn"
    MANUFACTURE_DATE = "mndt"
    MICOM_ASSAY_CODE = "micomAssayCode"
    MODE = "mode"
    MODEL_CLASSIFICATION_CODE = "modelClassificationCode"
    MODEL_CODE = "modelCode"
    MODEL_NAME = "modelName"
    MODEL_NUMBER = "mnmo"
    MOTION = "motion"
    NEW_VERSION_AVAILABLE = "newVersionAvailable"
    OPERATING_STATE = "operatingState"
    OPERATION_TIME = "operationTime"
    OS_VERSION = "mnos"
    OTN_D_U_I_D = "otnDUID"
    OVEN_CAVITY_STATUS = "ovenCavityStatus"
    OVEN_JOB_STATE = "ovenJobState"
    OVEN_MODE = "ovenMode"
    OVEN_SETPOINT = "ovenSetpoint"
    OVEN_SETPOINT_RANGE = "ovenSetpointRange"
    PLATFORM_ID = "pi"
    PLATFORM_VERSION = "mnpv"
    PROGRESS = "progress"
    QUANTITY = "quantity"
    REGION_CODE = "regionCode"
    RELEASE_YEAR = "releaseYear"
    REMOTE_CONTROL_ENABLED = "remoteControlEnabled"
    REPRESENTATIVE_COMPONENT = "representativeComponent"
    SATURATION = "saturation"
    SERIAL_NUMBER = "serialNumber"
    SERIAL_NUMBER_EXTRA = "serialNumberExtra"
    SPECIFICATION = "specification"
    SPEC_VERSION = "icv"
    STATUS = "status"
    SUPPORTED_BRIGHTNESS_LEVEL = "supportedBrightnessLevel"
    SUPPORTED_COOKTOP_OPERATING_STATE = "supportedCooktopOperatingState"
    SUPPORTED_MACHINE_STATES = "supportedMachineStates"
    SUPPORTED_OVEN_MODES = "supportedOvenModes"
    SUPPORTED_THERMOSTAT_MODES = "supportedThermostatModes"
    SUPPORTED_WINDOW_SHADE_COMMANDS = "supportedWindowShadeCommands"
    SUPPORT_LINK = "mnsl"
    SWITCH = "switch"
    SYSTEM_TIME = "st"
    TARGET_MODULE = "targetModule"
    TEMPERATURE = "temperature"
    TEMPERATURE_RANGE = "temperatureRange"
    TEMPERATURE_SETPOINT = "temperatureSetpoint"
    THERMOSTAT_MODE = "thermostatMode"
    TYPE = "type"
    VENDOR_ID = "vid"
    VERSION_NUMBER = "versionNumber"
    WINDOW_SHADE = "windowShade"


class Command(StrEnum):
    """Command model."""

    AUTO = "auto"
    CLOSE = "close"
    COOL = "cool"
    EMERGENCY_HEAT = "emergencyHeat"
    HEAT = "heat"
    OPEN = "open"
    ON = "on"
    OFF = "off"
    PAUSE = "pause"
    PING = "ping"
    REFRESH = "refresh"
    SET_COLOR = "setColor"
    SET_COLOR_TEMPERATURE = "setColorTemperature"
    SET_HUE = "setHue"
    SET_LEVEL = "setLevel"
    SET_SATURATION = "setSaturation"
    SET_THERMOSTAT_MODE = "setThermostatMode"


CAPABILITY_ATTRIBUTES: dict[Capability, list[Attribute]] = {
    Capability.BATTERY: [Attribute.BATTERY, Attribute.QUANTITY, Attribute.TYPE],
    Capability.COLOR_CONTROL: [Attribute.COLOR, Attribute.HUE, Attribute.SATURATION],
    Capability.COLOR_TEMPERATURE: [
        Attribute.COLOR_TEMPERATURE,
        Attribute.COLOR_TEMPERATURE_RANGE,
    ],
    Capability.EXECUTE: [Attribute.DATA],
    Capability.HEALTH_CHECK: [
        Attribute.DEVICE_WATCH_ENROLL,
        Attribute.DEVICE_WATCH_DEVICE_STATUS,
        Attribute.CHECK_INTERVAL,
        Attribute.HEALTH_STATUS,
    ],
    Capability.MOTION_SENSOR: [Attribute.MOTION],
    Capability.OCF: [
        Attribute.SYSTEM_TIME,
        Attribute.MANUFACTURE_DATE,
        Attribute.FIRMWARE_VERSION,
        Attribute.HARDWARE_VERSION,
        Attribute.DEVICE_ID,
        Attribute.SUPPORT_LINK,
        Attribute.DATA_MODEL_VERSION,
        Attribute.DEVICE_NAME,
        Attribute.MODEL_NUMBER,
        Attribute.VENDOR_ID,
        Attribute.MANUFACTURER_NAME,
        Attribute.MANUFACTURER_DETAILS_LINK,
        Attribute.OS_VERSION,
        Attribute.PLATFORM_ID,
        Attribute.PLATFORM_VERSION,
        Attribute.SPEC_VERSION,
    ],
    Capability.OVEN_MODE: [
        Attribute.OVEN_MODE,
        Attribute.SUPPORTED_OVEN_MODES,
    ],
    Capability.OVEN_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_MACHINE_STATES,
        Attribute.OVEN_JOB_STATE,
        Attribute.OPERATION_TIME,
    ],
    Capability.OVEN_SETPOINT: [Attribute.OVEN_SETPOINT, Attribute.OVEN_SETPOINT_RANGE],
    Capability.REFRESH: [],
    Capability.RELATIVE_HUMIDITY_MEASUREMENT: [Attribute.HUMIDITY],
    Capability.REMOTE_CONTROL_STATUS: [Attribute.REMOTE_CONTROL_ENABLED],
    Capability.SWITCH: [Attribute.SWITCH],
    Capability.SWITCH_LEVEL: [Attribute.LEVEL, Attribute.LEVEL_RANGE],
    Capability.TEMPERATURE_MEASUREMENT: [
        Attribute.TEMPERATURE,
        Attribute.TEMPERATURE_RANGE,
    ],
    Capability.THERMOSTAT_MODE: [
        Attribute.THERMOSTAT_MODE,
        Attribute.SUPPORTED_THERMOSTAT_MODES,
    ],
    Capability.WINDOW_SHADE: [
        Attribute.WINDOW_SHADE,
        Attribute.SUPPORTED_WINDOW_SHADE_COMMANDS,
    ],
    # Synthetic capabilities
    Capability.SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT: [Attribute.CIRCADIAN],
    Capability.SYNTHETIC_FADE_LIGHTNING_EFFECT: [Attribute.FADE],
    # Samsung IM capabilities
    Capability.SAMSUNG_IM_HUE_SYNC_MODE: [Attribute.MODE],
    # Samsung CE capabilities
    Capability.SAMSUNG_CE_DRIVER_VERSION: [Attribute.VERSION_NUMBER],
    Capability.SAMSUNG_CE_OVEN_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.OPERATING_STATE,
        Attribute.PROGRESS,
        Attribute.OVEN_JOB_STATE,
        Attribute.OPERATION_TIME,
    ],
    Capability.SAMSUNG_CE_KITCHEN_DEVICE_DEFAULTS: [
        Attribute.DEFAULT_OPERATION_TIME,
        Attribute.DEFAULT_OVEN_MODE,
        Attribute.DEFAULT_OVEN_SETPOINT,
    ],
    Capability.SAMSUNG_CE_OVEN_MODE: [
        Attribute.SUPPORTED_OVEN_MODES,
        Attribute.OVEN_MODE,
    ],
    Capability.SAMSUNG_CE_MEAT_PROBE: [
        Attribute.TEMPERATURE_SETPOINT,
        Attribute.TEMPERATURE,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_DOOR_STATE: [Attribute.DOOR_STATE],
    Capability.SAMSUNG_CE_DEVICE_IDENTIFICATION: [
        Attribute.MICOM_ASSAY_CODE,
        Attribute.MODEL_NAME,
        Attribute.SERIAL_NUMBER,
        Attribute.SERIAL_NUMBER_EXTRA,
        Attribute.MODEL_CLASSIFICATION_CODE,
        Attribute.DESCRIPTION,
        Attribute.RELEASE_YEAR,
        Attribute.BINARY_ID,
        Attribute.REGION_CODE,
        Attribute.MODEL_CODE,
        Attribute.FUEL,
        Attribute.REPRESENTATIVE_COMPONENT,
        Attribute.TYPE,
    ],
    Capability.SAMSUNG_CE_KITCHEN_MODE_SPECIFICATION: [Attribute.SPECIFICATION],
    Capability.SAMSUNG_CE_SOFTWARE_UPDATE: [
        Attribute.TARGET_MODULE,
        Attribute.OTN_D_U_I_D,
        Attribute.LAST_UPDATED_DATE,
        Attribute.AVAILABLE_MODULES,
        Attribute.NEW_VERSION_AVAILABLE,
        Attribute.OPERATING_STATE,
        Attribute.PROGRESS,
    ],
    Capability.SAMSUNG_CE_LAMP: [
        Attribute.BRIGHTNESS_LEVEL,
        Attribute.SUPPORTED_BRIGHTNESS_LEVEL,
    ],
    Capability.SAMSUNG_CE_KIDS_LOCK: [Attribute.LOCK_STATE],
    # Custom capabilities
    Capability.CUSTOM_DISABLED_CAPABILITIES: [Attribute.DISABLED_CAPABILITIES],
    Capability.CUSTOM_OVEN_CAVITY_STATUS: [Attribute.OVEN_CAVITY_STATUS],
    Capability.CUSTOM_COOKTOP_OPERATING_STATE: [
        Attribute.COOKTOP_OPERATING_STATE,
        Attribute.SUPPORTED_COOKTOP_OPERATING_STATE,
    ],
}

CAPABILITY_COMMANDS: dict[Capability, list[Command]] = {
    Capability.COLOR_CONTROL: [
        Command.SET_COLOR,
        Command.SET_HUE,
        Command.SET_SATURATION,
    ],
    Capability.COLOR_TEMPERATURE: [Command.SET_COLOR_TEMPERATURE],
    Capability.HEALTH_CHECK: [Command.PING],
    Capability.REFRESH: [Command.REFRESH],
    Capability.SWITCH: [Command.ON, Command.OFF],
    Capability.SWITCH_LEVEL: [Command.SET_LEVEL],
    Capability.THERMOSTAT_MODE: [
        Command.AUTO,
        Command.COOL,
        Command.EMERGENCY_HEAT,
        Command.HEAT,
        Command.OFF,
        Command.SET_THERMOSTAT_MODE,
    ],
    Capability.WINDOW_SHADE: [Command.CLOSE, Command.OPEN, Command.PAUSE],
}


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

    value: str | int | float | dict[str, Any] | None
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
