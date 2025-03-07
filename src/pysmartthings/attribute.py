"""Attribute model."""

from enum import StrEnum

from pysmartthings.capability import Capability


class Attribute(StrEnum):
    """Attribute model."""

    ACCELERATION = "acceleration"
    ACCURACY = "accuracy"
    ACTIVATED = "activated"
    ACTIVITY = "activity"
    AC_OPTIONAL_MODE = "acOptionalMode"
    AC_TROPICAL_NIGHT_MODE_LEVEL = "acTropicalNightModeLevel"
    ADD_RINSE = "addRinse"
    AIR_CONDITIONER_MODE = "airConditionerMode"
    AIR_CONDITIONER_ODOR_CONTROLLER_PROGRESS = "airConditionerOdorControllerProgress"
    AIR_CONDITIONER_ODOR_CONTROLLER_STATE = "airConditionerOdorControllerState"
    AIR_PURIFIER_FAN_MODE = "airPurifierFanMode"
    AIR_QUALITY = "airQuality"
    AIR_QUALITY_HEALTH_CONCERN = "airQualityHealthConcern"
    ALARM = "alarm"
    ALARM_ENABLED = "alarmEnabled"
    ALARM_THRESHOLD = "alarmThreshold"
    ALTITUDE_ACCURACY = "altitudeAccuracy"
    ALWAYS_ON = "alwaysOn"
    AMOUNT = "amount"
    ASSOCIATION_GROUP_FOUR = "associationGroupFour"
    ASSOCIATION_GROUP_THREE = "associationGroupThree"
    ASSOCIATION_GROUP_TWO = "associationGroupTwo"
    ATMOSPHERIC_PRESSURE = "atmosphericPressure"
    AUDIO_ONLY = "audioOnly"
    AUDIO_TRACK_DATA = "audioTrackData"
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
    BMI_MEASUREMENT = "bmiMeasurement"
    BODY_WEIGHT_MEASUREMENT = "bodyWeightMeasurement"
    BRIGHTNESS_INTENSITY = "brightnessIntensity"
    BRIGHTNESS_LEVEL = "brightnessLevel"
    BUTTON = "button"
    BYPASS_STATUS = "bypassStatus"
    CALL_STATUS = "callStatus"
    CAMERA = "camera"
    CAPTURE_TIME = "captureTime"
    CARBON_DIOXIDE = "carbonDioxide"
    CARBON_DIOXIDE_HEALTH_CONCERN = "carbonDioxideHealthConcern"
    CARBON_MONOXIDE = "carbonMonoxide"
    CARBON_MONOXIDE_LEVEL = "carbonMonoxideLevel"
    CATEGORY = "category"
    CHANNEL = "channel"
    CHECK_INTERVAL = "checkInterval"
    CHIME = "chime"
    CIRCADIAN = "circadian"
    CLEANING_MODE = "cleaningMode"
    CLEANING_STEP = "cleaningStep"
    CLIP = "clip"
    CODE_CHANGED = "codeChanged"
    CODE_LENGTH = "codeLength"
    CODE_REPORT = "codeReport"
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
    COOKER_MODE = "cookerMode"
    COOKER_STATE = "cookerState"
    COOKTOP_OPERATING_STATE = "cooktopOperatingState"
    COOLING_SETPOINT = "coolingSetpoint"
    COOLING_SETPOINT_RANGE = "coolingSetpointRange"
    COURSE = "course"
    CREATE_DEVICE = "createDevice"
    CURRENT = "current"
    CURRENT_TIME_PERIOD = "currentTimePeriod"
    CURRENT_TWILIGHT = "currentTwilight"
    CURRENT_VERSION = "currentVersion"
    CUSTOM_COURSE_CANDIDATES = "customCourseCandidates"
    DATA = "data"
    DATA_MODEL_VERSION = "dmv"
    DAY_LENGTH = "dayLength"
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
    DESIRED_TEMPERATURE = "desiredTemperature"
    DETAIL_NAME = "detailName"
    DETECTED = "detected"
    DETECTION_PROXIMITY = "detectionProximity"
    DETERGENT_TYPE = "detergentType"
    DEVICE_CONNECTION_STATE = "deviceConnectionState"
    DEVICE_ICE = "deviceIce"
    DEVICE_ID = "di"
    DEVICE_NAME = "n"
    DEVICE_NETWORK_ID = "deviceNetworkId"
    DEVICE_WATCH_DEVICE_STATUS = "DeviceWatch-DeviceStatus"
    DEVICE_WATCH_ENROLL = "DeviceWatch-Enroll"
    DEWPOINT = "dewpoint"
    DISABLED_CAPABILITIES = "disabledCapabilities"
    DISABLED_COMPONENTS = "disabledComponents"
    DISHWASHER_DELAY_START_TIME = "dishwasherDelayStartTime"
    DISHWASHER_JOB_STATE = "dishwasherJobState"
    DISHWASHER_OPERATING_PERCENTAGE = "dishwasherOperatingPercentage"
    DISHWASHER_OPERATING_PROGRESS = "dishwasherOperatingProgress"
    DOOR = "door"
    DOOR_STATE = "doorState"
    DOSAGE = "dosage"
    DOWNLINK_SPEED = "downlinkSpeed"
    DO_NOT_DISTURB = "doNotDisturb"
    DRIVER_STATE = "driverState"
    DRIVER_VERSION = "driverVersion"
    DRYER_AUTO_CYCLE_LINK = "dryerAutoCycleLink"
    DRYER_CYCLE = "dryerCycle"
    DRYER_DRY_LEVEL = "dryerDryLevel"
    DRYER_JOB_STATE = "dryerJobState"
    DRYER_MODE = "dryerMode"
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
    DUST_HEALTH_CONCERN = "dustHealthConcern"
    DUST_LEVEL = "dustLevel"
    EFFECTS_SET_COMMAND = "effectsSetCommand"
    ELAPSED_TIME = "elapsedTime"
    ELECTRIC_HEPA_FILTER_CAPACITY = "electricHepaFilterCapacity"
    ELECTRIC_HEPA_FILTER_LAST_RESET_DATE = "electricHepaFilterLastResetDate"
    ELECTRIC_HEPA_FILTER_RESET_TYPE = "electricHepaFilterResetType"
    ELECTRIC_HEPA_FILTER_STATUS = "electricHepaFilterStatus"
    ELECTRIC_HEPA_FILTER_USAGE = "electricHepaFilterUsage"
    ELECTRIC_HEPA_FILTER_USAGE_STEP = "electricHepaFilterUsageStep"
    ENABLED = "enabled"
    ENABLE_STATE = "enableState"
    ENCRYPTED = "encrypted"
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
    EP_EVENT = "epEvent"
    EP_INFO = "epInfo"
    EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT = "equivalentCarbonDioxideMeasurement"
    ERROR = "error"
    ERRORS = "errors"
    ERROR_CODE = "errorCode"
    EVENT = "event"
    EVEN_ODD_DAY = "evenOddDay"
    EXECUTABLE_SERVICE_LIST = "executableServiceList"
    FADE = "fade"
    FAN_MODE = "fanMode"
    FAN_OSCILLATION_MODE = "fanOscillationMode"
    FAN_SPEED = "fanSpeed"
    FILTER_LIFE_REMAINING = "filterLifeRemaining"
    FILTER_STATUS = "filterStatus"
    FINE_DUST_HEALTH_CONCERN = "fineDustHealthConcern"
    FINE_DUST_LEVEL = "fineDustLevel"
    FIRMWARE_VERSION = "firmwareVersion"
    FOOD_TYPE = "foodType"
    FORCED_ON_LEVEL = "forcedOnLevel"
    FORMALDEHYDE_HEALTH_CONCERN = "formaldehydeHealthConcern"
    FORMALDEHYDE_LEVEL = "formaldehydeLevel"
    FREEZER_CONVERT_MODE = "freezerConvertMode"
    FRIDGE_MODE = "fridgeMode"
    FRIDGE_MODE_VALUE = "fridgeModeValue"
    FUEL = "fuel"
    GAS = "gas"
    GAS_METER = "gasMeter"
    GAS_METER_CALORIFIC = "gasMeterCalorific"
    GAS_METER_CONVERSION = "gasMeterConversion"
    GAS_METER_PRECISION = "gasMeterPrecision"
    GAS_METER_TIME = "gasMeterTime"
    GAS_METER_VOLUME = "gasMeterVolume"
    GEOFENCE = "geofence"
    GET_GROUPS = "getGroups"
    GROUP_ID = "groupId"
    GROUP_MUTE = "groupMute"
    GROUP_PRIMARY_DEVICE_ID = "groupPrimaryDeviceId"
    GROUP_ROLE = "groupRole"
    GROUP_VOLUME = "groupVolume"
    HARDWARE_FAULT = "hardwareFault"
    HARDWARE_VERSION = "mnhw"
    HEADING = "heading"
    HEALTH_STATUS = "healthStatus"
    HEATED_DRY = "heatedDry"
    HEATING_SETPOINT = "heatingSetpoint"
    HEATING_SETPOINT_RANGE = "heatingSetpointRange"
    HEPA_FILTER_CAPACITY = "hepaFilterCapacity"
    HEPA_FILTER_LAST_RESET_DATE = "hepaFilterLastResetDate"
    HEPA_FILTER_RESET_TYPE = "hepaFilterResetType"
    HEPA_FILTER_STATUS = "hepaFilterStatus"
    HEPA_FILTER_USAGE = "hepaFilterUsage"
    HEPA_FILTER_USAGE_STEP = "hepaFilterUsageStep"
    HIGH_TEMP_WASH = "highTempWash"
    HOMING_REASON = "homingReason"
    HOOD_FAN_SPEED = "hoodFanSpeed"
    HOT_AIR_DRY = "hotAirDry"
    HUE = "hue"
    HUMIDIFIER_MODE = "humidifierMode"
    HUMIDITY = "humidity"
    ILLUMINANCE = "illuminance"
    IMAGE = "image"
    IME_ADV_SUPPORTED = "imeAdvSupported"
    INFRARED_LEVEL = "infraredLevel"
    INITIAL_AMOUNT = "initialAmount"
    INPUT_SOURCE = "inputSource"
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
    LEVEL_STEPS = "levelSteps"
    LIGHTING = "lighting"
    LIGHTING_MODE = "lightningMode"
    LOCAL_DATE = "localDate"
    LOCAL_DATE_ONE = "localDateOne"
    LOCAL_DATE_TWO = "localDateTwo"
    LOCAL_DAY = "localDay"
    LOCAL_DAY_TWO = "localDayTwo"
    LOCAL_HOUR = "localHour"
    LOCAL_HOUR_OFFSET = "localHourOffset"
    LOCAL_HOUR_TWO = "localHourTwo"
    LOCAL_MONTH = "localMonth"
    LOCAL_MONTH_DAY_ONE = "localMonthDayOne"
    LOCAL_MONTH_DAY_TWO = "localMonthDayTwo"
    LOCAL_MONTH_TWO = "localMonthTwo"
    LOCAL_WEEK_DAY = "localWeekDay"
    LOCAL_YEAR = "localYear"
    LOCK = "lock"
    LOCK_CODES = "lockCodes"
    LOCK_STATE = "lockState"
    LOG_TYPE = "logType"
    LONGITUDE = "longitude"
    LQI = "lqi"
    MACHINE_STATE = "machineState"
    MANUFACTURER_DETAILS_LINK = "mnml"
    MANUFACTURER_NAME = "mnmn"
    MANUFACTURE_DATE = "mndt"
    MASTER_NAME = "masterName"
    MAXIMUM_SETPOINT = "maximumSetpoint"
    MAX_CODES = "maxCodes"
    MAX_CODE_LENGTH = "maxCodeLength"
    MAX_NUMBER_OF_PRESETS = "maxNumberOfPresets"
    MEDIA_OUTPUT_SUPPORTED = "mediaOutputSupported"
    MENU = "menu"
    METHOD = "method"
    MESSAGE = "message"
    MICOM_ASSAY_CODE = "micomAssayCode"
    MINIMUM_RESERVABLE_TIME = "minimumReservableTime"
    MINIMUM_SETPOINT = "minimumSetpoint"
    MIN_CODE_LENGTH = "minCodeLength"
    MIN_VERSION = "minVersion"
    MIRROR_GROUP_FUNCTION = "mirrorGroupFunction"
    MN_ID = "mnId"
    MOBILE_CAM_SUPPORTED = "mobileCamSupported"
    MODE = "mode"
    MODEL_CLASSIFICATION_CODE = "modelClassificationCode"
    MODEL_CODE = "modelCode"
    MODEL_NAME = "modelName"
    MODEL_NUMBER = "mnmo"
    MOLD_HEALTH_CONCERN = "moldHealthConcern"
    MOTION = "motion"
    MUTE = "mute"
    NAME = "name"
    NEUTRAL_DETERGENT_ALARM_ENABLED = "neutralDetergentAlarmEnabled"
    NEUTRAL_DETERGENT_DOSAGE = "neutralDetergentDosage"
    NEUTRAL_DETERGENT_INITIAL_AMOUNT = "neutralDetergentInitialAmount"
    NEUTRAL_DETERGENT_ORDER_THRESHOLD = "neutralDetergentOrderThreshold"
    NEUTRAL_DETERGENT_REMAINING_AMOUNT = "neutralDetergentRemainingAmount"
    NEUTRAL_DETERGENT_TYPE = "neutralDetergentType"
    NEW_VERSION_AVAILABLE = "newVersionAvailable"
    NITROGEN_DIOXIDE = "nitrogenDioxide"
    NITROGEN_DIOXIDE_HEALTH_CONCERN = "nitrogenDioxideHealthConcern"
    NOTIFICATION_TEMPLATE_I_D = "notificationTemplateID"
    NUMBER_OF_BUTTONS = "numberOfButtons"
    NUMBER_OF_CONNECTED_DEVICES = "numberOfConnectedDevices"
    OCCUPANCY = "occupancy"
    OCF_FIRMWARE_VERSION = "mnfv"
    OCF_RESOURCE_UPDATED_TIME = "ocfResourceUpdatedTime"
    OCF_RESOURCE_VERSION = "ocfResourceVersion"
    ODOR_LEVEL = "odorLevel"
    OPERATING_STATE = "operatingState"
    OPERATION_MODE = "operationMode"
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
    OZONE = "ozone"
    OZONE_HEALTH_CONCERN = "ozoneHealthConcern"
    PANIC_ALARM = "panicAlarm"
    PERIODIC_SENSING = "periodicSensing"
    PERIODIC_SENSING_INTERVAL = "periodicSensingInterval"
    PERIODIC_SENSING_STATUS = "periodicSensingStatus"
    PEST_CONTROL = "pestControl"
    PH = "pH"
    PICTURE_MODE = "pictureMode"
    PLAN = "plan"
    PLATFORM_ID = "pi"
    PLATFORM_VERSION = "mnpv"
    PLAYBACK_REPEAT_MODE = "playbackRepeatMode"
    PLAYBACK_SHUFFLE = "playbackShuffle"
    PLAYBACK_STATUS = "playbackStatus"
    POWER = "power"
    POWER_CONSUMPTION = "powerConsumption"
    POWER_LEVEL = "powerLevel"
    POWER_SOURCE = "powerSource"
    PRECIPITATION_INTENSITY = "precipitationIntensity"
    PREDEFINED_COURSES = "predefinedCourses"
    PRESENCE = "presence"
    PRESETS = "presets"
    PROGRESS = "progress"
    PROGRESS_PERCENTAGE = "progressPercentage"
    PROG_OFF = "progOff"
    PROG_ON = "progOn"
    PROTOCOLS = "protocols"
    PROTOCOL_TYPE = "protocolType"
    QUANTITY = "quantity"
    RADON_LEVEL = "radonLevel"
    RANDOM_NEXT = "randomNext"
    RANDOM_ON_OFF = "randomOnOff"
    RAPID_COOLING = "rapidCooling"
    RAPID_FREEZING = "rapidFreezing"
    RECOMMENDED_AMOUNT = "recommendedAmount"
    REFERENCE_TABLE = "referenceTable"
    REFRESH_RESULT = "refreshResult"
    REFRIGERATION_SETPOINT = "refrigerationSetpoint"
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
    REMOTELESS_SUPPORTED = "remotelessSupported"
    REMOTE_CONTROL_ENABLED = "remoteControlEnabled"
    REPEAT_MODE_ENABLED = "repeatModeEnabled"
    REPORT_STATE_PERIOD = "reportStatePeriod"
    REPORT_STATE_REALTIME = "reportStateRealtime"
    REPORT_STATE_REALTIME_PERIOD = "reportStateRealtimePeriod"
    REPRESENTATIVE_COMPONENT = "representativeComponent"
    REQUEST_ID = "requestId"
    RESERVABLE = "reservable"
    RESULT = "result"
    RINSE_MODE = "rinseMode"
    RINSE_PLUS = "rinsePlus"
    ROBOT_CLEANER_CLEANING_MODE = "robotCleanerCleaningMode"
    ROBOT_CLEANER_MOVEMENT = "robotCleanerMovement"
    ROBOT_CLEANER_TURBO_MODE = "robotCleanerTurboMode"
    ROLE = "role"
    RSSI = "rssi"
    SANITIZE = "sanitize"
    SANITIZING_WASH = "sanitizingWash"
    SATURATION = "saturation"
    SCAN_CODES = "scanCodes"
    SCHEDULABLE_MENUS = "schedulableMenus"
    SCHEDULED_JOBS = "scheduledJobs"
    SCHEDULED_PHASES = "scheduledPhases"
    SCHEDULED_TIME = "scheduledTime"
    SCHEDULING_ENABLED = "schedulingEnabled"
    SDP_ANSWER = "sdpAnswer"
    SEARCHING_STATUS = "searchingStatus"
    SECURITY_SYSTEM_STATUS = "securitySystemStatus"
    SELECTED_APP_ID = "selectedAppId"
    SELECTED_MODE = "selectedMode"
    SELECTED_ZONE = "selectedZone"
    SENSOR_STATUS = "sensorStatus"
    SERIAL_NUMBER = "serialNumber"
    SERIAL_NUMBER_EXTRA = "serialNumberExtra"
    SETTABLE_MAX_FAN_SPEED = "settableMaxFanSpeed"
    SETTABLE_MIN_FAN_SPEED = "settableMinFanSpeed"
    SETTINGS = "settings"
    SETUP_ID = "setupId"
    SHADE_LEVEL = "shadeLevel"
    SIGNAL_METRICS = "signalMetrics"
    SIGNIN_PERMISSION = "signinPermission"
    SLEEPING = "sleeping"
    SLOT_STATE = "slotState"
    SMOKE = "smoke"
    SOFTENER_TYPE = "softenerType"
    SOUND = "sound"
    SOUND_DETECTED = "soundDetected"
    SOUND_DETECTION_STATE = "soundDetectionState"
    SOUND_MODE = "soundMode"
    SOUND_PRESSURE_LEVEL = "soundPressureLevel"
    SPECIALIZED_FUNCTION_CLASSIFICATION = "specializedFunctionClassification"
    SPECIFICATION = "specification"
    SPEC_VERSION = "icv"
    SPEED = "speed"
    SPEED_BOOSTER = "speedBooster"
    SPIN_SPEED = "spinSpeed"
    SPI_MODE = "spiMode"
    START_TIME = "startTime"
    STATE = "state"
    STATUS = "status"
    STATUS_MESSAGE = "statusMessage"
    STEAM_CLOSET_AUTO_CYCLE_LINK = "steamClosetAutoCycleLink"
    STEAM_CLOSET_CYCLE = "steamClosetCycle"
    STEAM_CLOSET_DELAY_END_TIME = "steamClosetDelayEndTime"
    STEAM_CLOSET_JOB_STATE = "steamClosetJobState"
    STEAM_CLOSET_MACHINE_STATE = "steamClosetMachineState"
    STEAM_CLOSET_WRINKLE_PREVENT = "steamClosetWrinklePrevent"
    STEAM_SOAK = "steamSoak"
    STORM_WASH = "stormWash"
    STREAM = "stream"
    STREAM_CONTROL = "streamControl"
    STUN_URL = "stunUrl"
    SUB_DEVICES = "subDevices"
    SUN_AZIMUTH_ANGLE = "sunAzimuthAngle"
    SUN_ELEVATION_ANGLE = "sunElevationAngle"
    SUN_RISE = "sunRise"
    SUN_RISE_OFFSET = "sunRiseOffset"
    SUN_SET = "sunSet"
    SUN_SET_OFFSET = "sunSetOffset"
    SUPPORTED_ACTIONS = "supportedActions"
    SUPPORTED_AC_FAN_MODES = "supportedAcFanModes"
    SUPPORTED_AC_MODES = "supportedAcModes"
    SUPPORTED_AC_OPTIONAL_MODE = "supportedAcOptionalMode"
    SUPPORTED_AGING_METHODS = "supportedAgingMethods"
    SUPPORTED_AIR_PURIFIER_FAN_MODES = "supportedAirPurifierFanModes"
    SUPPORTED_AIR_QUALITY_HEALTH_CONCERNS = "supportedAirQualityHealthConcerns"
    SUPPORTED_ALARM_THRESHOLDS = "supportedAlarmThresholds"
    SUPPORTED_AMBIENT_APPS = "supportedAmbientApps"
    SUPPORTED_AMOUNT = "supportedAmount"
    SUPPORTED_ARGUMENTS = "supportedArguments"
    SUPPORTED_AUTH_TYPE = "supportedAuthType"
    SUPPORTED_AUTOMATIC_EXECUTION_MODE = "supportedAutomaticExecutionMode"
    SUPPORTED_AUTOMATIC_EXECUTION_SETTING = "supportedAutomaticExecutionSetting"
    SUPPORTED_AUTO_CLEANING_MODES = "supportedAutoCleaningModes"
    SUPPORTED_BRIGHTNESS_LEVEL = "supportedBrightnessLevel"
    SUPPORTED_BUTTON_VALUES = "supportedButtonValues"
    SUPPORTED_CLEANING_MODE = "supportedCleaningMode"
    SUPPORTED_COMMANDS = "supportedCommands"
    SUPPORTED_CONTEXTS = "supportedContexts"
    SUPPORTED_COOKER_MODES = "supportedCookerModes"
    SUPPORTED_COOKTOP_OPERATING_STATE = "supportedCooktopOperatingState"
    SUPPORTED_COURSES = "supportedCourses"
    SUPPORTED_CYCLES = "supportedCycles"
    SUPPORTED_DENSITY = "supportedDensity"
    SUPPORTED_DESIRED_TEMPERATURES = "supportedDesiredTemperatures"
    SUPPORTED_DETECTION_PROXIMITIES = "supportedDetectionProximities"
    SUPPORTED_DRYER_DRY_LEVEL = "supportedDryerDryLevel"
    SUPPORTED_DRYING_TEMPERATURE = "supportedDryingTemperature"
    SUPPORTED_DRYING_TIME = "supportedDryingTime"
    SUPPORTED_ENERGY_SAVING_LEVELS = "supportedEnergySavingLevels"
    SUPPORTED_EVENTS = "supportedEvents"
    SUPPORTED_FAN_OSCILLATION_MODES = "supportedFanOscillationModes"
    SUPPORTED_FEATURES = "supportedFeatures"
    SUPPORTED_FILTER_COMMANDS = "supportedFilterCommands"
    SUPPORTED_FOCUS_AREAS = "supportedFocusAreas"
    SUPPORTED_FREEZER_CONVERT_MODES = "supportedFreezerConvertModes"
    SUPPORTED_FRIDGE_MODES = "supportedFridgeModes"
    SUPPORTED_HOOD_FAN_SPEED = "supportedHoodFanSpeed"
    SUPPORTED_INPUT_SOURCES = "supportedInputSources"
    SUPPORTED_INPUT_SOURCES_MAP = "supportedInputSourcesMap"
    SUPPORTED_KEY_CODES = "supportedKeyCodes"
    SUPPORTED_LIGHTING_LEVELS = "supportedLightingLevels"
    SUPPORTED_LIST = "supportedList"
    SUPPORTED_LOCK_COMMANDS = "supportedLockCommands"
    SUPPORTED_LOCK_VALUES = "supportedLockValues"
    SUPPORTED_MACHINE_STATES = "supportedMachineStates"
    SUPPORTED_MEAT_TYPES = "supportedMeatTypes"
    SUPPORTED_MENUS = "supportedMenus"
    SUPPORTED_MODES = "supportedModes"
    SUPPORTED_MODE_MAP = "supportedModeMap"
    SUPPORTED_OPERATING_STATE = "supportedOperatingState"
    SUPPORTED_OPERATING_STATES = "supportedOperatingStates"
    SUPPORTED_OPTIONS = "supportedOptions"
    SUPPORTED_OVEN_MODES = "supportedOvenModes"
    SUPPORTED_PICTURE_MODES = "supportedPictureModes"
    SUPPORTED_PICTURE_MODES_MAP = "supportedPictureModesMap"
    SUPPORTED_PLAYBACK_COMMANDS = "supportedPlaybackCommands"
    SUPPORTED_POWER_LEVELS = "supportedPowerLevels"
    SUPPORTED_RINSE_MODES = "supportedRinseModes"
    SUPPORTED_SECURITY_SYSTEM_COMMANDS = "supportedSecuritySystemCommands"
    SUPPORTED_SECURITY_SYSTEM_STATUSES = "supportedSecuritySystemStatuses"
    SUPPORTED_SOUND_MODES = "supportedSoundModes"
    SUPPORTED_SOUND_MODES_MAP = "supportedSoundModesMap"
    SUPPORTED_SOUND_TYPES = "supportedSoundTypes"
    SUPPORTED_SPIN_SPEEDS = "supportedSpinSpeeds"
    SUPPORTED_STEAM_CLOSET_JOB_STATE = "supportedSteamClosetJobState"
    SUPPORTED_STEAM_CLOSET_MACHINE_STATE = "supportedSteamClosetMachineState"
    SUPPORTED_TEMPERATURE_LEVELS = "supportedTemperatureLevels"
    SUPPORTED_THERMOSTAT_FAN_MODES = "supportedThermostatFanModes"
    SUPPORTED_THERMOSTAT_MODES = "supportedThermostatModes"
    SUPPORTED_TRACK_CONTROL_COMMANDS = "supportedTrackControlCommands"
    SUPPORTED_UNLOCK_DIRECTIONS = "supportedUnlockDirections"
    SUPPORTED_VALUES = "supportedValues"
    SUPPORTED_WASHER_RINSE_CYCLES = "supportedWasherRinseCycles"
    SUPPORTED_WASHER_SOIL_LEVEL = "supportedWasherSoilLevel"
    SUPPORTED_WASHER_SPIN_LEVEL = "supportedWasherSpinLevel"
    SUPPORTED_WASHER_WATER_TEMPERATURE = "supportedWasherWaterTemperature"
    SUPPORTED_WASHING_TIMES = "supportedWashingTimes"
    SUPPORTED_WATER_LEVEL = "supportedWaterLevel"
    SUPPORTED_WATER_VALVE = "supportedWaterValve"
    SUPPORTED_WINDOW_SHADE_COMMANDS = "supportedWindowShadeCommands"
    SUPPORTED_WIND_MODES = "supportedWindModes"
    SUPPORTED_WI_FI_FREQ = "supportedWiFiFreq"
    SUPPORTS_POWER_ON_BY_OCF = "supportsPowerOnByOcf"
    SUPPORT_LINK = "mnsl"
    SUPPORT_REPEAT_MODE = "supportRepeatMode"
    SWITCH = "switch"
    SYSTEM_TIME = "st"
    TAG_BUTTON = "tagButton"
    TAG_STATUS = "tagStatus"
    TALKBACK = "talkback"
    TAMPER = "tamper"
    TARGET_MODULE = "targetModule"
    TEMPERATURE = "temperature"
    TEMPERATURE_ALARM = "temperatureAlarm"
    TEMPERATURE_LEVEL = "temperatureLevel"
    TEMPERATURE_RANGE = "temperatureRange"
    TEMPERATURE_SETPOINT = "temperatureSetpoint"
    TEMPERATURE_SETPOINT_RANGE = "temperatureSetpointRange"
    THERMOSTAT_FAN_MODE = "thermostatFanMode"
    THERMOSTAT_MODE = "thermostatMode"
    THERMOSTAT_OPERATING_STATE = "thermostatOperatingState"
    THERMOSTAT_SETPOINT = "thermostatSetpoint"
    THREE_AXIS = "threeAxis"
    TIMED_CLEAN_DURATION = "timedCleanDuration"
    TIMED_CLEAN_DURATION_RANGE = "timedCleanDurationRange"
    TIME_LEFT_TO_START = "timeLeftToStart"
    TOTAL_TIME = "totalTime"
    TS_ID = "tsId"
    TURN_INFO = "turnInfo"
    TVOC_LEVEL = "tvocLevel"
    TV_CHANNEL = "tvChannel"
    TV_CHANNEL_NAME = "tvChannelName"
    TYPE = "type"
    ULTRAVIOLET_INDEX = "ultravioletIndex"
    UNAVAILABLE_COMMANDS = "unavailableCommands"
    UPDATED_TIME = "updatedTime"
    UPDATE_AVAILABLE = "updateAvailable"
    UPLINK_SPEED = "uplinkSpeed"
    URI = "uri"
    USER_LOCATION = "userLocation"
    UWB_ACTIVATION = "uwbActivation"
    VACATION_MODE = "vacationMode"
    VALVE = "valve"
    VENDOR_ID = "vid"
    VERSION = "version"
    VERSION_NUMBER = "versionNumber"
    VERY_FINE_DUST_FILTER_CAPACITY = "veryFineDustFilterCapacity"
    VERY_FINE_DUST_FILTER_LAST_RESET_DATE = "veryFineDustFilterLastResetDate"
    VERY_FINE_DUST_FILTER_RESET_TYPE = "veryFineDustFilterResetType"
    VERY_FINE_DUST_FILTER_STATUS = "veryFineDustFilterStatus"
    VERY_FINE_DUST_FILTER_USAGE = "veryFineDustFilterUsage"
    VERY_FINE_DUST_FILTER_USAGE_STEP = "veryFineDustFilterUsageStep"
    VERY_FINE_DUST_HEALTH_CONCERN = "veryFineDustHealthConcern"
    VERY_FINE_DUST_LEVEL = "veryFineDustLevel"
    VOLTAGE = "voltage"
    VOLUME = "volume"
    WASHER_AUTO_DETERGENT = "washerAutoDetergent"
    WASHER_AUTO_SOFTENER = "washerAutoSoftener"
    WASHER_CYCLE = "washerCycle"
    WASHER_JOB_PHASE = "washerJobPhase"
    WASHER_JOB_STATE = "washerJobState"
    WASHER_MODE = "washerMode"
    WASHER_RINSE_CYCLES = "washerRinseCycles"
    WASHER_SOIL_LEVEL = "washerSoilLevel"
    WASHER_SPIN_LEVEL = "washerSpinLevel"
    WASHER_WATER_TEMPERATURE = "washerWaterTemperature"
    WASHING_COURSE = "washingCourse"
    WASHING_TIME = "washingTime"
    WATER = "water"
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
    WIFI_UPDATE_SUPPORT = "wifiUpdateSupport"
    WINDOW_SHADE = "windowShade"
    WIND_MODE = "windMode"
    ZONE_BOOSTER = "zoneBooster"
    ZONE_INFO = "zoneInfo"


