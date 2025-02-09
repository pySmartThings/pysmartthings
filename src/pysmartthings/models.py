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
    DEMAND_RESPONSE_LOAD_CONTROL = "demandResponseLoadControl"
    DISHWASHER_OPERATING_STATE = "dishwasherOperatingState"
    DOOR_CONTROL = "doorControl"
    DRYER_OPERATING_STATE = "dryerOperatingState"
    EXECUTE = "execute"
    HEALTH_CHECK = "healthCheck"
    MOTION_SENSOR = "motionSensor"
    OCF = "ocf"
    OVEN_MODE = "ovenMode"
    OVEN_OPERATING_STATE = "ovenOperatingState"
    OVEN_SETPOINT = "ovenSetpoint"
    POWER_CONSUMPTION_REPORT = "powerConsumptionReport"
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
    CUSTOM_DISHWASHER_DELAY_START_TIME = "custom.dishwasherDelayStartTime"
    CUSTOM_DISHWASHER_OPERATING_PERCENTAGE = "custom.dishwasherOperatingPercentage"
    CUSTOM_DISHWASHER_OPERATING_PROGRESS = "custom.dishwasherOperatingProgress"
    CUSTOM_DRYER_DRY_LEVEL = "custom.dryerDryLevel"
    CUSTOM_DRYER_WRINKLE_PREVENT = "custom.dryerWrinklePrevent"
    CUSTOM_ENERGY_TYPE = "custom.energyType"
    CUSTOM_JOB_BEGINNING_STATUS = "custom.jobBeginningStatus"
    CUSTOM_OVEN_CAVITY_STATUS = "custom.ovenCavityStatus"
    CUSTOM_SUPPORTED_OPTIONS = "custom.supportedOptions"
    CUSTOM_WATER_FILTER = "custom.waterFilter"

    SAMSUNG_CE_CUSTOM_RECIPE = "samsungce.customRecipe"
    SAMSUNG_CE_DEFINED_RECIPE = "samsungce.definedRecipe"
    SAMSUNG_CE_DETERGENT_ORDER = "samsungce.detergentOrder"
    SAMSUNG_CE_DETERGENT_STATE = "samsungce.detergentState"
    SAMSUNG_CE_DEVICE_IDENTIFICATION = "samsungce.deviceIdentification"
    SAMSUNG_CE_DISHWASHER_JOB_STATE = "samsungce.dishwasherJobState"
    SAMSUNG_CE_DISHWASHER_OPERATION = "samsungce.dishwasherOperation"
    SAMSUNG_CE_DISHWASHER_WASHING_COURSE = "samsungce.dishwasherWashingCourse"
    SAMSUNG_CE_DISHWASHER_WASHING_COURSE_DETAILS = (
        "samsungce.dishwasherWashingCourseDetails"
    )
    SAMSUNG_CE_DISHWASHER_WASHING_OPTIONS = "samsungce.dishwasherWashingOptions"
    SAMSUNG_CE_DONGLE_SOFTWARE_INSTALLATION = "samsungce.dongleSoftwareInstallation"
    SAMSUNG_CE_DOOR_STATE = "samsungce.doorState"
    SAMSUNG_CE_DRIVER_VERSION = "samsungce.driverVersion"
    SAMSUNG_CE_DRYER_AUTO_CYCLE_LINK = "samsungce.dryerAutoCycleLink"
    SAMSUNG_CE_DRYER_CYCLE = "samsungce.dryerCycle"
    SAMSUNG_CE_DRYER_CYCLE_PRESET = "samsungce.dryerCyclePreset"
    SAMSUNG_CE_DRYER_DELAY_END = "samsungce.dryerDelayEnd"
    SAMSUNG_CE_DRYER_DRYING_TEMPERATURE = "samsungce.dryerDryingTemperature"
    SAMSUNG_CE_DRYER_DRYING_TIME = "samsungce.dryerDryingTime"
    SAMSUNG_CE_DRYER_FREEZE_PREVENT = "samsungce.dryerFreezePrevent"
    SAMSUNG_CE_DRYER_OPERATING_STATE = "samsungce.dryerOperatingState"
    SAMSUNG_CE_HOOD_FAN_SPEED = "samsungce.hoodFanSpeed"
    SAMSUNG_CE_KIDS_LOCK = "samsungce.kidsLock"
    SAMSUNG_CE_KITCHEN_DEVICE_DEFAULTS = "samsungce.kitchenDeviceDefaults"
    SAMSUNG_CE_KITCHEN_DEVICE_IDENTIFICATION = "samsungce.kitchenDeviceIdentification"
    SAMSUNG_CE_KITCHEN_MODE_SPECIFICATION = "samsungce.kitchenModeSpecification"
    SAMSUNG_CE_LAMP = "samsungce.lamp"
    SAMSUNG_CE_MEAT_PROBE = "samsungce.meatProbe"
    SAMSUNG_CE_MICROWAVE_POWER = "samsungce.microwavePower"
    SAMSUNG_CE_OVEN_MODE = "samsungce.ovenMode"
    SAMSUNG_CE_OVEN_OPERATING_STATE = "samsungce.ovenOperatingState"
    SAMSUNG_CE_QUICK_CONTROL = "samsungce.quickControl"
    SAMSUNG_CE_SOFTWARE_UPDATE = "samsungce.softwareUpdate"
    SAMSUNG_CE_WATER_CONSUMPTION_REPORT = "samsungce.waterConsumptionReport"
    SAMSUNG_CE_WELCOME_MESSAGE = "samsungce.welcomeMessage"

    SAMSUNG_IM_HUE_SYNC_MODE = "samsungim.hueSyncMode"

    SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT = "synthetic.lightingEffectCircadian"
    SYNTHETIC_FADE_LIGHTNING_EFFECT = "synthetic.lightingEffectFade"

    HCA_DRYER_MODE = "hca.dryerMode"

    SEC_DIAGNOSTICS_INFORMATION = "sec.diagnosticsInformation"
    SEC_WIFI_CONFIGURATION = "sec.wifiConfiguration"


