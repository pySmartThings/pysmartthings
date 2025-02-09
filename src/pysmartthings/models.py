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

    AIR_CONDITIONER_FAN_MODE = "airConditionerFanMode"
    AIR_CONDITIONER_MODE = "airConditionerMode"
    AIR_QUALITY_SENSOR = "airQualitySensor"
    ALARM = "alarm"
    AUDIO_NOTIFICATION = "audioNotification"
    AUDIO_VOLUME = "audioVolume"
    BATTERY = "battery"
    BRIDGE = "bridge"
    BYPASSABLE = "bypassable"
    COLOR_CONTROL = "colorControl"
    COLOR_TEMPERATURE = "colorTemperature"
    CONTACT_SENSOR = "contactSensor"
    DEMAND_RESPONSE_LOAD_CONTROL = "demandResponseLoadControl"
    DISHWASHER_OPERATING_STATE = "dishwasherOperatingState"
    DOOR_CONTROL = "doorControl"
    DRYER_OPERATING_STATE = "dryerOperatingState"
    DUST_SENSOR = "dustSensor"
    ENERGY_METER = "energyMeter"
    EXECUTE = "execute"
    FAN_OSCILLATION_MODE = "fanOscillationMode"
    FIRMWARE_UPDATE = "firmwareUpdate"
    GEOFENCE = "geofence"
    GEOLOCATION = "geolocation"
    HEALTH_CHECK = "healthCheck"
    MOTION_SENSOR = "motionSensor"
    OCF = "ocf"
    ODOR_SENSOR = "odorSensor"
    OVEN_MODE = "ovenMode"
    OVEN_OPERATING_STATE = "ovenOperatingState"
    OVEN_SETPOINT = "ovenSetpoint"
    POWER_CONSUMPTION_REPORT = "powerConsumptionReport"
    POWER_METER = "powerMeter"
    REFRESH = "refresh"
    REFRIGERATION = "refrigeration"
    RELATIVE_HUMIDITY_MEASUREMENT = "relativeHumidityMeasurement"
    REMOTE_CONTROL_STATUS = "remoteControlStatus"
    ROBOT_CLEANER_CLEANING_MODE = "robotCleanerCleaningMode"
    ROBOT_CLEANER_MOVEMENT = "robotCleanerMovement"
    ROBOT_CLEANER_TURBO_MODE = "robotCleanerTurboMode"
    SWITCH = "switch"
    SWITCH_LEVEL = "switchLevel"
    TEMPERATURE_MEASUREMENT = "temperatureMeasurement"
    THERMOSTAT_COOLING_SETPOINT = "thermostatCoolingSetpoint"
    THERMOSTAT_MODE = "thermostatMode"
    VERY_FINE_DUST_SENSOR = "veryFineDustSensor"
    WASHER_OPERATING_STATE = "washerOperatingState"
    WINDOW_SHADE = "windowShade"

    CUSTOM_AIR_CONDITIONER_ODOR_CONTROLLER = "custom.airConditionerOdorController"
    CUSTOM_AIR_CONDITIONER_OPTIONAL_MODE = "custom.airConditionerOptionalMode"
    CUSTOM_AIR_CONDITIONER_TROPICAL_NIGHT_MODE = (
        "custom.airConditionerTropicalNightMode"
    )
    CUSTOM_AUTO_CLEANING_MODE = "custom.autoCleaningMode"
    CUSTOM_COOKTOP_OPERATING_STATE = "custom.cooktopOperatingState"
    CUSTOM_DEODOR_FILTER = "custom.deodorFilter"
    CUSTOM_DEVICE_REPORT_STATE_CONFIGURATION = "custom.deviceReportStateConfiguration"
    CUSTOM_DISABLED_CAPABILITIES = "custom.disabledCapabilities"
    CUSTOM_DISABLED_COMPONENTS = "custom.disabledComponents"
    CUSTOM_DISHWASHER_DELAY_START_TIME = "custom.dishwasherDelayStartTime"
    CUSTOM_DISHWASHER_OPERATING_PERCENTAGE = "custom.dishwasherOperatingPercentage"
    CUSTOM_DISHWASHER_OPERATING_PROGRESS = "custom.dishwasherOperatingProgress"
    CUSTOM_DO_NOT_DISTURB_MODE = "custom.doNotDisturbMode"
    CUSTOM_DRYER_DRY_LEVEL = "custom.dryerDryLevel"
    CUSTOM_DRYER_WRINKLE_PREVENT = "custom.dryerWrinklePrevent"
    CUSTOM_DUST_FILTER = "custom.dustFilter"
    CUSTOM_ELECTRIC_HEPA_FILTER = "custom.electricHepaFilter"
    CUSTOM_ENERGY_TYPE = "custom.energyType"
    CUSTOM_FRIDGE_MODE = "custom.fridgeMode"
    CUSTOM_JOB_BEGINNING_STATUS = "custom.jobBeginningStatus"
    CUSTOM_OVEN_CAVITY_STATUS = "custom.ovenCavityStatus"
    CUSTOM_PERIODIC_SENSING = "custom.periodicSensing"
    CUSTOM_SPI_MODE = "custom.spiMode"
    CUSTOM_SUPPORTED_OPTIONS = "custom.supportedOptions"
    CUSTOM_THERMOSTAT_SETPOINT_CONTROL = "custom.thermostatSetpointControl"
    CUSTOM_VERY_FINE_DUST_FILTER = "custom.veryFineDustFilter"
    CUSTOM_WASHER_AUTO_DETERGENT = "custom.washerAutoDetergent"
    CUSTOM_WASHER_AUTO_SOFTENER = "custom.washerAutoSoftener"
    CUSTOM_WASHER_RINSE_CYCLES = "custom.washerRinseCycles"
    CUSTOM_WASHER_SOIL_LEVEL = "custom.washerSoilLevel"
    CUSTOM_WASHER_SPIN_LEVEL = "custom.washerSpinLevel"
    CUSTOM_WASHER_WATER_TEMPERATURE = "custom.washerWaterTemperature"
    CUSTOM_WATER_FILTER = "custom.waterFilter"

    SAMSUNG_CE_AIR_CONDITIONER_BEEP = "samsungce.airConditionerBeep"
    SAMSUNG_CE_AIR_CONDITIONER_LIGHTING = "samsungce.airConditionerLighting"
    SAMSUNG_CE_AIR_QUALITY_HEALTH_CONCERN = "samsungce.airQualityHealthConcern"
    SAMSUNG_CE_ALWAYS_ON_SENSING = "samsungce.alwaysOnSensing"
    SAMSUNG_CE_AUTO_DISPENSE_DETERGENT = "samsungce.autoDispenseDetergent"
    SAMSUNG_CE_AUTO_DISPENSE_SOFTENER = "samsungce.autoDispenseSoftener"
    SAMSUNG_CE_BUTTON_DISPLAY_CONDITION = "samsungce.buttonDisplayCondition"
    SAMSUNG_CE_CONNECTION_STATE = "samsungce.connectionState"
    SAMSUNG_CE_CUSTOM_RECIPE = "samsungce.customRecipe"
    SAMSUNG_CE_DEFINED_RECIPE = "samsungce.definedRecipe"
    SAMSUNG_CE_DETERGENT_AUTO_REPLENISHMENT = "samsungce.detergentAutoReplenishment"
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
    SAMSUNG_CE_DUST_FILTER_ALARM = "samsungce.dustFilterAlarm"
    SAMSUNG_CE_ENERGY_PLANNER = "samsungce.energyPlanner"
    SAMSUNG_CE_FOOD_DEFROST = "samsungce.foodDefrost"
    SAMSUNG_CE_FREEZER_CONVERT_MODE = "samsungce.freezerConvertMode"
    SAMSUNG_CE_FRIDGE_FOOD_LIST = "samsungce.fridgeFoodList"
    SAMSUNG_CE_FRIDGE_PANTRY_INFO = "samsungce.fridgePantryInfo"
    SAMSUNG_CE_FRIDGE_PANTRY_MODE = "samsungce.fridgePantryMode"
    SAMSUNG_CE_FRIDGE_VACATION_MODE = "samsungce.fridgeVacationMode"
    SAMSUNG_CE_HOOD_FAN_SPEED = "samsungce.hoodFanSpeed"
    SAMSUNG_CE_INDIVIDUAL_CONTROL_LOCK = "samsungce.individualControlLock"
    SAMSUNG_CE_KIDS_LOCK = "samsungce.kidsLock"
    SAMSUNG_CE_KITCHEN_DEVICE_DEFAULTS = "samsungce.kitchenDeviceDefaults"
    SAMSUNG_CE_KITCHEN_DEVICE_IDENTIFICATION = "samsungce.kitchenDeviceIdentification"
    SAMSUNG_CE_KITCHEN_MODE_SPECIFICATION = "samsungce.kitchenModeSpecification"
    SAMSUNG_CE_LAMP = "samsungce.lamp"
    SAMSUNG_CE_MEAT_AGING = "samsungce.meatAging"
    SAMSUNG_CE_MEAT_PROBE = "samsungce.meatProbe"
    SAMSUNG_CE_MICROWAVE_POWER = "samsungce.microwavePower"
    SAMSUNG_CE_OVEN_MODE = "samsungce.ovenMode"
    SAMSUNG_CE_OVEN_OPERATING_STATE = "samsungce.ovenOperatingState"
    SAMSUNG_CE_POWER_COOL = "samsungce.powerCool"
    SAMSUNG_CE_POWER_FREEZE = "samsungce.powerFreeze"
    SAMSUNG_CE_QUICK_CONTROL = "samsungce.quickControl"
    SAMSUNG_CE_ROBOT_CLEANER_CLEANING_MODE = "samsungce.robotCleanerCleaningMode"
    SAMSUNG_CE_ROBOT_CLEANER_OPERATING_STATE = "samsungce.robotCleanerOperatingState"
    SAMSUNG_CE_RUNESTONE_HOME_CONTEXT = "samsungce.runestoneHomeContext"
    SAMSUNG_CE_SABBATH_MODE = "samsungce.sabbathMode"
    SAMSUNG_CE_SCALE_SETTINGS = "samsungce.scaleSettings"
    SAMSUNG_CE_SELF_CHECK = "samsungce.selfCheck"
    SAMSUNG_CE_SILENT_ACTION = "samsungce.silentAction"
    SAMSUNG_CE_SOFTENER_AUTO_REPLENISHMENT = "samsungce.softenerAutoReplenishment"
    SAMSUNG_CE_SOFTENER_ORDER = "samsungce.softenerOrder"
    SAMSUNG_CE_SOFTENER_STATE = "samsungce.softenerState"
    SAMSUNG_CE_SOFTWARE_UPDATE = "samsungce.softwareUpdate"
    SAMSUNG_CE_UNAVAILABLE_CAPABILITIES = "samsungce.unavailableCapabilities"
    SAMSUNG_CE_VIEW_INSIDE = "samsungce.viewInside"
    SAMSUNG_CE_WASHER_BUBBLE_SOAK = "samsungce.washerBubbleSoak"
    SAMSUNG_CE_WASHER_CYCLE = "samsungce.washerCycle"
    SAMSUNG_CE_WASHER_CYCLE_PRESET = "samsungce.washerCyclePreset"
    SAMSUNG_CE_WASHER_DELAY_END = "samsungce.washerDelayEnd"
    SAMSUNG_CE_WASHER_FREEZE_PREVENT = "samsungce.washerFreezePrevent"
    SAMSUNG_CE_WASHER_OPERATING_STATE = "samsungce.washerOperatingState"
    SAMSUNG_CE_WASHER_WASHING_TIME = "samsungce.washerWashingTime"
    SAMSUNG_CE_WASHER_WATER_LEVEL = "samsungce.washerWaterLevel"
    SAMSUNG_CE_WASHER_WATER_VALVE = "samsungce.washerWaterValve"
    SAMSUNG_CE_WATER_CONSUMPTION_REPORT = "samsungce.waterConsumptionReport"
    SAMSUNG_CE_WEIGHT_MEASUREMENT = "samsungce.weightMeasurement"
    SAMSUNG_CE_WEIGHT_MEASUREMENT_CALIBRATION = "samsungce.weightMeasurementCalibration"
    SAMSUNG_CE_WELCOME_COOLING = "samsungce.welcomeCooling"
    SAMSUNG_CE_WELCOME_MESSAGE = "samsungce.welcomeMessage"
    SAMSUNG_CE_WIFI_KIT_SUB_DEVICES = "samsungce.wifiKitSubDevices"

    SAMSUNG_IM_HUE_SYNC_MODE = "samsungim.hueSyncMode"

    SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT = "synthetic.lightingEffectCircadian"
    SYNTHETIC_FADE_LIGHTNING_EFFECT = "synthetic.lightingEffectFade"

    HCA_DRYER_MODE = "hca.dryerMode"
    HCA_WASHER_MODE = "hca.washerMode"

    SEC_CALM_CONNECTION_CARE = "sec.calmConnectionCare"
    SEC_DIAGNOSTICS_INFORMATION = "sec.diagnosticsInformation"
    SEC_WIFI_CONFIGURATION = "sec.wifiConfiguration"

    TAG_E2E_ENCRYPTION = "tag.e2eEncryption"
    TAG_FACTORY_RESET = "tag.factoryReset"
    TAG_SEARCHING_STATUS = "tag.searchingStatus"
    TAG_TAG_BUTTON = "tag.tagButton"
    TAG_TAG_STATUS = "tag.tagStatus"
    TAG_UPDATED_INFO = "tag.updatedInfo"
    TAG_UWB_ACTIVATION = "tag.uwbActivation"