CAPABILITY_ATTRIBUTES: dict[Capability, list[Attribute]] = {
    Capability.ACCELERATION_SENSOR: [Attribute.ACCELERATION],
    Capability.ACTIVITY_LIGHTING_MODE: [Attribute.LIGHTING_MODE],
    Capability.ACTIVITY_SENSOR: [Attribute.ACTIVITY],
    Capability.AIR_CONDITIONER_FAN_MODE: [
        Attribute.FAN_MODE,
        Attribute.SUPPORTED_AC_FAN_MODES,
        Attribute.AVAILABLE_AC_FAN_MODES,
    ],
    Capability.AIR_CONDITIONER_MODE: [
        Attribute.AVAILABLE_AC_MODES,
        Attribute.SUPPORTED_AC_MODES,
        Attribute.AIR_CONDITIONER_MODE,
    ],
    Capability.AIR_PURIFIER_FAN_MODE: [
        Attribute.AIR_PURIFIER_FAN_MODE,
        Attribute.SUPPORTED_AIR_PURIFIER_FAN_MODES,
    ],
    Capability.AIR_QUALITY_HEALTH_CONCERN: [Attribute.AIR_QUALITY_HEALTH_CONCERN],
    Capability.AIR_QUALITY_SENSOR: [Attribute.AIR_QUALITY],
    Capability.ALARM: [Attribute.ALARM],
    Capability.ATMOSPHERIC_PRESSURE_MEASUREMENT: [Attribute.ATMOSPHERIC_PRESSURE],
    Capability.AUDIO_MUTE: [Attribute.MUTE],
    Capability.AUDIO_STREAM: [Attribute.URI],
    Capability.AUDIO_TRACK_DATA: [
        Attribute.TOTAL_TIME,
        Attribute.AUDIO_TRACK_DATA,
        Attribute.ELAPSED_TIME,
    ],
    Capability.AUDIO_VOLUME: [Attribute.VOLUME],
    Capability.BATTERY: [Attribute.BATTERY, Attribute.QUANTITY, Attribute.TYPE],
    Capability.BODY_MASS_INDEX_MEASUREMENT: [Attribute.BMI_MEASUREMENT],
    Capability.BODY_WEIGHT_MEASUREMENT: [Attribute.BODY_WEIGHT_MEASUREMENT],
    Capability.BUTTON: [
        Attribute.BUTTON,
        Attribute.NUMBER_OF_BUTTONS,
        Attribute.SUPPORTED_BUTTON_VALUES,
    ],
    Capability.BYPASSABLE: [Attribute.BYPASS_STATUS],
    Capability.CARBON_DIOXIDE_HEALTH_CONCERN: [Attribute.CARBON_DIOXIDE_HEALTH_CONCERN],
    Capability.CARBON_DIOXIDE_MEASUREMENT: [Attribute.CARBON_DIOXIDE],
    Capability.CARBON_MONOXIDE_DETECTOR: [Attribute.CARBON_MONOXIDE],
    Capability.CARBON_MONOXIDE_MEASUREMENT: [Attribute.CARBON_MONOXIDE_LEVEL],
    Capability.CHIME: [Attribute.CHIME],
    Capability.COLOR_CONTROL: [Attribute.COLOR, Attribute.HUE, Attribute.SATURATION],
    Capability.COLOR_TEMPERATURE: [
        Attribute.COLOR_TEMPERATURE,
        Attribute.COLOR_TEMPERATURE_RANGE,
    ],
    Capability.CONTACT_SENSOR: [Attribute.CONTACT],
    Capability.CURRENT_MEASUREMENT: [Attribute.CURRENT],
    Capability.DEMAND_RESPONSE_LOAD_CONTROL: [
        Attribute.DEMAND_RESPONSE_LOAD_CONTROL_STATUS
    ],
    Capability.DEW_POINT: [Attribute.DEWPOINT],
    Capability.DISHWASHER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_MACHINE_STATES,
        Attribute.DISHWASHER_JOB_STATE,
    ],
    Capability.DOOR_CONTROL: [
        Attribute.DOOR,
    ],
    Capability.DRYER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
        Attribute.DRYER_JOB_STATE,
    ],
    Capability.DRYER_MODE: [Attribute.DRYER_MODE],
    Capability.DUST_SENSOR: [Attribute.DUST_LEVEL, Attribute.FINE_DUST_LEVEL],
    Capability.DUST_HEALTH_CONCERN: [Attribute.DUST_HEALTH_CONCERN],
    Capability.ELEVATOR_CALL: [Attribute.CALL_STATUS],
    Capability.ENERGY_METER: [Attribute.ENERGY],
    Capability.EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT: [
        Attribute.EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT
    ],
    Capability.EXECUTE: [Attribute.DATA],
    Capability.FAN_OSCILLATION_MODE: [
        Attribute.SUPPORTED_FAN_OSCILLATION_MODES,
        Attribute.AVAILABLE_FAN_OSCILLATION_MODES,
        Attribute.FAN_OSCILLATION_MODE,
    ],
    Capability.FAN_SPEED: [Attribute.FAN_SPEED],
    Capability.FILTER_STATE: [
        Attribute.FILTER_LIFE_REMAINING,
        Attribute.SUPPORTED_FILTER_COMMANDS,
    ],
    Capability.FILTER_STATUS: [Attribute.FILTER_STATUS],
    Capability.FINE_DUST_HEALTH_CONCERN: [Attribute.FINE_DUST_HEALTH_CONCERN],
    Capability.FINE_DUST_SENSOR: [Attribute.FINE_DUST_LEVEL],
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
    Capability.FORMALDEHYDE_HEALTH_CONCERN: [Attribute.FORMALDEHYDE_HEALTH_CONCERN],
    Capability.FORMALDEHYDE_MEASUREMENT: [Attribute.FORMALDEHYDE_LEVEL],
    Capability.GAS_DETECTOR: [Attribute.GAS],
    Capability.GAS_METER: [
        Attribute.GAS_METER,
        Attribute.GAS_METER_CALORIFIC,
        Attribute.GAS_METER_CONVERSION,
        Attribute.GAS_METER_PRECISION,
        Attribute.GAS_METER_TIME,
        Attribute.GAS_METER_VOLUME,
    ],
    Capability.HARDWARE_FAULT: [Attribute.HARDWARE_FAULT],
    Capability.HUMIDIFIER_MODE: [Attribute.HUMIDIFIER_MODE],
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
    Capability.ILLUMINANCE_MEASUREMENT: [Attribute.ILLUMINANCE],
    Capability.INFRARED_LEVEL: [Attribute.INFRARED_LEVEL],
    Capability.KEYPAD_INPUT: [Attribute.SUPPORTED_KEY_CODES],
    Capability.LAUNDRY_WASHER_RINSE_MODE: [
        Attribute.RINSE_MODE,
        Attribute.SUPPORTED_RINSE_MODES,
    ],
    Capability.LAUNDRY_WASHER_SPIN_SPEED: [
        Attribute.SPIN_SPEED,
        Attribute.SUPPORTED_SPIN_SPEEDS,
    ],
    Capability.LOCK_CODES: [
        Attribute.CODE_LENGTH,
        Attribute.MAX_CODES,
        Attribute.MAX_CODE_LENGTH,
        Attribute.CODE_CHANGED,
        Attribute.LOCK,
        Attribute.MIN_CODE_LENGTH,
        Attribute.CODE_REPORT,
        Attribute.SCAN_CODES,
        Attribute.LOCK_CODES,
    ],
    Capability.LOCK: [
        Attribute.SUPPORTED_UNLOCK_DIRECTIONS,
        Attribute.SUPPORTED_LOCK_VALUES,
        Attribute.LOCK,
        Attribute.SUPPORTED_LOCK_COMMANDS,
    ],
    Capability.MEDIA_GROUP: [
        Attribute.GROUP_MUTE,
        Attribute.GROUP_PRIMARY_DEVICE_ID,
        Attribute.GROUP_ID,
        Attribute.GROUP_VOLUME,
        Attribute.GROUP_ROLE,
    ],
    Capability.MEDIA_PLAYBACK: [
        Attribute.SUPPORTED_PLAYBACK_COMMANDS,
        Attribute.PLAYBACK_STATUS,
    ],
    Capability.MEDIA_PLAYBACK_REPEAT: [Attribute.PLAYBACK_REPEAT_MODE],
    Capability.MEDIA_PLAYBACK_SHUFFLE: [Attribute.PLAYBACK_SHUFFLE],
    Capability.MEDIA_PRESETS: [Attribute.PRESETS],
    Capability.MEDIA_INPUT_SOURCE: [
        Attribute.SUPPORTED_INPUT_SOURCES,
        Attribute.INPUT_SOURCE,
    ],
    Capability.MEDIA_TRACK_CONTROL: [Attribute.SUPPORTED_TRACK_CONTROL_COMMANDS],
    Capability.MODE: [
        Attribute.MODE,
        Attribute.SUPPORTED_ARGUMENTS,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.MOLD_HEALTH_CONCERN: [Attribute.MOLD_HEALTH_CONCERN],
    Capability.MOTION_SENSOR: [Attribute.MOTION],
    Capability.NETWORK_METER: [Attribute.DOWNLINK_SPEED, Attribute.UPLINK_SPEED],
    Capability.NITROGEN_DIOXIDE_HEALTH_CONCERN: [
        Attribute.NITROGEN_DIOXIDE_HEALTH_CONCERN
    ],
    Capability.NITROGEN_DIOXIDE_MEASUREMENT: [Attribute.NITROGEN_DIOXIDE],
    Capability.OBJECT_DETECTION: [Attribute.DETECTED, Attribute.SUPPORTED_VALUES],
    Capability.OCCUPANCY_SENSOR: [Attribute.OCCUPANCY],
    Capability.OCF: [
        Attribute.SYSTEM_TIME,
        Attribute.MANUFACTURE_DATE,
        Attribute.OCF_FIRMWARE_VERSION,
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
    Capability.OZONE_HEALTH_CONCERN: [Attribute.OZONE_HEALTH_CONCERN],
    Capability.OZONE_MEASUREMENT: [Attribute.OZONE],
    Capability.PANIC_ALARM: [Attribute.PANIC_ALARM],
    Capability.PEST_CONTROL: [Attribute.PEST_CONTROL],
    Capability.PH_MEASUREMENT: [Attribute.PH],
    Capability.POWER_CONSUMPTION_REPORT: [Attribute.POWER_CONSUMPTION],
    Capability.POWER_METER: [Attribute.POWER],
    Capability.POWER_SOURCE: [Attribute.POWER_SOURCE],
    Capability.PRECIPITATION_SENSOR: [Attribute.PRECIPITATION_INTENSITY],
    Capability.PRESENCE_SENSOR: [Attribute.PRESENCE],
    Capability.RADON_MEASUREMENT: [Attribute.RADON_LEVEL],
    Capability.REFRESH: [],
    Capability.REFRIGERATION: [
        Attribute.DEFROST,
        Attribute.RAPID_COOLING,
        Attribute.RAPID_FREEZING,
    ],
    Capability.REFRIGERATION_SETPOINT: [Attribute.REFRIGERATION_SETPOINT],
    Capability.RELATIVE_BRIGHTNESS: [Attribute.BRIGHTNESS_INTENSITY],
    Capability.RELATIVE_HUMIDITY_MEASUREMENT: [Attribute.HUMIDITY],
    Capability.REMOTE_CONTROL_STATUS: [Attribute.REMOTE_CONTROL_ENABLED],
    Capability.RICE_COOKER: [
        Attribute.COMPLETION_TIME,
        Attribute.COOKER_MODE,
        Attribute.COOKER_STATE,
        Attribute.EVENT,
        Attribute.MENU,
        Attribute.SCHEDULABLE_MENUS,
        Attribute.SCHEDULED_TIME,
        Attribute.SCHEDULING_ENABLED,
        Attribute.START_TIME,
        Attribute.SUPPORTED_COOKER_MODES,
        Attribute.SUPPORTED_EVENTS,
        Attribute.SUPPORTED_MENUS,
    ],
    Capability.ROBOT_CLEANER_CLEANING_MODE: [Attribute.ROBOT_CLEANER_CLEANING_MODE],
    Capability.ROBOT_CLEANER_MOVEMENT: [Attribute.ROBOT_CLEANER_MOVEMENT],
    Capability.ROBOT_CLEANER_OPERATING_STATE: [
        Attribute.OPERATING_STATE,
        Attribute.SUPPORTED_OPERATING_STATES,
    ],
    Capability.ROBOT_CLEANER_TURBO_MODE: [Attribute.ROBOT_CLEANER_TURBO_MODE],
    Capability.SECURITY_SYSTEM: [
        Attribute.ALARM,
        Attribute.SECURITY_SYSTEM_STATUS,
        Attribute.SENSOR_STATUS,
        Attribute.SUPPORTED_SECURITY_SYSTEM_COMMANDS,
        Attribute.SUPPORTED_SECURITY_SYSTEM_STATUSES,
    ],
    Capability.SIGNAL_STRENGTH: [Attribute.LQI, Attribute.RSSI],
    Capability.SLEEP_SENSOR: [Attribute.SLEEPING],
    Capability.SMOKE_DETECTOR: [Attribute.SMOKE],
    Capability.SOUND_DETECTION: [
        Attribute.SOUND_DETECTED,
        Attribute.SOUND_DETECTION_STATE,
        Attribute.SUPPORTED_SOUND_TYPES,
    ],
    Capability.SOUND_PRESSURE_LEVEL: [Attribute.SOUND_PRESSURE_LEVEL],
    Capability.SOUND_SENSOR: [Attribute.SOUND],
    Capability.SWITCH: [Attribute.SWITCH],
    Capability.SWITCH_LEVEL: [Attribute.LEVEL, Attribute.LEVEL_RANGE],
    Capability.TAMPER_ALERT: [Attribute.TAMPER],
    Capability.TEMPERATURE_ALARM: [Attribute.TEMPERATURE_ALARM],
    Capability.TEMPERATURE_LEVEL: [
        Attribute.TEMPERATURE_LEVEL,
        Attribute.SUPPORTED_TEMPERATURE_LEVELS,
    ],
    Capability.TEMPERATURE_MEASUREMENT: [
        Attribute.TEMPERATURE,
        Attribute.TEMPERATURE_RANGE,
    ],
    Capability.TEMPERATURE_SETPOINT: [
        Attribute.TEMPERATURE_SETPOINT,
        Attribute.TEMPERATURE_SETPOINT_RANGE,
    ],
    Capability.THERMOSTAT_COOLING_SETPOINT: [
        Attribute.COOLING_SETPOINT_RANGE,
        Attribute.COOLING_SETPOINT,
    ],
    Capability.THERMOSTAT_FAN_MODE: [
        Attribute.THERMOSTAT_FAN_MODE,
        Attribute.SUPPORTED_THERMOSTAT_FAN_MODES,
    ],
    Capability.THERMOSTAT_HEATING_SETPOINT: [
        Attribute.HEATING_SETPOINT,
        Attribute.HEATING_SETPOINT_RANGE,
    ],
    Capability.THERMOSTAT_MODE: [
        Attribute.THERMOSTAT_MODE,
        Attribute.SUPPORTED_THERMOSTAT_MODES,
    ],
    Capability.THERMOSTAT_OPERATING_STATE: [Attribute.THERMOSTAT_OPERATING_STATE],
    Capability.THERMOSTAT_SETPOINT: [Attribute.THERMOSTAT_SETPOINT],
    Capability.THREE_AXIS: [Attribute.THREE_AXIS],
    Capability.TV_CHANNEL: [Attribute.TV_CHANNEL, Attribute.TV_CHANNEL_NAME],
    Capability.TVOC_MEASUREMENT: [Attribute.TVOC_LEVEL],
    Capability.ULTRAVIOLET_INDEX: [Attribute.ULTRAVIOLET_INDEX],
    Capability.VALVE: [Attribute.VALVE],
    Capability.VERY_FINE_DUST_HEALTH_CONCERN: [Attribute.VERY_FINE_DUST_HEALTH_CONCERN],
    Capability.VERY_FINE_DUST_SENSOR: [Attribute.VERY_FINE_DUST_LEVEL],
    Capability.VIDEO_CAMERA: [
        Attribute.CAMERA,
        Attribute.MUTE,
        Attribute.SETTINGS,
        Attribute.STATUS_MESSAGE,
    ],
    Capability.VIDEO_CAPTURE: [Attribute.STREAM, Attribute.CLIP],
    Capability.VIDEO_STREAM: [Attribute.SUPPORTED_FEATURES, Attribute.STREAM],
    Capability.VOLTAGE_MEASUREMENT: [Attribute.VOLTAGE],
    Capability.WASHER_MODE: [Attribute.WASHER_MODE],
    Capability.WASHER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.WASHER_JOB_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.WATER_SENSOR: [Attribute.WATER],
    Capability.WEBRTC: [
        Attribute.AUDIO_ONLY,
        Attribute.DEVICE_ICE,
        Attribute.SDP_ANSWER,
        Attribute.STUN_URL,
        Attribute.SUPPORTED_FEATURES,
        Attribute.TALKBACK,
        Attribute.TURN_INFO,
    ],
    Capability.WIND_MODE: [
        Attribute.WIND_MODE,
        Attribute.SUPPORTED_WIND_MODES,
    ],
    Capability.WINDOW_SHADE_LEVEL: [Attribute.SHADE_LEVEL],
    Capability.WINDOW_SHADE: [
        Attribute.WINDOW_SHADE,
        Attribute.SUPPORTED_WINDOW_SHADE_COMMANDS,
    ],
    Capability.ZWAVE_MULTICHANNEL: [Attribute.EP_INFO, Attribute.EP_EVENT],
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
    Capability.SAMSUNG_IM_FIXED_FIND_NODE: [],
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
    Capability.SAMSUNG_CE_DRYER_LABEL_SCAN_CYCLE_PRESET: [Attribute.PRESETS],
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
        Attribute.SUPPORTED_FREEZER_CONVERT_MODES,
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
    Capability.SAMSUNG_CE_SAC_DISPLAY_CONDITION: [Attribute.SWITCH],
    Capability.SAMSUNG_CE_WASHER_LABEL_SCAN_CYCLE_PRESET: [Attribute.PRESETS],
    Capability.SAMSUNG_CE_CLOTHING_EXTRA_CARE: [
        Attribute.OPERATION_MODE,
        Attribute.USER_LOCATION,
    ],
    Capability.SAMSUNG_CE_FLEXIBLE_AUTO_DISPENSE_DETERGENT: [
        Attribute.REMAINING_AMOUNT,
        Attribute.AMOUNT,
        Attribute.SUPPORTED_DENSITY,
        Attribute.DENSITY,
        Attribute.SUPPORTED_AMOUNT,
        Attribute.AVAILABLE_TYPES,
        Attribute.TYPE,
        Attribute.RECOMMENDED_AMOUNT,
    ],
    Capability.SAMSUNG_CE_TEMPERATURE_SETTING: [
        Attribute.SUPPORTED_DESIRED_TEMPERATURES,
        Attribute.DESIRED_TEMPERATURE,
    ],
    Capability.SAMSUNG_CE_FRIDGE_WELCOME_LIGHTING: [
        Attribute.DETECTION_PROXIMITY,
        Attribute.SUPPORTED_DETECTION_PROXIMITIES,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_CYCLE: [
        Attribute.SUPPORTED_CYCLES,
        Attribute.STEAM_CLOSET_CYCLE,
        Attribute.REFERENCE_TABLE,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_CYCLE_PRESET: [
        Attribute.MAX_NUMBER_OF_PRESETS,
        Attribute.PRESETS,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_KEEP_FRESH_MODE: [
        Attribute.OPERATING_STATE,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_SANITIZE_MODE: [Attribute.STATUS],
    Capability.SAMSUNG_CE_STEAM_CLOSET_DELAY_END: [Attribute.REMAINING_TIME],
    Capability.SAMSUNG_CE_STEAM_CLOSET_AUTO_CYCLE_LINK: [
        Attribute.STEAM_CLOSET_AUTO_CYCLE_LINK
    ],
    Capability.SAMSUNG_CE_DRIVER_STATE: [Attribute.DRIVER_STATE],
    Capability.SAMSUNG_CE_WATER_RESERVOIR: [Attribute.SLOT_STATE],
    # Samsung VD capabilities
    Capability.SAMSUNG_VD_SOUND_FROM: [Attribute.MODE, Attribute.DETAIL_NAME],
    Capability.SAMSUNG_VD_AUDIO_GROUP_INFO: [Attribute.ROLE, Attribute.STATUS],
    Capability.SAMSUNG_VD_AUDIO_INPUT_SOURCE: [
        Attribute.SUPPORTED_INPUT_SOURCES,
        Attribute.INPUT_SOURCE,
    ],
    Capability.SAMSUNG_VD_THING_STATUS: [Attribute.UPDATED_TIME, Attribute.STATUS],
    Capability.SAMSUNG_VD_SUPPORTS_POWER_ON_BY_OCF: [
        Attribute.SUPPORTS_POWER_ON_BY_OCF
    ],
    Capability.SAMSUNG_VD_DEVICE_CATEGORY: [Attribute.CATEGORY],
    Capability.SAMSUNG_VD_SUPPORTS_FEATURES: [
        Attribute.MEDIA_OUTPUT_SUPPORTED,
        Attribute.IME_ADV_SUPPORTED,
        Attribute.WIFI_UPDATE_SUPPORT,
        Attribute.EXECUTABLE_SERVICE_LIST,
        Attribute.REMOTELESS_SUPPORTED,
        Attribute.MOBILE_CAM_SUPPORTED,
    ],
    Capability.SAMSUNG_VD_FIRMWARE_VERSION: [Attribute.FIRMWARE_VERSION],
    Capability.SAMSUNG_VD_MEDIA_INPUT_SOURCE: [
        Attribute.SUPPORTED_INPUT_SOURCES_MAP,
        Attribute.INPUT_SOURCE,
    ],
    Capability.SAMSUNG_VD_AMBIENT_CONTENT: [Attribute.SUPPORTED_AMBIENT_APPS],
    Capability.SAMSUNG_VD_LIGHT_CONTROL: [
        Attribute.SUPPORTED_MODE_MAP,
        Attribute.REQUEST_ID,
        Attribute.SELECTED_MODE,
        Attribute.STREAM_CONTROL,
        Attribute.SELECTED_APP_ID,
        Attribute.ERROR_CODE,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.SAMSUNG_VD_GROUP_INFO: [
        Attribute.ROLE,
        Attribute.CHANNEL,
        Attribute.MASTER_NAME,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_VD_PICTURE_MODE: [
        Attribute.PICTURE_MODE,
        Attribute.SUPPORTED_PICTURE_MODES,
        Attribute.SUPPORTED_PICTURE_MODES_MAP,
    ],
    Capability.SAMSUNG_VD_SOUND_MODE: [
        Attribute.SUPPORTED_SOUND_MODES_MAP,
        Attribute.SOUND_MODE,
        Attribute.SUPPORTED_SOUND_MODES,
    ],
    Capability.SAMSUNG_VD_SOUND_DETECTION: [Attribute.SOUND_DETECTED],
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
    Capability.CUSTOM_HEPA_FILTER: [
        Attribute.HEPA_FILTER_CAPACITY,
        Attribute.HEPA_FILTER_STATUS,
        Attribute.HEPA_FILTER_RESET_TYPE,
        Attribute.HEPA_FILTER_USAGE_STEP,
        Attribute.HEPA_FILTER_USAGE,
        Attribute.HEPA_FILTER_LAST_RESET_DATE,
    ],
    Capability.CUSTOM_ERROR: [Attribute.ERROR],
    Capability.CUSTOM_PICTURE_MODE: [
        Attribute.PICTURE_MODE,
        Attribute.SUPPORTED_PICTURE_MODES,
        Attribute.SUPPORTED_PICTURE_MODES_MAP,
    ],
    Capability.CUSTOM_SOUND_MODE: [
        Attribute.SUPPORTED_SOUND_MODES_MAP,
        Attribute.SOUND_MODE,
        Attribute.SUPPORTED_SOUND_MODES,
    ],
    Capability.CUSTOM_OCF_RESOURCE_VERSION: [
        Attribute.OCF_RESOURCE_VERSION,
        Attribute.OCF_RESOURCE_UPDATED_TIME,
    ],
    Capability.CUSTOM_STEAM_CLOSET_WRINKLE_PREVENT: [
        Attribute.STEAM_CLOSET_WRINKLE_PREVENT
    ],
    Capability.CUSTOM_STEAM_CLOSET_OPERATING_STATE: [
        Attribute.SUPPORTED_STEAM_CLOSET_JOB_STATE,
        Attribute.COMPLETION_TIME,
        Attribute.STEAM_CLOSET_MACHINE_STATE,
        Attribute.SUPPORTED_STEAM_CLOSET_MACHINE_STATE,
        Attribute.STEAM_CLOSET_JOB_STATE,
        Attribute.PROGRESS,
        Attribute.REMAINING_TIME_STR,
        Attribute.STEAM_CLOSET_DELAY_END_TIME,
        Attribute.REMAINING_TIME,
    ],
    Capability.CUSTOM_USER_NOTIFICATION: [Attribute.MESSAGE],
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
    Capability.SEC_DEVICE_CONNECTION_STATE: [Attribute.DEVICE_CONNECTION_STATE],
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
    # Legendabsolute60419 capabilities
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP: [
        Attribute.RANDOM_NEXT,
    ],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF1: [Attribute.RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_GET_GROUPS: [Attribute.GET_GROUPS],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_ON1: [Attribute.PROG_ON],
    Capability.LEGENDABSOLUTE60149_MIRROR_GROUP_FUNCTION: [
        Attribute.MIRROR_GROUP_FUNCTION
    ],
    Capability.LEGENDABSOLUTE60149_DRIVER_VERSION1: [Attribute.DRIVER_VERSION],
    Capability.LEGENDABSOLUTE60149_EFFECTS_SET_COMMAND: [Attribute.EFFECTS_SET_COMMAND],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_OFF1: [Attribute.PROG_OFF],
    Capability.LEGENDABSOLUTE60149_SIGNAL_METRICS: [Attribute.SIGNAL_METRICS],
    Capability.LEGENDABSOLUTE60149_LEVEL_STEPS: [Attribute.LEVEL_STEPS],
    Capability.LEGENDABSOLUTE60149_FORCED_ON_LEVEL: [Attribute.FORCED_ON_LEVEL],
    Capability.LEGENDABSOLUTE60149_SUN_AZIMUTH_ANGLE: [Attribute.SUN_AZIMUTH_ANGLE],
    Capability.LEGENDABSOLUTE60149_EVEN_ODD_DAY: [Attribute.EVEN_ODD_DAY],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR_TWO: [Attribute.LOCAL_HOUR_TWO],
    Capability.LEGENDABSOLUTE60149_CURRENT_TIME_PERIOD: [Attribute.CURRENT_TIME_PERIOD],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH: [Attribute.LOCAL_MONTH],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR_OFFSET: [Attribute.LOCAL_HOUR_OFFSET],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR: [Attribute.LOCAL_HOUR],
    Capability.LEGENDABSOLUTE60149_SUN_RISE_OFFSET1: [Attribute.SUN_RISE_OFFSET],
    Capability.LEGENDABSOLUTE60149_LOCAL_DAY_TWO: [Attribute.LOCAL_DAY_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE: [Attribute.LOCAL_DATE],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_ONE: [Attribute.LOCAL_MONTH_DAY_ONE],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE_TWO1: [Attribute.LOCAL_DATE_TWO],
    Capability.LEGENDABSOLUTE60149_SUN_RISE: [Attribute.SUN_RISE],
    Capability.LEGENDABSOLUTE60149_DAY_LENGTH: [Attribute.DAY_LENGTH],
    Capability.LEGENDABSOLUTE60149_SUN_ELEVATION_ANGLE: [Attribute.SUN_ELEVATION_ANGLE],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE_ONE: [Attribute.LOCAL_DATE_ONE],
    Capability.LEGENDABSOLUTE60149_CURRENT_TWILIGHT: [Attribute.CURRENT_TWILIGHT],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_TWO: [Attribute.LOCAL_MONTH_DAY_TWO],
    Capability.LEGENDABSOLUTE60149_SUN_SET_OFFSET1: [Attribute.SUN_SET_OFFSET],
    Capability.LEGENDABSOLUTE60149_SUN_SET: [Attribute.SUN_SET],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_TWO: [Attribute.LOCAL_MONTH_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_YEAR: [Attribute.LOCAL_YEAR],
    Capability.LEGENDABSOLUTE60149_LOCAL_WEEK_DAY: [Attribute.LOCAL_WEEK_DAY],
    Capability.LEGENDABSOLUTE60149_LOCAL_DAY: [Attribute.LOCAL_DAY],
    Capability.LEGENDABSOLUTE60149_CREATE_DEVICE2: [Attribute.CREATE_DEVICE],
    # PlateMusic11009 capabilities
    Capability.PLATEMUSIC11009_FIRMWARE: [
        Attribute.FIRMWARE_VERSION,
    ],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_THREE: [
        Attribute.ASSOCIATION_GROUP_THREE,
    ],
    Capability.PLATEMUSIC11009_DEVICE_NETWORK_ID: [
        Attribute.DEVICE_NETWORK_ID,
    ],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_TWO: [
        Attribute.ASSOCIATION_GROUP_TWO,
    ],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_FOUR: [
        Attribute.ASSOCIATION_GROUP_FOUR,
    ],
}