class Attribute(StrEnum):
    """Attribute model."""

    ADD_RINSE = "addRinse"
    ALARM_ENABLED = "alarmEnabled"
    AUTO_RECONNECTION = "autoReconnection"
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
    COURSE = "course"
    CUSTOM_COURSE_CANDIDATES = "customCourseCandidates"
    DATA = "data"
    DATA_MODEL_VERSION = "dmv"
    DEFAULT_OPERATION_TIME = "defaultOperationTime"
    DEFAULT_OVEN_MODE = "defaultOvenMode"
    DEFAULT_OVEN_SETPOINT = "defaultOvenSetpoint"
    DEFINED_RECIPE = "definedRecipe"
    DEMAND_RESPONSE_LOAD_CONTROL_STATUS = "drlcStatus"
    DESCRIPTION = "description"
    DETERGENT_TYPE = "detergentType"
    DEVICE_ID = "di"
    DEVICE_NAME = "n"
    DEVICE_WATCH_DEVICE_STATUS = "DeviceWatch-DeviceStatus"
    DEVICE_WATCH_ENROLL = "DeviceWatch-Enroll"
    DISABLED_CAPABILITIES = "disabledCapabilities"
    DISHWASHER_DELAY_START_TIME = "dishwasherDelayStartTime"
    DISHWASHER_JOB_STATE = "dishwasherJobState"
    DISHWASHER_OPERATING_PERCENTAGE = "dishwasherOperatingPercentage"
    DISHWASHER_OPERATING_PROGRESS = "dishwasherOperatingProgress"
    DOOR = "door"
    DOOR_STATE = "doorState"
    DOSAGE = "dosage"
    DRYER_AUTO_CYCLE_LINK = "dryerAutoCycleLink"
    DRYER_CYCLE = "dryerCycle"
    DRYER_DRY_LEVEL = "dryerDryLevel"
    DRYER_JOB_STATE = "dryerJobState"
    DRYER_WRINKLE_PREVENT = "dryerWrinklePrevent"
    DRYING_TEMPERATURE = "dryingTemperature"
    DRYING_TIME = "dryingTime"
    DRY_PLUS = "dryPlus"
    DR_MAX_DURATION = "drMaxDuration"
    DUMP_TYPE = "dumpType"
    ENDPOINT = "endpoint"
    ENERGY_SAVING_INFO = "energySavingInfo"
    ENERGY_SAVING_LEVEL = "energySavingLevel"
    ENERGY_SAVING_OPERATION = "energySavingOperation"
    ENERGY_SAVING_OPERATION_SUPPORT = "energySavingOperationSupport"
    ENERGY_SAVING_SUPPORT = "energySavingSupport"
    ENERGY_TYPE = "energyType"
    ENERGY_USAGE_MAX = "energyUsageMax"
    FADE = "fade"
    FIRMWARE_VERSION = "mnfv"
    FUEL = "fuel"
    HARDWARE_VERSION = "mnhw"
    HEALTH_STATUS = "healthStatus"
    HEATED_DRY = "heatedDry"
    HIGH_TEMP_WASH = "highTempWash"
    HOOD_FAN_SPEED = "hoodFanSpeed"
    HOT_AIR_DRY = "hotAirDry"
    HUE = "hue"
    HUMIDITY = "humidity"
    INITIAL_AMOUNT = "initialAmount"
    JOB_BEGINNING_STATUS = "jobBeginningStatus"
    LAST_UPDATED_DATE = "lastUpdatedDate"
    LEVEL = "level"
    LEVEL_RANGE = "levelRange"
    LOCK_STATE = "lockState"
    LOG_TYPE = "logType"
    MACHINE_STATE = "machineState"
    MANUFACTURER_DETAILS_LINK = "mnml"
    MANUFACTURER_NAME = "mnmn"
    MANUFACTURE_DATE = "mndt"
    MAX_NUMBER_OF_PRESETS = "maxNumberOfPresets"
    MICOM_ASSAY_CODE = "micomAssayCode"
    MIN_VERSION = "minVersion"
    MN_ID = "mnId"
    MODE = "mode"
    MODEL_CLASSIFICATION_CODE = "modelClassificationCode"
    MODEL_CODE = "modelCode"
    MODEL_NAME = "modelName"
    MODEL_NUMBER = "mnmo"
    MOTION = "motion"
    NEW_VERSION_AVAILABLE = "newVersionAvailable"
    NOTIFICATION_TEMPLATE_I_D = "notificationTemplateID"
    OPERATING_STATE = "operatingState"
    OPERATION_TIME = "operationTime"
    ORDER_THRESHOLD = "orderThreshold"
    OS_VERSION = "mnos"
    OTN_D_U_I_D = "otnDUID"
    OVEN_CAVITY_STATUS = "ovenCavityStatus"
    OVEN_JOB_STATE = "ovenJobState"
    OVEN_MODE = "ovenMode"
    OVEN_SETPOINT = "ovenSetpoint"
    OVEN_SETPOINT_RANGE = "ovenSetpointRange"
    PLATFORM_ID = "pi"
    PLATFORM_VERSION = "mnpv"
    POWER_CONSUMPTION = "powerConsumption"
    POWER_LEVEL = "powerLevel"
    PREDEFINED_COURSES = "predefinedCourses"
    PRESETS = "presets"
    PROGRESS = "progress"
    PROGRESS_PERCENTAGE = "progressPercentage"
    PROTOCOL_TYPE = "protocolType"
    QUANTITY = "quantity"
    REFERENCE_TABLE = "referenceTable"
    REGION_CODE = "regionCode"
    RELEASE_YEAR = "releaseYear"
    REMAINING_AMOUNT = "remainingAmount"
    REMAINING_TIME = "remainingTime"
    REMAINING_TIME_STR = "remainingTimeStr"
    REMOTE_CONTROL_ENABLED = "remoteControlEnabled"
    REPRESENTATIVE_COMPONENT = "representativeComponent"
    RESERVABLE = "reservable"
    RINSE_PLUS = "rinsePlus"
    SANITIZE = "sanitize"
    SANITIZING_WASH = "sanitizingWash"
    SATURATION = "saturation"
    SCHEDULED_JOBS = "scheduledJobs"
    SELECTED_ZONE = "selectedZone"
    SERIAL_NUMBER = "serialNumber"
    SERIAL_NUMBER_EXTRA = "serialNumberExtra"
    SETTABLE_MAX_FAN_SPEED = "settableMaxFanSpeed"
    SETTABLE_MIN_FAN_SPEED = "settableMinFanSpeed"
    SETUP_ID = "setupId"
    SIGNIN_PERMISSION = "signinPermission"
    SPECIALIZED_FUNCTION_CLASSIFICATION = "specializedFunctionClassification"
    SPECIFICATION = "specification"
    SPEC_VERSION = "icv"
    SPEED_BOOSTER = "speedBooster"
    STATUS = "status"
    STEAM_SOAK = "steamSoak"
    STORM_WASH = "stormWash"
    SUPPORTED_AUTH_TYPE = "supportedAuthType"
    SUPPORTED_BRIGHTNESS_LEVEL = "supportedBrightnessLevel"
    SUPPORTED_COOKTOP_OPERATING_STATE = "supportedCooktopOperatingState"
    SUPPORTED_COURSES = "supportedCourses"
    SUPPORTED_CYCLES = "supportedCycles"
    SUPPORTED_DRYER_DRY_LEVEL = "supportedDryerDryLevel"
    SUPPORTED_DRYING_TEMPERATURE = "supportedDryingTemperature"
    SUPPORTED_DRYING_TIME = "supportedDryingTime"
    SUPPORTED_ENERGY_SAVING_LEVELS = "supportedEnergySavingLevels"
    SUPPORTED_HOOD_FAN_SPEED = "supportedHoodFanSpeed"
    SUPPORTED_LIST = "supportedList"
    SUPPORTED_MACHINE_STATES = "supportedMachineStates"
    SUPPORTED_MODES = "supportedModes"
    SUPPORTED_OPERATING_STATE = "supportedOperatingState"
    SUPPORTED_OPERATING_STATES = "supportedOperatingStates"
    SUPPORTED_OVEN_MODES = "supportedOvenModes"
    SUPPORTED_POWER_LEVELS = "supportedPowerLevels"
    SUPPORTED_THERMOSTAT_MODES = "supportedThermostatModes"
    SUPPORTED_WINDOW_SHADE_COMMANDS = "supportedWindowShadeCommands"
    SUPPORTED_WI_FI_FREQ = "supportedWiFiFreq"
    SUPPORT_LINK = "mnsl"
    SWITCH = "switch"
    SYSTEM_TIME = "st"
    TARGET_MODULE = "targetModule"
    TEMPERATURE = "temperature"
    TEMPERATURE_RANGE = "temperatureRange"
    TEMPERATURE_SETPOINT = "temperatureSetpoint"
    THERMOSTAT_MODE = "thermostatMode"
    TIME_LEFT_TO_START = "timeLeftToStart"
    TS_ID = "tsId"
    TYPE = "type"
    VENDOR_ID = "vid"
    VERSION = "version"
    VERSION_NUMBER = "versionNumber"
    WASHING_COURSE = "washingCourse"
    WATER_CONSUMPTION = "waterConsumption"
    WATER_FILTER_CAPACITY = "waterFilterCapacity"
    WATER_FILTER_LAST_RESET_DATE = "waterFilterLastResetDate"
    WATER_FILTER_RESET_TYPE = "waterFilterResetType"
    WATER_FILTER_STATUS = "waterFilterStatus"
    WATER_FILTER_USAGE = "waterFilterUsage"
    WATER_FILTER_USAGE_STEP = "waterFilterUsageStep"
    WATER_USAGE_MAX = "waterUsageMax"
    WELCOME_MESSAGE = "welcomeMessage"
    WINDOW_SHADE = "windowShade"
    ZONE_BOOSTER = "zoneBooster"


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
    Capability.DOOR_CONTROL: [
        Attribute.DOOR,
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
    Capability.DEMAND_RESPONSE_LOAD_CONTROL: [
        Attribute.DEMAND_RESPONSE_LOAD_CONTROL_STATUS
    ],
    Capability.POWER_CONSUMPTION_REPORT: [Attribute.POWER_CONSUMPTION],
    Capability.DRYER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
        Attribute.DRYER_JOB_STATE,
    ],
    Capability.DISHWASHER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_MACHINE_STATES,
        Attribute.DISHWASHER_JOB_STATE,
    ],
    # HCA capabilities
    Capability.HCA_DRYER_MODE: [Attribute.MODE, Attribute.SUPPORTED_MODES],
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
    ],
    Capability.SAMSUNG_CE_KITCHEN_MODE_SPECIFICATION: [Attribute.SPECIFICATION],
    Capability.SAMSUNG_CE_KITCHEN_DEVICE_IDENTIFICATION: [
        Attribute.REGION_CODE,
        Attribute.MODEL_CODE,
        Attribute.FUEL,
        Attribute.TYPE,
        Attribute.REPRESENTATIVE_COMPONENT,
    ],
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
    Capability.SAMSUNG_CE_DRYER_DRYING_TEMPERATURE: [
        Attribute.DRYING_TEMPERATURE,
        Attribute.SUPPORTED_DRYING_TEMPERATURE,
    ],
    Capability.SAMSUNG_CE_WELCOME_MESSAGE: [Attribute.WELCOME_MESSAGE],
    Capability.SAMSUNG_CE_DONGLE_SOFTWARE_INSTALLATION: [Attribute.STATUS],
    Capability.SAMSUNG_CE_DRYER_CYCLE_PRESET: [
        Attribute.MAX_NUMBER_OF_PRESETS,
        Attribute.PRESETS,
    ],
    Capability.SAMSUNG_CE_QUICK_CONTROL: [Attribute.VERSION],
    Capability.SAMSUNG_CE_DRYER_FREEZE_PREVENT: [Attribute.OPERATING_STATE],
    Capability.SAMSUNG_CE_DRYER_AUTO_CYCLE_LINK: [Attribute.DRYER_AUTO_CYCLE_LINK],
    Capability.SAMSUNG_CE_DRYER_CYCLE: [
        Attribute.DRYER_CYCLE,
        Attribute.SUPPORTED_CYCLES,
        Attribute.REFERENCE_TABLE,
        Attribute.SPECIALIZED_FUNCTION_CLASSIFICATION,
    ],
    Capability.SAMSUNG_CE_DETERGENT_ORDER: [
        Attribute.ALARM_ENABLED,
        Attribute.ORDER_THRESHOLD,
    ],
    Capability.SAMSUNG_CE_DETERGENT_STATE: [
        Attribute.REMAINING_AMOUNT,
        Attribute.DOSAGE,
        Attribute.INITIAL_AMOUNT,
        Attribute.DETERGENT_TYPE,
    ],
    Capability.SAMSUNG_CE_DRYER_DELAY_END: [Attribute.REMAINING_TIME],
    Capability.SAMSUNG_CE_DRYER_OPERATING_STATE: [
        Attribute.OPERATING_STATE,
        Attribute.SUPPORTED_OPERATING_STATES,
        Attribute.SCHEDULED_JOBS,
        Attribute.PROGRESS,
        Attribute.REMAINING_TIME_STR,
        Attribute.DRYER_JOB_STATE,
        Attribute.REMAINING_TIME,
    ],
    Capability.SAMSUNG_CE_DRYER_DRYING_TIME: [
        Attribute.DRYING_TIME,
        Attribute.SUPPORTED_DRYING_TIME,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_COURSE: [
        Attribute.WASHING_COURSE,
        Attribute.SUPPORTED_COURSES,
        Attribute.CUSTOM_COURSE_CANDIDATES,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_OPTIONS: [
        Attribute.DRY_PLUS,
        Attribute.STORM_WASH,
        Attribute.HOT_AIR_DRY,
        Attribute.SELECTED_ZONE,
        Attribute.SPEED_BOOSTER,
        Attribute.HIGH_TEMP_WASH,
        Attribute.SANITIZING_WASH,
        Attribute.HEATED_DRY,
        Attribute.ZONE_BOOSTER,
        Attribute.ADD_RINSE,
        Attribute.RINSE_PLUS,
        Attribute.SUPPORTED_LIST,
        Attribute.SANITIZE,
        Attribute.STEAM_SOAK,
    ],
    Capability.SAMSUNG_CE_WATER_CONSUMPTION_REPORT: [
        Attribute.WATER_CONSUMPTION,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_JOB_STATE: [
        Attribute.SCHEDULED_JOBS,
        Attribute.DISHWASHER_JOB_STATE,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_COURSE_DETAILS: [
        Attribute.PREDEFINED_COURSES,
        Attribute.WATER_USAGE_MAX,
        Attribute.ENERGY_USAGE_MAX,
    ],
    Capability.SAMSUNG_CE_HOOD_FAN_SPEED: [
        Attribute.SETTABLE_MAX_FAN_SPEED,
        Attribute.HOOD_FAN_SPEED,
        Attribute.SUPPORTED_HOOD_FAN_SPEED,
        Attribute.SETTABLE_MIN_FAN_SPEED,
    ],
    Capability.SAMSUNG_CE_MICROWAVE_POWER: [
        Attribute.SUPPORTED_POWER_LEVELS,
        Attribute.POWER_LEVEL,
    ],
    Capability.SAMSUNG_CE_DEFINED_RECIPE: [
        Attribute.DEFINED_RECIPE,
    ],
    # Custom capabilities
    Capability.CUSTOM_DISABLED_CAPABILITIES: [Attribute.DISABLED_CAPABILITIES],
    Capability.CUSTOM_OVEN_CAVITY_STATUS: [Attribute.OVEN_CAVITY_STATUS],
    Capability.CUSTOM_COOKTOP_OPERATING_STATE: [
        Attribute.COOKTOP_OPERATING_STATE,
        Attribute.SUPPORTED_COOKTOP_OPERATING_STATE,
    ],
    Capability.CUSTOM_DRYER_WRINKLE_PREVENT: [
        Attribute.DRYER_WRINKLE_PREVENT,
        Attribute.OPERATING_STATE,
    ],
    Capability.CUSTOM_DRYER_DRY_LEVEL: [
        Attribute.DRYER_DRY_LEVEL,
        Attribute.SUPPORTED_DRYER_DRY_LEVEL,
    ],
    Capability.CUSTOM_JOB_BEGINNING_STATUS: [Attribute.JOB_BEGINNING_STATUS],
    Capability.CUSTOM_SUPPORTED_OPTIONS: [
        Attribute.COURSE,
        Attribute.REFERENCE_TABLE,
        Attribute.SUPPORTED_COURSES,
    ],
    Capability.CUSTOM_ENERGY_TYPE: [
        Attribute.ENERGY_TYPE,
        Attribute.ENERGY_SAVING_SUPPORT,
        Attribute.DR_MAX_DURATION,
        Attribute.ENERGY_SAVING_LEVEL,
        Attribute.ENERGY_SAVING_INFO,
        Attribute.SUPPORTED_ENERGY_SAVING_LEVELS,
        Attribute.ENERGY_SAVING_OPERATION,
        Attribute.NOTIFICATION_TEMPLATE_I_D,
        Attribute.ENERGY_SAVING_OPERATION_SUPPORT,
    ],
    Capability.CUSTOM_DISHWASHER_OPERATING_PROGRESS: [
        Attribute.DISHWASHER_OPERATING_PROGRESS,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_OPERATION: [
        Attribute.SUPPORTED_OPERATING_STATE,
        Attribute.OPERATING_STATE,
        Attribute.RESERVABLE,
        Attribute.PROGRESS_PERCENTAGE,
        Attribute.REMAINING_TIME_STR,
        Attribute.OPERATION_TIME,
        Attribute.REMAINING_TIME,
        Attribute.TIME_LEFT_TO_START,
    ],
    Capability.CUSTOM_DISHWASHER_OPERATING_PERCENTAGE: [
        Attribute.DISHWASHER_OPERATING_PERCENTAGE,
    ],
    Capability.CUSTOM_DISHWASHER_DELAY_START_TIME: [
        Attribute.DISHWASHER_DELAY_START_TIME,
    ],
    Capability.CUSTOM_WATER_FILTER: [
        Attribute.WATER_FILTER_STATUS,
        Attribute.WATER_FILTER_USAGE_STEP,
        Attribute.WATER_FILTER_USAGE,
        Attribute.WATER_FILTER_CAPACITY,
        Attribute.WATER_FILTER_LAST_RESET_DATE,
        Attribute.WATER_FILTER_RESET_TYPE,
    ],
    # Sec capabilities
    Capability.SEC_DIAGNOSTICS_INFORMATION: [
        Attribute.LOG_TYPE,
        Attribute.ENDPOINT,
        Attribute.MIN_VERSION,
        Attribute.SIGNIN_PERMISSION,
        Attribute.SETUP_ID,
        Attribute.PROTOCOL_TYPE,
        Attribute.TS_ID,
        Attribute.MN_ID,
        Attribute.DUMP_TYPE,
    ],
    Capability.SEC_WIFI_CONFIGURATION: [
        Attribute.SUPPORTED_AUTH_TYPE,
        Attribute.SUPPORTED_WI_FI_FREQ,
        Attribute.AUTO_RECONNECTION,
        Attribute.MIN_VERSION,
        Attribute.PROTOCOL_TYPE,
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
