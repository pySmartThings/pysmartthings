"""Attribute model."""

from enum import StrEnum

from pysmartthings.capability import Capability


class Attribute(StrEnum):
    """Attribute model."""

    AC_OPTIONAL_MODE = "acOptionalMode"
    AC_TROPICAL_NIGHT_MODE_LEVEL = "acTropicalNightModeLevel"
    ACCELERATION = "acceleration"
    ACCURACY = "accuracy"
    ACM_MODE = "acmMode"
    ACTIVATED = "activated"
    ACTIVITY = "activity"
    ADD_RINSE = "addRinse"
    AIR_CONDITIONER_MODE = "airConditionerMode"
    AIR_CONDITIONER_ODOR_CONTROLLER_PROGRESS = "airConditionerOdorControllerProgress"
    AIR_CONDITIONER_ODOR_CONTROLLER_STATE = "airConditionerOdorControllerState"
    AIR_PURIFIER_FAN_MODE = "airPurifierFanMode"
    AIR_QUALITY = "airQuality"
    AIR_QUALITY_HEALTH_CONCERN = "airQualityHealthConcern"
    AIR_QUALITY_MAX_LEVEL = "airQualityMaxLevel"
    ALARM = "alarm"
    ALARM_ENABLED = "alarmEnabled"
    ALARM_THRESHOLD = "alarmThreshold"
    ALTITUDE_ACCURACY = "altitudeAccuracy"
    ALWAYS_ON = "alwaysOn"
    AMOUNT = "amount"
    APP_NAME = "appName"
    APP_VERSION = "appVersion"
    AREA = "area"
    AREA_IDS = "areaIds"
    AREA_INFO = "areaInfo"
    ASSOCIATION_GROUP_FOUR = "associationGroupFour"
    ASSOCIATION_GROUP_THREE = "associationGroupThree"
    ASSOCIATION_GROUP_TWO = "associationGroupTwo"
    ATMOS_PRESSURE = "atmosPressure"
    ATMOSPHERIC_PRESSURE = "atmosphericPressure"
    AUDIO_ONLY = "audioOnly"
    AUDIO_TRACK_DATA = "audioTrackData"
    AUTO_CLEANING_MODE = "autoCleaningMode"
    AUTO_DOOR_RELEASE_ENABLED = "autoDoorReleaseEnabled"
    AUTO_RECONNECTION = "autoReconnection"
    AUTOMATIC_EXECUTION_MODE = "automaticExecutionMode"
    AUTOMATIC_EXECUTION_SETTING = "automaticExecutionSetting"
    AVAILABLE_AC_FAN_MODES = "availableAcFanModes"
    AVAILABLE_AC_MODES = "availableAcModes"
    AVAILABLE_CUSTOM_BUTTONS = "availableCustomButtons"
    AVAILABLE_FAN_OSCILLATION_MODES = "availableFanOscillationModes"
    AVAILABLE_FANSPEED_BUTTONS = "availableFanspeedButtons"
    AVAILABLE_MODULES = "availableModules"
    AVAILABLE_POWER_TOGGLE_BUTTONS = "availablePowerToggleButtons"
    AVAILABLE_TYPES = "availableTypes"
    AVAILABLE_VERSION = "availableVersion"
    BABY_DETERGENT_ALARM_ENABLED = "babyDetergentAlarmEnabled"
    BABY_DETERGENT_DOSAGE = "babyDetergentDosage"
    BABY_DETERGENT_INITIAL_AMOUNT = "babyDetergentInitialAmount"
    BABY_DETERGENT_ORDER_THRESHOLD = "babyDetergentOrderThreshold"
    BABY_DETERGENT_REMAINING_AMOUNT = "babyDetergentRemainingAmount"
    BABY_DETERGENT_TYPE = "babyDetergentType"
    BASIC_HTML = "basicHtml"
    BASIC_HTML_DISABLE = "basicHtmlDisable"
    BATON_TOUCH = "batonTouch"
    BATTERY = "battery"
    BEEP = "beep"
    BINARY_ID = "binaryId"
    BLOCKING_STATUS = "blockingStatus"
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
    CHARGING_STATUS = "chargingStatus"
    CHECK_INTERVAL = "checkInterval"
    CHIME = "chime"
    CIRCADIAN = "circadian"
    CLEANED_EXTENT = "cleanedExtent"
    CLEANING_MODE = "cleaningMode"
    CLEANING_STEP = "cleaningStep"
    CLIP = "clip"
    CLOUDCOVER = "cloudcover"
    CLUSTER_ID = "clusterId"
    CLUSTER_ID_DEC = "clusterIdDec"
    CLUSTER_NAME = "clusterName"
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
    COOKTOP_BURNER_MODE = "cooktopBurnerMode"
    COOKTOP_OPERATING_STATE = "cooktopOperatingState"
    COOLING_SETPOINT = "coolingSetpoint"
    COOLING_SETPOINT_RANGE = "coolingSetpointRange"
    COORDINATES = "coordinates"
    COURSE = "course"
    CREATE_DEVICE = "createDevice"
    CREATE_QTY = "createQty"
    CURRENT = "current"
    CURRENT_TIME_PERIOD = "currentTimePeriod"
    CURRENT_TRACK = "currentTrack"
    CURRENT_TWILIGHT = "currentTwilight"
    CURRENT_VALUE = "currentValue"
    CURRENT_VERSION = "currentVersion"
    CUSTOM_COURSE_CANDIDATES = "customCourseCandidates"
    DASH_BOARD_VALUE = "dashBoardValue"
    DATA = "data"
    DATE_STARTED = "dateStarted"
    DAY_LENGTH = "dayLength"
    DAY_OF_WEEK = "dayOfWeek"
    DEFAULT_OPERATION_TIME = "defaultOperationTime"
    DEFAULT_OVEN_MODE = "defaultOvenMode"
    DEFAULT_OVEN_SETPOINT = "defaultOvenSetpoint"
    DEFINED_RECIPE = "definedRecipe"
    DEFROST = "defrost"
    DENSITY = "density"
    DEODOR_FILTER_CAPACITY = "deodorFilterCapacity"
    DEODOR_FILTER_LAST_RESET_DATE = "deodorFilterLastResetDate"
    DEODOR_FILTER_RESET_TYPE = "deodorFilterResetType"
    DEODOR_FILTER_STATUS = "deodorFilterStatus"
    DEODOR_FILTER_USAGE = "deodorFilterUsage"
    DEODOR_FILTER_USAGE_STEP = "deodorFilterUsageStep"
    DEPENDENCY_STATUS = "dependencyStatus"
    DESCRIPTION = "description"
    DESIRED_TEMPERATURE = "desiredTemperature"
    DETAIL_NAME = "detailName"
    DETECTED = "detected"
    DETECTION_INTERVAL = "detectionInterval"
    DETECTION_PROXIMITY = "detectionProximity"
    DETERGENT_TYPE = "detergentType"
    DEVICE_CONNECTION_STATE = "deviceConnectionState"
    DEVICE_ICE = "deviceIce"
    DEVICE_NETWORK_ID = "deviceNetworkId"
    DEVICE_TYPE = "deviceType"
    DEVICE_WATCH_DEVICE_STATUS = "DeviceWatch-DeviceStatus"
    DEVICE_WATCH_ENROLL = "DeviceWatch-Enroll"
    DEWPOINT = "dewpoint"
    DEVICE_ID = "di"
    DIRECTION = "direction"
    DISABLED_CAPABILITIES = "disabledCapabilities"
    DISABLED_COMPONENTS = "disabledComponents"
    DISHWASHER_DELAY_START_TIME = "dishwasherDelayStartTime"
    DISHWASHER_JOB_STATE = "dishwasherJobState"
    DISHWASHER_OPERATING_PERCENTAGE = "dishwasherOperatingPercentage"
    DISHWASHER_OPERATING_PROGRESS = "dishwasherOperatingProgress"
    DATA_MODEL_VERSION = "dmv"
    DO_NOT_DISTURB = "doNotDisturb"
    DOOR = "door"
    DOOR_STATE = "doorState"
    DOSAGE = "dosage"
    DOWNLINK_SPEED = "downlinkSpeed"
    DR_MAX_DURATION = "drMaxDuration"
    DRAINAGE_REQUIREMENT = "drainageRequirement"
    DRCAPABLE = "drcapable"
    DRIVER_STATE = "driverState"
    DRIVER_VERSION = "driverVersion"
    DRIVING_MODE = "drivingMode"
    DEMAND_RESPONSE_LOAD_CONTROL_STATUS = "drlcStatus"
    DRY_PLUS = "dryPlus"
    DRYER_AUTO_CYCLE_LINK = "dryerAutoCycleLink"
    DRYER_CYCLE = "dryerCycle"
    DRYER_DRY_LEVEL = "dryerDryLevel"
    DRYER_JOB_STATE = "dryerJobState"
    DRYER_MODE = "dryerMode"
    DRYER_WRINKLE_PREVENT = "dryerWrinklePrevent"
    DRYING_TEMPERATURE = "dryingTemperature"
    DRYING_TIME = "dryingTime"
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
    ENABLE_STATE = "enableState"
    ENABLED = "enabled"
    ENCRYPTED = "encrypted"
    ENCRYPTION = "encryption"
    END_TIME = "endTime"
    ENDPOINT = "endpoint"
    ENERGY = "energy"
    ENERGY_RESET = "energyReset"
    ENERGY_SAVING_INFO = "energySavingInfo"
    ENERGY_SAVING_LEVEL = "energySavingLevel"
    ENERGY_SAVING_OPERATION = "energySavingOperation"
    ENERGY_SAVING_OPERATION_SUPPORT = "energySavingOperationSupport"
    ENERGY_SAVING_SUPPORT = "energySavingSupport"
    ENERGY_TYPE = "energyType"
    ENERGY_USAGE_MAX = "energyUsageMax"
    ENERGY_USAGE_STATE = "energyUsageState"
    EP_EVENT = "epEvent"
    EP_INFO = "epInfo"
    EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT = "equivalentCarbonDioxideMeasurement"
    ERROR = "error"
    ERROR_CODE = "errorCode"
    ERRORS = "errors"
    EUI = "eui"
    EVEN_ODD_DAY = "evenOddDay"
    EVENT = "event"
    EVENTS = "events"
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
    FSV_SETTINGS = "fsvSettings"
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
    GRID_STATUS_STATUS = "gridStatusStatus"
    GRID_STATUS_SUPPORT = "gridStatusSupport"
    GROUP_ID = "groupId"
    GROUP_MUTE = "groupMute"
    GROUP_NAME = "groupName"
    GROUP_PRIMARY_DEVICE_ID = "groupPrimaryDeviceId"
    GROUP_ROLE = "groupRole"
    GROUP_VOLUME = "groupVolume"
    HARDWARE_FAULT = "hardwareFault"
    HAS_COST = "hasCost"
    HAS_FROM_GRID = "hasFromGrid"
    HAS_TO_GRID = "hasToGrid"
    HAS_TODAY_USAGE = "hasTodayUsage"
    HAS_TOTAL_USAGE = "hasTotalUsage"
    HEADING = "heading"
    HEALTH_STATUS = "healthStatus"
    HEATED_DRY = "heatedDry"
    HEATING_MODE = "heatingMode"
    HEATING_SETPOINT = "heatingSetpoint"
    HEATING_SETPOINT_RANGE = "heatingSetpointRange"
    HEPA_FILTER_CAPACITY = "hepaFilterCapacity"
    HEPA_FILTER_LAST_RESET_DATE = "hepaFilterLastResetDate"
    HEPA_FILTER_RESET_TYPE = "hepaFilterResetType"
    HEPA_FILTER_STATUS = "hepaFilterStatus"
    HEPA_FILTER_USAGE = "hepaFilterUsage"
    HEPA_FILTER_USAGE_STEP = "hepaFilterUsageStep"
    HIGH_TEMP_WASH = "highTempWash"
    HISTORY = "history"
    HOMING_REASON = "homingReason"
    HOOD_FAN_SPEED = "hoodFanSpeed"
    HOT_AIR_DRY = "hotAirDry"
    HTTPCODE = "httpcode"
    HUE = "hue"
    HUMIDIFIER_MODE = "humidifierMode"
    HUMIDITY = "humidity"
    SPEC_VERSION = "icv"
    ILLUMINANCE = "illuminance"
    ILLUMVALUE = "illumvalue"
    IMAGE = "image"
    IME_ADV_SUPPORTED = "imeAdvSupported"
    INFO = "info"
    INFO_HTML = "infoHtml"
    INFO_TEXT = "infoText"
    INFRARED_LEVEL = "infraredLevel"
    INITIAL_AMOUNT = "initialAmount"
    INPUT_SOURCE = "inputSource"
    INTERVAL = "interval"
    INVENTORY = "inventory"
    INVISIBLE_FEATURES = "invisibleFeatures"
    IS_MAP_BASED_OPERATION_AVAILABLE = "isMapBasedOperationAvailable"
    JOB_BEGINNING_STATUS = "jobBeginningStatus"
    LAST_SENSING_LEVEL = "lastSensingLevel"
    LAST_SENSING_TIME = "lastSensingTime"
    LAST_UPDATE_STATUS = "lastUpdateStatus"
    LAST_UPDATE_STATUS_REASON = "lastUpdateStatusReason"
    LAST_UPDATE_TIME = "lastUpdateTime"
    LAST_UPDATED_DATE = "lastUpdatedDate"
    LAST_UPDATED_TIME = "lastUpdatedTime"
    LATEST_REQUEST_ID = "latestRequestId"
    LATITUDE = "latitude"
    LEVEL = "level"
    LEVEL_RANGE = "levelRange"
    LEVEL_STEPS = "levelSteps"
    LIGHTING = "lighting"
    LIGHTING_MODE = "lightingMode"
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
    MANUAL_LEVEL = "manualLevel"
    MANUAL_LEVEL_MAX = "manualLevelMax"
    MANUAL_LEVEL_MIN = "manualLevelMin"
    MAP_ID = "mapId"
    MAPS = "maps"
    MASTER_DI = "masterDi"
    MASTER_NAME = "masterName"
    MAX_CODE_LENGTH = "maxCodeLength"
    MAX_CODES = "maxCodes"
    MAX_NUMBER_OF_PRESETS = "maxNumberOfPresets"
    MAX_NUMBER_OF_RESERVATIONS = "maxNumberOfReservations"
    MAXIMUM_SETPOINT = "maximumSetpoint"
    MAXTEMP = "maxtemp"
    MEASURE_INTERVAL = "measureInterval"
    MEDIA_OUTPUT_SUPPORTED = "mediaOutputSupported"
    MENU = "menu"
    MESSAGE = "message"
    METERING_DATE = "meteringDate"
    METHOD = "method"
    MICOM_ASSAY_CODE = "micomAssayCode"
    MIN_CODE_LENGTH = "minCodeLength"
    MIN_VERSION = "minVersion"
    MINIMUM_RESERVABLE_TIME = "minimumReservableTime"
    MINIMUM_SETPOINT = "minimumSetpoint"
    MINTEMP = "mintemp"
    MIRROR_GROUP_FUNCTION = "mirrorGroupFunction"
    MN_ID = "mnId"
    MANUFACTURE_DATE = "mndt"
    OCF_FIRMWARE_VERSION = "mnfv"
    HARDWARE_VERSION = "mnhw"
    MANUFACTURER_DETAILS_LINK = "mnml"
    MANUFACTURER_NAME = "mnmn"
    MODEL_NUMBER = "mnmo"
    OS_VERSION = "mnos"
    PLATFORM_VERSION = "mnpv"
    SUPPORT_LINK = "mnsl"
    MOBILE_CAM_SUPPORTED = "mobileCamSupported"
    MODE = "mode"
    MODEL_CLASSIFICATION_CODE = "modelClassificationCode"
    MODEL_CODE = "modelCode"
    MODEL_NAME = "modelName"
    MOLD_HEALTH_CONCERN = "moldHealthConcern"
    MONITORING_STATUS = "monitoringStatus"
    MONTHLY_USAGE = "monthlyUsage"
    MOTION = "motion"
    MOTOR_FILTER_RESET_TYPE = "motorFilterResetType"
    MOTOR_FILTER_STATUS = "motorFilterStatus"
    MUTE = "mute"
    DEVICE_NAME = "n"
    NAME = "name"
    NEAR_OBJECT = "nearObject"
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
    NUMBER_OF_SUB_DEVICES = "numberOfSubDevices"
    OBSOLETED = "obsoleted"
    OCCUPANCY = "occupancy"
    OCF_RESOURCE_UPDATED_TIME = "ocfResourceUpdatedTime"
    OCF_RESOURCE_VERSION = "ocfResourceVersion"
    ODOR_LEVEL = "odorLevel"
    OPERATING_STATE = "operatingState"
    OPERATION_MODE = "operationMode"
    OPERATION_TIME = "operationTime"
    ORDER_THRESHOLD = "orderThreshold"
    ORIGINATOR = "originator"
    ORIGINS = "origins"
    OTN_D_U_I_D = "otnDUID"
    OUT_OF_SYNC_CHANGES = "outOfSyncChanges"
    OUTING_MODE = "outingMode"
    OVEN_CAVITY_STATUS = "ovenCavityStatus"
    OVEN_JOB_STATE = "ovenJobState"
    OVEN_MODE = "ovenMode"
    OVEN_SETPOINT = "ovenSetpoint"
    OVEN_SETPOINT_RANGE = "ovenSetpointRange"
    OZONE = "ozone"
    OZONE_HEALTH_CONCERN = "ozoneHealthConcern"
    PH = "pH"
    PANIC_ALARM = "panicAlarm"
    PATROL_STATUS = "patrolStatus"
    PAYLOAD = "payload"
    PERCENT = "percent"
    PERIODIC_SENSING = "periodicSensing"
    PERIODIC_SENSING_INTERVAL = "periodicSensingInterval"
    PERIODIC_SENSING_STATUS = "periodicSensingStatus"
    PEST_CONTROL = "pestControl"
    PLATFORM_ID = "pi"
    PICTURE_MODE = "pictureMode"
    PLAN = "plan"
    PLAYBACK_REPEAT_MODE = "playbackRepeatMode"
    PLAYBACK_SHUFFLE = "playbackShuffle"
    PLAYBACK_STATUS = "playbackStatus"
    PLAYLIST = "playlist"
    POWER = "power"
    POWER_CONSUMPTION = "powerConsumption"
    POWER_LEVEL = "powerLevel"
    POWER_SOURCE = "powerSource"
    POWER_STATE = "powerState"
    PRECIP = "precip"
    PRECIPITATION_INTENSITY = "precipitationIntensity"
    PREDEFINED_COURSES = "predefinedCourses"
    PRESENCE = "presence"
    PRESETS = "presets"
    PRESSURE = "pressure"
    PROBABILITY = "probability"
    PROG_OFF = "progOff"
    PROG_ON = "progOn"
    PROGRESS = "progress"
    PROGRESS_PERCENTAGE = "progressPercentage"
    PROTOCOL_TYPE = "protocolType"
    PROTOCOLS = "protocols"
    QUANTITY = "quantity"
    RADON_LEVEL = "radonLevel"
    RANDOM_NEXT = "randomNext"
    RANDOM_ON_OFF = "randomOnOff"
    RAPID_COOLING = "rapidCooling"
    RAPID_FREEZING = "rapidFreezing"
    RATE_TYPE = "rateType"
    RECOMMENDED_AMOUNT = "recommendedAmount"
    REFERENCE_TABLE = "referenceTable"
    REFRESH_RESULT = "refreshResult"
    REFRIGERATION_SETPOINT = "refrigerationSetpoint"
    REGION_CODE = "regionCode"
    REGISTRATION_STATUS = "registrationStatus"
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
    REMOTELESS_SUPPORTED = "remotelessSupported"
    REPEAT_MODE = "repeatMode"
    REPEAT_MODE_ENABLED = "repeatModeEnabled"
    REPORT = "report"
    REPORT_RAW_DATA = "reportRawData"
    REPORT_STATE_PERIOD = "reportStatePeriod"
    REPORT_STATE_REALTIME = "reportStateRealtime"
    REPORT_STATE_REALTIME_PERIOD = "reportStateRealtimePeriod"
    REPRESENTATIVE_COMPONENT = "representativeComponent"
    REQUEST_ID = "requestId"
    RESERVABLE = "reservable"
    RESERVATIONS = "reservations"
    RESOLUTION = "resolution"
    RESPONSE = "response"
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
    SENSITIVITY_MODE = "sensitivityMode"
    SENSOR_STATUS = "sensorStatus"
    SERIAL_NUMBER = "serialNumber"
    SERIAL_NUMBER_EXTRA = "serialNumberExtra"
    SERVICE_MESSAGE = "serviceMessage"
    SETTABLE = "settable"
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
    SOURCE = "source"
    SPECIALIZED_FUNCTION_CLASSIFICATION = "specializedFunctionClassification"
    SPECIFICATION = "specification"
    SPEED = "speed"
    SPEED_BOOSTER = "speedBooster"
    SPI_MODE = "spiMode"
    SPIN_SPEED = "spinSpeed"
    SYSTEM_TIME = "st"
    START_TIME = "startTime"
    START_VALUE = "startValue"
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
    STEREO_TYPE = "stereoType"
    STORM_WASH = "stormWash"
    STORM_WATCH_ACTIVE = "stormWatchActive"
    STORM_WATCH_ENABLED = "stormWatchEnabled"
    STORM_WATCH_SUPPORT = "stormWatchSupport"
    STREAM = "stream"
    STREAM_CONTROL = "streamControl"
    STUN_URL = "stunUrl"
    SUB_DEVICE_ACTIVE = "subDeviceActive"
    SUB_DEVICES = "subDevices"
    SUGGESTION_THRESHOLD = "suggestionThreshold"
    SUMMARY = "summary"
    SUN_AZIMUTH_ANGLE = "sunAzimuthAngle"
    SUN_ELEVATION_ANGLE = "sunElevationAngle"
    SUN_RISE = "sunRise"
    SUN_RISE_OFFSET = "sunRiseOffset"
    SUN_SET = "sunSet"
    SUN_SET_OFFSET = "sunSetOffset"
    SUPPORT_REPEAT_MODE = "supportRepeatMode"
    SUPPORT_TOU_EVENT_NOTIFICATION = "supportTouEventNotification"
    SUPPORT_TOU_INFO = "supportTouInfo"
    SUPPORTED_AC_FAN_MODES = "supportedAcFanModes"
    SUPPORTED_AC_MODES = "supportedAcModes"
    SUPPORTED_AC_OPTIONAL_MODE = "supportedAcOptionalMode"
    SUPPORTED_ACTIONS = "supportedActions"
    SUPPORTED_AGING_METHODS = "supportedAgingMethods"
    SUPPORTED_AIR_PURIFIER_FAN_MODES = "supportedAirPurifierFanModes"
    SUPPORTED_AIR_QUALITY_HEALTH_CONCERNS = "supportedAirQualityHealthConcerns"
    SUPPORTED_ALARM_THRESHOLDS = "supportedAlarmThresholds"
    SUPPORTED_AMBIENT_APPS = "supportedAmbientApps"
    SUPPORTED_AMOUNT = "supportedAmount"
    SUPPORTED_ARGUMENTS = "supportedArguments"
    SUPPORTED_AUTH_TYPE = "supportedAuthType"
    SUPPORTED_AUTO_CLEANING_MODES = "supportedAutoCleaningModes"
    SUPPORTED_AUTOMATIC_EXECUTION_MODE = "supportedAutomaticExecutionMode"
    SUPPORTED_AUTOMATIC_EXECUTION_SETTING = "supportedAutomaticExecutionSetting"
    SUPPORTED_BRIGHTNESS_LEVEL = "supportedBrightnessLevel"
    SUPPORTED_BUTTON_VALUES = "supportedButtonValues"
    SUPPORTED_CATEGORIES = "supportedCategories"
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
    SUPPORTED_DRIVING_MODES = "supportedDrivingModes"
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
    SUPPORTED_HEATING_MODES = "supportedHeatingModes"
    SUPPORTED_HOOD_FAN_SPEED = "supportedHoodFanSpeed"
    SUPPORTED_INPUT_SOURCES = "supportedInputSources"
    SUPPORTED_INPUT_SOURCES_MAP = "supportedInputSourcesMap"
    SUPPORTED_KEY_CODES = "supportedKeyCodes"
    SUPPORTED_LEVELS = "supportedLevels"
    SUPPORTED_LIGHTING_LEVELS = "supportedLightingLevels"
    SUPPORTED_LIST = "supportedList"
    SUPPORTED_LOCK_COMMANDS = "supportedLockCommands"
    SUPPORTED_LOCK_VALUES = "supportedLockValues"
    SUPPORTED_MACHINE_STATES = "supportedMachineStates"
    SUPPORTED_MEAT_TYPES = "supportedMeatTypes"
    SUPPORTED_MENUS = "supportedMenus"
    SUPPORTED_MIMES = "supportedMimes"
    SUPPORTED_MODE_MAP = "supportedModeMap"
    SUPPORTED_MODES = "supportedModes"
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
    SUPPORTED_STATUS = "supportedStatus"
    SUPPORTED_STEAM_CLOSET_JOB_STATE = "supportedSteamClosetJobState"
    SUPPORTED_STEAM_CLOSET_MACHINE_STATE = "supportedSteamClosetMachineState"
    SUPPORTED_TEMPERATURE_LEVELS = "supportedTemperatureLevels"
    SUPPORTED_THERMOSTAT_FAN_MODES = "supportedThermostatFanModes"
    SUPPORTED_THERMOSTAT_MODES = "supportedThermostatModes"
    SUPPORTED_TRACK_CONTROL_COMMANDS = "supportedTrackControlCommands"
    SUPPORTED_TYPES = "supportedTypes"
    SUPPORTED_UNLOCK_DIRECTIONS = "supportedUnlockDirections"
    SUPPORTED_VALUES = "supportedValues"
    SUPPORTED_WASHER_RINSE_CYCLES = "supportedWasherRinseCycles"
    SUPPORTED_WASHER_SOIL_LEVEL = "supportedWasherSoilLevel"
    SUPPORTED_WASHER_SPIN_LEVEL = "supportedWasherSpinLevel"
    SUPPORTED_WASHER_WATER_TEMPERATURE = "supportedWasherWaterTemperature"
    SUPPORTED_WASHING_TIMES = "supportedWashingTimes"
    SUPPORTED_WATER_LEVEL = "supportedWaterLevel"
    SUPPORTED_WATER_VALVE = "supportedWaterValve"
    SUPPORTED_WI_FI_FREQ = "supportedWiFiFreq"
    SUPPORTED_WIND_MODES = "supportedWindModes"
    SUPPORTED_WINDOW_SHADE_COMMANDS = "supportedWindowShadeCommands"
    SUPPORTS_POWER_ON_BY_OCF = "supportsPowerOnByOcf"
    SURFACE_RESIDUAL_HEAT = "surfaceResidualHeat"
    SWITCH = "switch"
    SWITCH_ALL_ON_OFF = "switchAllOnOff"
    TAG_BUTTON = "tagButton"
    TAG_STATUS = "tagStatus"
    TALKBACK = "talkback"
    TAMPER = "tamper"
    TARGET_MODULE = "targetModule"
    TARIFF_NAME = "tariffName"
    TARIFF_PROVIDER = "tariffProvider"
    TEMPERATURE = "temperature"
    TEMPERATURE_ALARM = "temperatureAlarm"
    TEMPERATURE_LEVEL = "temperatureLevel"
    TEMPERATURE_RANGE = "temperatureRange"
    TEMPERATURE_REFERENCE = "temperatureReference"
    TEMPERATURE_SETPOINT = "temperatureSetpoint"
    TEMPERATURE_SETPOINT_RANGE = "temperatureSetpointRange"
    THERMOSTAT_FAN_MODE = "thermostatFanMode"
    THERMOSTAT_MODE = "thermostatMode"
    THERMOSTAT_OPERATING_STATE = "thermostatOperatingState"
    THERMOSTAT_SETPOINT = "thermostatSetpoint"
    THREE_AXIS = "threeAxis"
    TIME_LEFT_TO_START = "timeLeftToStart"
    TIME_OFFSET = "timeOffset"
    TIMED_CLEAN_DURATION = "timedCleanDuration"
    TIMED_CLEAN_DURATION_RANGE = "timedCleanDurationRange"
    TOPICLIST = "topiclist"
    TOTAL_TIME = "totalTime"
    TOU_EVENT_NOTIFICATION = "touEventNotification"
    TOU_INFO = "touInfo"
    TRACK_DATA = "trackData"
    TRACK_DESCRIPTION = "trackDescription"
    TS_ID = "tsId"
    TURN_INFO = "turnInfo"
    TV_CHANNEL = "tvChannel"
    TV_CHANNEL_NAME = "tvChannelName"
    TVOC_LEVEL = "tvocLevel"
    TYPE = "type"
    ULTRAVIOLET_INDEX = "ultravioletIndex"
    UNAVAILABLE_COMMANDS = "unavailableCommands"
    UPDATE_AVAILABLE = "updateAvailable"
    UPDATED_TIME = "updatedTime"
    UPLINK_SPEED = "uplinkSpeed"
    URI = "uri"
    USAGE_TIME = "usageTime"
    USER_LOCATION = "userLocation"
    UWB_ACTIVATION = "uwbActivation"
    VACATION_MODE = "vacationMode"
    VALUE = "value"
    VALVE = "valve"
    VERSION = "version"
    VERSION_NUMBER = "versionNumber"
    VERSIONS = "versions"
    VERY_FINE_DUST_FILTER_CAPACITY = "veryFineDustFilterCapacity"
    VERY_FINE_DUST_FILTER_LAST_RESET_DATE = "veryFineDustFilterLastResetDate"
    VERY_FINE_DUST_FILTER_RESET_TYPE = "veryFineDustFilterResetType"
    VERY_FINE_DUST_FILTER_STATUS = "veryFineDustFilterStatus"
    VERY_FINE_DUST_FILTER_USAGE = "veryFineDustFilterUsage"
    VERY_FINE_DUST_FILTER_USAGE_STEP = "veryFineDustFilterUsageStep"
    VERY_FINE_DUST_HEALTH_CONCERN = "veryFineDustHealthConcern"
    VERY_FINE_DUST_LEVEL = "veryFineDustLevel"
    VHUMIDITY = "vhumidity"
    VENDOR_ID = "vid"
    VISIBLE_FEATURES = "visibleFeatures"
    VOLTAGE = "voltage"
    VOLUME = "volume"
    VTEMP = "vtemp"
    W_SPEED = "wSpeed"
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
    WASHING_COUNT_AFTER_SELF_CLEAN = "washingCountAfterSelfClean"
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
    WAYPOINTS = "waypoints"
    WEIGHT = "weight"
    WELCOME_CARE_MODE = "welcomeCareMode"
    WELCOME_MESSAGE = "welcomeMessage"
    WIFI_UPDATE_SUPPORT = "wifiUpdateSupport"
    WIND_MODE = "windMode"
    WINDDEG = "winddeg"
    WINDGUST = "windgust"
    WINDOW_SHADE = "windowShade"
    ZCL_VERSION = "zclVersion"
    ZONE_BOOSTER = "zoneBooster"
    ZONE_INFO = "zoneInfo"