class Attribute(StrEnum):
    """Attribute model."""

    ACCURACY = "accuracy"
    ACTIVATED = "activated"
    AC_OPTIONAL_MODE = "acOptionalMode"
    AC_TROPICAL_NIGHT_MODE_LEVEL = "acTropicalNightModeLevel"
    ADD_RINSE = "addRinse"
    AIR_CONDITIONER_MODE = "airConditionerMode"
    AIR_CONDITIONER_ODOR_CONTROLLER_PROGRESS = "airConditionerOdorControllerProgress"
    AIR_CONDITIONER_ODOR_CONTROLLER_STATE = "airConditionerOdorControllerState"
    AIR_QUALITY = "airQuality"
    AIR_QUALITY_HEALTH_CONCERN = "airQualityHealthConcern"
    ALARM = "alarm"
    ALARM_ENABLED = "alarmEnabled"
    ALARM_THRESHOLD = "alarmThreshold"
    ALTITUDE_ACCURACY = "altitudeAccuracy"
    ALWAYS_ON = "alwaysOn"
    AMOUNT = "amount"
    AUTOMATIC_EXECUTION_MODE = "automaticExecutionMode"
    AUTOMATIC_EXECUTION_SETTING = "automaticExecutionSetting"
    AUTO_CLEANING_MODE = "autoCleaningMode"
    AUTO_RECONNECTION = "autoReconnection"
    AVAILABLE_AC_FAN_MODES = "availableAcFanModes"
    AVAILABLE_AC_MODES = "availableAcModes"
    AVAILABLE_FAN_OSCILLATION_MODES = "availableFanOscillationModes"
    AVAILABLE_MODULES = "availableModules"
    AVAILABLE_TYPES = "availableTypes"
    AVAILABLE_VERSION = "availableVersion"
    BABY_DETERGENT_ALARM_ENABLED = "babyDetergentAlarmEnabled"
    BABY_DETERGENT_DOSAGE = "babyDetergentDosage"
    BABY_DETERGENT_INITIAL_AMOUNT = "babyDetergentInitialAmount"
    BABY_DETERGENT_ORDER_THRESHOLD = "babyDetergentOrderThreshold"
    BABY_DETERGENT_REMAINING_AMOUNT = "babyDetergentRemainingAmount"
    BABY_DETERGENT_TYPE = "babyDetergentType"
    BATTERY = "battery"
    BEEP = "beep"
    BINARY_ID = "binaryId"
    BRIGHTNESS_LEVEL = "brightnessLevel"
    BYPASS_STATUS = "bypassStatus"
    CHECK_INTERVAL = "checkInterval"
    CIRCADIAN = "circadian"
    CLEANING_MODE = "cleaningMode"
    CLEANING_STEP = "cleaningStep"
    COLOR = "color"
    COLOR_TEMPERATURE = "colorTemperature"
    COLOR_TEMPERATURE_RANGE = "colorTemperatureRange"
    COMPLETION_TIME = "completionTime"
    CONNECTED_DEVICE_ID = "connectedDeviceId"
    CONNECTED_USER_ID = "connectedUserId"
    CONNECTION = "connection"
    CONNECTION_STATE = "connectionState"
    CONTACT = "contact"
    CONTENTS = "contents"
    COOKTOP_OPERATING_STATE = "cooktopOperatingState"
    COOLING_SETPOINT = "coolingSetpoint"
    COOLING_SETPOINT_RANGE = "coolingSetpointRange"
    COURSE = "course"
    CURRENT_VERSION = "currentVersion"
    CUSTOM_COURSE_CANDIDATES = "customCourseCandidates"
    DATA = "data"
    DATA_MODEL_VERSION = "dmv"
    DEFAULT_OPERATION_TIME = "defaultOperationTime"
    DEFAULT_OVEN_MODE = "defaultOvenMode"
    DEFAULT_OVEN_SETPOINT = "defaultOvenSetpoint"
    DEFINED_RECIPE = "definedRecipe"
    DEFROST = "defrost"
    DEMAND_RESPONSE_LOAD_CONTROL_STATUS = "drlcStatus"
    DENSITY = "density"
    DEODOR_FILTER_CAPACITY = "deodorFilterCapacity"
    DEODOR_FILTER_LAST_RESET_DATE = "deodorFilterLastResetDate"
    DEODOR_FILTER_RESET_TYPE = "deodorFilterResetType"
    DEODOR_FILTER_STATUS = "deodorFilterStatus"
    DEODOR_FILTER_USAGE = "deodorFilterUsage"
    DEODOR_FILTER_USAGE_STEP = "deodorFilterUsageStep"
    DESCRIPTION = "description"
    DETERGENT_TYPE = "detergentType"
    DEVICE_ID = "di"
    DEVICE_NAME = "n"
    DEVICE_WATCH_DEVICE_STATUS = "DeviceWatch-DeviceStatus"
    DEVICE_WATCH_ENROLL = "DeviceWatch-Enroll"
    DISABLED_CAPABILITIES = "disabledCapabilities"
    DISABLED_COMPONENTS = "disabledComponents"
    DISHWASHER_DELAY_START_TIME = "dishwasherDelayStartTime"
    DISHWASHER_JOB_STATE = "dishwasherJobState"
    DISHWASHER_OPERATING_PERCENTAGE = "dishwasherOperatingPercentage"
    DISHWASHER_OPERATING_PROGRESS = "dishwasherOperatingProgress"
    DOOR = "door"
    DOOR_STATE = "doorState"
    DOSAGE = "dosage"
    DO_NOT_DISTURB = "doNotDisturb"
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
    DUST_FILTER_CAPACITY = "dustFilterCapacity"
    DUST_FILTER_LAST_RESET_DATE = "dustFilterLastResetDate"
    DUST_FILTER_RESET_TYPE = "dustFilterResetType"
    DUST_FILTER_STATUS = "dustFilterStatus"
    DUST_FILTER_USAGE = "dustFilterUsage"
    DUST_FILTER_USAGE_STEP = "dustFilterUsageStep"
    DUST_LEVEL = "dustLevel"
    ELECTRIC_HEPA_FILTER_CAPACITY = "electricHepaFilterCapacity"
    ELECTRIC_HEPA_FILTER_LAST_RESET_DATE = "electricHepaFilterLastResetDate"
    ELECTRIC_HEPA_FILTER_RESET_TYPE = "electricHepaFilterResetType"
    ELECTRIC_HEPA_FILTER_STATUS = "electricHepaFilterStatus"
    ELECTRIC_HEPA_FILTER_USAGE = "electricHepaFilterUsage"
    ELECTRIC_HEPA_FILTER_USAGE_STEP = "electricHepaFilterUsageStep"
    ENABLED = "enabled"
    ENABLE_STATE = "enableState"
    ENCRYPTION = "encryption"
    ENDPOINT = "endpoint"
    END_TIME = "endTime"
    ENERGY = "energy"
    ENERGY_SAVING_INFO = "energySavingInfo"
    ENERGY_SAVING_LEVEL = "energySavingLevel"
    ENERGY_SAVING_OPERATION = "energySavingOperation"
    ENERGY_SAVING_OPERATION_SUPPORT = "energySavingOperationSupport"
    ENERGY_SAVING_SUPPORT = "energySavingSupport"
    ENERGY_TYPE = "energyType"
    ENERGY_USAGE_MAX = "energyUsageMax"
    ERRORS = "errors"
    FADE = "fade"
    FAN_MODE = "fanMode"
    FAN_OSCILLATION_MODE = "fanOscillationMode"
    FINE_DUST_LEVEL = "fineDustLevel"
    FIRMWARE_VERSION = "mnfv"
    FOOD_TYPE = "foodType"
    FREEZER_CONVERT_MODE = "freezerConvertMode"
    FRIDGE_MODE = "fridgeMode"
    FRIDGE_MODE_VALUE = "fridgeModeValue"
    FUEL = "fuel"
    GEOFENCE = "geofence"
    HARDWARE_VERSION = "mnhw"
    HEADING = "heading"
    HEALTH_STATUS = "healthStatus"
    HEATED_DRY = "heatedDry"
    HIGH_TEMP_WASH = "highTempWash"
    HOMING_REASON = "homingReason"
    HOOD_FAN_SPEED = "hoodFanSpeed"
    HOT_AIR_DRY = "hotAirDry"
    HUE = "hue"
    HUMIDITY = "humidity"
    INITIAL_AMOUNT = "initialAmount"
    IS_MAP_BASED_OPERATION_AVAILABLE = "isMapBasedOperationAvailable"
    JOB_BEGINNING_STATUS = "jobBeginningStatus"
    LAST_SENSING_LEVEL = "lastSensingLevel"
    LAST_SENSING_TIME = "lastSensingTime"
    LAST_UPDATED_DATE = "lastUpdatedDate"
    LAST_UPDATED_TIME = "lastUpdatedTime"
    LAST_UPDATE_STATUS = "lastUpdateStatus"
    LAST_UPDATE_STATUS_REASON = "lastUpdateStatusReason"
    LAST_UPDATE_TIME = "lastUpdateTime"
    LATEST_REQUEST_ID = "latestRequestId"
    LATITUDE = "latitude"
    LEVEL = "level"
    LEVEL_RANGE = "levelRange"
    LIGHTING = "lighting"
    LOCK_STATE = "lockState"
    LOG_TYPE = "logType"
    LONGITUDE = "longitude"
    MACHINE_STATE = "machineState"
    MANUFACTURER_DETAILS_LINK = "mnml"
    MANUFACTURER_NAME = "mnmn"
    MANUFACTURE_DATE = "mndt"
    MAXIMUM_SETPOINT = "maximumSetpoint"
    MAX_NUMBER_OF_PRESETS = "maxNumberOfPresets"
    METHOD = "method"
    MICOM_ASSAY_CODE = "micomAssayCode"
    MINIMUM_RESERVABLE_TIME = "minimumReservableTime"
    MINIMUM_SETPOINT = "minimumSetpoint"
    MIN_VERSION = "minVersion"
    MN_ID = "mnId"
    MODE = "mode"
    MODEL_CLASSIFICATION_CODE = "modelClassificationCode"
    MODEL_CODE = "modelCode"
    MODEL_NAME = "modelName"
    MODEL_NUMBER = "mnmo"
    MOTION = "motion"
    NAME = "name"
    NEUTRAL_DETERGENT_ALARM_ENABLED = "neutralDetergentAlarmEnabled"
    NEUTRAL_DETERGENT_DOSAGE = "neutralDetergentDosage"
    NEUTRAL_DETERGENT_INITIAL_AMOUNT = "neutralDetergentInitialAmount"
    NEUTRAL_DETERGENT_ORDER_THRESHOLD = "neutralDetergentOrderThreshold"
    NEUTRAL_DETERGENT_REMAINING_AMOUNT = "neutralDetergentRemainingAmount"
    NEUTRAL_DETERGENT_TYPE = "neutralDetergentType"
    NEW_VERSION_AVAILABLE = "newVersionAvailable"
    NOTIFICATION_TEMPLATE_I_D = "notificationTemplateID"
    NUMBER_OF_CONNECTED_DEVICES = "numberOfConnectedDevices"
    ODOR_LEVEL = "odorLevel"
    OPERATING_STATE = "operatingState"
    OPERATION_TIME = "operationTime"
    ORDER_THRESHOLD = "orderThreshold"
    ORIGINS = "origins"
    OS_VERSION = "mnos"
    OTN_D_U_I_D = "otnDUID"
    OUT_OF_SYNC_CHANGES = "outOfSyncChanges"
    OVEN_CAVITY_STATUS = "ovenCavityStatus"
    OVEN_JOB_STATE = "ovenJobState"
    OVEN_MODE = "ovenMode"
    OVEN_SETPOINT = "ovenSetpoint"
    OVEN_SETPOINT_RANGE = "ovenSetpointRange"
    PERIODIC_SENSING = "periodicSensing"
    PERIODIC_SENSING_INTERVAL = "periodicSensingInterval"
    PERIODIC_SENSING_STATUS = "periodicSensingStatus"
    PLAN = "plan"
    PLATFORM_ID = "pi"
    PLATFORM_VERSION = "mnpv"
    POWER = "power"
    POWER_CONSUMPTION = "powerConsumption"
    POWER_LEVEL = "powerLevel"
    PREDEFINED_COURSES = "predefinedCourses"
    PRESETS = "presets"
    PROGRESS = "progress"
    PROGRESS_PERCENTAGE = "progressPercentage"
    PROTOCOLS = "protocols"
    PROTOCOL_TYPE = "protocolType"
    QUANTITY = "quantity"
    RAPID_COOLING = "rapidCooling"
    RAPID_FREEZING = "rapidFreezing"
    RECOMMENDED_AMOUNT = "recommendedAmount"
    REFERENCE_TABLE = "referenceTable"
    REFRESH_RESULT = "refreshResult"
    REGION_CODE = "regionCode"
    REGULAR_DETERGENT_ALARM_ENABLED = "regularDetergentAlarmEnabled"
    REGULAR_DETERGENT_DOSAGE = "regularDetergentDosage"
    REGULAR_DETERGENT_INITIAL_AMOUNT = "regularDetergentInitialAmount"
    REGULAR_DETERGENT_ORDER_THRESHOLD = "regularDetergentOrderThreshold"
    REGULAR_DETERGENT_REMAINING_AMOUNT = "regularDetergentRemainingAmount"
    REGULAR_DETERGENT_TYPE = "regularDetergentType"
    REGULAR_SOFTENER_ALARM_ENABLED = "regularSoftenerAlarmEnabled"
    REGULAR_SOFTENER_DOSAGE = "regularSoftenerDosage"
    REGULAR_SOFTENER_INITIAL_AMOUNT = "regularSoftenerInitialAmount"
    REGULAR_SOFTENER_ORDER_THRESHOLD = "regularSoftenerOrderThreshold"
    REGULAR_SOFTENER_REMAINING_AMOUNT = "regularSoftenerRemainingAmount"
    REGULAR_SOFTENER_TYPE = "regularSoftenerType"
    RELEASE_YEAR = "releaseYear"
    REMAINING_AMOUNT = "remainingAmount"
    REMAINING_TIME = "remainingTime"
    REMAINING_TIME_STR = "remainingTimeStr"
    REMOTE_CONTROL_ENABLED = "remoteControlEnabled"
    REPEAT_MODE_ENABLED = "repeatModeEnabled"
    REPORT_STATE_PERIOD = "reportStatePeriod"
    REPORT_STATE_REALTIME = "reportStateRealtime"
    REPORT_STATE_REALTIME_PERIOD = "reportStateRealtimePeriod"
    REPRESENTATIVE_COMPONENT = "representativeComponent"
    RESERVABLE = "reservable"
    RESULT = "result"
    RINSE_PLUS = "rinsePlus"
    ROBOT_CLEANER_CLEANING_MODE = "robotCleanerCleaningMode"
    ROBOT_CLEANER_MOVEMENT = "robotCleanerMovement"
    ROBOT_CLEANER_TURBO_MODE = "robotCleanerTurboMode"
    ROLE = "role"
    SANITIZE = "sanitize"
    SANITIZING_WASH = "sanitizingWash"
    SATURATION = "saturation"
    SCHEDULED_JOBS = "scheduledJobs"
    SCHEDULED_PHASES = "scheduledPhases"
    SEARCHING_STATUS = "searchingStatus"
    SELECTED_ZONE = "selectedZone"
    SERIAL_NUMBER = "serialNumber"
    SERIAL_NUMBER_EXTRA = "serialNumberExtra"
    SETTABLE_MAX_FAN_SPEED = "settableMaxFanSpeed"
    SETTABLE_MIN_FAN_SPEED = "settableMinFanSpeed"
    SETUP_ID = "setupId"
    SIGNIN_PERMISSION = "signinPermission"
    SOFTENER_TYPE = "softenerType"
    SPECIALIZED_FUNCTION_CLASSIFICATION = "specializedFunctionClassification"
    SPECIFICATION = "specification"
    SPEC_VERSION = "icv"
    SPEED = "speed"
    SPEED_BOOSTER = "speedBooster"
    SPI_MODE = "spiMode"
    START_TIME = "startTime"
    STATE = "state"
    STATUS = "status"
    STEAM_SOAK = "steamSoak"
    STORM_WASH = "stormWash"
    SUB_DEVICES = "subDevices"
    SUPPORTED_ACTIONS = "supportedActions"
    SUPPORTED_AC_FAN_MODES = "supportedAcFanModes"
    SUPPORTED_AC_MODES = "supportedAcModes"
    SUPPORTED_AC_OPTIONAL_MODE = "supportedAcOptionalMode"
    SUPPORTED_AGING_METHODS = "supportedAgingMethods"
    SUPPORTED_AIR_QUALITY_HEALTH_CONCERNS = "supportedAirQualityHealthConcerns"
    SUPPORTED_ALARM_THRESHOLDS = "supportedAlarmThresholds"
    SUPPORTED_AMOUNT = "supportedAmount"
    SUPPORTED_AUTH_TYPE = "supportedAuthType"
    SUPPORTED_AUTOMATIC_EXECUTION_MODE = "supportedAutomaticExecutionMode"
    SUPPORTED_AUTOMATIC_EXECUTION_SETTING = "supportedAutomaticExecutionSetting"
    SUPPORTED_AUTO_CLEANING_MODES = "supportedAutoCleaningModes"
    SUPPORTED_BRIGHTNESS_LEVEL = "supportedBrightnessLevel"
    SUPPORTED_CLEANING_MODE = "supportedCleaningMode"
    SUPPORTED_COMMANDS = "supportedCommands"
    SUPPORTED_CONTEXTS = "supportedContexts"
    SUPPORTED_COOKTOP_OPERATING_STATE = "supportedCooktopOperatingState"
    SUPPORTED_COURSES = "supportedCourses"
    SUPPORTED_CYCLES = "supportedCycles"
    SUPPORTED_DENSITY = "supportedDensity"
    SUPPORTED_DRYER_DRY_LEVEL = "supportedDryerDryLevel"
    SUPPORTED_DRYING_TEMPERATURE = "supportedDryingTemperature"
    SUPPORTED_DRYING_TIME = "supportedDryingTime"
    SUPPORTED_ENERGY_SAVING_LEVELS = "supportedEnergySavingLevels"
    SUPPORTED_FAN_OSCILLATION_MODES = "supportedFanOscillationModes"
    SUPPORTED_FOCUS_AREAS = "supportedFocusAreas"
    SUPPORTED_FREEZER_CONVERT_MODES = "supportedFreezerConvertModes"
    SUPPORTED_FRIDGE_MODES = "supportedFridgeModes"
    SUPPORTED_HOOD_FAN_SPEED = "supportedHoodFanSpeed"
    SUPPORTED_LIGHTING_LEVELS = "supportedLightingLevels"
    SUPPORTED_LIST = "supportedList"
    SUPPORTED_MACHINE_STATES = "supportedMachineStates"
    SUPPORTED_MEAT_TYPES = "supportedMeatTypes"
    SUPPORTED_MODES = "supportedModes"
    SUPPORTED_OPERATING_STATE = "supportedOperatingState"
    SUPPORTED_OPERATING_STATES = "supportedOperatingStates"
    SUPPORTED_OPTIONS = "supportedOptions"
    SUPPORTED_OVEN_MODES = "supportedOvenModes"
    SUPPORTED_POWER_LEVELS = "supportedPowerLevels"
    SUPPORTED_THERMOSTAT_MODES = "supportedThermostatModes"
    SUPPORTED_WASHER_RINSE_CYCLES = "supportedWasherRinseCycles"
    SUPPORTED_WASHER_SOIL_LEVEL = "supportedWasherSoilLevel"
    SUPPORTED_WASHER_SPIN_LEVEL = "supportedWasherSpinLevel"
    SUPPORTED_WASHER_WATER_TEMPERATURE = "supportedWasherWaterTemperature"
    SUPPORTED_WASHING_TIMES = "supportedWashingTimes"
    SUPPORTED_WATER_LEVEL = "supportedWaterLevel"
    SUPPORTED_WATER_VALVE = "supportedWaterValve"
    SUPPORTED_WINDOW_SHADE_COMMANDS = "supportedWindowShadeCommands"
    SUPPORTED_WI_FI_FREQ = "supportedWiFiFreq"
    SUPPORT_LINK = "mnsl"
    SUPPORT_REPEAT_MODE = "supportRepeatMode"
    SWITCH = "switch"
    SYSTEM_TIME = "st"
    TAG_BUTTON = "tagButton"
    TAG_STATUS = "tagStatus"
    TARGET_MODULE = "targetModule"
    TEMPERATURE = "temperature"
    TEMPERATURE_RANGE = "temperatureRange"
    TEMPERATURE_SETPOINT = "temperatureSetpoint"
    THERMOSTAT_MODE = "thermostatMode"
    TIMED_CLEAN_DURATION = "timedCleanDuration"
    TIMED_CLEAN_DURATION_RANGE = "timedCleanDurationRange"
    TIME_LEFT_TO_START = "timeLeftToStart"
    TS_ID = "tsId"
    TYPE = "type"
    UNAVAILABLE_COMMANDS = "unavailableCommands"
    UPDATE_AVAILABLE = "updateAvailable"
    UWB_ACTIVATION = "uwbActivation"
    VACATION_MODE = "vacationMode"
    VENDOR_ID = "vid"
    VERSION = "version"
    VERSION_NUMBER = "versionNumber"
    VERY_FINE_DUST_FILTER_CAPACITY = "veryFineDustFilterCapacity"
    VERY_FINE_DUST_FILTER_LAST_RESET_DATE = "veryFineDustFilterLastResetDate"
    VERY_FINE_DUST_FILTER_RESET_TYPE = "veryFineDustFilterResetType"
    VERY_FINE_DUST_FILTER_STATUS = "veryFineDustFilterStatus"
    VERY_FINE_DUST_FILTER_USAGE = "veryFineDustFilterUsage"
    VERY_FINE_DUST_FILTER_USAGE_STEP = "veryFineDustFilterUsageStep"
    VERY_FINE_DUST_LEVEL = "veryFineDustLevel"
    VOLUME = "volume"
    WASHER_AUTO_DETERGENT = "washerAutoDetergent"
    WASHER_AUTO_SOFTENER = "washerAutoSoftener"
    WASHER_CYCLE = "washerCycle"
    WASHER_JOB_PHASE = "washerJobPhase"
    WASHER_JOB_STATE = "washerJobState"
    WASHER_RINSE_CYCLES = "washerRinseCycles"
    WASHER_SOIL_LEVEL = "washerSoilLevel"
    WASHER_SPIN_LEVEL = "washerSpinLevel"
    WASHER_WATER_TEMPERATURE = "washerWaterTemperature"
    WASHING_COURSE = "washingCourse"
    WASHING_TIME = "washingTime"
    WATER_CONSUMPTION = "waterConsumption"
    WATER_FILTER_CAPACITY = "waterFilterCapacity"
    WATER_FILTER_LAST_RESET_DATE = "waterFilterLastResetDate"
    WATER_FILTER_RESET_TYPE = "waterFilterResetType"
    WATER_FILTER_STATUS = "waterFilterStatus"
    WATER_FILTER_USAGE = "waterFilterUsage"
    WATER_FILTER_USAGE_STEP = "waterFilterUsageStep"
    WATER_LEVEL = "waterLevel"
    WATER_USAGE_MAX = "waterUsageMax"
    WATER_VALVE = "waterValve"
    WEIGHT = "weight"
    WELCOME_MESSAGE = "welcomeMessage"
    WINDOW_SHADE = "windowShade"
    ZONE_BOOSTER = "zoneBooster"
    ZONE_INFO = "zoneInfo"


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
    Capability.AIR_CONDITIONER_MODE: [
        Attribute.AVAILABLE_AC_MODES,
        Attribute.SUPPORTED_AC_MODES,
        Attribute.AIR_CONDITIONER_MODE,
    ],
    Capability.AIR_CONDITIONER_FAN_MODE: [
        Attribute.FAN_MODE,
        Attribute.SUPPORTED_AC_FAN_MODES,
        Attribute.AVAILABLE_AC_FAN_MODES,
    ],
    Capability.AIR_QUALITY_SENSOR: [Attribute.AIR_QUALITY],
    Capability.ALARM: [Attribute.ALARM],
    Capability.AUDIO_VOLUME: [Attribute.VOLUME],
    Capability.BATTERY: [Attribute.BATTERY, Attribute.QUANTITY, Attribute.TYPE],
    Capability.BYPASSABLE: [Attribute.BYPASS_STATUS],
    Capability.COLOR_CONTROL: [Attribute.COLOR, Attribute.HUE, Attribute.SATURATION],
    Capability.COLOR_TEMPERATURE: [
        Attribute.COLOR_TEMPERATURE,
        Attribute.COLOR_TEMPERATURE_RANGE,
    ],
    Capability.DOOR_CONTROL: [
        Attribute.DOOR,
    ],
    Capability.DUST_SENSOR: [Attribute.DUST_LEVEL, Attribute.FINE_DUST_LEVEL],
    Capability.ENERGY_METER: [Attribute.ENERGY],
    Capability.EXECUTE: [Attribute.DATA],
    Capability.FAN_OSCILLATION_MODE: [
        Attribute.SUPPORTED_FAN_OSCILLATION_MODES,
        Attribute.AVAILABLE_FAN_OSCILLATION_MODES,
        Attribute.FAN_OSCILLATION_MODE,
    ],
    Capability.FIRMWARE_UPDATE: [
        Attribute.LAST_UPDATE_STATUS_REASON,
        Attribute.AVAILABLE_VERSION,
        Attribute.LAST_UPDATE_STATUS,
        Attribute.SUPPORTED_COMMANDS,
        Attribute.STATE,
        Attribute.UPDATE_AVAILABLE,
        Attribute.CURRENT_VERSION,
        Attribute.LAST_UPDATE_TIME,
    ],
    Capability.GEOFENCE: [Attribute.ENABLE_STATE, Attribute.GEOFENCE, Attribute.NAME],
    Capability.GEOLOCATION: [
        Attribute.METHOD,
        Attribute.HEADING,
        Attribute.LATITUDE,
        Attribute.ACCURACY,
        Attribute.ALTITUDE_ACCURACY,
        Attribute.SPEED,
        Attribute.LONGITUDE,
        Attribute.LAST_UPDATE_TIME,
    ],
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
    Capability.ODOR_SENSOR: [Attribute.ODOR_LEVEL],
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
    Capability.POWER_METER: [Attribute.POWER],
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
    Capability.CONTACT_SENSOR: [Attribute.CONTACT],
    Capability.THERMOSTAT_COOLING_SETPOINT: [
        Attribute.COOLING_SETPOINT_RANGE,
        Attribute.COOLING_SETPOINT,
    ],
    Capability.REFRIGERATION: [
        Attribute.DEFROST,
        Attribute.RAPID_COOLING,
        Attribute.RAPID_FREEZING,
    ],
    Capability.ROBOT_CLEANER_TURBO_MODE: [Attribute.ROBOT_CLEANER_TURBO_MODE],
    Capability.ROBOT_CLEANER_MOVEMENT: [Attribute.ROBOT_CLEANER_MOVEMENT],
    Capability.ROBOT_CLEANER_CLEANING_MODE: [Attribute.ROBOT_CLEANER_CLEANING_MODE],
    Capability.VERY_FINE_DUST_SENSOR: [Attribute.VERY_FINE_DUST_LEVEL],
    Capability.WASHER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.WASHER_JOB_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.WINDOW_SHADE: [
        Attribute.WINDOW_SHADE,
        Attribute.SUPPORTED_WINDOW_SHADE_COMMANDS,
    ],
    # HCA capabilities
    Capability.HCA_DRYER_MODE: [Attribute.MODE, Attribute.SUPPORTED_MODES],
    Capability.HCA_WASHER_MODE: [
        Attribute.MODE,
        Attribute.SUPPORTED_MODES,
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
    Capability.SAMSUNG_CE_FOOD_DEFROST: [
        Attribute.SUPPORTED_OPTIONS,
        Attribute.FOOD_TYPE,
        Attribute.WEIGHT,
        Attribute.OPERATION_TIME,
        Attribute.REMAINING_TIME,
    ],
    Capability.SAMSUNG_CE_FRIDGE_PANTRY_INFO: [Attribute.NAME],
    Capability.SAMSUNG_CE_MEAT_AGING: [
        Attribute.ZONE_INFO,
        Attribute.SUPPORTED_MEAT_TYPES,
        Attribute.SUPPORTED_AGING_METHODS,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_FRIDGE_PANTRY_MODE: [
        Attribute.MODE,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.SAMSUNG_CE_CONNECTION_STATE: [
        Attribute.CONNECTION_STATE,
    ],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT: [
        Attribute.WEIGHT,
    ],
    Capability.SAMSUNG_CE_SCALE_SETTINGS: [Attribute.ENABLED],
    Capability.SAMSUNG_CE_UNAVAILABLE_CAPABILITIES: [Attribute.UNAVAILABLE_COMMANDS],
    Capability.SAMSUNG_CE_FREEZER_CONVERT_MODE: [
        Attribute.FREEZER_CONVERT_MODE,
        Attribute.FREEZER_CONVERT_MODE,
    ],
    Capability.SAMSUNG_CE_VIEW_INSIDE: [
        Attribute.SUPPORTED_FOCUS_AREAS,
        Attribute.CONTENTS,
        Attribute.LAST_UPDATED_TIME,
    ],
    Capability.SAMSUNG_CE_FRIDGE_FOOD_LIST: [
        Attribute.OUT_OF_SYNC_CHANGES,
        Attribute.REFRESH_RESULT,
    ],
    Capability.SAMSUNG_CE_FRIDGE_VACATION_MODE: [
        Attribute.VACATION_MODE,
    ],
    Capability.SAMSUNG_CE_SABBATH_MODE: [
        Attribute.SUPPORTED_ACTIONS,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_RUNESTONE_HOME_CONTEXT: [
        Attribute.SUPPORTED_CONTEXTS,
    ],
    Capability.SAMSUNG_CE_POWER_COOL: [
        Attribute.ACTIVATED,
    ],
    Capability.SAMSUNG_CE_POWER_FREEZE: [Attribute.ACTIVATED],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_OPERATING_STATE: [
        Attribute.SUPPORTED_OPERATING_STATE,
        Attribute.OPERATING_STATE,
        Attribute.CLEANING_STEP,
        Attribute.HOMING_REASON,
        Attribute.IS_MAP_BASED_OPERATION_AVAILABLE,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_CLEANING_MODE: [
        Attribute.SUPPORTED_CLEANING_MODE,
        Attribute.REPEAT_MODE_ENABLED,
        Attribute.SUPPORT_REPEAT_MODE,
        Attribute.CLEANING_MODE,
    ],
    Capability.SAMSUNG_CE_WASHER_DELAY_END: [
        Attribute.REMAINING_TIME,
        Attribute.MINIMUM_RESERVABLE_TIME,
    ],
    Capability.SAMSUNG_CE_WASHER_WATER_LEVEL: [
        Attribute.WATER_LEVEL,
        Attribute.SUPPORTED_WATER_LEVEL,
    ],
    Capability.SAMSUNG_CE_SOFTENER_AUTO_REPLENISHMENT: [
        Attribute.REGULAR_SOFTENER_TYPE,
        Attribute.REGULAR_SOFTENER_ALARM_ENABLED,
        Attribute.REGULAR_SOFTENER_INITIAL_AMOUNT,
        Attribute.REGULAR_SOFTENER_REMAINING_AMOUNT,
        Attribute.REGULAR_SOFTENER_DOSAGE,
        Attribute.REGULAR_SOFTENER_ORDER_THRESHOLD,
    ],
    Capability.SAMSUNG_CE_AUTO_DISPENSE_SOFTENER: [
        Attribute.REMAINING_AMOUNT,
        Attribute.AMOUNT,
        Attribute.SUPPORTED_DENSITY,
        Attribute.DENSITY,
        Attribute.SUPPORTED_AMOUNT,
    ],
    Capability.SAMSUNG_CE_AUTO_DISPENSE_DETERGENT: [
        Attribute.REMAINING_AMOUNT,
        Attribute.AMOUNT,
        Attribute.SUPPORTED_DENSITY,
        Attribute.DENSITY,
        Attribute.SUPPORTED_AMOUNT,
        Attribute.AVAILABLE_TYPES,
        Attribute.TYPE,
        Attribute.RECOMMENDED_AMOUNT,
    ],
    Capability.SAMSUNG_CE_WASHER_WATER_VALVE: [
        Attribute.WATER_VALVE,
        Attribute.SUPPORTED_WATER_VALVE,
    ],
    Capability.SAMSUNG_CE_WASHER_FREEZE_PREVENT: [
        Attribute.OPERATING_STATE,
    ],
    Capability.SAMSUNG_CE_WASHER_CYCLE: [
        Attribute.SUPPORTED_CYCLES,
        Attribute.WASHER_CYCLE,
        Attribute.REFERENCE_TABLE,
        Attribute.SPECIALIZED_FUNCTION_CLASSIFICATION,
    ],
    Capability.SAMSUNG_CE_WASHER_OPERATING_STATE: [
        Attribute.WASHER_JOB_STATE,
        Attribute.OPERATING_STATE,
        Attribute.SUPPORTED_OPERATING_STATES,
        Attribute.SCHEDULED_JOBS,
        Attribute.SCHEDULED_PHASES,
        Attribute.PROGRESS,
        Attribute.REMAINING_TIME_STR,
        Attribute.WASHER_JOB_PHASE,
        Attribute.OPERATION_TIME,
        Attribute.REMAINING_TIME,
    ],
    Capability.SAMSUNG_CE_DETERGENT_AUTO_REPLENISHMENT: [
        Attribute.NEUTRAL_DETERGENT_TYPE,
        Attribute.REGULAR_DETERGENT_REMAINING_AMOUNT,
        Attribute.BABY_DETERGENT_REMAINING_AMOUNT,
        Attribute.NEUTRAL_DETERGENT_REMAINING_AMOUNT,
        Attribute.NEUTRAL_DETERGENT_ALARM_ENABLED,
        Attribute.NEUTRAL_DETERGENT_ORDER_THRESHOLD,
        Attribute.BABY_DETERGENT_INITIAL_AMOUNT,
        Attribute.BABY_DETERGENT_TYPE,
        Attribute.NEUTRAL_DETERGENT_INITIAL_AMOUNT,
        Attribute.REGULAR_DETERGENT_DOSAGE,
        Attribute.BABY_DETERGENT_DOSAGE,
        Attribute.REGULAR_DETERGENT_ORDER_THRESHOLD,
        Attribute.REGULAR_DETERGENT_TYPE,
        Attribute.REGULAR_DETERGENT_INITIAL_AMOUNT,
        Attribute.REGULAR_DETERGENT_ALARM_ENABLED,
        Attribute.NEUTRAL_DETERGENT_DOSAGE,
        Attribute.BABY_DETERGENT_ORDER_THRESHOLD,
        Attribute.BABY_DETERGENT_ALARM_ENABLED,
    ],
    Capability.SAMSUNG_CE_SOFTENER_ORDER: [
        Attribute.ALARM_ENABLED,
        Attribute.ORDER_THRESHOLD,
    ],
    Capability.SAMSUNG_CE_WASHER_BUBBLE_SOAK: [Attribute.STATUS],
    Capability.SAMSUNG_CE_WASHER_CYCLE_PRESET: [
        Attribute.MAX_NUMBER_OF_PRESETS,
        Attribute.PRESETS,
    ],
    Capability.SAMSUNG_CE_SOFTENER_STATE: [
        Attribute.REMAINING_AMOUNT,
        Attribute.DOSAGE,
        Attribute.SOFTENER_TYPE,
        Attribute.INITIAL_AMOUNT,
    ],
    Capability.SAMSUNG_CE_ENERGY_PLANNER: [Attribute.DATA, Attribute.PLAN],
    Capability.SAMSUNG_CE_WASHER_WASHING_TIME: [
        Attribute.SUPPORTED_WASHING_TIMES,
        Attribute.WASHING_TIME,
    ],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_BEEP: [Attribute.BEEP],
    Capability.SAMSUNG_CE_INDIVIDUAL_CONTROL_LOCK: [Attribute.LOCK_STATE],
    Capability.SAMSUNG_CE_WELCOME_COOLING: [
        Attribute.LATEST_REQUEST_ID,
        Attribute.OPERATING_STATE,
    ],
    Capability.SAMSUNG_CE_SELF_CHECK: [
        Attribute.RESULT,
        Attribute.SUPPORTED_ACTIONS,
        Attribute.PROGRESS,
        Attribute.ERRORS,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_AIR_QUALITY_HEALTH_CONCERN: [
        Attribute.SUPPORTED_AIR_QUALITY_HEALTH_CONCERNS,
        Attribute.AIR_QUALITY_HEALTH_CONCERN,
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
    Capability.SAMSUNG_CE_DUST_FILTER_ALARM: [
        Attribute.ALARM_THRESHOLD,
        Attribute.SUPPORTED_ALARM_THRESHOLDS,
    ],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_LIGHTING: [
        Attribute.SUPPORTED_LIGHTING_LEVELS,
        Attribute.LIGHTING,
    ],
    Capability.SAMSUNG_CE_BUTTON_DISPLAY_CONDITION: [
        Attribute.SWITCH,
    ],
    Capability.SAMSUNG_CE_ALWAYS_ON_SENSING: [Attribute.ORIGINS, Attribute.ALWAYS_ON],
    Capability.SAMSUNG_CE_WIFI_KIT_SUB_DEVICES: [
        Attribute.NUMBER_OF_CONNECTED_DEVICES,
        Attribute.SUB_DEVICES,
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
    Capability.CUSTOM_WASHER_SOIL_LEVEL: [
        Attribute.SUPPORTED_WASHER_SOIL_LEVEL,
        Attribute.WASHER_SOIL_LEVEL,
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
    Capability.CUSTOM_THERMOSTAT_SETPOINT_CONTROL: [
        Attribute.MINIMUM_SETPOINT,
        Attribute.MAXIMUM_SETPOINT,
    ],
    Capability.CUSTOM_FRIDGE_MODE: [
        Attribute.FRIDGE_MODE_VALUE,
        Attribute.FRIDGE_MODE,
        Attribute.SUPPORTED_FRIDGE_MODES,
    ],
    Capability.CUSTOM_DEVICE_REPORT_STATE_CONFIGURATION: [
        Attribute.REPORT_STATE_REALTIME_PERIOD,
        Attribute.REPORT_STATE_REALTIME,
        Attribute.REPORT_STATE_PERIOD,
    ],
    Capability.CUSTOM_DISABLED_COMPONENTS: [
        Attribute.DISABLED_COMPONENTS,
    ],
    Capability.CUSTOM_WASHER_WATER_TEMPERATURE: [
        Attribute.WASHER_WATER_TEMPERATURE,
        Attribute.SUPPORTED_WASHER_WATER_TEMPERATURE,
    ],
    Capability.CUSTOM_WASHER_AUTO_SOFTENER: [
        Attribute.WASHER_AUTO_SOFTENER,
    ],
    Capability.CUSTOM_WASHER_RINSE_CYCLES: [
        Attribute.WASHER_RINSE_CYCLES,
        Attribute.SUPPORTED_WASHER_RINSE_CYCLES,
    ],
    Capability.CUSTOM_WASHER_AUTO_DETERGENT: [
        Attribute.WASHER_AUTO_DETERGENT,
    ],
    Capability.CUSTOM_WASHER_SPIN_LEVEL: [
        Attribute.WASHER_SPIN_LEVEL,
        Attribute.SUPPORTED_WASHER_SPIN_LEVEL,
    ],
    Capability.CUSTOM_SPI_MODE: [Attribute.SPI_MODE],
    Capability.CUSTOM_AIR_CONDITIONER_OPTIONAL_MODE: [
        Attribute.SUPPORTED_AC_OPTIONAL_MODE,
        Attribute.AC_OPTIONAL_MODE,
    ],
    Capability.CUSTOM_PERIODIC_SENSING: [
        Attribute.AUTOMATIC_EXECUTION_SETTING,
        Attribute.AUTOMATIC_EXECUTION_MODE,
        Attribute.SUPPORTED_AUTOMATIC_EXECUTION_SETTING,
        Attribute.SUPPORTED_AUTOMATIC_EXECUTION_MODE,
        Attribute.PERIODIC_SENSING,
        Attribute.PERIODIC_SENSING_INTERVAL,
        Attribute.LAST_SENSING_TIME,
        Attribute.LAST_SENSING_LEVEL,
        Attribute.PERIODIC_SENSING_STATUS,
    ],
    Capability.CUSTOM_AUTO_CLEANING_MODE: [
        Attribute.SUPPORTED_AUTO_CLEANING_MODES,
        Attribute.TIMED_CLEAN_DURATION,
        Attribute.OPERATING_STATE,
        Attribute.TIMED_CLEAN_DURATION_RANGE,
        Attribute.SUPPORTED_OPERATING_STATES,
        Attribute.PROGRESS,
        Attribute.AUTO_CLEANING_MODE,
    ],
    Capability.CUSTOM_DUST_FILTER: [
        Attribute.DUST_FILTER_USAGE_STEP,
        Attribute.DUST_FILTER_USAGE,
        Attribute.DUST_FILTER_LAST_RESET_DATE,
        Attribute.DUST_FILTER_STATUS,
        Attribute.DUST_FILTER_CAPACITY,
        Attribute.DUST_FILTER_RESET_TYPE,
    ],
    Capability.CUSTOM_VERY_FINE_DUST_FILTER: [
        Attribute.VERY_FINE_DUST_FILTER_STATUS,
        Attribute.VERY_FINE_DUST_FILTER_RESET_TYPE,
        Attribute.VERY_FINE_DUST_FILTER_USAGE,
        Attribute.VERY_FINE_DUST_FILTER_LAST_RESET_DATE,
        Attribute.VERY_FINE_DUST_FILTER_USAGE_STEP,
        Attribute.VERY_FINE_DUST_FILTER_CAPACITY,
    ],
    Capability.CUSTOM_AIR_CONDITIONER_ODOR_CONTROLLER: [
        Attribute.AIR_CONDITIONER_ODOR_CONTROLLER_PROGRESS,
        Attribute.AIR_CONDITIONER_ODOR_CONTROLLER_STATE,
    ],
    Capability.CUSTOM_AIR_CONDITIONER_TROPICAL_NIGHT_MODE: [
        Attribute.AC_TROPICAL_NIGHT_MODE_LEVEL
    ],
    Capability.CUSTOM_ELECTRIC_HEPA_FILTER: [
        Attribute.ELECTRIC_HEPA_FILTER_CAPACITY,
        Attribute.ELECTRIC_HEPA_FILTER_USAGE_STEP,
        Attribute.ELECTRIC_HEPA_FILTER_LAST_RESET_DATE,
        Attribute.ELECTRIC_HEPA_FILTER_STATUS,
        Attribute.ELECTRIC_HEPA_FILTER_USAGE,
        Attribute.ELECTRIC_HEPA_FILTER_RESET_TYPE,
    ],
    Capability.CUSTOM_DEODOR_FILTER: [
        Attribute.DEODOR_FILTER_CAPACITY,
        Attribute.DEODOR_FILTER_LAST_RESET_DATE,
        Attribute.DEODOR_FILTER_STATUS,
        Attribute.DEODOR_FILTER_RESET_TYPE,
        Attribute.DEODOR_FILTER_USAGE,
        Attribute.DEODOR_FILTER_USAGE_STEP,
    ],
    Capability.CUSTOM_DO_NOT_DISTURB_MODE: [
        Attribute.DO_NOT_DISTURB,
        Attribute.START_TIME,
        Attribute.END_TIME,
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
    Capability.SEC_CALM_CONNECTION_CARE: [
        Attribute.ROLE,
        Attribute.PROTOCOLS,
        Attribute.VERSION,
    ],
    # Tag capabilities
    Capability.TAG_E2E_ENCRYPTION: [
        Attribute.ENCRYPTION,
    ],
    Capability.TAG_UPDATED_INFO: [Attribute.CONNECTION],
    Capability.TAG_SEARCHING_STATUS: [
        Attribute.SEARCHING_STATUS,
    ],
    Capability.TAG_TAG_STATUS: [
        Attribute.TAG_STATUS,
        Attribute.CONNECTED_USER_ID,
        Attribute.CONNECTED_DEVICE_ID,
    ],
    Capability.TAG_TAG_BUTTON: [Attribute.TAG_BUTTON],
    Capability.TAG_UWB_ACTIVATION: [Attribute.UWB_ACTIVATION],
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
