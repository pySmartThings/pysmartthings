"""Models for SmartThings API."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime  # noqa: TC003
from enum import StrEnum
from typing import Any

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin

from .attribute import Attribute  # noqa: TC001
from .capability import Capability
from .const import LOGGER


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


class Category(StrEnum):
    """Category model."""

    AIR_CONDITIONER = "AirConditioner"
    AIR_PURIFIER = "AirPurifier"
    AIR_QUALITY_DETECTOR = "AirQualityDetector"
    BATTERY = "Battery"
    BED = "Bed"
    BIDET = "Bidet"
    BLIND = "Blind"
    BLU_RAY_PLAYER = "BluRayPlayer"
    BLUETOOTH_CAR_SPEAKER = "BluetoothCarSpeaker"
    BLUETOOTH_TRACKER = "BluetoothTracker"
    BRIDGES = "Bridges"
    BUTTON = "Button"
    CAMERA = "Camera"
    CAR = "Car"
    CHARGER = "Charger"
    CLOTHING_CARE_MACHINE = "ClothingCareMachine"
    COFFEE_MAKER = "CoffeeMaker"
    CONTACT_SENSOR = "ContactSensor"
    COOKTOP = "Cooktop"
    CUBE_REFRIGERATOR = "CubeRefrigerator"
    CURB_POWER_METER = "CurbPowerMeter"
    DEHUMIDIFIER = "Dehumidifier"
    DISHWASHER = "Dishwasher"
    DOOR = "Door"
    DOOR_BELL = "DoorBell"
    DRYER = "Dryer"
    EARBUDS = "Earbuds"
    ELEVATOR = "Elevator"
    FAN = "Fan"
    FEEDER = "Feeder"
    FITNESS_MAT = "FitnessMat"
    FLASHLIGHT = "Flashlight"
    GARAGE_DOOR = "GarageDoor"
    GAS_VALVE = "GasValve"
    GAS_METER = "GasMeter"
    GENERIC_SENSOR = "GenericSensor"
    HEALTH_TRACKER = "HealthTracker"
    HEATED_MATTRESS_PAD = "Heatedmattresspad"
    HOME_THEATER = "HomeTheater"
    HUB = "Hub"
    HUMIDIFIER = "Humidifier"
    HUMIDITY_SENSOR = "HumiditySensor"
    IR_REMOTE = "IrRemote"
    IRRIGATION = "Irrigation"
    KIMCHI_REFRIGERATOR = "KimchiRefrigerator"
    KITCHEN_HOOD = "KitchenHood"
    LEAK_SENSOR = "LeakSensor"
    LIGHT = "Light"
    LIGHT_SENSOR = "LightSensor"
    MICRO_FIBER_FILTER = "MicroFiberFilter"
    MICROWAVE = "Microwave"
    MOBILE = "Mobile"
    MOBILE_PRESENCE = "MobilePresence"
    MOTION_SENSOR = "MotionSensor"
    MULTI_FUNCTIONAL_SENSOR = "MultiFunctionalSensor"
    NETWORK_AUDIO = "NetworkAudio"
    NETWORKING = "Networking"
    OTHER = "Other"
    OVEN = "Oven"
    PRESENCE_SENSOR = "PresenceSensor"
    PRESENCE_SENSOR_2 = "Presence Sensor"
    PRINTER = "Printer"
    PRINTER_MULTI_FUNCTION = "PrinterMultiFunction"
    PROJECTOR = "Projector"
    PUMP = "Pump"
    RAIN_SENSOR = "RainSensor"
    RANGE = "Range"
    RECEIVER = "Receiver"
    REFRIGERATOR = "Refrigerator"
    REMOTE_CONTROLLER = "RemoteController"
    RICE_COOKER = "RiceCooker"
    ROBOT_CLEANER = "RobotCleaner"
    SCALE_TO_MEASURE_MASS_OF_HUMAN_BODY = "ScaleToMeasureMassOfHumanBody"
    SCANNER = "Scanner"
    SECURITY_PANEL = "SecurityPanel"
    SET_TOP = "SetTop"
    SHADE = "Shade"
    SHOES_CARE_MACHINE = "ShoesCareMachine"
    SHOWER = "Shower"
    SIREN = "Siren"
    SMART_LOCK = "SmartLock"
    SMART_MONITOR = "SmartMonitor"
    SMART_PLUG = "SmartPlug"
    SMOKE_DETECTOR = "SmokeDetector"
    SOLAR_PANEL = "SolarPanel"
    SOUND_SENSOR = "SoundSensor"
    SOUND_MACHINE = "SoundMachine"
    SPEAKER = "Speaker"
    STICK_VACUUM_CLEANER = "StickVacuumCleaner"
    STORAGE = "Storage"
    STOVE = "Stove"
    SWITCH = "Switch"
    TELEVISION = "Television"
    TEMP_HUMIDITY_SENSOR = "TempHumiditySensor"
    TEMP_SENSOR = "TempSensor"
    THERMOSTAT = "Thermostat"
    TRACKER = "Tracker"
    UPNP_MEDIA_RENDERER = "UPnPMediaRenderer"
    VENT = "Vent"
    VISION_SENSOR = "VisionSensor"
    VOICE_ASSISTANCE = "VoiceAssistance"
    WASHER = "Washer"
    WATER_FREEZER_DETECTOR = "WaterFreezeDetector"
    WATER_HEATER = "WaterHeater"
    WATER_VALVE = "WaterValve"
    WATER_PURIFIER = "WaterPurifier"
    WEATHER_STATION = "WeatherStation"
    WIFI_ROUTER = "WiFiRouter"
    WINDOW = "Window"
    WINE_CELLAR = "WineCellar"


@dataclass
class Component(DataClassORJSONMixin):
    """Component model."""

    id: str
    capabilities: list[Capability | str]
    manufacturer_category: Category | str
    label: str | None = None
    user_category: Category | str | None = None

    @classmethod
    def __pre_deserialize__(cls, d: dict[str, Any]) -> dict[str, Any]:
        """Pre deserialize hook."""
        d["capabilities"] = [c["id"] for c in d["capabilities"]]
        for cat in d["categories"]:
            if (category := cat["name"]) not in Category:
                LOGGER.error(
                    "Unknown category `%s`. Please raise an issue at https://github.com/pySmartThings/pysmartthings.",
                    category,
                )
            if cat["categoryType"] == "manufacturer":
                d["manufacturer_category"] = category
            else:
                d["user_category"] = category
        return d


@dataclass
class OCF(DataClassORJSONMixin):
    """OCF model."""

    device_type: str = field(metadata=field_options(alias="ocfDeviceType"))
    manufacturer_name: str = field(metadata=field_options(alias="manufacturerName"))
    vendor_id: str = field(metadata=field_options(alias="vendorId"))
    last_signup: str = field(metadata=field_options(alias="lastSignupTime"))
    transfer_candidate: bool = field(metadata=field_options(alias="transferCandidate"))
    additional_auth_code_required: bool = field(
        metadata=field_options(alias="additionalAuthCodeRequired")
    )
    spec_version: str | None = field(
        metadata=field_options(alias="specVersion"), default=None
    )
    spec_version_vertical: str | None = field(
        metadata=field_options(alias="verticalDomainSpecVersion"), default=None
    )
    name: str | None = None
    model_number: str | None = field(
        metadata=field_options(alias="modelNumber"), default=None
    )
    platform_version: str | None = field(
        metadata=field_options(alias="platformVersion"), default=None
    )
    platform_os: str | None = field(
        metadata=field_options(alias="platformOS"), default=None
    )
    hardware_version: str | None = field(
        metadata=field_options(alias="hwVersion"), default=None
    )
    firmware_version: str | None = field(
        metadata=field_options(alias="firmwareVersion"), default=None
    )


@dataclass
class Viper(DataClassORJSONMixin):
    """Viper model."""

    manufacturer_name: str = field(metadata=field_options(alias="manufacturerName"))
    model_name: str = field(metadata=field_options(alias="modelName"))
    hardware_version: str | None = field(
        metadata=field_options(alias="hwVersion"), default=None
    )
    software_version: str | None = field(
        metadata=field_options(alias="swVersion"), default=None
    )


@dataclass
class Hub(DataClassORJSONMixin):
    """Hub model."""

    firmware_version: str = field(metadata=field_options(alias="firmwareVersion"))
    hardware_type: str = field(metadata=field_options(alias="hardwareType"))
    mac_address: str | None = field(metadata=field_options(alias="macAddress"))

    @classmethod
    def __pre_deserialize__(cls, d: dict[str, Any]) -> dict[str, Any]:
        """Pre deserialize hook."""
        return {
            **d,
            "hardwareType": d["hubData"]["hardwareType"],
            "macAddress": d["hubData"].get("macAddress"),
        }


@dataclass
class Device(DataClassORJSONMixin):
    """Device model."""

    device_id: str = field(metadata=field_options(alias="deviceId"))
    name: str
    label: str
    location_id: str = field(metadata=field_options(alias="locationId"))
    type: DeviceType
    components: list[Component]
    parent_device_id: str | None = field(
        metadata=field_options(alias="parentDeviceId"), default=None
    )
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
    room_id: str | None = field(metadata=field_options(alias="roomId"), default=None)
    ocf: OCF | None = None
    viper: Viper | None = None
    hub: Hub | None = None


@dataclass
class Scene(DataClassORJSONMixin):
    """Scene model."""

    scene_id: str = field(metadata=field_options(alias="sceneId"))
    name: str = field(metadata=field_options(alias="sceneName"))
    location_id: str = field(metadata=field_options(alias="locationId"))
    icon: str = field(metadata=field_options(alias="sceneIcon"))
    color: str | None = field(metadata=field_options(alias="sceneColor"), default=None)


@dataclass
class Status(DataClassORJSONMixin):
    """Status model."""

    value: str | int | float | dict[str, Any] | list[Any] | None
    unit: str | None = None
    data: dict[str, Any] | None = None
    timestamp: datetime | None = None


@dataclass
class DeviceStatus(DataClassORJSONMixin):
    """Device status model."""

    components: dict[str, dict[Capability | str, dict[Attribute | str, Status]]]

    @classmethod
    def __post_deserialize__(cls, obj: DeviceStatus) -> DeviceStatus:
        """Make sure we let the user know about unknown capabilities."""
        for component in obj.components.values():
            for capability in component:
                if capability not in Capability:
                    LOGGER.warning(
                        "Unknown capability %s. Please raise an issue at https://github.com/pySmartThings/pysmartthings.",
                        capability,
                    )
        return obj


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


@dataclass
class ErrorResponse(DataClassORJSONMixin):
    """Error response model."""

    request_id: str = field(metadata=field_options(alias="requestId"))
    error: ErrorDetails


@dataclass
class ErrorDetails:
    """Error details model."""

    code: str
    message: str
    details: list[ErrorDetails]
    target: str | None = field(default=None)


@dataclass
class Subscription(DataClassORJSONMixin):
    """Subscription model."""

    subscription_id: str = field(metadata=field_options(alias="subscriptionId"))
    registration_url: str = field(metadata=field_options(alias="registrationUrl"))
    name: str


@dataclass
class DeviceEvent(DataClassORJSONMixin):
    """Device event model."""

    event_id: str = field(metadata=field_options(alias="eventId"))
    location_id: str = field(metadata=field_options(alias="locationId"))
    owner_id: str = field(metadata=field_options(alias="ownerId"))
    device_id: str = field(metadata=field_options(alias="deviceId"))
    component_id: str = field(metadata=field_options(alias="componentId"))
    capability: Capability | str
    attribute: Attribute | str
    value: str | int | float | dict[str, Any] | list[Any] | None
    data: dict[str, Any] | None = None


@dataclass
class Event(DataClassORJSONMixin):
    """Event model."""

    event_time: int = field(metadata=field_options(alias="eventTime"))
    event_type: str = field(metadata=field_options(alias="eventType"))


class Lifecycle(StrEnum):
    """Lifecycle model."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


@dataclass
class DeviceLifecycleEvent(DataClassORJSONMixin):
    """Device lifecycle event model."""

    lifecycle: Lifecycle
    device_id: str = field(metadata=field_options(alias="deviceId"))
    location_id: str = field(metadata=field_options(alias="locationId"))


@dataclass
class DeviceEventRoot(Event):
    """Device event root model."""

    device_event: DeviceEvent = field(metadata=field_options(alias="deviceEvent"))


@dataclass
class DeviceLifecycleEventRoot(Event):
    """Device lifecycle event root model."""

    device_lifecycle_event: DeviceLifecycleEvent = field(
        metadata=field_options(alias="deviceLifecycleEvent")
    )


class EventType(StrEnum):
    """Event type."""

    DEVICE_EVENT = "DEVICE_EVENT"
    DEVICE_LIFECYCLE_EVENT = "DEVICE_LIFECYCLE_EVENT"