CAPABILITY_ATTRIBUTES: dict[Capability, list[Attribute]] = {
    Capability.ACCELERATION_SENSOR: [Attribute.ACCELERATION],
    Capability.ACTIVITY_LIGHTING_MODE: [Attribute.LIGHTING_MODE],
    Capability.ACTIVITY_SENSOR: [Attribute.ACTIVITY],
    Capability.AIR_CONDITIONER_FAN_MODE: [
        Attribute.AVAILABLE_AC_FAN_MODES,
        Attribute.FAN_MODE,
        Attribute.SUPPORTED_AC_FAN_MODES,
    ],
    Capability.AIR_CONDITIONER_MODE: [
        Attribute.AIR_CONDITIONER_MODE,
        Attribute.AVAILABLE_AC_MODES,
        Attribute.SUPPORTED_AC_MODES,
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
    Capability.AUDIO_NOTIFICATION: [],
    Capability.AUDIO_STREAM: [Attribute.URI],
    Capability.AUDIO_TRACK_ADDRESSING: [],
    Capability.AUDIO_TRACK_DATA: [
        Attribute.AUDIO_TRACK_DATA,
        Attribute.ELAPSED_TIME,
        Attribute.TOTAL_TIME,
    ],
    Capability.AUDIO_VOLUME: [Attribute.VOLUME],
    Capability.BATTERY: [Attribute.BATTERY, Attribute.QUANTITY, Attribute.TYPE],
    Capability.BATTERY_LEVEL: [Attribute.BATTERY, Attribute.QUANTITY, Attribute.TYPE],
    Capability.BODY_MASS_INDEX_MEASUREMENT: [Attribute.BMI_MEASUREMENT],
    Capability.BODY_WEIGHT_MEASUREMENT: [Attribute.BODY_WEIGHT_MEASUREMENT],
    Capability.BRIDGE: [],
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
    Capability.CONFIGURATION: [],
    Capability.CONTACT_SENSOR: [Attribute.CONTACT],
    Capability.CURRENT_MEASUREMENT: [Attribute.CURRENT],
    Capability.DEMAND_RESPONSE_LOAD_CONTROL: [
        Attribute.DEMAND_RESPONSE_LOAD_CONTROL_STATUS
    ],
    Capability.DEW_POINT: [Attribute.DEWPOINT],
    Capability.DISHWASHER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.DISHWASHER_JOB_STATE,
        Attribute.MACHINE_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.DOOR_CONTROL: [Attribute.DOOR],
    Capability.DRYER_MODE: [Attribute.DRYER_MODE],
    Capability.DRYER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.DRYER_JOB_STATE,
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.DUST_HEALTH_CONCERN: [Attribute.DUST_HEALTH_CONCERN],
    Capability.DUST_SENSOR: [Attribute.DUST_LEVEL, Attribute.FINE_DUST_LEVEL],
    Capability.ELEVATOR_CALL: [Attribute.CALL_STATUS],
    Capability.ENERGY_METER: [Attribute.ENERGY],
    Capability.EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT: [
        Attribute.EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT
    ],
    Capability.EXECUTE: [Attribute.DATA],
    Capability.FAN_OSCILLATION_MODE: [
        Attribute.AVAILABLE_FAN_OSCILLATION_MODES,
        Attribute.FAN_OSCILLATION_MODE,
        Attribute.SUPPORTED_FAN_OSCILLATION_MODES,
    ],
    Capability.FAN_SPEED: [Attribute.FAN_SPEED],
    Capability.FAN_SPEED_PERCENT: [Attribute.PERCENT],
    Capability.FILTER_STATE: [
        Attribute.FILTER_LIFE_REMAINING,
        Attribute.SUPPORTED_FILTER_COMMANDS,
    ],
    Capability.FILTER_STATUS: [Attribute.FILTER_STATUS],
    Capability.FINE_DUST_HEALTH_CONCERN: [Attribute.FINE_DUST_HEALTH_CONCERN],
    Capability.FINE_DUST_SENSOR: [Attribute.FINE_DUST_LEVEL],
    Capability.FIRMWARE_UPDATE: [
        Attribute.AVAILABLE_VERSION,
        Attribute.CURRENT_VERSION,
        Attribute.LAST_UPDATE_STATUS,
        Attribute.LAST_UPDATE_STATUS_REASON,
        Attribute.LAST_UPDATE_TIME,
        Attribute.STATE,
        Attribute.SUPPORTED_COMMANDS,
        Attribute.UPDATE_AVAILABLE,
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
    Capability.GEOFENCE: [Attribute.ENABLE_STATE, Attribute.GEOFENCE, Attribute.NAME],
    Capability.GEOLOCATION: [
        Attribute.ACCURACY,
        Attribute.ALTITUDE_ACCURACY,
        Attribute.HEADING,
        Attribute.LAST_UPDATE_TIME,
        Attribute.LATITUDE,
        Attribute.LONGITUDE,
        Attribute.METHOD,
        Attribute.SPEED,
    ],
    Capability.HARDWARE_FAULT: [Attribute.HARDWARE_FAULT],
    Capability.HEALTH_CHECK: [
        Attribute.CHECK_INTERVAL,
        Attribute.DEVICE_WATCH_DEVICE_STATUS,
        Attribute.DEVICE_WATCH_ENROLL,
        Attribute.HEALTH_STATUS,
    ],
    Capability.HUMIDIFIER_MODE: [Attribute.HUMIDIFIER_MODE],
    Capability.ILLUMINANCE_MEASUREMENT: [Attribute.ILLUMINANCE],
    Capability.IMAGE_CAPTURE: [
        Attribute.CAPTURE_TIME,
        Attribute.ENCRYPTED,
        Attribute.IMAGE,
    ],
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
    Capability.LOCK: [
        Attribute.LOCK,
        Attribute.SUPPORTED_LOCK_COMMANDS,
        Attribute.SUPPORTED_LOCK_VALUES,
        Attribute.SUPPORTED_UNLOCK_DIRECTIONS,
    ],
    Capability.LOCK_CODES: [
        Attribute.CODE_CHANGED,
        Attribute.CODE_LENGTH,
        Attribute.CODE_REPORT,
        Attribute.LOCK,
        Attribute.LOCK_CODES,
        Attribute.MAX_CODES,
        Attribute.MAX_CODE_LENGTH,
        Attribute.MIN_CODE_LENGTH,
        Attribute.SCAN_CODES,
    ],
    Capability.MEDIA_GROUP: [
        Attribute.GROUP_ID,
        Attribute.GROUP_MUTE,
        Attribute.GROUP_PRIMARY_DEVICE_ID,
        Attribute.GROUP_ROLE,
        Attribute.GROUP_VOLUME,
    ],
    Capability.MEDIA_INPUT_SOURCE: [
        Attribute.INPUT_SOURCE,
        Attribute.SUPPORTED_INPUT_SOURCES,
    ],
    Capability.MEDIA_PLAYBACK: [
        Attribute.PLAYBACK_STATUS,
        Attribute.SUPPORTED_PLAYBACK_COMMANDS,
    ],
    Capability.MEDIA_PLAYBACK_REPEAT: [Attribute.PLAYBACK_REPEAT_MODE],
    Capability.MEDIA_PLAYBACK_SHUFFLE: [Attribute.PLAYBACK_SHUFFLE],
    Capability.MEDIA_PRESETS: [Attribute.PRESETS],
    Capability.MEDIA_TRACK_CONTROL: [Attribute.SUPPORTED_TRACK_CONTROL_COMMANDS],
    Capability.MODE: [
        Attribute.MODE,
        Attribute.SUPPORTED_ARGUMENTS,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.MOLD_HEALTH_CONCERN: [Attribute.MOLD_HEALTH_CONCERN],
    Capability.MOMENTARY: [],
    Capability.MOTION_SENSOR: [Attribute.MOTION],
    Capability.MUSIC_PLAYER: [
        Attribute.LEVEL,
        Attribute.MUTE,
        Attribute.STATUS,
        Attribute.TRACK_DATA,
        Attribute.TRACK_DESCRIPTION,
    ],
    Capability.NETWORK_METER: [Attribute.DOWNLINK_SPEED, Attribute.UPLINK_SPEED],
    Capability.NITROGEN_DIOXIDE_HEALTH_CONCERN: [
        Attribute.NITROGEN_DIOXIDE_HEALTH_CONCERN
    ],
    Capability.NITROGEN_DIOXIDE_MEASUREMENT: [Attribute.NITROGEN_DIOXIDE],
    Capability.NOTIFICATION: [],
    Capability.OBJECT_DETECTION: [Attribute.DETECTED, Attribute.SUPPORTED_VALUES],
    Capability.OCCUPANCY_SENSOR: [Attribute.OCCUPANCY],
    Capability.OCF: [
        Attribute.DATA_MODEL_VERSION,
        Attribute.DEVICE_ID,
        Attribute.DEVICE_NAME,
        Attribute.HARDWARE_VERSION,
        Attribute.MANUFACTURER_DETAILS_LINK,
        Attribute.MANUFACTURER_NAME,
        Attribute.MANUFACTURE_DATE,
        Attribute.MODEL_NUMBER,
        Attribute.OCF_FIRMWARE_VERSION,
        Attribute.OS_VERSION,
        Attribute.PLATFORM_ID,
        Attribute.PLATFORM_VERSION,
        Attribute.SPEC_VERSION,
        Attribute.SUPPORT_LINK,
        Attribute.SYSTEM_TIME,
        Attribute.VENDOR_ID,
    ],
    Capability.ODOR_SENSOR: [Attribute.ODOR_LEVEL],
    Capability.OVEN_MODE: [Attribute.OVEN_MODE, Attribute.SUPPORTED_OVEN_MODES],
    Capability.OVEN_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.OPERATION_TIME,
        Attribute.OVEN_JOB_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.OVEN_SETPOINT: [Attribute.OVEN_SETPOINT, Attribute.OVEN_SETPOINT_RANGE],
    Capability.OZONE_HEALTH_CONCERN: [Attribute.OZONE_HEALTH_CONCERN],
    Capability.OZONE_MEASUREMENT: [Attribute.OZONE],
    Capability.PH_MEASUREMENT: [Attribute.PH],
    Capability.PANIC_ALARM: [Attribute.PANIC_ALARM],
    Capability.PEST_CONTROL: [Attribute.PEST_CONTROL],
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
    Capability.SPEECH_SYNTHESIS: [],
    Capability.STATELESS_CUSTOM_BUTTON: [Attribute.AVAILABLE_CUSTOM_BUTTONS],
    Capability.STATELESS_FANSPEED_BUTTON: [Attribute.AVAILABLE_FANSPEED_BUTTONS],
    Capability.STATELESS_POWER_TOGGLE_BUTTON: [
        Attribute.AVAILABLE_POWER_TOGGLE_BUTTONS
    ],
    Capability.SWITCH: [Attribute.SWITCH],
    Capability.SWITCH_LEVEL: [Attribute.LEVEL, Attribute.LEVEL_RANGE],
    Capability.TAMPER_ALERT: [Attribute.TAMPER],
    Capability.TEMPERATURE_ALARM: [Attribute.TEMPERATURE_ALARM],
    Capability.TEMPERATURE_LEVEL: [
        Attribute.SUPPORTED_TEMPERATURE_LEVELS,
        Attribute.TEMPERATURE_LEVEL,
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
        Attribute.COOLING_SETPOINT,
        Attribute.COOLING_SETPOINT_RANGE,
    ],
    Capability.THERMOSTAT_FAN_MODE: [
        Attribute.SUPPORTED_THERMOSTAT_FAN_MODES,
        Attribute.THERMOSTAT_FAN_MODE,
    ],
    Capability.THERMOSTAT_HEATING_SETPOINT: [
        Attribute.HEATING_SETPOINT,
        Attribute.HEATING_SETPOINT_RANGE,
    ],
    Capability.THERMOSTAT_MODE: [
        Attribute.SUPPORTED_THERMOSTAT_MODES,
        Attribute.THERMOSTAT_MODE,
    ],
    Capability.THERMOSTAT_OPERATING_STATE: [Attribute.THERMOSTAT_OPERATING_STATE],
    Capability.THERMOSTAT_SETPOINT: [Attribute.THERMOSTAT_SETPOINT],
    Capability.THREE_AXIS: [Attribute.THREE_AXIS],
    Capability.TONE: [],
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
    Capability.VIDEO_CAPTURE: [Attribute.CLIP, Attribute.STREAM],
    Capability.VIDEO_STREAM: [Attribute.STREAM, Attribute.SUPPORTED_FEATURES],
    Capability.VOLTAGE_MEASUREMENT: [Attribute.VOLTAGE],
    Capability.WASHER_MODE: [Attribute.WASHER_MODE],
    Capability.WASHER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
        Attribute.WASHER_JOB_STATE,
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
    Capability.WIND_MODE: [Attribute.SUPPORTED_WIND_MODES, Attribute.WIND_MODE],
    Capability.WINDOW_SHADE: [
        Attribute.SUPPORTED_WINDOW_SHADE_COMMANDS,
        Attribute.WINDOW_SHADE,
    ],
    Capability.WINDOW_SHADE_LEVEL: [Attribute.SHADE_LEVEL],
    Capability.WINDOW_SHADE_PRESET: [],
    Capability.ZWAVE_MULTICHANNEL: [Attribute.EP_EVENT, Attribute.EP_INFO],
    Capability.CUSTOM_ACCESSIBILITY: [],
    Capability.CUSTOM_AIR_CONDITIONER_ODOR_CONTROLLER: [
        Attribute.AIR_CONDITIONER_ODOR_CONTROLLER_PROGRESS,
        Attribute.AIR_CONDITIONER_ODOR_CONTROLLER_STATE,
    ],
    Capability.CUSTOM_AIR_CONDITIONER_OPTIONAL_MODE: [
        Attribute.AC_OPTIONAL_MODE,
        Attribute.SUPPORTED_AC_OPTIONAL_MODE,
    ],
    Capability.CUSTOM_AIR_CONDITIONER_TROPICAL_NIGHT_MODE: [
        Attribute.AC_TROPICAL_NIGHT_MODE_LEVEL
    ],
    Capability.CUSTOM_AIR_QUALITY_MAX_LEVEL: [Attribute.AIR_QUALITY_MAX_LEVEL],
    Capability.CUSTOM_AUTO_CLEANING_MODE: [
        Attribute.AUTO_CLEANING_MODE,
        Attribute.OPERATING_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_AUTO_CLEANING_MODES,
        Attribute.SUPPORTED_OPERATING_STATES,
        Attribute.TIMED_CLEAN_DURATION,
        Attribute.TIMED_CLEAN_DURATION_RANGE,
    ],
    Capability.CUSTOM_COOKTOP_OPERATING_STATE: [
        Attribute.COOKTOP_OPERATING_STATE,
        Attribute.SUPPORTED_COOKTOP_OPERATING_STATE,
    ],
    Capability.CUSTOM_DEODOR_FILTER: [
        Attribute.DEODOR_FILTER_CAPACITY,
        Attribute.DEODOR_FILTER_LAST_RESET_DATE,
        Attribute.DEODOR_FILTER_RESET_TYPE,
        Attribute.DEODOR_FILTER_STATUS,
        Attribute.DEODOR_FILTER_USAGE,
        Attribute.DEODOR_FILTER_USAGE_STEP,
    ],
    Capability.CUSTOM_DEVICE_DEPENDENCY_STATUS: [
        Attribute.DEPENDENCY_STATUS,
        Attribute.NUMBER_OF_SUB_DEVICES,
        Attribute.SUB_DEVICE_ACTIVE,
    ],
    Capability.CUSTOM_DEVICE_REPORT_STATE_CONFIGURATION: [
        Attribute.REPORT_STATE_PERIOD,
        Attribute.REPORT_STATE_REALTIME,
        Attribute.REPORT_STATE_REALTIME_PERIOD,
    ],
    Capability.CUSTOM_DISABLED_CAPABILITIES: [Attribute.DISABLED_CAPABILITIES],
    Capability.CUSTOM_DISABLED_COMPONENTS: [Attribute.DISABLED_COMPONENTS],
    Capability.CUSTOM_DISHWASHER_DELAY_START_TIME: [
        Attribute.DISHWASHER_DELAY_START_TIME
    ],
    Capability.CUSTOM_DISHWASHER_OPERATING_PERCENTAGE: [
        Attribute.DISHWASHER_OPERATING_PERCENTAGE
    ],
    Capability.CUSTOM_DISHWASHER_OPERATING_PROGRESS: [
        Attribute.DISHWASHER_OPERATING_PROGRESS
    ],
    Capability.CUSTOM_DO_NOT_DISTURB_MODE: [
        Attribute.DO_NOT_DISTURB,
        Attribute.END_TIME,
        Attribute.START_TIME,
    ],
    Capability.CUSTOM_DRYER_DRY_LEVEL: [
        Attribute.DRYER_DRY_LEVEL,
        Attribute.SUPPORTED_DRYER_DRY_LEVEL,
    ],
    Capability.CUSTOM_DRYER_WRINKLE_PREVENT: [
        Attribute.DRYER_WRINKLE_PREVENT,
        Attribute.OPERATING_STATE,
    ],
    Capability.CUSTOM_DUST_FILTER: [
        Attribute.DUST_FILTER_CAPACITY,
        Attribute.DUST_FILTER_LAST_RESET_DATE,
        Attribute.DUST_FILTER_RESET_TYPE,
        Attribute.DUST_FILTER_STATUS,
        Attribute.DUST_FILTER_USAGE,
        Attribute.DUST_FILTER_USAGE_STEP,
    ],
    Capability.CUSTOM_ELECTRIC_HEPA_FILTER: [
        Attribute.ELECTRIC_HEPA_FILTER_CAPACITY,
        Attribute.ELECTRIC_HEPA_FILTER_LAST_RESET_DATE,
        Attribute.ELECTRIC_HEPA_FILTER_RESET_TYPE,
        Attribute.ELECTRIC_HEPA_FILTER_STATUS,
        Attribute.ELECTRIC_HEPA_FILTER_USAGE,
        Attribute.ELECTRIC_HEPA_FILTER_USAGE_STEP,
    ],
    Capability.CUSTOM_ENERGY_TYPE: [
        Attribute.DR_MAX_DURATION,
        Attribute.ENERGY_SAVING_INFO,
        Attribute.ENERGY_SAVING_LEVEL,
        Attribute.ENERGY_SAVING_OPERATION,
        Attribute.ENERGY_SAVING_OPERATION_SUPPORT,
        Attribute.ENERGY_SAVING_SUPPORT,
        Attribute.ENERGY_TYPE,
        Attribute.NOTIFICATION_TEMPLATE_I_D,
        Attribute.SUPPORTED_ENERGY_SAVING_LEVELS,
    ],
    Capability.CUSTOM_ERROR: [Attribute.ERROR],
    Capability.CUSTOM_FILTER_USAGE_TIME: [Attribute.USAGE_TIME],
    Capability.CUSTOM_FRIDGE_MODE: [
        Attribute.FRIDGE_MODE,
        Attribute.FRIDGE_MODE_VALUE,
        Attribute.SUPPORTED_FRIDGE_MODES,
    ],
    Capability.CUSTOM_HEPA_FILTER: [
        Attribute.HEPA_FILTER_CAPACITY,
        Attribute.HEPA_FILTER_LAST_RESET_DATE,
        Attribute.HEPA_FILTER_RESET_TYPE,
        Attribute.HEPA_FILTER_STATUS,
        Attribute.HEPA_FILTER_USAGE,
        Attribute.HEPA_FILTER_USAGE_STEP,
    ],
    Capability.CUSTOM_JOB_BEGINNING_STATUS: [Attribute.JOB_BEGINNING_STATUS],
    Capability.CUSTOM_LAUNCH_APP: [],
    Capability.CUSTOM_LOWER_DEVICE_POWER: [Attribute.POWER_STATE],
    Capability.CUSTOM_OCF_RESOURCE_VERSION: [
        Attribute.OCF_RESOURCE_UPDATED_TIME,
        Attribute.OCF_RESOURCE_VERSION,
    ],
    Capability.CUSTOM_OUTING_MODE: [Attribute.OUTING_MODE],
    Capability.CUSTOM_OVEN_CAVITY_STATUS: [Attribute.OVEN_CAVITY_STATUS],
    Capability.CUSTOM_PERIODIC_SENSING: [
        Attribute.AUTOMATIC_EXECUTION_MODE,
        Attribute.AUTOMATIC_EXECUTION_SETTING,
        Attribute.LAST_SENSING_LEVEL,
        Attribute.LAST_SENSING_TIME,
        Attribute.PERIODIC_SENSING,
        Attribute.PERIODIC_SENSING_INTERVAL,
        Attribute.PERIODIC_SENSING_STATUS,
        Attribute.SUPPORTED_AUTOMATIC_EXECUTION_MODE,
        Attribute.SUPPORTED_AUTOMATIC_EXECUTION_SETTING,
    ],
    Capability.CUSTOM_PICTURE_MODE: [
        Attribute.PICTURE_MODE,
        Attribute.SUPPORTED_PICTURE_MODES,
        Attribute.SUPPORTED_PICTURE_MODES_MAP,
    ],
    Capability.CUSTOM_RECORDING: [],
    Capability.CUSTOM_SOUND_MODE: [
        Attribute.SOUND_MODE,
        Attribute.SUPPORTED_SOUND_MODES,
        Attribute.SUPPORTED_SOUND_MODES_MAP,
    ],
    Capability.CUSTOM_SPI_MODE: [Attribute.SPI_MODE],
    Capability.CUSTOM_STEAM_CLOSET_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.PROGRESS,
        Attribute.REMAINING_TIME,
        Attribute.REMAINING_TIME_STR,
        Attribute.STEAM_CLOSET_DELAY_END_TIME,
        Attribute.STEAM_CLOSET_JOB_STATE,
        Attribute.STEAM_CLOSET_MACHINE_STATE,
        Attribute.SUPPORTED_STEAM_CLOSET_JOB_STATE,
        Attribute.SUPPORTED_STEAM_CLOSET_MACHINE_STATE,
    ],
    Capability.CUSTOM_STEAM_CLOSET_WRINKLE_PREVENT: [
        Attribute.STEAM_CLOSET_WRINKLE_PREVENT
    ],
    Capability.CUSTOM_SUPPORTED_OPTIONS: [
        Attribute.COURSE,
        Attribute.REFERENCE_TABLE,
        Attribute.SUPPORTED_COURSES,
    ],
    Capability.CUSTOM_THERMOSTAT_SETPOINT_CONTROL: [
        Attribute.MAXIMUM_SETPOINT,
        Attribute.MINIMUM_SETPOINT,
    ],
    Capability.CUSTOM_TV_SEARCH: [],
    Capability.CUSTOM_USER_NOTIFICATION: [Attribute.MESSAGE],
    Capability.CUSTOM_VERY_FINE_DUST_FILTER: [
        Attribute.VERY_FINE_DUST_FILTER_CAPACITY,
        Attribute.VERY_FINE_DUST_FILTER_LAST_RESET_DATE,
        Attribute.VERY_FINE_DUST_FILTER_RESET_TYPE,
        Attribute.VERY_FINE_DUST_FILTER_STATUS,
        Attribute.VERY_FINE_DUST_FILTER_USAGE,
        Attribute.VERY_FINE_DUST_FILTER_USAGE_STEP,
    ],
    Capability.CUSTOM_WASHER_AUTO_DETERGENT: [Attribute.WASHER_AUTO_DETERGENT],
    Capability.CUSTOM_WASHER_AUTO_SOFTENER: [Attribute.WASHER_AUTO_SOFTENER],
    Capability.CUSTOM_WASHER_RINSE_CYCLES: [
        Attribute.SUPPORTED_WASHER_RINSE_CYCLES,
        Attribute.WASHER_RINSE_CYCLES,
    ],
    Capability.CUSTOM_WASHER_SOIL_LEVEL: [
        Attribute.SUPPORTED_WASHER_SOIL_LEVEL,
        Attribute.WASHER_SOIL_LEVEL,
    ],
    Capability.CUSTOM_WASHER_SPIN_LEVEL: [
        Attribute.SUPPORTED_WASHER_SPIN_LEVEL,
        Attribute.WASHER_SPIN_LEVEL,
    ],
    Capability.CUSTOM_WASHER_WATER_TEMPERATURE: [
        Attribute.SUPPORTED_WASHER_WATER_TEMPERATURE,
        Attribute.WASHER_WATER_TEMPERATURE,
    ],
    Capability.CUSTOM_WATER_FILTER: [
        Attribute.WATER_FILTER_CAPACITY,
        Attribute.WATER_FILTER_LAST_RESET_DATE,
        Attribute.WATER_FILTER_RESET_TYPE,
        Attribute.WATER_FILTER_STATUS,
        Attribute.WATER_FILTER_USAGE,
        Attribute.WATER_FILTER_USAGE_STEP,
    ],
    Capability.CUSTOM_WELCOME_CARE_MODE: [Attribute.WELCOME_CARE_MODE],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_BEEP: [Attribute.BEEP],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_LIGHTING: [
        Attribute.LIGHTING,
        Attribute.SUPPORTED_LIGHTING_LEVELS,
    ],
    Capability.SAMSUNG_CE_AIR_QUALITY_HEALTH_CONCERN: [
        Attribute.AIR_QUALITY_HEALTH_CONCERN,
        Attribute.SUPPORTED_AIR_QUALITY_HEALTH_CONCERNS,
    ],
    Capability.SAMSUNG_CE_ALWAYS_ON_SENSING: [Attribute.ALWAYS_ON, Attribute.ORIGINS],
    Capability.SAMSUNG_CE_AUTO_DISPENSE_DETERGENT: [
        Attribute.AMOUNT,
        Attribute.AVAILABLE_TYPES,
        Attribute.DENSITY,
        Attribute.RECOMMENDED_AMOUNT,
        Attribute.REMAINING_AMOUNT,
        Attribute.SUPPORTED_AMOUNT,
        Attribute.SUPPORTED_DENSITY,
        Attribute.TYPE,
    ],
    Capability.SAMSUNG_CE_AUTO_DISPENSE_SOFTENER: [
        Attribute.AMOUNT,
        Attribute.DENSITY,
        Attribute.REMAINING_AMOUNT,
        Attribute.SUPPORTED_AMOUNT,
        Attribute.SUPPORTED_DENSITY,
    ],
    Capability.SAMSUNG_CE_AUTO_DOOR_RELEASE: [Attribute.AUTO_DOOR_RELEASE_ENABLED],
    Capability.SAMSUNG_CE_BUTTON_DISPLAY_CONDITION: [Attribute.SWITCH],
    Capability.SAMSUNG_CE_CLOTHING_EXTRA_CARE: [
        Attribute.OPERATION_MODE,
        Attribute.USER_LOCATION,
    ],
    Capability.SAMSUNG_CE_CONNECTION_STATE: [Attribute.CONNECTION_STATE],
    Capability.SAMSUNG_CE_CONSUMED_ENERGY: [
        Attribute.MONTHLY_USAGE,
        Attribute.TIME_OFFSET,
    ],
    Capability.SAMSUNG_CE_COOKTOP_BURNER_MODE: [Attribute.COOKTOP_BURNER_MODE],
    Capability.SAMSUNG_CE_COOKTOP_HEATING_POWER: [
        Attribute.HEATING_MODE,
        Attribute.MANUAL_LEVEL,
        Attribute.MANUAL_LEVEL_MAX,
        Attribute.MANUAL_LEVEL_MIN,
        Attribute.SUPPORTED_HEATING_MODES,
    ],
    Capability.SAMSUNG_CE_COOKTOP_PAN_DETECTION: [Attribute.DETECTED],
    Capability.SAMSUNG_CE_COUNT_DOWN_TIMER: [
        Attribute.CURRENT_VALUE,
        Attribute.START_VALUE,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_CUSTOM_RECIPE: [],
    Capability.SAMSUNG_CE_DEFINED_RECIPE: [Attribute.DEFINED_RECIPE],
    Capability.SAMSUNG_CE_DETERGENT_AUTO_REPLENISHMENT: [
        Attribute.BABY_DETERGENT_ALARM_ENABLED,
        Attribute.BABY_DETERGENT_DOSAGE,
        Attribute.BABY_DETERGENT_INITIAL_AMOUNT,
        Attribute.BABY_DETERGENT_ORDER_THRESHOLD,
        Attribute.BABY_DETERGENT_REMAINING_AMOUNT,
        Attribute.BABY_DETERGENT_TYPE,
        Attribute.NEUTRAL_DETERGENT_ALARM_ENABLED,
        Attribute.NEUTRAL_DETERGENT_DOSAGE,
        Attribute.NEUTRAL_DETERGENT_INITIAL_AMOUNT,
        Attribute.NEUTRAL_DETERGENT_ORDER_THRESHOLD,
        Attribute.NEUTRAL_DETERGENT_REMAINING_AMOUNT,
        Attribute.NEUTRAL_DETERGENT_TYPE,
        Attribute.REGULAR_DETERGENT_ALARM_ENABLED,
        Attribute.REGULAR_DETERGENT_DOSAGE,
        Attribute.REGULAR_DETERGENT_INITIAL_AMOUNT,
        Attribute.REGULAR_DETERGENT_ORDER_THRESHOLD,
        Attribute.REGULAR_DETERGENT_REMAINING_AMOUNT,
        Attribute.REGULAR_DETERGENT_TYPE,
    ],
    Capability.SAMSUNG_CE_DETERGENT_ORDER: [
        Attribute.ALARM_ENABLED,
        Attribute.ORDER_THRESHOLD,
    ],
    Capability.SAMSUNG_CE_DETERGENT_STATE: [
        Attribute.DETERGENT_TYPE,
        Attribute.DOSAGE,
        Attribute.INITIAL_AMOUNT,
        Attribute.REMAINING_AMOUNT,
    ],
    Capability.SAMSUNG_CE_DEVICE_IDENTIFICATION: [
        Attribute.BINARY_ID,
        Attribute.DESCRIPTION,
        Attribute.MICOM_ASSAY_CODE,
        Attribute.MODEL_CLASSIFICATION_CODE,
        Attribute.MODEL_NAME,
        Attribute.RELEASE_YEAR,
        Attribute.SERIAL_NUMBER,
        Attribute.SERIAL_NUMBER_EXTRA,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_JOB_STATE: [
        Attribute.DISHWASHER_JOB_STATE,
        Attribute.SCHEDULED_JOBS,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_OPERATION: [
        Attribute.OPERATING_STATE,
        Attribute.OPERATION_TIME,
        Attribute.PROGRESS_PERCENTAGE,
        Attribute.REMAINING_TIME,
        Attribute.REMAINING_TIME_STR,
        Attribute.RESERVABLE,
        Attribute.SUPPORTED_OPERATING_STATE,
        Attribute.TIME_LEFT_TO_START,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_COURSE: [
        Attribute.CUSTOM_COURSE_CANDIDATES,
        Attribute.SUPPORTED_COURSES,
        Attribute.WASHING_COURSE,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_COURSE_DETAILS: [
        Attribute.ENERGY_USAGE_MAX,
        Attribute.PREDEFINED_COURSES,
        Attribute.WATER_USAGE_MAX,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_OPTIONS: [
        Attribute.ADD_RINSE,
        Attribute.DRY_PLUS,
        Attribute.HEATED_DRY,
        Attribute.HIGH_TEMP_WASH,
        Attribute.HOT_AIR_DRY,
        Attribute.RINSE_PLUS,
        Attribute.SANITIZE,
        Attribute.SANITIZING_WASH,
        Attribute.SELECTED_ZONE,
        Attribute.SPEED_BOOSTER,
        Attribute.STEAM_SOAK,
        Attribute.STORM_WASH,
        Attribute.SUPPORTED_LIST,
        Attribute.ZONE_BOOSTER,
    ],
    Capability.SAMSUNG_CE_DO_NOT_DISTURB: [
        Attribute.ACTIVATED,
        Attribute.DAY_OF_WEEK,
        Attribute.END_TIME,
        Attribute.REPEAT_MODE,
        Attribute.SETTABLE,
        Attribute.START_TIME,
    ],
    Capability.SAMSUNG_CE_DONGLE_SOFTWARE_INSTALLATION: [Attribute.STATUS],
    Capability.SAMSUNG_CE_DOOR_STATE: [Attribute.DOOR_STATE],
    Capability.SAMSUNG_CE_DRIVER_STATE: [Attribute.DRIVER_STATE],
    Capability.SAMSUNG_CE_DRIVER_VERSION: [Attribute.VERSION_NUMBER],
    Capability.SAMSUNG_CE_DRUM_SELF_CLEANING: [
        Attribute.HISTORY,
        Attribute.SUGGESTION_THRESHOLD,
        Attribute.WASHING_COUNT_AFTER_SELF_CLEAN,
    ],
    Capability.SAMSUNG_CE_DRYER_AUTO_CYCLE_LINK: [Attribute.DRYER_AUTO_CYCLE_LINK],
    Capability.SAMSUNG_CE_DRYER_CYCLE: [
        Attribute.DRYER_CYCLE,
        Attribute.REFERENCE_TABLE,
        Attribute.SPECIALIZED_FUNCTION_CLASSIFICATION,
        Attribute.SUPPORTED_CYCLES,
    ],
    Capability.SAMSUNG_CE_DRYER_CYCLE_PRESET: [
        Attribute.MAX_NUMBER_OF_PRESETS,
        Attribute.PRESETS,
    ],
    Capability.SAMSUNG_CE_DRYER_DELAY_END: [Attribute.REMAINING_TIME],
    Capability.SAMSUNG_CE_DRYER_DRYING_TEMPERATURE: [
        Attribute.DRYING_TEMPERATURE,
        Attribute.SUPPORTED_DRYING_TEMPERATURE,
    ],
    Capability.SAMSUNG_CE_DRYER_DRYING_TIME: [
        Attribute.DRYING_TIME,
        Attribute.SUPPORTED_DRYING_TIME,
    ],
    Capability.SAMSUNG_CE_DRYER_FREEZE_PREVENT: [Attribute.OPERATING_STATE],
    Capability.SAMSUNG_CE_DRYER_LABEL_SCAN_CYCLE_PRESET: [Attribute.PRESETS],
    Capability.SAMSUNG_CE_DRYER_OPERATING_STATE: [
        Attribute.DRYER_JOB_STATE,
        Attribute.OPERATING_STATE,
        Attribute.PROGRESS,
        Attribute.REMAINING_TIME,
        Attribute.REMAINING_TIME_STR,
        Attribute.SCHEDULED_JOBS,
        Attribute.SUPPORTED_OPERATING_STATES,
    ],
    Capability.SAMSUNG_CE_DUST_FILTER_ALARM: [
        Attribute.ALARM_THRESHOLD,
        Attribute.SUPPORTED_ALARM_THRESHOLDS,
    ],
    Capability.SAMSUNG_CE_EHS_FSV_SETTINGS: [Attribute.FSV_SETTINGS],
    Capability.SAMSUNG_CE_EHS_TEMPERATURE_REFERENCE: [Attribute.TEMPERATURE_REFERENCE],
    Capability.SAMSUNG_CE_EHS_THERMOSTAT: [Attribute.CONNECTION_STATE],
    Capability.SAMSUNG_CE_ENERGY_PLANNER: [Attribute.DATA, Attribute.PLAN],
    Capability.SAMSUNG_CE_ERROR_AND_ALARM_STATE: [Attribute.EVENTS],
    Capability.SAMSUNG_CE_FLEXIBLE_AUTO_DISPENSE_DETERGENT: [
        Attribute.AMOUNT,
        Attribute.AVAILABLE_TYPES,
        Attribute.DENSITY,
        Attribute.RECOMMENDED_AMOUNT,
        Attribute.REMAINING_AMOUNT,
        Attribute.SUPPORTED_AMOUNT,
        Attribute.SUPPORTED_DENSITY,
        Attribute.TYPE,
    ],
    Capability.SAMSUNG_CE_FOOD_DEFROST: [
        Attribute.FOOD_TYPE,
        Attribute.OPERATION_TIME,
        Attribute.REMAINING_TIME,
        Attribute.SUPPORTED_OPTIONS,
        Attribute.WEIGHT,
    ],
    Capability.SAMSUNG_CE_FREEZER_CONVERT_MODE: [
        Attribute.FREEZER_CONVERT_MODE,
        Attribute.SUPPORTED_FREEZER_CONVERT_MODES,
    ],
    Capability.SAMSUNG_CE_FRIDGE_FOOD_LIST: [
        Attribute.OUT_OF_SYNC_CHANGES,
        Attribute.REFRESH_RESULT,
    ],
    Capability.SAMSUNG_CE_FRIDGE_PANTRY_INFO: [Attribute.NAME],
    Capability.SAMSUNG_CE_FRIDGE_PANTRY_MODE: [
        Attribute.MODE,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.SAMSUNG_CE_FRIDGE_VACATION_MODE: [Attribute.VACATION_MODE],
    Capability.SAMSUNG_CE_FRIDGE_WELCOME_LIGHTING: [
        Attribute.DETECTION_PROXIMITY,
        Attribute.STATUS,
        Attribute.SUPPORTED_DETECTION_PROXIMITIES,
    ],
    Capability.SAMSUNG_CE_HOOD_FAN_SPEED: [
        Attribute.HOOD_FAN_SPEED,
        Attribute.SETTABLE_MAX_FAN_SPEED,
        Attribute.SETTABLE_MIN_FAN_SPEED,
        Attribute.SUPPORTED_HOOD_FAN_SPEED,
    ],
    Capability.SAMSUNG_CE_INDIVIDUAL_CONTROL_LOCK: [Attribute.LOCK_STATE],
    Capability.SAMSUNG_CE_KIDS_LOCK: [Attribute.LOCK_STATE],
    Capability.SAMSUNG_CE_KIDS_LOCK_CONTROL: [Attribute.LOCK_STATE],
    Capability.SAMSUNG_CE_KITCHEN_DEVICE_DEFAULTS: [
        Attribute.DEFAULT_OPERATION_TIME,
        Attribute.DEFAULT_OVEN_MODE,
        Attribute.DEFAULT_OVEN_SETPOINT,
    ],
    Capability.SAMSUNG_CE_KITCHEN_DEVICE_IDENTIFICATION: [
        Attribute.FUEL,
        Attribute.MODEL_CODE,
        Attribute.REGION_CODE,
        Attribute.REPRESENTATIVE_COMPONENT,
        Attribute.TYPE,
    ],
    Capability.SAMSUNG_CE_KITCHEN_MODE_SPECIFICATION: [Attribute.SPECIFICATION],
    Capability.SAMSUNG_CE_LAMP: [
        Attribute.BRIGHTNESS_LEVEL,
        Attribute.SUPPORTED_BRIGHTNESS_LEVEL,
    ],
    Capability.SAMSUNG_CE_MEAT_AGING: [
        Attribute.STATUS,
        Attribute.SUPPORTED_AGING_METHODS,
        Attribute.SUPPORTED_MEAT_TYPES,
        Attribute.ZONE_INFO,
    ],
    Capability.SAMSUNG_CE_MEAT_PROBE: [
        Attribute.STATUS,
        Attribute.TEMPERATURE,
        Attribute.TEMPERATURE_SETPOINT,
    ],
    Capability.SAMSUNG_CE_MICROWAVE_POWER: [
        Attribute.POWER_LEVEL,
        Attribute.SUPPORTED_POWER_LEVELS,
    ],
    Capability.SAMSUNG_CE_MUSIC_PLAYLIST: [Attribute.CURRENT_TRACK, Attribute.PLAYLIST],
    Capability.SAMSUNG_CE_OPERATION_ORIGIN: [],
    Capability.SAMSUNG_CE_OVEN_DRAINAGE_REQUIREMENT: [Attribute.DRAINAGE_REQUIREMENT],
    Capability.SAMSUNG_CE_OVEN_MODE: [
        Attribute.OVEN_MODE,
        Attribute.SUPPORTED_OVEN_MODES,
    ],
    Capability.SAMSUNG_CE_OVEN_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.OPERATING_STATE,
        Attribute.OPERATION_TIME,
        Attribute.OVEN_JOB_STATE,
        Attribute.PROGRESS,
    ],
    Capability.SAMSUNG_CE_POWER_CONSUMPTION_RECORD: [Attribute.PAYLOAD],
    Capability.SAMSUNG_CE_POWER_COOL: [Attribute.ACTIVATED],
    Capability.SAMSUNG_CE_POWER_FREEZE: [Attribute.ACTIVATED],
    Capability.SAMSUNG_CE_QUICK_CONTROL: [Attribute.VERSION],
    Capability.SAMSUNG_CE_RECHARGEABLE_BATTERY: [
        Attribute.BATTERY,
        Attribute.CHARGING_STATUS,
        Attribute.RESOLUTION,
    ],
    Capability.SAMSUNG_CE_REMOTE_MANAGEMENT_DATA: [
        Attribute.REPORT_RAW_DATA,
        Attribute.VERSION,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_AUDIO_CLIP: [Attribute.ENABLED],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_AVP_REGISTRATION: [
        Attribute.REGISTRATION_STATUS
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_CLEANING_MODE: [
        Attribute.CLEANING_MODE,
        Attribute.REPEAT_MODE_ENABLED,
        Attribute.SUPPORTED_CLEANING_MODE,
        Attribute.SUPPORT_REPEAT_MODE,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_DRIVING_MODE: [
        Attribute.DRIVING_MODE,
        Attribute.SUPPORTED_DRIVING_MODES,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_DUST_BAG: [
        Attribute.STATUS,
        Attribute.SUPPORTED_STATUS,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_FEATURE_VISIBILITY: [
        Attribute.INVISIBLE_FEATURES,
        Attribute.VISIBLE_FEATURES,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_AREA_INFO: [Attribute.AREA_INFO],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_CLEANING_INFO: [
        Attribute.AREA,
        Attribute.CLEANED_EXTENT,
        Attribute.NEAR_OBJECT,
        Attribute.REMAINING_TIME,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_LIST: [Attribute.MAPS],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MONITORING_AUTOMATION: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MOTOR_FILTER: [
        Attribute.MOTOR_FILTER_RESET_TYPE,
        Attribute.MOTOR_FILTER_STATUS,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_OPERATING_STATE: [
        Attribute.CLEANING_STEP,
        Attribute.HOMING_REASON,
        Attribute.IS_MAP_BASED_OPERATION_AVAILABLE,
        Attribute.OPERATING_STATE,
        Attribute.SUPPORTED_OPERATING_STATE,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PATROL: [
        Attribute.AREA_IDS,
        Attribute.BLOCKING_STATUS,
        Attribute.DAY_OF_WEEK,
        Attribute.ENABLED,
        Attribute.END_TIME,
        Attribute.INTERVAL,
        Attribute.OBSOLETED,
        Attribute.PATROL_STATUS,
        Attribute.START_TIME,
        Attribute.WAYPOINTS,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PET_CLEANING_SCHEDULE: [
        Attribute.AREA_IDS,
        Attribute.DAY_OF_WEEK,
        Attribute.ENABLED,
        Attribute.MAP_ID,
        Attribute.OBSOLETED,
        Attribute.ORIGINATOR,
        Attribute.START_TIME,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PET_MONITOR: [
        Attribute.AREA_IDS,
        Attribute.BLOCKING_STATUS,
        Attribute.DAY_OF_WEEK,
        Attribute.ENABLED,
        Attribute.END_TIME,
        Attribute.INTERVAL,
        Attribute.MAP_ID,
        Attribute.MONITORING_STATUS,
        Attribute.OBSOLETED,
        Attribute.ORIGINATOR,
        Attribute.START_TIME,
        Attribute.WAYPOINTS,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PET_MONITOR_REPORT: [Attribute.REPORT],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_RELAY_CLEANING: [Attribute.BATON_TOUCH],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_RESERVATION: [
        Attribute.MAX_NUMBER_OF_RESERVATIONS,
        Attribute.RESERVATIONS,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_WELCOME: [Attribute.COORDINATES],
    Capability.SAMSUNG_CE_RUNESTONE_HOME_CONTEXT: [Attribute.SUPPORTED_CONTEXTS],
    Capability.SAMSUNG_CE_SABBATH_MODE: [Attribute.STATUS, Attribute.SUPPORTED_ACTIONS],
    Capability.SAMSUNG_CE_SAC_DISPLAY_CONDITION: [Attribute.SWITCH],
    Capability.SAMSUNG_CE_SCALE_SETTINGS: [Attribute.ENABLED],
    Capability.SAMSUNG_CE_SELF_CHECK: [
        Attribute.ERRORS,
        Attribute.PROGRESS,
        Attribute.RESULT,
        Attribute.STATUS,
        Attribute.SUPPORTED_ACTIONS,
    ],
    Capability.SAMSUNG_CE_SILENT_ACTION: [],
    Capability.SAMSUNG_CE_SOFTENER_AUTO_REPLENISHMENT: [
        Attribute.REGULAR_SOFTENER_ALARM_ENABLED,
        Attribute.REGULAR_SOFTENER_DOSAGE,
        Attribute.REGULAR_SOFTENER_INITIAL_AMOUNT,
        Attribute.REGULAR_SOFTENER_ORDER_THRESHOLD,
        Attribute.REGULAR_SOFTENER_REMAINING_AMOUNT,
        Attribute.REGULAR_SOFTENER_TYPE,
    ],
    Capability.SAMSUNG_CE_SOFTENER_ORDER: [
        Attribute.ALARM_ENABLED,
        Attribute.ORDER_THRESHOLD,
    ],
    Capability.SAMSUNG_CE_SOFTENER_STATE: [
        Attribute.DOSAGE,
        Attribute.INITIAL_AMOUNT,
        Attribute.REMAINING_AMOUNT,
        Attribute.SOFTENER_TYPE,
    ],
    Capability.SAMSUNG_CE_SOFTWARE_UPDATE: [
        Attribute.AVAILABLE_MODULES,
        Attribute.LAST_UPDATED_DATE,
        Attribute.NEW_VERSION_AVAILABLE,
        Attribute.OPERATING_STATE,
        Attribute.OTN_D_U_I_D,
        Attribute.PROGRESS,
        Attribute.TARGET_MODULE,
    ],
    Capability.SAMSUNG_CE_SOFTWARE_VERSION: [Attribute.VERSIONS],
    Capability.SAMSUNG_CE_SOUND_DETECTION_SENSITIVITY: [
        Attribute.LEVEL,
        Attribute.SUPPORTED_LEVELS,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_AUTO_CYCLE_LINK: [
        Attribute.STEAM_CLOSET_AUTO_CYCLE_LINK
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_CYCLE: [
        Attribute.REFERENCE_TABLE,
        Attribute.STEAM_CLOSET_CYCLE,
        Attribute.SUPPORTED_CYCLES,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_CYCLE_PRESET: [
        Attribute.MAX_NUMBER_OF_PRESETS,
        Attribute.PRESETS,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_DELAY_END: [Attribute.REMAINING_TIME],
    Capability.SAMSUNG_CE_STEAM_CLOSET_KEEP_FRESH_MODE: [
        Attribute.OPERATING_STATE,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_SANITIZE_MODE: [Attribute.STATUS],
    Capability.SAMSUNG_CE_SURFACE_RESIDUAL_HEAT: [Attribute.SURFACE_RESIDUAL_HEAT],
    Capability.SAMSUNG_CE_TEMPERATURE_SETTING: [
        Attribute.DESIRED_TEMPERATURE,
        Attribute.SUPPORTED_DESIRED_TEMPERATURES,
    ],
    Capability.SAMSUNG_CE_TOGGLE_SWITCH: [Attribute.SWITCH],
    Capability.SAMSUNG_CE_UNAVAILABLE_CAPABILITIES: [Attribute.UNAVAILABLE_COMMANDS],
    Capability.SAMSUNG_CE_VIEW_INSIDE: [
        Attribute.CONTENTS,
        Attribute.LAST_UPDATED_TIME,
        Attribute.SUPPORTED_FOCUS_AREAS,
    ],
    Capability.SAMSUNG_CE_WASHER_BUBBLE_SOAK: [Attribute.STATUS],
    Capability.SAMSUNG_CE_WASHER_CYCLE: [
        Attribute.REFERENCE_TABLE,
        Attribute.SPECIALIZED_FUNCTION_CLASSIFICATION,
        Attribute.SUPPORTED_CYCLES,
        Attribute.WASHER_CYCLE,
    ],
    Capability.SAMSUNG_CE_WASHER_CYCLE_PRESET: [
        Attribute.MAX_NUMBER_OF_PRESETS,
        Attribute.PRESETS,
    ],
    Capability.SAMSUNG_CE_WASHER_DELAY_END: [
        Attribute.MINIMUM_RESERVABLE_TIME,
        Attribute.REMAINING_TIME,
    ],
    Capability.SAMSUNG_CE_WASHER_FREEZE_PREVENT: [Attribute.OPERATING_STATE],
    Capability.SAMSUNG_CE_WASHER_LABEL_SCAN_CYCLE_PRESET: [Attribute.PRESETS],
    Capability.SAMSUNG_CE_WASHER_OPERATING_STATE: [
        Attribute.OPERATING_STATE,
        Attribute.OPERATION_TIME,
        Attribute.PROGRESS,
        Attribute.REMAINING_TIME,
        Attribute.REMAINING_TIME_STR,
        Attribute.SCHEDULED_JOBS,
        Attribute.SCHEDULED_PHASES,
        Attribute.SUPPORTED_OPERATING_STATES,
        Attribute.WASHER_JOB_PHASE,
        Attribute.WASHER_JOB_STATE,
    ],
    Capability.SAMSUNG_CE_WASHER_WASHING_TIME: [
        Attribute.SUPPORTED_WASHING_TIMES,
        Attribute.WASHING_TIME,
    ],
    Capability.SAMSUNG_CE_WASHER_WATER_LEVEL: [
        Attribute.SUPPORTED_WATER_LEVEL,
        Attribute.WATER_LEVEL,
    ],
    Capability.SAMSUNG_CE_WASHER_WATER_VALVE: [
        Attribute.SUPPORTED_WATER_VALVE,
        Attribute.WATER_VALVE,
    ],
    Capability.SAMSUNG_CE_WATER_CONSUMPTION_REPORT: [Attribute.WATER_CONSUMPTION],
    Capability.SAMSUNG_CE_WATER_RESERVOIR: [Attribute.SLOT_STATE],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT: [Attribute.WEIGHT],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT_CALIBRATION: [],
    Capability.SAMSUNG_CE_WELCOME_COOLING: [
        Attribute.LATEST_REQUEST_ID,
        Attribute.OPERATING_STATE,
    ],
    Capability.SAMSUNG_CE_WELCOME_MESSAGE: [Attribute.WELCOME_MESSAGE],
    Capability.SAMSUNG_CE_WIFI_KIT_SUB_DEVICES: [
        Attribute.NUMBER_OF_CONNECTED_DEVICES,
        Attribute.SUB_DEVICES,
    ],
    Capability.SAMSUNG_VD_AMBIENT: [],
    Capability.SAMSUNG_VD_AMBIENT18: [],
    Capability.SAMSUNG_VD_AMBIENT_CONTENT: [Attribute.SUPPORTED_AMBIENT_APPS],
    Capability.SAMSUNG_VD_AUDIO_GROUP_INFO: [
        Attribute.CHANNEL,
        Attribute.ROLE,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_VD_AUDIO_INPUT_SOURCE: [
        Attribute.INPUT_SOURCE,
        Attribute.SUPPORTED_INPUT_SOURCES,
    ],
    Capability.SAMSUNG_VD_DEVICE_CATEGORY: [Attribute.CATEGORY],
    Capability.SAMSUNG_VD_FIRMWARE_VERSION: [Attribute.FIRMWARE_VERSION],
    Capability.SAMSUNG_VD_GROUP_INFO: [
        Attribute.CHANNEL,
        Attribute.MASTER_NAME,
        Attribute.ROLE,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_VD_LIGHT_CONTROL: [
        Attribute.ERROR_CODE,
        Attribute.REQUEST_ID,
        Attribute.SELECTED_APP_ID,
        Attribute.SELECTED_MODE,
        Attribute.STREAM_CONTROL,
        Attribute.SUPPORTED_MODES,
        Attribute.SUPPORTED_MODE_MAP,
    ],
    Capability.SAMSUNG_VD_MEDIA_INPUT_SOURCE: [
        Attribute.INPUT_SOURCE,
        Attribute.SUPPORTED_INPUT_SOURCES_MAP,
    ],
    Capability.SAMSUNG_VD_PICTURE_MODE: [
        Attribute.PICTURE_MODE,
        Attribute.SUPPORTED_PICTURE_MODES,
        Attribute.SUPPORTED_PICTURE_MODES_MAP,
    ],
    Capability.SAMSUNG_VD_REMOTE_CONTROL: [],
    Capability.SAMSUNG_VD_SOUND_DETECTION: [Attribute.SOUND_DETECTED],
    Capability.SAMSUNG_VD_SOUND_FROM: [Attribute.DETAIL_NAME, Attribute.MODE],
    Capability.SAMSUNG_VD_SOUND_MODE: [
        Attribute.SOUND_MODE,
        Attribute.SUPPORTED_SOUND_MODES,
        Attribute.SUPPORTED_SOUND_MODES_MAP,
    ],
    Capability.SAMSUNG_VD_SUPPORTS_FEATURES: [
        Attribute.EXECUTABLE_SERVICE_LIST,
        Attribute.IME_ADV_SUPPORTED,
        Attribute.MEDIA_OUTPUT_SUPPORTED,
        Attribute.MOBILE_CAM_SUPPORTED,
        Attribute.REMOTELESS_SUPPORTED,
        Attribute.WIFI_UPDATE_SUPPORT,
    ],
    Capability.SAMSUNG_VD_SUPPORTS_POWER_ON_BY_OCF: [
        Attribute.SUPPORTS_POWER_ON_BY_OCF
    ],
    Capability.SAMSUNG_VD_THING_STATUS: [Attribute.STATUS, Attribute.UPDATED_TIME],
    Capability.SAMSUNG_IM_ANNOUNCEMENT: [
        Attribute.ENABLE_STATE,
        Attribute.SUPPORTED_CATEGORIES,
        Attribute.SUPPORTED_MIMES,
        Attribute.SUPPORTED_TYPES,
    ],
    Capability.SAMSUNG_IM_BIXBY_CONTENT: [Attribute.SUPPORTED_MODES],
    Capability.SAMSUNG_IM_FIXED_FIND_NODE: [],
    Capability.SAMSUNG_IM_HUE_SYNC_MODE: [Attribute.MODE],
    Capability.SAMSUNG_IM_NETWORK_AUDIO_GROUP_INFO: [
        Attribute.ACM_MODE,
        Attribute.CHANNEL,
        Attribute.GROUP_NAME,
        Attribute.MASTER_DI,
        Attribute.MASTER_NAME,
        Attribute.ROLE,
        Attribute.STATUS,
        Attribute.STEREO_TYPE,
    ],
    Capability.SAMSUNG_IM_NETWORK_AUDIO_MODE: [Attribute.MODE],
    Capability.SAMSUNG_IM_NETWORK_AUDIO_TRACK_DATA: [
        Attribute.APP_NAME,
        Attribute.SOURCE,
    ],
    Capability.HCA_DRYER_MODE: [Attribute.MODE, Attribute.SUPPORTED_MODES],
    Capability.HCA_WASHER_MODE: [Attribute.MODE, Attribute.SUPPORTED_MODES],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_MUTE: [],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_DOWN: [],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_UP: [],
    Capability.ABATEACHIEVE62503_STATELESS_CHANNEL_DOWN: [],
    Capability.ABATEACHIEVE62503_STATELESS_CHANNEL_UP: [],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_FOUR: [
        Attribute.ASSOCIATION_GROUP_FOUR
    ],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_THREE: [
        Attribute.ASSOCIATION_GROUP_THREE
    ],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_TWO: [Attribute.ASSOCIATION_GROUP_TWO],
    Capability.PLATEMUSIC11009_DEVICE_NETWORK_ID: [Attribute.DEVICE_NETWORK_ID],
    Capability.PLATEMUSIC11009_FIRMWARE: [Attribute.FIRMWARE_VERSION],
    Capability.SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT: [Attribute.CIRCADIAN],
    Capability.SYNTHETIC_FADE_LIGHTNING_EFFECT: [Attribute.FADE],
    Capability.WATCHPANEL55613_LCCTHERMOSTAT: [Attribute.DRCAPABLE],
    Capability.LEGENDABSOLUTE60149_ATMOS_PRESSURE: [Attribute.ATMOS_PRESSURE],
    Capability.LEGENDABSOLUTE60149_CREATE_DEVICE2: [Attribute.CREATE_DEVICE],
    Capability.LEGENDABSOLUTE60149_CURRENT_TIME_PERIOD: [Attribute.CURRENT_TIME_PERIOD],
    Capability.LEGENDABSOLUTE60149_CURRENT_TWILIGHT: [Attribute.CURRENT_TWILIGHT],
    Capability.LEGENDABSOLUTE60149_DAY_LENGTH: [Attribute.DAY_LENGTH],
    Capability.LEGENDABSOLUTE60149_DRIVER_VERSION1: [Attribute.DRIVER_VERSION],
    Capability.LEGENDABSOLUTE60149_EFFECTS_SET_COMMAND: [Attribute.EFFECTS_SET_COMMAND],
    Capability.LEGENDABSOLUTE60149_ENERGY_RESET1: [Attribute.ENERGY_RESET],
    Capability.LEGENDABSOLUTE60149_EVEN_ODD_DAY: [Attribute.EVEN_ODD_DAY],
    Capability.LEGENDABSOLUTE60149_FORCED_ON_LEVEL: [Attribute.FORCED_ON_LEVEL],
    Capability.LEGENDABSOLUTE60149_GET_GROUPS: [Attribute.GET_GROUPS],
    Capability.LEGENDABSOLUTE60149_LEVEL_STEPS: [Attribute.LEVEL_STEPS],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE: [Attribute.LOCAL_DATE],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE_ONE: [Attribute.LOCAL_DATE_ONE],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE_TWO1: [Attribute.LOCAL_DATE_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_DAY: [Attribute.LOCAL_DAY],
    Capability.LEGENDABSOLUTE60149_LOCAL_DAY_TWO: [Attribute.LOCAL_DAY_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR: [Attribute.LOCAL_HOUR],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR_OFFSET: [Attribute.LOCAL_HOUR_OFFSET],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR_TWO: [Attribute.LOCAL_HOUR_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH: [Attribute.LOCAL_MONTH],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_ONE: [Attribute.LOCAL_MONTH_DAY_ONE],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_TWO: [Attribute.LOCAL_MONTH_DAY_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_TWO: [Attribute.LOCAL_MONTH_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_WEEK_DAY: [Attribute.LOCAL_WEEK_DAY],
    Capability.LEGENDABSOLUTE60149_LOCAL_YEAR: [Attribute.LOCAL_YEAR],
    Capability.LEGENDABSOLUTE60149_MIRROR_GROUP_FUNCTION: [
        Attribute.MIRROR_GROUP_FUNCTION
    ],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_OFF1: [Attribute.PROG_OFF],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_ON1: [Attribute.PROG_ON],
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP: [Attribute.RANDOM_NEXT],
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP2: [Attribute.RANDOM_NEXT],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF1: [Attribute.RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF2: [Attribute.RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_SIGNAL_METRICS: [Attribute.SIGNAL_METRICS],
    Capability.LEGENDABSOLUTE60149_SUN_AZIMUTH_ANGLE: [Attribute.SUN_AZIMUTH_ANGLE],
    Capability.LEGENDABSOLUTE60149_SUN_ELEVATION_ANGLE: [Attribute.SUN_ELEVATION_ANGLE],
    Capability.LEGENDABSOLUTE60149_SUN_RISE: [Attribute.SUN_RISE],
    Capability.LEGENDABSOLUTE60149_SUN_RISE_OFFSET1: [Attribute.SUN_RISE_OFFSET],
    Capability.LEGENDABSOLUTE60149_SUN_SET: [Attribute.SUN_SET],
    Capability.LEGENDABSOLUTE60149_SUN_SET_OFFSET1: [Attribute.SUN_SET_OFFSET],
    Capability.LEGENDABSOLUTE60149_SWITCH_ALL_ON_OFF1: [Attribute.SWITCH_ALL_ON_OFF],
    Capability.SEC_CALM_CONNECTION_CARE: [
        Attribute.PROTOCOLS,
        Attribute.ROLE,
        Attribute.VERSION,
    ],
    Capability.SEC_DEVICE_CONNECTION_STATE: [Attribute.DEVICE_CONNECTION_STATE],
    Capability.SEC_DIAGNOSTICS_INFORMATION: [
        Attribute.DUMP_TYPE,
        Attribute.ENDPOINT,
        Attribute.LOG_TYPE,
        Attribute.MIN_VERSION,
        Attribute.MN_ID,
        Attribute.PROTOCOL_TYPE,
        Attribute.SETUP_ID,
        Attribute.SIGNIN_PERMISSION,
        Attribute.TS_ID,
    ],
    Capability.SEC_WIFI_CONFIGURATION: [
        Attribute.AUTO_RECONNECTION,
        Attribute.MIN_VERSION,
        Attribute.PROTOCOL_TYPE,
        Attribute.SUPPORTED_AUTH_TYPE,
        Attribute.SUPPORTED_WI_FI_FREQ,
    ],
    Capability.PARTYVOICE23922_BAROMETER2: [Attribute.PRESSURE],
    Capability.PARTYVOICE23922_CLOUDCOVER: [Attribute.CLOUDCOVER],
    Capability.PARTYVOICE23922_CREATEANOTHER: [],
    Capability.PARTYVOICE23922_CREATEDEV8: [Attribute.DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEHTTPDEV2B: [Attribute.DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEMQTTDEV9: [Attribute.DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEQTY: [Attribute.CREATE_QTY],
    Capability.PARTYVOICE23922_HTTPCODE: [Attribute.HTTPCODE],
    Capability.PARTYVOICE23922_HTTPRESPONSE: [Attribute.RESPONSE],
    Capability.PARTYVOICE23922_INVENTORY8: [Attribute.INVENTORY],
    Capability.PARTYVOICE23922_MQTTPUBLISH: [],
    Capability.PARTYVOICE23922_ONVIFINFO: [Attribute.INFO],
    Capability.PARTYVOICE23922_ONVIFSTATUS: [Attribute.STATUS],
    Capability.PARTYVOICE23922_PRECIPPROB: [Attribute.PROBABILITY],
    Capability.PARTYVOICE23922_PRECIPRATE: [Attribute.PRECIP],
    Capability.PARTYVOICE23922_REFRESH: [],
    Capability.PARTYVOICE23922_SETILLUMINANCE: [Attribute.ILLUMVALUE],
    Capability.PARTYVOICE23922_STATUS: [Attribute.STATUS],
    Capability.PARTYVOICE23922_SUMMARY: [Attribute.SUMMARY],
    Capability.PARTYVOICE23922_TEMPMAX: [Attribute.MAXTEMP],
    Capability.PARTYVOICE23922_TEMPMIN: [Attribute.MINTEMP],
    Capability.PARTYVOICE23922_TOPICLIST: [Attribute.TOPICLIST],
    Capability.PARTYVOICE23922_VHUMIDITYSET: [Attribute.VHUMIDITY],
    Capability.PARTYVOICE23922_VTEMPSET: [Attribute.VTEMP],
    Capability.PARTYVOICE23922_WINDDIRDEG: [Attribute.WINDDEG],
    Capability.PARTYVOICE23922_WINDDIRECTION2: [Attribute.DIRECTION],
    Capability.PARTYVOICE23922_WINDGUST: [Attribute.WINDGUST],
    Capability.PARTYVOICE23922_WINDSPEED5: [Attribute.W_SPEED],
    Capability.VALLEYBOARD16460_DEBUG: [Attribute.VALUE],
    Capability.RIVERTALENT14263_ADAPTIVE_ENERGY_USAGE_STATE: [
        Attribute.ENERGY_USAGE_STATE,
        Attribute.GRID_STATUS_STATUS,
        Attribute.GRID_STATUS_SUPPORT,
        Attribute.STORM_WATCH_ACTIVE,
        Attribute.STORM_WATCH_ENABLED,
        Attribute.STORM_WATCH_SUPPORT,
    ],
    Capability.RIVERTALENT14263_ENERGY_METER_PROPERTIES: [
        Attribute.DATE_STARTED,
        Attribute.HAS_COST,
        Attribute.HAS_FROM_GRID,
        Attribute.HAS_TODAY_USAGE,
        Attribute.HAS_TOTAL_USAGE,
        Attribute.HAS_TO_GRID,
        Attribute.MEASURE_INTERVAL,
        Attribute.METERING_DATE,
        Attribute.RATE_TYPE,
        Attribute.SERVICE_MESSAGE,
        Attribute.SUPPORT_TOU_EVENT_NOTIFICATION,
        Attribute.SUPPORT_TOU_INFO,
        Attribute.TARIFF_NAME,
        Attribute.TARIFF_PROVIDER,
        Attribute.TOU_EVENT_NOTIFICATION,
        Attribute.TOU_INFO,
    ],
    Capability.TAG_E2E_ENCRYPTION: [Attribute.ENCRYPTION],
    Capability.TAG_FACTORY_RESET: [],
    Capability.TAG_SEARCHING_STATUS: [Attribute.SEARCHING_STATUS],
    Capability.TAG_TAG_BUTTON: [Attribute.TAG_BUTTON],
    Capability.TAG_TAG_STATUS: [
        Attribute.CONNECTED_DEVICE_ID,
        Attribute.CONNECTED_USER_ID,
        Attribute.TAG_STATUS,
    ],
    Capability.TAG_UPDATED_INFO: [Attribute.CONNECTION],
    Capability.TAG_UWB_ACTIVATION: [Attribute.UWB_ACTIVATION],
    Capability.AMBERPIANO10217_BINDING_INFO: [Attribute.INFO_HTML, Attribute.INFO_TEXT],
    Capability.AMBERPIANO10217_CLUSTER: [
        Attribute.CLUSTER_ID,
        Attribute.CLUSTER_ID_DEC,
        Attribute.CLUSTER_NAME,
    ],
    Capability.AMBERPIANO10217_CONTROLLER_STATUS: [Attribute.INFO, Attribute.STATUS],
    Capability.AMBERPIANO10217_DETECTION_INTERVAL: [Attribute.DETECTION_INTERVAL],
    Capability.AMBERPIANO10217_DEVICE_EUI: [Attribute.EUI],
    Capability.AMBERPIANO10217_DEVICEINFO: [
        Attribute.APP_VERSION,
        Attribute.BASIC_HTML,
        Attribute.BASIC_HTML_DISABLE,
        Attribute.DASH_BOARD_VALUE,
        Attribute.ZCL_VERSION,
    ],
    Capability.AMBERPIANO10217_GROUP_ADD: [Attribute.STATUS],
    Capability.AMBERPIANO10217_GROUP_INFO: [Attribute.INFO_HTML, Attribute.INFO_TEXT],
    Capability.AMBERPIANO10217_GROUP_REMOVE: [Attribute.GROUP_ID],
    Capability.AMBERPIANO10217_GROUP_REMOVE_ALL: [],
    Capability.AMBERPIANO10217_OBJECT: [Attribute.DATA],
    Capability.AMBERPIANO10217_SENSOR_DETECTION_SENSITIVITY: [
        Attribute.SENSITIVITY_MODE,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.AMBERPIANO10217_VIRTUAL_THING_TYPE: [
        Attribute.SUPPORTED_TYPES,
        Attribute.TYPE,
    ],
}
