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
    ACTION_SETTING = "actionSetting"
    ACTIVATED = "activated"
    ACTIVATED_SCENE = "activatedScene"
    ACTIVATION_STATE = "activationState"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    ACTIVITY_SENSITIVITY = "activitySensitivity"
    ACTUAL_FAN_SPEED = "actualFanSpeed"
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
    ALARM_MODE = "alarmMode"
    ALARM_SENSOR_STATE = "alarmSensorState"
    ALARM_THRESHOLD = "alarmThreshold"
    ALTITUDE_ACCURACY = "altitudeAccuracy"
    ALWAYS_ON = "alwaysOn"
    AMOUNT = "amount"
    AMOUNT_RESOLUTION = "amountResolution"
    AMPERAGE = "amperage"
    AP_OPERATION_MODE = "apOperationMode"
    APP_NAME = "appName"
    APP_VERSION = "appVersion"
    AREA = "area"
    AREA_IDS = "areaIds"
    AREA_INFO = "areaInfo"
    ART_SUPPORTED = "artSupported"
    ASSOCIATION_GROUP_FOUR = "associationGroupFour"
    ASSOCIATION_GROUP_THREE = "associationGroupThree"
    ASSOCIATION_GROUP_TWO = "associationGroupTwo"
    ATMOS_PRESSURE = "atmosPressure"
    ATMOSPHERIC_PRESSURE = "atmosphericPressure"
    AUDIO = "audio"
    AUDIO_ONLY = "audioOnly"
    AUDIO_TRACK_DATA = "audioTrackData"
    AUTO_CLEANING_MODE = "autoCleaningMode"
    AUTO_DOOR_RELEASE_ENABLED = "autoDoorReleaseEnabled"
    AUTO_LOCK = "autoLock"
    AUTO_MODE = "autoMode"
    AUTO_RECONNECTION = "autoReconnection"
    AUTO_UPDATE_ENABLED = "autoUpdateEnabled"
    AUTOLOCK = "autolock"
    AUTOMATIC_EXECUTION_MODE = "automaticExecutionMode"
    AUTOMATIC_EXECUTION_SETTING = "automaticExecutionSetting"
    AVAILABILITY = "availability"
    AVAILABLE = "available"
    AVAILABLE_AC_FAN_MODES = "availableAcFanModes"
    AVAILABLE_AC_MODES = "availableAcModes"
    AVAILABLE_CUSTOM_BUTTONS = "availableCustomButtons"
    AVAILABLE_FAN_OSCILLATION_MODES = "availableFanOscillationModes"
    AVAILABLE_FANSPEED_BUTTONS = "availableFanspeedButtons"
    AVAILABLE_MODULES = "availableModules"
    AVAILABLE_POWER_BUTTONS = "availablePowerButtons"
    AVAILABLE_POWER_TOGGLE_BUTTONS = "availablePowerToggleButtons"
    AVAILABLE_PROGRAMS = "availablePrograms"
    AVAILABLE_TYPES = "availableTypes"
    AVAILABLE_VERSION = "availableVersion"
    AVAILABLE_WATER_SPRAY_LEVELS = "availableWaterSprayLevels"
    BABY_DETERGENT_ALARM_ENABLED = "babyDetergentAlarmEnabled"
    BABY_DETERGENT_DOSAGE = "babyDetergentDosage"
    BABY_DETERGENT_INITIAL_AMOUNT = "babyDetergentInitialAmount"
    BABY_DETERGENT_ORDER_THRESHOLD = "babyDetergentOrderThreshold"
    BABY_DETERGENT_REMAINING_AMOUNT = "babyDetergentRemainingAmount"
    BABY_DETERGENT_TYPE = "babyDetergentType"
    BASIC_HTML = "basicHtml"
    BASIC_HTML_DISABLE = "basicHtmlDisable"
    BASIC_SET_ASSOCIATION_GROUP = "basicSetAssociationGroup"
    BATON_TOUCH = "batonTouch"
    BATTERY = "battery"
    BEEP = "beep"
    BELL_SOUNDS = "bellSounds"
    BINARY_ID = "binaryId"
    BLE_CONNECTION_STATE = "bleConnectionState"
    BLOCKING_STATUS = "blockingStatus"
    BMI_MEASUREMENT = "bmiMeasurement"
    BODY_WEIGHT_MEASUREMENT = "bodyWeightMeasurement"
    BRIGHTNESS_INTENSITY = "brightnessIntensity"
    BRIGHTNESS_LEVEL = "brightnessLevel"
    BURNER_ID = "burnerId"
    BUTTON = "button"
    BYPASS_STATUS = "bypassStatus"
    CALL_STATUS = "callStatus"
    CAMERA = "camera"
    CAPTURE_TIME = "captureTime"
    CARBON_DIOXIDE = "carbonDioxide"
    CARBON_DIOXIDE_HEALTH_CONCERN = "carbonDioxideHealthConcern"
    CARBON_MONOXIDE = "carbonMonoxide"
    CARBON_MONOXIDE_HEALTH_CONCERN = "carbonMonoxideHealthConcern"
    CARBON_MONOXIDE_LEVEL = "carbonMonoxideLevel"
    CAST_CONTROL = "castControl"
    CATEGORY = "category"
    CELL_SIZE = "cellSize"
    CHANNEL = "channel"
    CHARGE_POINT_STATE = "chargePointState"
    CHARGING_STATE = "chargingState"
    CHARGING_STATUS = "chargingStatus"
    CHECK_INTERVAL = "checkInterval"
    CHIME = "chime"
    CIRCADIAN = "circadian"
    CLEANED_EXTENT = "cleanedExtent"
    CLEANING_MODE = "cleaningMode"
    CLEANING_STEP = "cleaningStep"
    CLEANING_TYPE = "cleaningType"
    CLIP = "clip"
    CLOSEDURATION = "closeduration"
    CLOUDCOVER = "cloudcover"
    CLUSTER_ID = "clusterId"
    CLUSTER_ID_DEC = "clusterIdDec"
    CLUSTER_NAME = "clusterName"
    CMD_SELECT = "cmdSelect"
    CODE_CHANGED = "codeChanged"
    CODE_LENGTH = "codeLength"
    CODE_REPORT = "codeReport"
    COFFEE_BREWING_RECIPES = "coffeeBrewingRecipes"
    COFFEE_BREWING_STATUS = "coffeeBrewingStatus"
    COLOR = "color"
    COLOR_CHANGE_MODE = "colorChangeMode"
    COLOR_CHANGE_TIMER = "colorChangeTimer"
    COLOR_CHANGING = "colorChanging"
    COLOR_MODE = "colorMode"
    COLOR_TEMP_STEPS = "colorTempSteps"
    COLOR_TEMPERATURE = "colorTemperature"
    COLOR_TEMPERATURE_RANGE = "colorTemperatureRange"
    COLOR_VALUE = "colorValue"
    COMMAND_CLASS = "commandClass"
    COMMAND_RESULT = "commandResult"
    COMPLETION_TIME = "completionTime"
    CONDITION = "condition"
    CONNECTED_DEVICE_COUNT = "connectedDeviceCount"
    CONNECTED_DEVICE_ID = "connectedDeviceId"
    CONNECTED_ROUTER_COUNT = "connectedRouterCount"
    CONNECTED_USER_ID = "connectedUserId"
    CONNECTION = "connection"
    CONNECTION_INFO = "connectionInfo"
    CONNECTION_STATE = "connectionState"
    CONSUMABLE_STATUS = "consumableStatus"
    CONTACT = "contact"
    CONTAINER_STATE = "containerState"
    CONTENT = "content"
    CONTENTS = "contents"
    CONTROL_MODE = "controlMode"
    COOK_RECIPE = "cookRecipe"
    COOK_TIME = "cookTime"
    COOK_TIME_RANGE = "cookTimeRange"
    COOKER_MODE = "cookerMode"
    COOKER_STATE = "cookerState"
    COOKTOP_BURNER_MODE = "cooktopBurnerMode"
    COOKTOP_COOK_RECIPE = "cooktopCookRecipe"
    COOKTOP_OPERATING_STATE = "cooktopOperatingState"
    COOLING_SETPOINT = "coolingSetpoint"
    COOLING_SETPOINT_RANGE = "coolingSetpointRange"
    COORDINATES = "coordinates"
    COUNT = "count"
    COURSE = "course"
    CREATE_DEVICE = "createDevice"
    CREATE_QTY = "createQty"
    CREDENTIALS = "credentials"
    CURATION_SUPPORT = "curationSupport"
    CURRENT = "current"
    CURRENT_ACTIVITY = "currentActivity"
    CURRENT_APP = "currentApp"
    CURRENT_CONTROL_MODE = "currentControlMode"
    CURRENT_LOOP = "currentLoop"
    CURRENT_OPERATION_MODE = "currentOperationMode"
    CURRENT_STATUS = "currentStatus"
    CURRENT_TIME_PERIOD = "currentTimePeriod"
    CURRENT_TRACK = "currentTrack"
    CURRENT_TWILIGHT = "currentTwilight"
    CURRENT_VALUE = "currentValue"
    CURRENT_VERSION = "currentVersion"
    CUSTOM_COURSE_CANDIDATES = "customCourseCandidates"
    CYCLE_TYPE = "cycleType"
    DASH_BOARD_VALUE = "dashBoardValue"
    DATA = "data"
    DATE_STARTED = "dateStarted"
    DAY_LENGTH = "dayLength"
    DAY_OF_WEEK = "dayOfWeek"
    DEFAULT_LEVEL = "defaultLevel"
    DEFAULT_OPERATION_TIME = "defaultOperationTime"
    DEFAULT_OVEN_MODE = "defaultOvenMode"
    DEFAULT_OVEN_SETPOINT = "defaultOvenSetpoint"
    DEFINED_RECIPE = "definedRecipe"
    DEFROST = "defrost"
    DEHUMIDIFIER_MODE = "dehumidifierMode"
    DENSITY = "density"
    DEODOR_FILTER_CAPACITY = "deodorFilterCapacity"
    DEODOR_FILTER_LAST_RESET_DATE = "deodorFilterLastResetDate"
    DEODOR_FILTER_RESET_TYPE = "deodorFilterResetType"
    DEODOR_FILTER_STATUS = "deodorFilterStatus"
    DEODOR_FILTER_USAGE = "deodorFilterUsage"
    DEODOR_FILTER_USAGE_STEP = "deodorFilterUsageStep"
    DEPENDENCY_STATUS = "dependencyStatus"
    DESCRIPTION = "description"
    DESIRED_HUMIDITY_LEVEL = "desiredHumidityLevel"
    DESIRED_HUMIDITY_LEVEL_RANGE = "desiredHumidityLevelRange"
    DESIRED_TEMPERATURE = "desiredTemperature"
    DETAIL_NAME = "detailName"
    DETECTED = "detected"
    DETECTION_INTERVAL = "detectionInterval"
    DETECTION_PROXIMITY = "detectionProximity"
    DETERGENT_TYPE = "detergentType"
    DEVICE_ASSOCIATION_TYPE = "deviceAssociationType"
    DEVICE_CONNECTION_STATE = "deviceConnectionState"
    DEVICE_ICE = "deviceIce"
    DEVICE_ID = "deviceId"
    DEVICE_INFO = "deviceInfo"
    DEVICE_NETWORK_ID = "deviceNetworkId"
    DEVICE_TYPE = "deviceType"
    DEVICE_WATCH_DEVICE_STATUS = "DeviceWatch-DeviceStatus"
    DEVICE_WATCH_ENROLL = "DeviceWatch-Enroll"
    DEWPOINT = "dewpoint"
    OCF_DEVICE_ID = "di"
    DIRECTION = "direction"
    DISABLED_CAPABILITIES = "disabledCapabilities"
    DISABLED_COMPONENTS = "disabledComponents"
    DISABLED_REASON = "disabledReason"
    DISCONNECTED_ROUTER_COUNT = "disconnectedRouterCount"
    DISHWASHER_DELAY_START_TIME = "dishwasherDelayStartTime"
    DISHWASHER_JOB_STATE = "dishwasherJobState"
    DISHWASHER_MODE = "dishwasherMode"
    DISHWASHER_OPERATING_PERCENTAGE = "dishwasherOperatingPercentage"
    DISHWASHER_OPERATING_PROGRESS = "dishwasherOperatingProgress"
    DISPLAY = "display"
    DISTANCE = "distance"
    DATA_MODEL_VERSION = "dmv"
    DO_NOT_DISTURB = "doNotDisturb"
    DOOR = "door"
    DOOR_STATE = "doorState"
    DOSAGE = "dosage"
    DOUBLE = "double"
    DOWNLINK_SPEED = "downlinkSpeed"
    DR_MAX_DURATION = "drMaxDuration"
    DRAIN_FILTER_LAST_RESET_DATE = "drainFilterLastResetDate"
    DRAIN_FILTER_RESET_TYPE = "drainFilterResetType"
    DRAIN_FILTER_STATUS = "drainFilterStatus"
    DRAIN_FILTER_USAGE = "drainFilterUsage"
    DRAIN_FILTER_USAGE_STEP = "drainFilterUsageStep"
    DRAINAGE_REQUIREMENT = "drainageRequirement"
    DRCAPABLE = "drcapable"
    DRIVER_STATE = "driverState"
    DRIVER_VERSION = "driverVersion"
    DRIVING_MODE = "drivingMode"
    DRIVING_STATUS = "drivingStatus"
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
    DURATION = "duration"
    DURATION_ALARM = "durationAlarm"
    DUST_FILTER_CAPACITY = "dustFilterCapacity"
    DUST_FILTER_LAST_RESET_DATE = "dustFilterLastResetDate"
    DUST_FILTER_RESET_TYPE = "dustFilterResetType"
    DUST_FILTER_STATUS = "dustFilterStatus"
    DUST_FILTER_USAGE = "dustFilterUsage"
    DUST_FILTER_USAGE_STEP = "dustFilterUsageStep"
    DUST_HEALTH_CONCERN = "dustHealthConcern"
    DUST_LEVEL = "dustLevel"
    EFFECT_MODE = "effectMode"
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
    ENCRYPTED_KEK = "encryptedKek"
    ENCRYPTION = "encryption"
    END_TIME = "endTime"
    ENDPOINT = "endpoint"
    ENERGY = "energy"
    ENERGY_DELIVERED = "energyDelivered"
    ENERGY_RESET = "energyReset"
    ENERGY_SAVING_INFO = "energySavingInfo"
    ENERGY_SAVING_LEVEL = "energySavingLevel"
    ENERGY_SAVING_OPERATION = "energySavingOperation"
    ENERGY_SAVING_OPERATION_SUPPORT = "energySavingOperationSupport"
    ENERGY_SAVING_SUPPORT = "energySavingSupport"
    ENERGY_TYPE = "energyType"
    ENERGY_USAGE_DAY = "energyUsageDay"
    ENERGY_USAGE_MAX = "energyUsageMax"
    ENERGY_USAGE_MONTH = "energyUsageMonth"
    ENERGY_USAGE_STATE = "energyUsageState"
    ENGINE_STATE = "engineState"
    ENROLLMENT_STATUS = "enrollmentStatus"
    ENROLLMENT_STATUS_CODE = "enrollmentStatusCode"
    EP_EVENT = "epEvent"
    EP_INFO = "epInfo"
    EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT = "equivalentCarbonDioxideMeasurement"
    ERROR = "error"
    ERROR_CODE = "errorCode"
    ERRORS = "errors"
    ERRORSTATUS = "errorstatus"
    ESTIMATED_REMAINING_RANGE = "estimatedRemainingRange"
    ESTIMATED_TIME_REMAINING = "estimatedTimeRemaining"
    ETA = "eta"
    EUI = "eui"
    EVEN_ODD_DAY = "evenOddDay"
    EVENT = "event"
    EVENTS = "events"
    EXCLUDE_HOLIDAYS = "excludeHolidays"
    EXECUTABLE_SERVICE_LIST = "executableServiceList"
    FACE_RECOGNIZED_EVENT = "faceRecognizedEvent"
    FADE = "fade"
    FAN_CYCLIC_MODE = "fanCyclicMode"
    FAN_MODE = "fanMode"
    FAN_NEXT_CHANGE = "fanNextChange"
    FAN_OSCILLATION_MODE = "fanOscillationMode"
    FAN_SPEED = "fanSpeed"
    FAULT_STATE = "faultState"
    FEED_PORTION = "feedPortion"
    FEEDER_OPERATING_STATE = "feederOperatingState"
    FILTER_CHANGE_NEEDED = "filterChangeNeeded"
    FILTER_LIFE_REMAINING = "filterLifeRemaining"
    FILTER_STATUS = "filterStatus"
    FINE_DUST_HEALTH_CONCERN = "fineDustHealthConcern"
    FINE_DUST_LEVEL = "fineDustLevel"
    FIRMWARE_VERSION = "firmwareVersion"
    FLEX_ZONES = "flexZones"
    FLOW = "flow"
    FLOW_RANGE = "flowRange"
    FOOD_TYPE = "foodType"
    FORCED_ENTRY_SENSITIVITY = "forcedEntrySensitivity"
    FORCED_ON_LEVEL = "forcedOnLevel"
    FORMALDEHYDE_HEALTH_CONCERN = "formaldehydeHealthConcern"
    FORMALDEHYDE_LEVEL = "formaldehydeLevel"
    FREEZER_CONVERT_MODE = "freezerConvertMode"
    FRIDGE_MODE = "fridgeMode"
    FRIDGE_MODE_VALUE = "fridgeModeValue"
    FSV_SETTINGS = "fsvSettings"
    FUEL = "fuel"
    FUEL_LEVEL = "fuelLevel"
    GAS = "gas"
    GAS_CONSUMPTION = "gasConsumption"
    GAS_CONSUMPTIONS = "gasConsumptions"
    GAS_METER = "gasMeter"
    GAS_METER_CALORIFIC = "gasMeterCalorific"
    GAS_METER_CONVERSION = "gasMeterConversion"
    GAS_METER_PRECISION = "gasMeterPrecision"
    GAS_METER_TIME = "gasMeterTime"
    GAS_METER_VOLUME = "gasMeterVolume"
    GENERATION = "generation"
    GEOFENCE = "geofence"
    GEOFENCES = "geofences"
    GET_GROUPS = "getGroups"
    GOAL = "goal"
    GRID = "grid"
    GRID_STATUS_STATUS = "gridStatusStatus"
    GRID_STATUS_SUPPORT = "gridStatusSupport"
    GROUP_COMMAND_OPTION = "groupCommandOption"
    GROUP_ID = "groupId"
    GROUP_MUTE = "groupMute"
    GROUP_NAME = "groupName"
    GROUP_NUMBER = "groupNumber"
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
    HELD = "held"
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
    HOOD_FILTER_CAPACITY = "hoodFilterCapacity"
    HOOD_FILTER_LAST_RESET_DATE = "hoodFilterLastResetDate"
    HOOD_FILTER_RESET_TYPE = "hoodFilterResetType"
    HOOD_FILTER_STATUS = "hoodFilterStatus"
    HOOD_FILTER_USAGE = "hoodFilterUsage"
    HOOD_FILTER_USAGE_STEP = "hoodFilterUsageStep"
    HOT_AIR_DRY = "hotAirDry"
    HOT_TEMPERATURE = "hotTemperature"
    HOURLY_GAS_CONSUMPTIONS = "hourlyGasConsumptions"
    HOURLY_USAGE_VIEW_AVAILABLE = "hourlyUsageViewAvailable"
    HTTPCODE = "httpcode"
    HUB_DEVICE_ID = "hubDeviceId"
    HUB_EUI = "hubEui"
    HUB_ONBOARDING_STATUS = "hubOnboardingStatus"
    HUE = "hue"
    HUE_STEPS = "hueSteps"
    HUMIDIFIER_MODE = "humidifierMode"
    HUMIDITY = "humidity"
    HUMIDITY_ALARM = "humidityAlarm"
    HUMIDITY_CONDITION = "humidityCondition"
    HUMIDITY_TARGET = "humidityTarget"
    SPEC_VERSION = "icv"
    ILLUMINANCE = "illuminance"
    ILLUMVALUE = "illumvalue"
    IMAGE = "image"
    IMAGE_SUPPORT = "imageSupport"
    IMAGE_TRANSFER_PROGRESS = "imageTransferProgress"
    IME_ADV_SUPPORTED = "imeAdvSupported"
    INDICATOR_STATUS = "indicatorStatus"
    INDOOR = "indoor"
    INFO = "info"
    INFO_HTML = "infoHtml"
    INFO_PANEL = "infoPanel"
    INFO_TEXT = "infoText"
    INFRARED_LEVEL = "infraredLevel"
    INITIAL_AMOUNT = "initialAmount"
    INPUT_SOURCE = "inputSource"
    INTENSITY_FOOT = "intensityFoot"
    INTENSITY_HEAD = "intensityHead"
    INTENSITY_RANGE = "intensityRange"
    INTENSITY_WHOLE = "intensityWhole"
    INTERIOR_BUTTON = "interiorButton"
    INTERVAL = "interval"
    INVALID_CODE = "invalidCode"
    INVENTORY = "inventory"
    INVISIBLE_FEATURES = "invisibleFeatures"
    IS_MAP_BASED_OPERATION_AVAILABLE = "isMapBasedOperationAvailable"
    JOB_BEGINNING_STATUS = "jobBeginningStatus"
    KEYNUMVALUE = "keynumvalue"
    KEYPAD = "keypad"
    KEYPAD_BEEP = "keypadBeep"
    KEYVALUE = "keyvalue"
    LANGUAGE = "language"
    LAST_EMPTIED_TIME = "lastEmptiedTime"
    LAST_FINISHED_TIME = "lastFinishedTime"
    LAST_HOUR = "lastHour"
    LAST_ONBOARDING_ERROR_CODE = "lastOnboardingErrorCode"
    LAST_ONBOARDING_RESULT = "lastOnboardingResult"
    LAST_SENSING_LEVEL = "lastSensingLevel"
    LAST_SENSING_TIME = "lastSensingTime"
    LAST_SEVEN_DAYS = "lastSevenDays"
    LAST_STERILIZED_TIME = "lastSterilizedTime"
    LAST_TWENTY_FOUR_HOURS = "lastTwentyFourHours"
    LAST_UPDATE_STATUS = "lastUpdateStatus"
    LAST_UPDATE_STATUS_REASON = "lastUpdateStatusReason"
    LAST_UPDATE_TIME = "lastUpdateTime"
    LAST_UPDATED_DATE = "lastUpdatedDate"
    LAST_UPDATED_TIME = "lastUpdatedTime"
    LATEST_REQUEST_ID = "latestRequestId"
    LATITUDE = "latitude"
    LED_BAR_OFF_COLOR = "ledBarOffColor"
    LED_BAR_OFF_LEVEL = "ledBarOffLevel"
    LED_BAR_ON_COLOR = "ledBarOnColor"
    LED_BAR_ON_LEVEL = "ledBarOnLevel"
    LED_BRIGHTNESS = "ledBrightness"
    LED_COLOR = "ledColor"
    LED_MODE = "ledMode"
    LED_NOTIFICATION = "ledNotification"
    LEVEL = "level"
    LEVEL_LOCAL = "levelLocal"
    LEVEL_RANGE = "levelRange"
    LEVEL_STEPS = "levelSteps"
    LIFESPAN = "lifespan"
    LIGHT_CONTROLLER_MODE = "lightControllerMode"
    LIGHT_SENSING = "lightSensing"
    LIGHTING = "lighting"
    LIGHTING_MODE = "lightingMode"
    LOCAL_CONTROL = "localControl"
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
    LOCATION = "location"
    LOCK = "lock"
    LOCK_AND_LEAVE = "lockAndLeave"
    LOCK_CODES = "lockCodes"
    LOCK_STATE = "lockState"
    LOCK_STATUS = "lockStatus"
    LOCK_TYPE = "lockType"
    LOG = "log"
    LOG_INFO = "logInfo"
    LOG_REQUEST_STATE = "logRequestState"
    LOG_STATE = "logState"
    LOG_TYPE = "logType"
    LONGITUDE = "longitude"
    LOOPS_NUMBER = "loopsNumber"
    LQI = "lqi"
    MACHINE_STATE = "machineState"
    MANUAL_LEVEL = "manualLevel"
    MANUAL_LEVEL_MAX = "manualLevelMax"
    MANUAL_LEVEL_MIN = "manualLevelMin"
    MAP_ID = "mapId"
    MAPS = "maps"
    MASSAGE_STATE = "massageState"
    MASTER_DI = "masterDi"
    MASTER_NAME = "masterName"
    MAX_CODE_LENGTH = "maxCodeLength"
    MAX_CODES = "maxCodes"
    MAX_CURRENT = "maxCurrent"
    MAX_NUMBER_OF_PRESETS = "maxNumberOfPresets"
    MAX_NUMBER_OF_RECIPES = "maxNumberOfRecipes"
    MAX_NUMBER_OF_RESERVATIONS = "maxNumberOfReservations"
    MAX_OPERATION_TIME = "maxOperationTime"
    MAX_PIN_CODE_LEN = "maxPinCodeLen"
    MAX_SUPPORTED_AMOUNT = "maxSupportedAmount"
    MAXIMUM_SETPOINT = "maximumSetpoint"
    MAXTEMP = "maxtemp"
    MCU_DEVICE_FW_VER = "mcuDeviceFwVer"
    MEASURE_INTERVAL = "measureInterval"
    MEDIA_OUTPUT_SUPPORTED = "mediaOutputSupported"
    MEDIA_STATUS = "mediaStatus"
    MENU = "menu"
    MESSAGE = "message"
    MESSAGE_BUTTON = "messageButton"
    METERING_DATE = "meteringDate"
    METHOD = "method"
    MICOM_ASSAY_CODE = "micomAssayCode"
    MIN_CODE_LENGTH = "minCodeLength"
    MIN_CURRENT = "minCurrent"
    MIN_PIN_CODE_LEN = "minPinCodeLen"
    MIN_SUPPORTED_AMOUNT = "minSupportedAmount"
    MIN_VERSION = "minVersion"
    MINIMUM_RESERVABLE_TIME = "minimumReservableTime"
    MINIMUM_SETPOINT = "minimumSetpoint"
    MINTEMP = "mintemp"
    MIRROR_GROUP_FUNCTION = "mirrorGroupFunction"
    MIRROR_IN = "mirrorIn"
    MIRROR_OUT = "mirrorOut"
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
    MONITORING_MODE = "monitoringMode"
    MONITORING_STATUS = "monitoringStatus"
    MONTHLY_USAGE = "monthlyUsage"
    MOTION = "motion"
    MOTION_SENSITIVITY = "motionSensitivity"
    MOTION_SENSOR_ENABLE = "motionSensorEnable"
    MOTOR_FILTER_RESET_TYPE = "motorFilterResetType"
    MOTOR_FILTER_STATUS = "motorFilterStatus"
    MOVEMENT = "movement"
    MOVIE_MODE = "movieMode"
    MUTE = "mute"
    DEVICE_NAME = "n"
    NAME = "name"
    NAME_TEXT = "nameText"
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
    NODE_END_POINT = "nodeEndPoint"
    NODE_TO_WRITE = "nodeToWrite"
    NONCE = "nonce"
    NORMAL_LED_COLOR = "normalLedColor"
    NOTIFICATION_COLOR = "notificationColor"
    NOTIFICATION_DURATION = "notificationDuration"
    NOTIFICATION_EFFECT = "notificationEffect"
    NOTIFICATION_LEVEL = "notificationLevel"
    NOTIFICATION_NUMBER = "notificationNumber"
    NOTIFICATION_TEMPLATE_I_D = "notificationTemplateID"
    NUMBER_OF_BUTTONS = "numberOfButtons"
    NUMBER_OF_CONNECTED_DEVICES = "numberOfConnectedDevices"
    NUMBER_OF_SUB_DEVICES = "numberOfSubDevices"
    OBSOLETED = "obsoleted"
    OCCUPANCY = "occupancy"
    OCF_RESOURCE_UPDATED_TIME = "ocfResourceUpdatedTime"
    OCF_RESOURCE_VERSION = "ocfResourceVersion"
    ODOMETER_READING = "odometerReading"
    ODOR_LEVEL = "odorLevel"
    ONBOARDING = "onboarding"
    ONBOARDING_PROGRESS = "onboardingProgress"
    ONETOUCHLOCK = "onetouchlock"
    OPENDURATION = "openduration"
    OPERATING_STATE = "operatingState"
    OPERATION_MODE = "operationMode"
    OPERATION_STATE = "operationState"
    OPERATION_TIME = "operationTime"
    OPERATIONAL_STATE = "operationalState"
    ORDER_THRESHOLD = "orderThreshold"
    ORIGINATOR = "originator"
    ORIGINS = "origins"
    OTN_D_U_I_D = "otnDUID"
    OUT_OF_SYNC_CHANGES = "outOfSyncChanges"
    OUTDOOR = "outdoor"
    OUTDOOR_UNIT_DEFROSTING = "outdoorUnitDefrosting"
    OUTING_MODE = "outingMode"
    OVEN_CAVITY_STATUS = "ovenCavityStatus"
    OVEN_JOB_STATE = "ovenJobState"
    OVEN_MODE = "ovenMode"
    OVEN_SETPOINT = "ovenSetpoint"
    OVEN_SETPOINT_RANGE = "ovenSetpointRange"
    OVERHEAT_FOR_RECIPES = "overheatForRecipes"
    OZONE = "ozone"
    OZONE_HEALTH_CONCERN = "ozoneHealthConcern"
    PH = "pH"
    PANIC_ALARM = "panicAlarm"
    PARAMETER_END = "parameterEnd"
    PARAMETER_START = "parameterStart"
    PATH = "path"
    PATROL_STATUS = "patrolStatus"
    PAYLOAD = "payload"
    PERCENT = "percent"
    PERIODIC_SENSING = "periodicSensing"
    PERIODIC_SENSING_INTERVAL = "periodicSensingInterval"
    PERIODIC_SENSING_STATUS = "periodicSensingStatus"
    PERSON_DETECTION = "personDetection"
    PEST_CONTROL = "pestControl"
    PET_ACTIVITY = "petActivity"
    PHRASE_SPOKEN = "phraseSpoken"
    PLATFORM_ID = "pi"
    PICTURE = "picture"
    PICTURE_MODE = "pictureMode"
    PIN_USERS_SUPPORTED = "pinUsersSupported"
    PLAN = "plan"
    PLAYBACK_REPEAT_MODE = "playbackRepeatMode"
    PLAYBACK_SHUFFLE = "playbackShuffle"
    PLAYBACK_STATUS = "playbackStatus"
    PLAYLIST = "playlist"
    PMODE = "pmode"
    POSITION = "position"
    POWER = "power"
    POWER_CONSUMPTION = "powerConsumption"
    POWER_CONSUMPTIONS = "powerConsumptions"
    POWER_CURRENT = "powerCurrent"
    POWER_LEVEL = "powerLevel"
    POWER_SOURCE = "powerSource"
    POWER_STATE = "powerState"
    POWERFACTOR = "powerfactor"
    PRECIP = "precip"
    PRECIPITATION_INTENSITY = "precipitationIntensity"
    PRECIPITATION_LEVEL = "precipitationLevel"
    PRECIPITATION_RATE = "precipitationRate"
    PREDEFINED_COURSES = "predefinedCourses"
    PRESENCE = "presence"
    PRESENCE_STATUS = "presenceStatus"
    PRESETS = "presets"
    PRESSURE = "pressure"
    PRESSURE_ALARM = "pressureAlarm"
    PROBABILITY = "probability"
    PROG_OFF = "progOff"
    PROG_ON = "progOn"
    PROGRAM = "program"
    PROGRESS = "progress"
    PROGRESS_PERCENTAGE = "progressPercentage"
    PROTOCOL_TYPE = "protocolType"
    PROTOCOL_VERSION = "protocolVersion"
    PROTOCOLS = "protocols"
    PUSHED = "pushed"
    QUANTITY = "quantity"
    RADON_HEALTH_CONCERN = "radonHealthConcern"
    RADON_LEVEL = "radonLevel"
    RAIN = "rain"
    RANDOM_MAXIMUM_TIMER = "randomMaximumTimer"
    RANDOM_MINIMUM_TIMER = "randomMinimumTimer"
    RANDOM_NEXT = "randomNext"
    RANDOM_ON_OFF = "randomOnOff"
    RAPID_COOLING = "rapidCooling"
    RAPID_FREEZING = "rapidFreezing"
    RATE_ALARM = "rateAlarm"
    RATE_TYPE = "rateType"
    REACTIVE = "reactive"
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
    RELATIVE_HUMIDITY_LEVEL = "relativeHumidityLevel"
    RELEASE_YEAR = "releaseYear"
    REMAINING_AMOUNT = "remainingAmount"
    REMAINING_TIME = "remainingTime"
    REMAINING_TIME_STR = "remainingTimeStr"
    REMOTE_CONTROL = "remoteControl"
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
    REQUEST_INVITATION = "requestInvitation"
    RESERVABLE = "reservable"
    RESERVATIONS = "reservations"
    RESOLUTION = "resolution"
    RESPONSE = "response"
    RESULT = "result"
    RING_MOBILE = "ringMobile"
    RINSE_MODE = "rinseMode"
    RINSE_PLUS = "rinsePlus"
    ROBOT_CLEANER_CLEANING_MODE = "robotCleanerCleaningMode"
    ROBOT_CLEANER_CLEANING_STATE = "robotCleanerCleaningState"
    ROBOT_CLEANER_CONTROL_STATE = "robotCleanerControlState"
    ROBOT_CLEANER_MOVEMENT = "robotCleanerMovement"
    ROBOT_CLEANER_TURBO_MODE = "robotCleanerTurboMode"
    ROBOT_CLEANER_TURBO_STATE = "robotCleanerTurboState"
    ROBOT_STATE = "robotState"
    ROLE = "role"
    RSSI = "rssi"
    SANITIZE = "sanitize"
    SANITIZING_WASH = "sanitizingWash"
    SATURATION = "saturation"
    SCAN_CODES = "scanCodes"
    SCAN_RESULTS = "scanResults"
    SCENE = "scene"
    SCENT_INTENSITY = "scentIntensity"
    SCENT_NAME = "scentName"
    SCHEDULABLE_MENUS = "schedulableMenus"
    SCHEDULE = "schedule"
    SCHEDULED_JOBS = "scheduledJobs"
    SCHEDULED_PHASES = "scheduledPhases"
    SCHEDULED_TIME = "scheduledTime"
    SCHEDULING_ENABLED = "schedulingEnabled"
    SDP_ANSWER = "sdpAnswer"
    SEARCHING_STATUS = "searchingStatus"
    SECURITY_SYSTEM_STATUS = "securitySystemStatus"
    SELECTED_APP_ID = "selectedAppId"
    SELECTED_AREAS = "selectedAreas"
    SELECTED_MODE = "selectedMode"
    SELECTED_ZONE = "selectedZone"
    SELECTION = "selection"
    SENSING_ON_SUSPEND_MODE = "sensingOnSuspendMode"
    SENSITIVE = "sensitive"
    SENSITIVITY_MODE = "sensitivityMode"
    SENSOR_STATUS = "sensorStatus"
    SERIAL_NUMBER = "serialNumber"
    SERIAL_NUMBER_EXTRA = "serialNumberExtra"
    SERVER = "server"
    SERVICE_MESSAGE = "serviceMessage"
    SESSION_STATUS = "sessionStatus"
    SESSION_TIME = "sessionTime"
    SETTABLE = "settable"
    SETTABLE_MAX_FAN_SPEED = "settableMaxFanSpeed"
    SETTABLE_MIN_FAN_SPEED = "settableMinFanSpeed"
    SETTINGS = "settings"
    SETUP_ID = "setupId"
    SHADE_LEVEL = "shadeLevel"
    SHADE_TILT_LEVEL = "shadeTiltLevel"
    SHOCK = "shock"
    SIGN_IN_STATUS = "signInStatus"
    SIGNAL_METRICS = "signalMetrics"
    SIGNIN_PERMISSION = "signinPermission"
    SIREN_OR_BELL_ACTIVE = "sirenOrBellActive"
    SIREN_SOUNDS = "sirenSounds"
    SLEEPING = "sleeping"
    SLOT_STATE = "slotState"
    SMOKE = "smoke"
    SNOOZE = "snooze"
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
    STAGE = "stage"
    STAGE_STATUS = "stageStatus"
    STANDBY_MODE = "standbyMode"
    START_DATE = "startDate"
    START_TIME = "startTime"
    START_VALUE = "startValue"
    STARTSTOP = "startstop"
    STATE = "state"
    STATELESS_MODE = "statelessMode"
    STATUS = "status"
    STATUS_LED_BLINKING_FREQ = "statusLedBlinkingFreq"
    STATUS_LED_COLOR = "statusLedColor"
    STATUS_LED_FIVE_COLOR = "statusLedFiveColor"
    STATUS_LED_FOUR_COLOR = "statusLedFourColor"
    STATUS_LED_ONE_COLOR = "statusLedOneColor"
    STATUS_LED_SEVEN_COLOR = "statusLedSevenColor"
    STATUS_LED_SIX_COLOR = "statusLedSixColor"
    STATUS_LED_THREE_COLOR = "statusLedThreeColor"
    STATUS_LED_TWO_COLOR = "statusLedTwoColor"
    STATUS_MESSAGE = "statusMessage"
    STEAM_CLOSET_AUTO_CYCLE_LINK = "steamClosetAutoCycleLink"
    STEAM_CLOSET_CYCLE = "steamClosetCycle"
    STEAM_CLOSET_DELAY_END_TIME = "steamClosetDelayEndTime"
    STEAM_CLOSET_JOB_STATE = "steamClosetJobState"
    STEAM_CLOSET_MACHINE_STATE = "steamClosetMachineState"
    STEAM_CLOSET_WRINKLE_PREVENT = "steamClosetWrinklePrevent"
    STEAM_SOAK = "steamSoak"
    STEPS = "steps"
    STEREO_TYPE = "stereoType"
    STOPPED_STATUS = "stoppedStatus"
    STORM_WASH = "stormWash"
    STORM_WATCH_ACTIVE = "stormWatchActive"
    STORM_WATCH_ENABLED = "stormWatchEnabled"
    STORM_WATCH_SUPPORT = "stormWatchSupport"
    STREAM = "stream"
    STREAM_CONTROL = "streamControl"
    STUN_URL = "stunUrl"
    SUB_DEVICE_ACTIVE = "subDeviceActive"
    SUB_DEVICES = "subDevices"
    SUBTITLE = "subtitle"
    SUGGESTION_THRESHOLD = "suggestionThreshold"
    SUMMARY = "summary"
    SUN_AZIMUTH_ANGLE = "sunAzimuthAngle"
    SUN_ELEVATION_ANGLE = "sunElevationAngle"
    SUN_RISE = "sunRise"
    SUN_RISE_OFFSET = "sunRiseOffset"
    SUN_SET = "sunSet"
    SUN_SET_OFFSET = "sunSetOffset"
    SUPPLY_STATE = "supplyState"
    SUPPORT_CUSTOM_CONTENT = "supportCustomContent"
    SUPPORT_REPEAT_MODE = "supportRepeatMode"
    SUPPORT_TOU_EVENT_NOTIFICATION = "supportTouEventNotification"
    SUPPORT_TOU_INFO = "supportTouInfo"
    SUPPORTED_AC_FAN_MODES = "supportedAcFanModes"
    SUPPORTED_AC_MODES = "supportedAcModes"
    SUPPORTED_AC_OPTIONAL_MODE = "supportedAcOptionalMode"
    SUPPORTED_ACTION_SETTINGS = "supportedActionSettings"
    SUPPORTED_ACTIONS = "supportedActions"
    SUPPORTED_AGING_METHODS = "supportedAgingMethods"
    SUPPORTED_AIR_PURIFIER_FAN_MODES = "supportedAirPurifierFanModes"
    SUPPORTED_AIR_QUALITY_HEALTH_CONCERNS = "supportedAirQualityHealthConcerns"
    SUPPORTED_AIR_QUALITY_VALUES = "supportedAirQualityValues"
    SUPPORTED_ALARM_SENSOR_STATES = "supportedAlarmSensorStates"
    SUPPORTED_ALARM_STATUSES = "supportedAlarmStatuses"
    SUPPORTED_ALARM_THRESHOLDS = "supportedAlarmThresholds"
    SUPPORTED_ALARM_VALUES = "supportedAlarmValues"
    SUPPORTED_AMBIENT_APPS = "supportedAmbientApps"
    SUPPORTED_AMOUNT = "supportedAmount"
    SUPPORTED_AP_OPERATION_MODE = "supportedApOperationMode"
    SUPPORTED_AREAS = "supportedAreas"
    SUPPORTED_ARGUMENTS = "supportedArguments"
    SUPPORTED_AUTH_TYPE = "supportedAuthType"
    SUPPORTED_AUTO_CLEANING_MODES = "supportedAutoCleaningModes"
    SUPPORTED_AUTOMATIC_EXECUTION_MODE = "supportedAutomaticExecutionMode"
    SUPPORTED_AUTOMATIC_EXECUTION_SETTING = "supportedAutomaticExecutionSetting"
    SUPPORTED_BRIGHTNESS_LEVEL = "supportedBrightnessLevel"
    SUPPORTED_BUTTON_VALUES = "supportedButtonValues"
    SUPPORTED_CARBON_DIOXIDE_VALUES = "supportedCarbonDioxideValues"
    SUPPORTED_CARBON_MONOXIDE_VALUES = "supportedCarbonMonoxideValues"
    SUPPORTED_CATEGORIES = "supportedCategories"
    SUPPORTED_CHARGE_POINT_STATES = "supportedChargePointStates"
    SUPPORTED_CHARGING_COMMANDS = "supportedChargingCommands"
    SUPPORTED_CHARGING_STATES = "supportedChargingStates"
    SUPPORTED_CLEANING_MODE = "supportedCleaningMode"
    SUPPORTED_CLEANING_TYPES = "supportedCleaningTypes"
    SUPPORTED_COMMANDS = "supportedCommands"
    SUPPORTED_CONDITIONS = "supportedConditions"
    SUPPORTED_CONTAINER_STATES = "supportedContainerStates"
    SUPPORTED_CONTEXTS = "supportedContexts"
    SUPPORTED_CONTROL_MODES = "supportedControlModes"
    SUPPORTED_COOKER_MODES = "supportedCookerModes"
    SUPPORTED_COOKTOP_OPERATING_STATE = "supportedCooktopOperatingState"
    SUPPORTED_COURSES = "supportedCourses"
    SUPPORTED_CREDENTIALS = "supportedCredentials"
    SUPPORTED_CYCLES = "supportedCycles"
    SUPPORTED_DEHUMIDIFIER_MODES = "supportedDehumidifierModes"
    SUPPORTED_DENSITY = "supportedDensity"
    SUPPORTED_DESIRED_TEMPERATURES = "supportedDesiredTemperatures"
    SUPPORTED_DETECTION_PROXIMITIES = "supportedDetectionProximities"
    SUPPORTED_DISHWASHER_MODES = "supportedDishwasherModes"
    SUPPORTED_DRIVING_MODES = "supportedDrivingModes"
    SUPPORTED_DRYER_DRY_LEVEL = "supportedDryerDryLevel"
    SUPPORTED_DRYING_TEMPERATURE = "supportedDryingTemperature"
    SUPPORTED_DRYING_TIME = "supportedDryingTime"
    SUPPORTED_DUST_VALUES = "supportedDustValues"
    SUPPORTED_ENERGY_SAVING_LEVELS = "supportedEnergySavingLevels"
    SUPPORTED_EVENTS = "supportedEvents"
    SUPPORTED_FAN_MODES = "supportedFanModes"
    SUPPORTED_FAN_OSCILLATION_MODES = "supportedFanOscillationModes"
    SUPPORTED_FEATURES = "supportedFeatures"
    SUPPORTED_FILTER_COMMANDS = "supportedFilterCommands"
    SUPPORTED_FINE_DUST_VALUES = "supportedFineDustValues"
    SUPPORTED_FOCUS_AREAS = "supportedFocusAreas"
    SUPPORTED_FORMALDEHYDE_VALUES = "supportedFormaldehydeValues"
    SUPPORTED_FREEZER_CONVERT_MODES = "supportedFreezerConvertModes"
    SUPPORTED_FRIDGE_MODES = "supportedFridgeModes"
    SUPPORTED_HEATING_MODES = "supportedHeatingModes"
    SUPPORTED_HOOD_FAN_SPEED = "supportedHoodFanSpeed"
    SUPPORTED_HOT_TEMPERATURES = "supportedHotTemperatures"
    SUPPORTED_INPUT_SOURCES = "supportedInputSources"
    SUPPORTED_INPUT_SOURCES_MAP = "supportedInputSourcesMap"
    SUPPORTED_KEY_CODES = "supportedKeyCodes"
    SUPPORTED_LANGUAGES = "supportedLanguages"
    SUPPORTED_LEVELS = "supportedLevels"
    SUPPORTED_LIGHT_CONTROLLER_MODES = "supportedLightControllerModes"
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
    SUPPORTED_MOLD_VALUES = "supportedMoldValues"
    SUPPORTED_MOTION_POSITIONS = "supportedMotionPositions"
    SUPPORTED_MOVEMENTS = "supportedMovements"
    SUPPORTED_NITROGEN_DIOXIDE_VALUES = "supportedNitrogenDioxideValues"
    SUPPORTED_OPERATING_STATE = "supportedOperatingState"
    SUPPORTED_OPERATING_STATE_COMMANDS = "supportedOperatingStateCommands"
    SUPPORTED_OPERATING_STATES = "supportedOperatingStates"
    SUPPORTED_OPERATION_MODES = "supportedOperationModes"
    SUPPORTED_OPERATIONAL_STATES = "supportedOperationalStates"
    SUPPORTED_OPTIONS = "supportedOptions"
    SUPPORTED_OVEN_MODES = "supportedOvenModes"
    SUPPORTED_OZONE_VALUES = "supportedOzoneValues"
    SUPPORTED_PET_ACTIVITIES = "supportedPetActivities"
    SUPPORTED_PICTURE_MODES = "supportedPictureModes"
    SUPPORTED_PICTURE_MODES_MAP = "supportedPictureModesMap"
    SUPPORTED_PLAYBACK_COMMANDS = "supportedPlaybackCommands"
    SUPPORTED_POSITIONS = "supportedPositions"
    SUPPORTED_POWER_LEVELS = "supportedPowerLevels"
    SUPPORTED_PUBLISHER_I_DS = "supportedPublisherIDs"
    SUPPORTED_RADON_VALUES = "supportedRadonValues"
    SUPPORTED_RINSE_MODES = "supportedRinseModes"
    SUPPORTED_ROBOT_CLEANER_STATES = "supportedRobotCleanerStates"
    SUPPORTED_ROBOT_COMMANDS = "supportedRobotCommands"
    SUPPORTED_ROBOT_STATES = "supportedRobotStates"
    SUPPORTED_SCENES = "supportedScenes"
    SUPPORTED_SECURITY_SYSTEM_COMMANDS = "supportedSecuritySystemCommands"
    SUPPORTED_SECURITY_SYSTEM_STATUSES = "supportedSecuritySystemStatuses"
    SUPPORTED_SET_TIMES = "supportedSetTimes"
    SUPPORTED_SOUND_MODES = "supportedSoundModes"
    SUPPORTED_SOUND_MODES_MAP = "supportedSoundModesMap"
    SUPPORTED_SOUND_TYPES = "supportedSoundTypes"
    SUPPORTED_SPIN_SPEEDS = "supportedSpinSpeeds"
    SUPPORTED_STATUS = "supportedStatus"
    SUPPORTED_STATUSES = "supportedStatuses"
    SUPPORTED_STEAM_CLOSET_JOB_STATE = "supportedSteamClosetJobState"
    SUPPORTED_STEAM_CLOSET_MACHINE_STATE = "supportedSteamClosetMachineState"
    SUPPORTED_TEMPERATURE_LEVELS = "supportedTemperatureLevels"
    SUPPORTED_THERMOSTAT_FAN_MODES = "supportedThermostatFanModes"
    SUPPORTED_THERMOSTAT_MODES = "supportedThermostatModes"
    SUPPORTED_THERMOSTAT_OPERATING_STATES = "supportedThermostatOperatingStates"
    SUPPORTED_TRACK_CONTROL_COMMANDS = "supportedTrackControlCommands"
    SUPPORTED_TVOC_VALUES = "supportedTvocValues"
    SUPPORTED_TYPES = "supportedTypes"
    SUPPORTED_UNLOCK_DIRECTIONS = "supportedUnlockDirections"
    SUPPORTED_VALUES = "supportedValues"
    SUPPORTED_VERY_FINE_DUST_VALUES = "supportedVeryFineDustValues"
    SUPPORTED_VOLUME_LEVELS = "supportedVolumeLevels"
    SUPPORTED_WASHER_RINSE_CYCLES = "supportedWasherRinseCycles"
    SUPPORTED_WASHER_SOIL_LEVEL = "supportedWasherSoilLevel"
    SUPPORTED_WASHER_SPIN_LEVEL = "supportedWasherSpinLevel"
    SUPPORTED_WASHER_WATER_TEMPERATURE = "supportedWasherWaterTemperature"
    SUPPORTED_WASHING_TIMES = "supportedWashingTimes"
    SUPPORTED_WATER_LEVEL = "supportedWaterLevel"
    SUPPORTED_WATER_SPRAY_LEVELS = "supportedWaterSprayLevels"
    SUPPORTED_WATER_VALVE = "supportedWaterValve"
    SUPPORTED_WI_FI_FREQ = "supportedWiFiFreq"
    SUPPORTED_WIND_MODES = "supportedWindModes"
    SUPPORTED_WINDOW_SHADE_COMMANDS = "supportedWindowShadeCommands"
    SUPPORTS_POWER_ON_BY_OCF = "supportsPowerOnByOcf"
    SUPPORTS_PROGRESS_REPORTS = "supportsProgressReports"
    SURFACE_RESIDUAL_HEAT = "surfaceResidualHeat"
    SWITCH = "switch"
    SWITCH_ALL_ON_OFF = "switchAllOnOff"
    SWITCH_STATE = "switchState"
    SYSTEM_PREHEATING = "systemPreheating"
    TAG_BUTTON = "tagButton"
    TAG_STATUS = "tagStatus"
    TALKBACK = "talkback"
    TAMPER = "tamper"
    TAMPER_SENSITIVITY = "tamperSensitivity"
    TARGET_END_TIME = "targetEndTime"
    TARGET_MODULE = "targetModule"
    TARIFF_NAME = "tariffName"
    TARIFF_PROVIDER = "tariffProvider"
    TEMP_CONDITION = "tempCondition"
    TEMP_TARGET = "tempTarget"
    TEMPERATURE = "temperature"
    TEMPERATURE_ALARM = "temperatureAlarm"
    TEMPERATURE_HUMIDITY = "temperatureHumidity"
    TEMPERATURE_LEVEL = "temperatureLevel"
    TEMPERATURE_RANGE = "temperatureRange"
    TEMPERATURE_REFERENCE = "temperatureReference"
    TEMPERATURE_SETPOINT = "temperatureSetpoint"
    TEMPERATURE_SETPOINT_RANGE = "temperatureSetpointRange"
    TEXT = "text"
    THERMOSTAT_FAN_MODE = "thermostatFanMode"
    THERMOSTAT_FAN_SETTING = "thermostatFanSetting"
    THERMOSTAT_LOCKED = "thermostatLocked"
    THERMOSTAT_MODE = "thermostatMode"
    THERMOSTAT_OPERATING_STATE = "thermostatOperatingState"
    THERMOSTAT_SETPOINT = "thermostatSetpoint"
    THERMOSTAT_SETPOINT_RANGE = "thermostatSetpointRange"
    THREAD_HARDWARE_AVAILABILITY = "threadHardwareAvailability"
    THREAD_REQUIRES_EXTERNAL_HARDWARE = "threadRequiresExternalHardware"
    THREE_AXIS = "threeAxis"
    TIME_LEFT_TO_START = "timeLeftToStart"
    TIME_OFFSET = "timeOffset"
    TIMED_CLEAN_DURATION = "timedCleanDuration"
    TIMED_CLEAN_DURATION_RANGE = "timedCleanDurationRange"
    TIMEOUT_DURATION = "timeoutDuration"
    TIMER_NEXT_CHANGE = "timerNextChange"
    TIMER_SECONDS = "timerSeconds"
    TIMER_TYPE = "timerType"
    TIMEZONE = "timezone"
    TIRE_PRESSURE_STATE = "tirePressureState"
    TITLE = "title"
    TODAY_USAGE_VIEW_AVAILABLE = "todayUsageViewAvailable"
    TOPICLIST = "topiclist"
    TOTAL_TIME = "totalTime"
    TOTAL_USERS_SUPPORTED = "totalUsersSupported"
    TOU_EVENT_NOTIFICATION = "touEventNotification"
    TOU_INFO = "touInfo"
    TOUCH = "touch"
    TRACK_DATA = "trackData"
    TRACK_DESCRIPTION = "trackDescription"
    TS_ID = "tsId"
    TURN_INFO = "turnInfo"
    TV_CHANNEL = "tvChannel"
    TV_CHANNEL_NAME = "tvChannelName"
    TVCHANNEL = "tvchannel"
    TVOC_HEALTH_CONCERN = "tvocHealthConcern"
    TVOC_LEVEL = "tvocLevel"
    TXIC_DEVICE_FW_VER = "txicDeviceFwVer"
    TYPE = "type"
    ULTRAVIOLET_INDEX = "ultravioletIndex"
    UNAVAILABLE_COMMANDS = "unavailableCommands"
    UNLOCK_CODE_NAME = "unlockCodeName"
    UPDATE_AVAILABLE = "updateAvailable"
    UPDATED_TIME = "updatedTime"
    UPLINK_SPEED = "uplinkSpeed"
    URI = "uri"
    USAGE = "usage"
    USAGE_TIME = "usageTime"
    USER_CODE = "userCode"
    USER_ID = "userId"
    USER_LIST = "userList"
    USER_LOCATION = "userLocation"
    USER_NAME = "userName"
    USERS = "users"
    UVC_INTENSIVE = "uvcIntensive"
    UWB_ACTIVATION = "uwbActivation"
    VACATION_MODE = "vacationMode"
    VALUE = "value"
    VALVE = "valve"
    VEHICLE_COLOR = "vehicleColor"
    VEHICLE_ID = "vehicleId"
    VEHICLE_IMAGE = "vehicleImage"
    VEHICLE_MAKE = "vehicleMake"
    VEHICLE_MODEL = "vehicleModel"
    VEHICLE_PLATE = "vehiclePlate"
    VEHICLE_TRIM = "vehicleTrim"
    VEHICLE_YEAR = "vehicleYear"
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
    VIDEO_CLIP = "videoClip"
    VIRUS_DOCTOR_MODE = "virusDoctorMode"
    VISIBLE_FEATURES = "visibleFeatures"
    VOLTAGE = "voltage"
    VOLUME = "volume"
    VOLUME_ALARM = "volumeAlarm"
    VOLUME_LEVEL = "volumeLevel"
    VOLUME_LEVEL_RANGE = "volumeLevelRange"
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
    WATER_PURIFIER_COLD_WATER_LOCK = "waterPurifierColdWaterLock"
    WATER_PURIFIER_HOT_WATER_LOCK = "waterPurifierHotWaterLock"
    WATER_SPRAY_LEVEL = "waterSprayLevel"
    WATER_USAGE_DAY = "waterUsageDay"
    WATER_USAGE_MAX = "waterUsageMax"
    WATER_USAGE_MONTH = "waterUsageMonth"
    WATER_VALVE = "waterValve"
    WATTS = "watts"
    WAYPOINTS = "waypoints"
    WEEK_DAY_SCHEDULES = "weekDaySchedules"
    WEEK_DAY_SCHEDULES_PER_USER = "weekDaySchedulesPerUser"
    WEIGHT = "weight"
    WELCOME_CARE_MODE = "welcomeCareMode"
    WELCOME_MESSAGE = "welcomeMessage"
    WIFI_GUEST_NETWORK_NAME = "wifiGuestNetworkName"
    WIFI_GUEST_NETWORK_STATUS = "wifiGuestNetworkStatus"
    WIFI_NETWORK_NAME = "wifiNetworkName"
    WIFI_NETWORK_STATUS = "wifiNetworkStatus"
    WIFI_UPDATE_SUPPORT = "wifiUpdateSupport"
    WIND_MODE = "windMode"
    WINDDEG = "winddeg"
    WINDGUST = "windgust"
    WINDOW_SHADE = "windowShade"
    WINDSPEED = "windspeed"
    WIRELESS_OPERATING_MODE = "wirelessOperatingMode"
    YEAR_DAY_SCHEDULES = "yearDaySchedules"
    YEAR_DAY_SCHEDULES_PER_USER = "yearDaySchedulesPerUser"
    ZCL_VERSION = "zclVersion"
    ZIGBEE_HARDWARE_AVAILABILITY = "zigbeeHardwareAvailability"
    ZIGBEE_REQUIRES_EXTERNAL_HARDWARE = "zigbeeRequiresExternalHardware"
    ZONE_BOOSTER = "zoneBooster"
    ZONE_INFO = "zoneInfo"
    ZONE_STATE = "zoneState"
    ZWAVE_HARDWARE_AVAILABILITY = "zwaveHardwareAvailability"
    ZWAVE_REQUIRES_EXTERNAL_HARDWARE = "zwaveRequiresExternalHardware"


CAPABILITY_ATTRIBUTES: dict[Capability, list[Attribute]] = {
    Capability.ACCELERATION_SENSOR: [Attribute.ACCELERATION],
    Capability.ACTIVITY_LIGHTING_MODE: [Attribute.LIGHTING_MODE],
    Capability.ACTIVITY_SENSOR: [Attribute.ACTIVITY],
    Capability.ACTUATOR: [],
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
    Capability.AIR_QUALITY_HEALTH_CONCERN: [
        Attribute.AIR_QUALITY_HEALTH_CONCERN,
        Attribute.SUPPORTED_AIR_QUALITY_VALUES,
    ],
    Capability.AIR_QUALITY_SENSOR: [Attribute.AIR_QUALITY],
    Capability.ALARM: [Attribute.ALARM],
    Capability.ALARM_SENSOR: [
        Attribute.ALARM_SENSOR_STATE,
        Attribute.SUPPORTED_ALARM_SENSOR_STATES,
    ],
    Capability.APPLIANCE_UTILIZATION: [Attribute.STATUS],
    Capability.ATMOSPHERIC_PRESSURE_MEASUREMENT: [Attribute.ATMOSPHERIC_PRESSURE],
    Capability.AUDIO_CAPTURE: [Attribute.CLIP, Attribute.STREAM],
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
    Capability.BATCH_GAS_CONSUMPTION_REPORT: [
        Attribute.HOURLY_GAS_CONSUMPTIONS,
        Attribute.HOURLY_USAGE_VIEW_AVAILABLE,
        Attribute.TODAY_USAGE_VIEW_AVAILABLE,
    ],
    Capability.BATTERY: [Attribute.BATTERY, Attribute.QUANTITY, Attribute.TYPE],
    Capability.BATTERY_LEVEL: [Attribute.BATTERY, Attribute.QUANTITY, Attribute.TYPE],
    Capability.BEACON: [Attribute.PRESENCE],
    Capability.BODY_MASS_INDEX_MEASUREMENT: [Attribute.BMI_MEASUREMENT],
    Capability.BODY_WEIGHT_MEASUREMENT: [Attribute.BODY_WEIGHT_MEASUREMENT],
    Capability.BRIDGE: [],
    Capability.BUFFERED_VIDEO_CAPTURE: [Attribute.CLIP],
    Capability.BUTTON: [
        Attribute.BUTTON,
        Attribute.NUMBER_OF_BUTTONS,
        Attribute.SUPPORTED_BUTTON_VALUES,
    ],
    Capability.BYPASSABLE: [Attribute.BYPASS_STATUS],
    Capability.CAMERA_EVENT: [Attribute.EVENT, Attribute.SUPPORTED_EVENTS],
    Capability.CAMERA_PRESET: [Attribute.PRESETS],
    Capability.CARBON_DIOXIDE_HEALTH_CONCERN: [
        Attribute.CARBON_DIOXIDE_HEALTH_CONCERN,
        Attribute.SUPPORTED_CARBON_DIOXIDE_VALUES,
    ],
    Capability.CARBON_DIOXIDE_MEASUREMENT: [Attribute.CARBON_DIOXIDE],
    Capability.CARBON_MONOXIDE_DETECTOR: [Attribute.CARBON_MONOXIDE],
    Capability.CARBON_MONOXIDE_HEALTH_CONCERN: [
        Attribute.CARBON_MONOXIDE_HEALTH_CONCERN,
        Attribute.SUPPORTED_CARBON_MONOXIDE_VALUES,
    ],
    Capability.CARBON_MONOXIDE_MEASUREMENT: [Attribute.CARBON_MONOXIDE_LEVEL],
    Capability.CHARGE_POINT_STATE: [
        Attribute.CHARGE_POINT_STATE,
        Attribute.SUPPORTED_CHARGE_POINT_STATES,
    ],
    Capability.CHARGING_STATE: [
        Attribute.CHARGING_STATE,
        Attribute.SUPPORTED_CHARGING_STATES,
    ],
    Capability.CHIME: [Attribute.CHIME],
    Capability.COLOR: [Attribute.COLOR_VALUE],
    Capability.COLOR_CONTROL: [Attribute.COLOR, Attribute.HUE, Attribute.SATURATION],
    Capability.COLOR_MODE: [Attribute.COLOR_MODE],
    Capability.COLOR_TEMPERATURE: [
        Attribute.COLOR_TEMPERATURE,
        Attribute.COLOR_TEMPERATURE_RANGE,
    ],
    Capability.CONFIGURATION: [],
    Capability.CONSUMABLE: [Attribute.CONSUMABLE_STATUS],
    Capability.CONSUMABLE_LIFE: [
        Attribute.LIFESPAN,
        Attribute.START_DATE,
        Attribute.TYPE,
    ],
    Capability.CONTACT_SENSOR: [Attribute.CONTACT],
    Capability.CONTAINER_STATE: [
        Attribute.CONTAINER_STATE,
        Attribute.CONTENT,
        Attribute.SUPPORTED_CONTAINER_STATES,
    ],
    Capability.COOK_TIME: [Attribute.COOK_TIME, Attribute.COOK_TIME_RANGE],
    Capability.CURRENT_MEASUREMENT: [Attribute.CURRENT],
    Capability.DELIVERY_ROBOT_CALL: [
        Attribute.ROBOT_STATE,
        Attribute.SUPPORTED_ROBOT_COMMANDS,
        Attribute.SUPPORTED_ROBOT_STATES,
    ],
    Capability.DEMAND_RESPONSE_LOAD_CONTROL: [
        Attribute.DEMAND_RESPONSE_LOAD_CONTROL_STATUS
    ],
    Capability.DEW_POINT: [Attribute.DEWPOINT],
    Capability.DISHWASHER_MODE: [
        Attribute.DISHWASHER_MODE,
        Attribute.SUPPORTED_DISHWASHER_MODES,
    ],
    Capability.DISHWASHER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.DISHWASHER_JOB_STATE,
        Attribute.MACHINE_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.DISHWASHER_OPERATIONAL_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.DISHWASHER_JOB_STATE,
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.DOOR_CONTROL: [Attribute.DOOR],
    Capability.DRIVING_STATUS: [Attribute.DRIVING_STATUS],
    Capability.DRYER_MODE: [Attribute.DRYER_MODE],
    Capability.DRYER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.DRYER_JOB_STATE,
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.DUST_HEALTH_CONCERN: [
        Attribute.DUST_HEALTH_CONCERN,
        Attribute.SUPPORTED_DUST_VALUES,
    ],
    Capability.DUST_SENSOR: [Attribute.DUST_LEVEL, Attribute.FINE_DUST_LEVEL],
    Capability.ELEVATOR_CALL: [Attribute.CALL_STATUS],
    Capability.END_TO_END_ENCRYPTION: [Attribute.ENCRYPTED_KEK, Attribute.NONCE],
    Capability.ENERGY_METER: [Attribute.ENERGY],
    Capability.EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT: [
        Attribute.EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT
    ],
    Capability.ESTIMATED_TIME_OF_ARRIVAL: [Attribute.ETA],
    Capability.EVSE_CHARGING_SESSION: [
        Attribute.CHARGING_STATE,
        Attribute.ENERGY_DELIVERED,
        Attribute.MAX_CURRENT,
        Attribute.MIN_CURRENT,
        Attribute.SESSION_TIME,
        Attribute.SUPPORTED_CHARGING_COMMANDS,
        Attribute.TARGET_END_TIME,
    ],
    Capability.EVSE_STATE: [
        Attribute.FAULT_STATE,
        Attribute.STATE,
        Attribute.SUPPLY_STATE,
    ],
    Capability.EXECUTE: [Attribute.DATA],
    Capability.FACE_RECOGNITION: [Attribute.FACE_RECOGNIZED_EVENT, Attribute.USER_LIST],
    Capability.FAN_MODE: [Attribute.FAN_MODE, Attribute.SUPPORTED_FAN_MODES],
    Capability.FAN_OSCILLATION_MODE: [
        Attribute.AVAILABLE_FAN_OSCILLATION_MODES,
        Attribute.FAN_OSCILLATION_MODE,
        Attribute.SUPPORTED_FAN_OSCILLATION_MODES,
    ],
    Capability.FAN_SPEED: [Attribute.FAN_SPEED],
    Capability.FAN_SPEED_PERCENT: [Attribute.PERCENT],
    Capability.FEEDER_OPERATING_STATE: [Attribute.FEEDER_OPERATING_STATE],
    Capability.FEEDER_PORTION: [Attribute.FEED_PORTION],
    Capability.FILTER_STATE: [
        Attribute.FILTER_LIFE_REMAINING,
        Attribute.SUPPORTED_FILTER_COMMANDS,
    ],
    Capability.FILTER_STATUS: [Attribute.FILTER_STATUS],
    Capability.FINE_DUST_HEALTH_CONCERN: [
        Attribute.FINE_DUST_HEALTH_CONCERN,
        Attribute.SUPPORTED_FINE_DUST_VALUES,
    ],
    Capability.FINE_DUST_SENSOR: [Attribute.FINE_DUST_LEVEL],
    Capability.FIRMWARE_UPDATE: [
        Attribute.AVAILABLE_VERSION,
        Attribute.CURRENT_VERSION,
        Attribute.ESTIMATED_TIME_REMAINING,
        Attribute.IMAGE_TRANSFER_PROGRESS,
        Attribute.LAST_UPDATE_STATUS,
        Attribute.LAST_UPDATE_STATUS_REASON,
        Attribute.LAST_UPDATE_TIME,
        Attribute.STATE,
        Attribute.SUPPORTED_COMMANDS,
        Attribute.SUPPORTS_PROGRESS_REPORTS,
        Attribute.UPDATE_AVAILABLE,
    ],
    Capability.FLOW_MEASUREMENT: [Attribute.FLOW, Attribute.FLOW_RANGE],
    Capability.FORMALDEHYDE_HEALTH_CONCERN: [
        Attribute.FORMALDEHYDE_HEALTH_CONCERN,
        Attribute.SUPPORTED_FORMALDEHYDE_VALUES,
    ],
    Capability.FORMALDEHYDE_MEASUREMENT: [Attribute.FORMALDEHYDE_LEVEL],
    Capability.GARAGE_DOOR_CONTROL: [Attribute.DOOR],
    Capability.GAS_CONSUMPTION_REPORT: [Attribute.GAS_CONSUMPTION],
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
    Capability.GEOFENCES: [Attribute.GEOFENCES],
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
    Capability.GRID_STATE: [Attribute.GRID],
    Capability.HARDWARE_FAULT: [Attribute.HARDWARE_FAULT],
    Capability.HEALTH_CHECK: [
        Attribute.CHECK_INTERVAL,
        Attribute.DEVICE_WATCH_DEVICE_STATUS,
        Attribute.DEVICE_WATCH_ENROLL,
        Attribute.HEALTH_STATUS,
    ],
    Capability.HOLDABLE_BUTTON: [Attribute.BUTTON, Attribute.NUMBER_OF_BUTTONS],
    Capability.HUMIDIFIER_MODE: [Attribute.HUMIDIFIER_MODE],
    Capability.ILLUMINANCE_MEASUREMENT: [Attribute.ILLUMINANCE],
    Capability.IMAGE_CAPTURE: [
        Attribute.CAPTURE_TIME,
        Attribute.ENCRYPTED,
        Attribute.IMAGE,
    ],
    Capability.INDICATOR: [Attribute.INDICATOR_STATUS],
    Capability.INFRARED_LEVEL: [Attribute.INFRARED_LEVEL],
    Capability.KEYPAD_INPUT: [Attribute.SUPPORTED_KEY_CODES],
    Capability.LANGUAGE_SETTING: [Attribute.LANGUAGE, Attribute.SUPPORTED_LANGUAGES],
    Capability.LAUNDRY_WASHER_RINSE_MODE: [
        Attribute.RINSE_MODE,
        Attribute.SUPPORTED_RINSE_MODES,
    ],
    Capability.LAUNDRY_WASHER_SPIN_SPEED: [
        Attribute.SPIN_SPEED,
        Attribute.SUPPORTED_SPIN_SPEEDS,
    ],
    Capability.LEVEL: [Attribute.LEVEL, Attribute.LEVEL_RANGE],
    Capability.LIGHT: [Attribute.SWITCH],
    Capability.LIGHT_CONTROLLER_MODE: [
        Attribute.LIGHT_CONTROLLER_MODE,
        Attribute.SUPPORTED_LIGHT_CONTROLLER_MODES,
    ],
    Capability.LOCATION_MODE: [Attribute.MODE],
    Capability.LOCK: [
        Attribute.LOCK,
        Attribute.SUPPORTED_LOCK_COMMANDS,
        Attribute.SUPPORTED_LOCK_VALUES,
        Attribute.SUPPORTED_UNLOCK_DIRECTIONS,
    ],
    Capability.LOCK_ALARM: [Attribute.ALARM, Attribute.SUPPORTED_ALARM_VALUES],
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
    Capability.LOCK_CREDENTIALS: [
        Attribute.COMMAND_RESULT,
        Attribute.CREDENTIALS,
        Attribute.MAX_PIN_CODE_LEN,
        Attribute.MIN_PIN_CODE_LEN,
        Attribute.PIN_USERS_SUPPORTED,
        Attribute.SUPPORTED_CREDENTIALS,
    ],
    Capability.LOCK_ONLY: [Attribute.LOCK],
    Capability.LOCK_SCHEDULES: [
        Attribute.COMMAND_RESULT,
        Attribute.WEEK_DAY_SCHEDULES,
        Attribute.WEEK_DAY_SCHEDULES_PER_USER,
        Attribute.YEAR_DAY_SCHEDULES,
        Attribute.YEAR_DAY_SCHEDULES_PER_USER,
    ],
    Capability.LOCK_USERS: [
        Attribute.COMMAND_RESULT,
        Attribute.TOTAL_USERS_SUPPORTED,
        Attribute.USERS,
    ],
    Capability.LOG_TRIGGER: [
        Attribute.LOG_INFO,
        Attribute.LOG_REQUEST_STATE,
        Attribute.LOG_STATE,
    ],
    Capability.MASSAGE_INTENSITY_CHANGE: [Attribute.SUPPORTED_POSITIONS],
    Capability.MASSAGE_INTENSITY_CONTROL: [
        Attribute.INTENSITY_FOOT,
        Attribute.INTENSITY_HEAD,
        Attribute.INTENSITY_RANGE,
        Attribute.INTENSITY_WHOLE,
        Attribute.SUPPORTED_POSITIONS,
    ],
    Capability.MASSAGE_OPERATING: [Attribute.MASSAGE_STATE],
    Capability.MASSAGE_OPERATING_STATE: [Attribute.MASSAGE_STATE],
    Capability.MASSAGE_TIME_CHANGE: [],
    Capability.MASSAGE_TIME_CONTROL: [
        Attribute.COMPLETION_TIME,
        Attribute.SUPPORTED_SET_TIMES,
    ],
    Capability.MEDIA_CONTROLLER: [Attribute.ACTIVITIES, Attribute.CURRENT_ACTIVITY],
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
    Capability.MOLD_HEALTH_CONCERN: [
        Attribute.MOLD_HEALTH_CONCERN,
        Attribute.SUPPORTED_MOLD_VALUES,
    ],
    Capability.MOMENTARY: [],
    Capability.MOTION_BED: [
        Attribute.MODE,
        Attribute.STATELESS_MODE,
        Attribute.SUPPORTED_MODES,
        Attribute.SUPPORTED_MOTION_POSITIONS,
    ],
    Capability.MOTION_SENSOR: [Attribute.MOTION],
    Capability.MOVEMENT_SENSOR: [Attribute.MOVEMENT, Attribute.SUPPORTED_MOVEMENTS],
    Capability.MULTIPLE_ZONE_PRESENCE: [Attribute.ZONE_STATE],
    Capability.MUSIC_PLAYER: [
        Attribute.LEVEL,
        Attribute.MUTE,
        Attribute.STATUS,
        Attribute.TRACK_DATA,
        Attribute.TRACK_DESCRIPTION,
    ],
    Capability.NETWORK_METER: [Attribute.DOWNLINK_SPEED, Attribute.UPLINK_SPEED],
    Capability.NITROGEN_DIOXIDE_HEALTH_CONCERN: [
        Attribute.NITROGEN_DIOXIDE_HEALTH_CONCERN,
        Attribute.SUPPORTED_NITROGEN_DIOXIDE_VALUES,
    ],
    Capability.NITROGEN_DIOXIDE_MEASUREMENT: [Attribute.NITROGEN_DIOXIDE],
    Capability.NOTIFICATION: [],
    Capability.OBJECT_DETECTION: [Attribute.DETECTED, Attribute.SUPPORTED_VALUES],
    Capability.OCCUPANCY_SENSOR: [Attribute.OCCUPANCY],
    Capability.OCF: [
        Attribute.DATA_MODEL_VERSION,
        Attribute.DEVICE_NAME,
        Attribute.HARDWARE_VERSION,
        Attribute.MANUFACTURER_DETAILS_LINK,
        Attribute.MANUFACTURER_NAME,
        Attribute.MANUFACTURE_DATE,
        Attribute.MODEL_NUMBER,
        Attribute.OCF_DEVICE_ID,
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
    Capability.OPERATING_STATE: [
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.OPERATIONAL_STATE: [
        Attribute.OPERATIONAL_STATE,
        Attribute.SUPPORTED_COMMANDS,
        Attribute.SUPPORTED_OPERATIONAL_STATES,
    ],
    Capability.OUTLET: [Attribute.SWITCH],
    Capability.OVEN_MODE: [Attribute.OVEN_MODE, Attribute.SUPPORTED_OVEN_MODES],
    Capability.OVEN_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.OPERATION_TIME,
        Attribute.OVEN_JOB_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.OVEN_OPERATIONAL_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.OPERATION_TIME,
        Attribute.OVEN_JOB_STATE,
        Attribute.PROGRESS,
        Attribute.SUPPORTED_MACHINE_STATES,
    ],
    Capability.OVEN_SETPOINT: [Attribute.OVEN_SETPOINT, Attribute.OVEN_SETPOINT_RANGE],
    Capability.OZONE_HEALTH_CONCERN: [
        Attribute.OZONE_HEALTH_CONCERN,
        Attribute.SUPPORTED_OZONE_VALUES,
    ],
    Capability.OZONE_MEASUREMENT: [Attribute.OZONE],
    Capability.PH_MEASUREMENT: [Attribute.PH],
    Capability.PANIC_ALARM: [Attribute.PANIC_ALARM],
    Capability.PEST_CONTROL: [Attribute.PEST_CONTROL],
    Capability.PET_ACTIVITY: [
        Attribute.PET_ACTIVITY,
        Attribute.SUPPORTED_PET_ACTIVITIES,
    ],
    Capability.POLLING: [],
    Capability.POWER_CONSUMPTION_REPORT: [Attribute.POWER_CONSUMPTION],
    Capability.POWER_METER: [Attribute.POWER],
    Capability.POWER_SOURCE: [Attribute.POWER_SOURCE],
    Capability.PRECIPITATION_MEASUREMENT: [Attribute.PRECIPITATION_LEVEL],
    Capability.PRECIPITATION_RATE: [Attribute.PRECIPITATION_RATE],
    Capability.PRECIPITATION_SENSOR: [Attribute.PRECIPITATION_INTENSITY],
    Capability.PRESENCE_SENSOR: [Attribute.PRESENCE],
    Capability.PUMP_CONTROL_MODE: [
        Attribute.CONTROL_MODE,
        Attribute.CURRENT_CONTROL_MODE,
        Attribute.SUPPORTED_CONTROL_MODES,
    ],
    Capability.PUMP_OPERATION_MODE: [
        Attribute.CURRENT_OPERATION_MODE,
        Attribute.OPERATION_MODE,
        Attribute.SUPPORTED_OPERATION_MODES,
    ],
    Capability.RADON_HEALTH_CONCERN: [
        Attribute.RADON_HEALTH_CONCERN,
        Attribute.SUPPORTED_RADON_VALUES,
    ],
    Capability.RADON_MEASUREMENT: [Attribute.RADON_LEVEL],
    Capability.RAIN_SENSOR: [Attribute.RAIN],
    Capability.RAPID_COOLING: [Attribute.RAPID_COOLING],
    Capability.REFRESH: [],
    Capability.REFRIGERATION: [
        Attribute.DEFROST,
        Attribute.RAPID_COOLING,
        Attribute.RAPID_FREEZING,
    ],
    Capability.REFRIGERATION_SETPOINT: [Attribute.REFRIGERATION_SETPOINT],
    Capability.RELATIVE_BRIGHTNESS: [Attribute.BRIGHTNESS_INTENSITY],
    Capability.RELATIVE_HUMIDITY_MEASUREMENT: [Attribute.HUMIDITY],
    Capability.RELAY_SWITCH: [Attribute.SWITCH],
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
        Attribute.SUPPORTED_OPERATING_STATE_COMMANDS,
    ],
    Capability.ROBOT_CLEANER_STATE: [
        Attribute.ROBOT_CLEANER_CLEANING_STATE,
        Attribute.ROBOT_CLEANER_CONTROL_STATE,
        Attribute.ROBOT_CLEANER_TURBO_STATE,
        Attribute.SUPPORTED_ROBOT_CLEANER_STATES,
    ],
    Capability.ROBOT_CLEANER_TURBO_MODE: [Attribute.ROBOT_CLEANER_TURBO_MODE],
    Capability.SAMSUNG_T_V: [
        Attribute.MESSAGE_BUTTON,
        Attribute.MUTE,
        Attribute.PICTURE_MODE,
        Attribute.SOUND_MODE,
        Attribute.SWITCH,
        Attribute.VOLUME,
    ],
    Capability.SCENE_ACTIVITY: [Attribute.ACTIVATED_SCENE, Attribute.SUPPORTED_SCENES],
    Capability.SCENES: [Attribute.SCENE, Attribute.SUPPORTED_SCENES],
    Capability.SCENT: [Attribute.SCENT_INTENSITY, Attribute.SCENT_NAME],
    Capability.SECURITY_SYSTEM: [
        Attribute.ALARM,
        Attribute.SECURITY_SYSTEM_STATUS,
        Attribute.SENSOR_STATUS,
        Attribute.SUPPORTED_SECURITY_SYSTEM_COMMANDS,
        Attribute.SUPPORTED_SECURITY_SYSTEM_STATUSES,
    ],
    Capability.SENSOR: [],
    Capability.SERVICE_AREA: [Attribute.SELECTED_AREAS, Attribute.SUPPORTED_AREAS],
    Capability.SHOCK_SENSOR: [Attribute.SHOCK],
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
    Capability.SPEECH_RECOGNITION: [Attribute.PHRASE_SPOKEN],
    Capability.SPEECH_SYNTHESIS: [],
    Capability.STATELESS_CUSTOM_BUTTON: [Attribute.AVAILABLE_CUSTOM_BUTTONS],
    Capability.STATELESS_FANSPEED_BUTTON: [Attribute.AVAILABLE_FANSPEED_BUTTONS],
    Capability.STATELESS_POWER_BUTTON: [Attribute.AVAILABLE_POWER_BUTTONS],
    Capability.STATELESS_POWER_TOGGLE_BUTTON: [
        Attribute.AVAILABLE_POWER_TOGGLE_BUTTONS
    ],
    Capability.STEP_SENSOR: [Attribute.GOAL, Attribute.STEPS],
    Capability.SWITCH: [Attribute.SWITCH],
    Capability.SWITCH_LEVEL: [Attribute.LEVEL, Attribute.LEVEL_RANGE],
    Capability.SWITCH_STATE: [Attribute.SWITCH_STATE],
    Capability.T_V: [
        Attribute.CHANNEL,
        Attribute.MOVIE_MODE,
        Attribute.PICTURE,
        Attribute.POWER,
        Attribute.SOUND,
        Attribute.VOLUME,
    ],
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
    Capability.THERMOSTAT: [
        Attribute.COOLING_SETPOINT,
        Attribute.COOLING_SETPOINT_RANGE,
        Attribute.HEATING_SETPOINT,
        Attribute.HEATING_SETPOINT_RANGE,
        Attribute.SCHEDULE,
        Attribute.SUPPORTED_THERMOSTAT_FAN_MODES,
        Attribute.SUPPORTED_THERMOSTAT_MODES,
        Attribute.TEMPERATURE,
        Attribute.THERMOSTAT_FAN_MODE,
        Attribute.THERMOSTAT_MODE,
        Attribute.THERMOSTAT_OPERATING_STATE,
        Attribute.THERMOSTAT_SETPOINT,
        Attribute.THERMOSTAT_SETPOINT_RANGE,
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
    Capability.THERMOSTAT_OPERATING_STATE: [
        Attribute.SUPPORTED_THERMOSTAT_OPERATING_STATES,
        Attribute.THERMOSTAT_OPERATING_STATE,
    ],
    Capability.THERMOSTAT_SCHEDULE: [Attribute.SCHEDULE],
    Capability.THERMOSTAT_SETPOINT: [Attribute.THERMOSTAT_SETPOINT],
    Capability.THERMOSTAT_WATER_HEATING_SETPOINT: [
        Attribute.HEATING_SETPOINT,
        Attribute.HEATING_SETPOINT_RANGE,
    ],
    Capability.THREE_AXIS: [Attribute.THREE_AXIS],
    Capability.TIMED_SESSION: [Attribute.COMPLETION_TIME, Attribute.SESSION_STATUS],
    Capability.TONE: [],
    Capability.TOUCH_SENSOR: [Attribute.TOUCH],
    Capability.TV_CHANNEL: [Attribute.TV_CHANNEL, Attribute.TV_CHANNEL_NAME],
    Capability.TVOC_HEALTH_CONCERN: [
        Attribute.SUPPORTED_TVOC_VALUES,
        Attribute.TVOC_HEALTH_CONCERN,
    ],
    Capability.TVOC_MEASUREMENT: [Attribute.TVOC_LEVEL],
    Capability.ULTRAVIOLET_INDEX: [Attribute.ULTRAVIOLET_INDEX],
    Capability.VALVE: [Attribute.VALVE],
    Capability.VEHICLE_ENGINE: [Attribute.ENGINE_STATE],
    Capability.VEHICLE_FUEL_LEVEL: [Attribute.FUEL_LEVEL],
    Capability.VEHICLE_INFORMATION: [
        Attribute.VEHICLE_COLOR,
        Attribute.VEHICLE_ID,
        Attribute.VEHICLE_IMAGE,
        Attribute.VEHICLE_MAKE,
        Attribute.VEHICLE_MODEL,
        Attribute.VEHICLE_PLATE,
        Attribute.VEHICLE_TRIM,
        Attribute.VEHICLE_YEAR,
    ],
    Capability.VEHICLE_ODOMETER: [Attribute.ODOMETER_READING],
    Capability.VEHICLE_RANGE: [Attribute.ESTIMATED_REMAINING_RANGE],
    Capability.VEHICLE_TIRE_PRESSURE_MONITOR: [Attribute.TIRE_PRESSURE_STATE],
    Capability.VERY_FINE_DUST_HEALTH_CONCERN: [
        Attribute.SUPPORTED_VERY_FINE_DUST_VALUES,
        Attribute.VERY_FINE_DUST_HEALTH_CONCERN,
    ],
    Capability.VERY_FINE_DUST_SENSOR: [Attribute.VERY_FINE_DUST_LEVEL],
    Capability.VIDEO_CAMERA: [
        Attribute.CAMERA,
        Attribute.MUTE,
        Attribute.SETTINGS,
        Attribute.STATUS_MESSAGE,
    ],
    Capability.VIDEO_CAPTURE: [Attribute.CLIP, Attribute.STREAM],
    Capability.VIDEO_CAPTURE2: [Attribute.CLIP],
    Capability.VIDEO_CLIPS: [Attribute.VIDEO_CLIP],
    Capability.VIDEO_STREAM: [Attribute.STREAM, Attribute.SUPPORTED_FEATURES],
    Capability.VOLTAGE_MEASUREMENT: [Attribute.VOLTAGE],
    Capability.WASHER_MODE: [Attribute.WASHER_MODE],
    Capability.WASHER_OPERATING_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
        Attribute.WASHER_JOB_STATE,
    ],
    Capability.WASHER_OPERATIONAL_STATE: [
        Attribute.COMPLETION_TIME,
        Attribute.MACHINE_STATE,
        Attribute.SUPPORTED_MACHINE_STATES,
        Attribute.WASHER_JOB_STATE,
    ],
    Capability.WATER_FLOW_ALARM: [
        Attribute.DURATION_ALARM,
        Attribute.RATE_ALARM,
        Attribute.SUPPORTED_ALARM_STATUSES,
        Attribute.VOLUME_ALARM,
    ],
    Capability.WATER_METER: [
        Attribute.LAST_HOUR,
        Attribute.LAST_SEVEN_DAYS,
        Attribute.LAST_TWENTY_FOUR_HOURS,
    ],
    Capability.WATER_PRESSURE_MEASUREMENT: [
        Attribute.PRESSURE,
        Attribute.PRESSURE_ALARM,
    ],
    Capability.WATER_SENSOR: [Attribute.WATER],
    Capability.WATER_TEMPERATURE_MEASUREMENT: [
        Attribute.TEMPERATURE,
        Attribute.TEMPERATURE_RANGE,
    ],
    Capability.WATER_USAGE_METER: [
        Attribute.WATER_USAGE_DAY,
        Attribute.WATER_USAGE_MONTH,
    ],
    Capability.WEBRTC: [
        Attribute.AUDIO_ONLY,
        Attribute.DEVICE_ICE,
        Attribute.SDP_ANSWER,
        Attribute.STUN_URL,
        Attribute.SUPPORTED_FEATURES,
        Attribute.TALKBACK,
        Attribute.TURN_INFO,
    ],
    Capability.WIFI_MESH_ROUTER: [
        Attribute.CONNECTED_DEVICE_COUNT,
        Attribute.CONNECTED_ROUTER_COUNT,
        Attribute.DISCONNECTED_ROUTER_COUNT,
        Attribute.WIFI_GUEST_NETWORK_NAME,
        Attribute.WIFI_GUEST_NETWORK_STATUS,
        Attribute.WIFI_NETWORK_NAME,
        Attribute.WIFI_NETWORK_STATUS,
    ],
    Capability.WIND_MODE: [Attribute.SUPPORTED_WIND_MODES, Attribute.WIND_MODE],
    Capability.WIND_SPEED: [Attribute.WINDSPEED],
    Capability.WINDOW_SHADE: [
        Attribute.SUPPORTED_WINDOW_SHADE_COMMANDS,
        Attribute.WINDOW_SHADE,
    ],
    Capability.WINDOW_SHADE_LEVEL: [Attribute.SHADE_LEVEL],
    Capability.WINDOW_SHADE_PRESET: [],
    Capability.WINDOW_SHADE_TILT_LEVEL: [Attribute.SHADE_TILT_LEVEL],
    Capability.WIRELESS_OPERATING_MODE: [Attribute.WIRELESS_OPERATING_MODE],
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
    Capability.CUSTOM_AIR_PURIFIER_OPERATION_MODE: [
        Attribute.AP_OPERATION_MODE,
        Attribute.SUPPORTED_AP_OPERATION_MODE,
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
    Capability.CUSTOM_VIRUS_DOCTOR_MODE: [Attribute.VIRUS_DOCTOR_MODE],
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
    Capability.SAMSUNG_CE_ACTIVATION_STATE: [Attribute.ACTIVATION_STATE],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_AUDIO_FEEDBACK: [
        Attribute.SUPPORTED_VOLUME_LEVELS,
        Attribute.VOLUME_LEVEL,
    ],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_BEEP: [Attribute.BEEP],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_DISPLAY: [Attribute.DISPLAY],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_LIGHTING: [
        Attribute.LIGHTING,
        Attribute.SUPPORTED_LIGHTING_LEVELS,
    ],
    Capability.SAMSUNG_CE_AIR_QUALITY_HEALTH_CONCERN: [
        Attribute.AIR_QUALITY_HEALTH_CONCERN,
        Attribute.SUPPORTED_AIR_QUALITY_HEALTH_CONCERNS,
    ],
    Capability.SAMSUNG_CE_ALWAYS_ON_SENSING: [Attribute.ALWAYS_ON, Attribute.ORIGINS],
    Capability.SAMSUNG_CE_AUDIO_VOLUME_LEVEL: [
        Attribute.VOLUME_LEVEL,
        Attribute.VOLUME_LEVEL_RANGE,
    ],
    Capability.SAMSUNG_CE_AUTO_DISPENSE_DETERGENT: [
        Attribute.AMOUNT,
        Attribute.AVAILABLE_TYPES,
        Attribute.DENSITY,
        Attribute.RECOMMENDED_AMOUNT,
        Attribute.REMAINING_AMOUNT,
        Attribute.SUPPORTED_AMOUNT,
        Attribute.SUPPORTED_DENSITY,
        Attribute.SUPPORTED_TYPES,
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
    Capability.SAMSUNG_CE_AUTO_VENTILATION: [Attribute.SUPPORTED_ACTIONS],
    Capability.SAMSUNG_CE_BURNER_INFO: [Attribute.BURNER_ID],
    Capability.SAMSUNG_CE_BUTTON_DISPLAY_CONDITION: [Attribute.SWITCH],
    Capability.SAMSUNG_CE_CAMERA_STREAMING: [
        Attribute.AVAILABLE,
        Attribute.REGISTRATION_STATUS,
    ],
    Capability.SAMSUNG_CE_CLEAN_STATION_STICK_STATUS: [Attribute.STATUS],
    Capability.SAMSUNG_CE_CLEAN_STATION_UV_CLEANING: [
        Attribute.LAST_FINISHED_TIME,
        Attribute.OPERATING_STATE,
        Attribute.OPERATION_TIME,
        Attribute.REMAINING_TIME,
        Attribute.UVC_INTENSIVE,
    ],
    Capability.SAMSUNG_CE_CLOTHING_EXTRA_CARE: [
        Attribute.OPERATION_MODE,
        Attribute.USER_LOCATION,
    ],
    Capability.SAMSUNG_CE_COFFEE_BREWING_RECIPE: [
        Attribute.COFFEE_BREWING_RECIPES,
        Attribute.COFFEE_BREWING_STATUS,
        Attribute.MAX_NUMBER_OF_RECIPES,
        Attribute.SUPPORTED_PUBLISHER_I_DS,
    ],
    Capability.SAMSUNG_CE_CONNECTION_STATE: [Attribute.CONNECTION_STATE],
    Capability.SAMSUNG_CE_CONSUMED_ENERGY: [
        Attribute.MONTHLY_USAGE,
        Attribute.TIME_OFFSET,
    ],
    Capability.SAMSUNG_CE_COOK_RECIPE: [Attribute.COOK_RECIPE, Attribute.STAGE_STATUS],
    Capability.SAMSUNG_CE_COOKTOP_BURNER_MODE: [Attribute.COOKTOP_BURNER_MODE],
    Capability.SAMSUNG_CE_COOKTOP_COOK_RECIPE: [
        Attribute.COOKTOP_COOK_RECIPE,
        Attribute.OVERHEAT_FOR_RECIPES,
        Attribute.PROTOCOL_VERSION,
    ],
    Capability.SAMSUNG_CE_COOKTOP_FLEX_ZONE: [Attribute.FLEX_ZONES],
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
    Capability.SAMSUNG_CE_DDMS_MODE: [Attribute.MODE],
    Capability.SAMSUNG_CE_DEFINED_RECIPE: [Attribute.DEFINED_RECIPE],
    Capability.SAMSUNG_CE_DEHUMIDIFIER_BEEP: [Attribute.BEEP],
    Capability.SAMSUNG_CE_DEHUMIDIFIER_MODE: [
        Attribute.DEHUMIDIFIER_MODE,
        Attribute.SUPPORTED_DEHUMIDIFIER_MODES,
    ],
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
    Capability.SAMSUNG_CE_DRAIN_FILTER: [
        Attribute.DRAIN_FILTER_LAST_RESET_DATE,
        Attribute.DRAIN_FILTER_RESET_TYPE,
        Attribute.DRAIN_FILTER_STATUS,
        Attribute.DRAIN_FILTER_USAGE,
        Attribute.DRAIN_FILTER_USAGE_STEP,
    ],
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
    Capability.SAMSUNG_CE_EHS_BOOSTER_HEATER: [Attribute.STATUS],
    Capability.SAMSUNG_CE_EHS_CYCLE_DATA: [Attribute.INDOOR, Attribute.OUTDOOR],
    Capability.SAMSUNG_CE_EHS_DEFROST_MODE: [Attribute.STATUS],
    Capability.SAMSUNG_CE_EHS_DIVERTER_VALVE: [Attribute.POSITION],
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
        Attribute.SUPPORTED_TYPES,
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
    Capability.SAMSUNG_CE_HOOD_FILTER: [
        Attribute.HOOD_FILTER_CAPACITY,
        Attribute.HOOD_FILTER_LAST_RESET_DATE,
        Attribute.HOOD_FILTER_RESET_TYPE,
        Attribute.HOOD_FILTER_STATUS,
        Attribute.HOOD_FILTER_USAGE,
        Attribute.HOOD_FILTER_USAGE_STEP,
    ],
    Capability.SAMSUNG_CE_HOOD_LAMP_AUTOMATION: [
        Attribute.CONDITION,
        Attribute.END_TIME,
        Attribute.START_TIME,
        Attribute.SUPPORTED_CONDITIONS,
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
    Capability.SAMSUNG_CE_MICROPHONE_SETTINGS: [Attribute.MUTE],
    Capability.SAMSUNG_CE_MICROWAVE_POWER: [
        Attribute.POWER_LEVEL,
        Attribute.SUPPORTED_POWER_LEVELS,
    ],
    Capability.SAMSUNG_CE_MUSIC_PLAYLIST: [Attribute.CURRENT_TRACK, Attribute.PLAYLIST],
    Capability.SAMSUNG_CE_NOTIFICATION: [
        Attribute.ACTION_SETTING,
        Attribute.SUPPORTED_ACTION_SETTINGS,
        Attribute.SUPPORTED_CONTEXTS,
        Attribute.SUPPORT_CUSTOM_CONTENT,
    ],
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
    Capability.SAMSUNG_CE_RELATIVE_HUMIDITY_LEVEL: [
        Attribute.DESIRED_HUMIDITY_LEVEL,
        Attribute.DESIRED_HUMIDITY_LEVEL_RANGE,
        Attribute.RELATIVE_HUMIDITY_LEVEL,
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
    Capability.SAMSUNG_CE_ROBOT_CLEANER_CLEANING_TYPE: [
        Attribute.CLEANING_TYPE,
        Attribute.SUPPORTED_CLEANING_TYPES,
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
    Capability.SAMSUNG_CE_ROBOT_CLEANER_GUIDED_PATROL: [
        Attribute.MAP_ID,
        Attribute.WAYPOINTS,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_AREA_INFO: [Attribute.AREA_INFO],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_CLEANING_INFO: [
        Attribute.AREA,
        Attribute.CLEANED_EXTENT,
        Attribute.NEAR_OBJECT,
        Attribute.REMAINING_TIME,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_LIST: [Attribute.MAPS],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_METADATA: [Attribute.CELL_SIZE],
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
        Attribute.MAP_ID,
        Attribute.OBSOLETED,
        Attribute.PATROL_STATUS,
        Attribute.START_TIME,
        Attribute.TIMEZONE,
        Attribute.TIME_OFFSET,
        Attribute.WAYPOINTS,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PET_CLEANING_SCHEDULE: [
        Attribute.AREA_IDS,
        Attribute.DAY_OF_WEEK,
        Attribute.ENABLED,
        Attribute.EXCLUDE_HOLIDAYS,
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
        Attribute.EXCLUDE_HOLIDAYS,
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
    Capability.SAMSUNG_CE_ROBOT_CLEANER_SAFETY_PATROL: [Attribute.PERSON_DETECTION],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_SYSTEM_SOUND_MODE: [
        Attribute.SOUND_MODE,
        Attribute.SUPPORTED_SOUND_MODES,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_WATER_SPRAY_LEVEL: [
        Attribute.AVAILABLE_WATER_SPRAY_LEVELS,
        Attribute.SUPPORTED_WATER_SPRAY_LEVELS,
        Attribute.WATER_SPRAY_LEVEL,
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
    Capability.SAMSUNG_CE_SENSING_ON_SUSPEND_MODE: [Attribute.SENSING_ON_SUSPEND_MODE],
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
    Capability.SAMSUNG_CE_STICK_CLEANER_DUST_BAG: [
        Attribute.STATUS,
        Attribute.SUPPORTED_STATUS,
        Attribute.USAGE,
    ],
    Capability.SAMSUNG_CE_STICK_CLEANER_DUSTBIN_STATUS: [
        Attribute.LAST_EMPTIED_TIME,
        Attribute.OPERATING_STATE,
    ],
    Capability.SAMSUNG_CE_STICK_CLEANER_STATUS: [Attribute.OPERATING_STATE],
    Capability.SAMSUNG_CE_STICK_CLEANER_STICK_STATUS: [
        Attribute.BLE_CONNECTION_STATE,
        Attribute.MODE,
        Attribute.STATUS,
    ],
    Capability.SAMSUNG_CE_SURFACE_RESIDUAL_HEAT: [Attribute.SURFACE_RESIDUAL_HEAT],
    Capability.SAMSUNG_CE_SYSTEM_AIR_CONDITIONER_RESERVATION: [
        Attribute.MAX_NUMBER_OF_RESERVATIONS,
        Attribute.RESERVATIONS,
    ],
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
        Attribute.CYCLE_TYPE,
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
    Capability.SAMSUNG_CE_WATER_DISPENSER: [
        Attribute.AMOUNT,
        Attribute.AMOUNT_RESOLUTION,
        Attribute.HOT_TEMPERATURE,
        Attribute.MAX_SUPPORTED_AMOUNT,
        Attribute.MIN_SUPPORTED_AMOUNT,
        Attribute.MODE,
        Attribute.STATUS,
        Attribute.SUPPORTED_HOT_TEMPERATURES,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.SAMSUNG_CE_WATER_PURIFIER_COLD_WATER_LOCK: [
        Attribute.WATER_PURIFIER_COLD_WATER_LOCK
    ],
    Capability.SAMSUNG_CE_WATER_PURIFIER_HOT_WATER_LOCK: [
        Attribute.WATER_PURIFIER_HOT_WATER_LOCK
    ],
    Capability.SAMSUNG_CE_WATER_PURIFIER_MEDICATION_MODE: [],
    Capability.SAMSUNG_CE_WATER_PURIFIER_OPERATING_STATE: [Attribute.OPERATING_STATE],
    Capability.SAMSUNG_CE_WATER_RESERVOIR: [Attribute.SLOT_STATE],
    Capability.SAMSUNG_CE_WATER_STERILIZATION_OPERATING_STATE: [
        Attribute.MAX_OPERATION_TIME,
        Attribute.REMAINING_TIME,
    ],
    Capability.SAMSUNG_CE_WATER_STERILIZATION_SCHEDULE: [
        Attribute.INTERVAL,
        Attribute.LAST_STERILIZED_TIME,
        Attribute.SCHEDULED_TIME,
        Attribute.START_TIME,
    ],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT: [Attribute.WEIGHT],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT_CALIBRATION: [],
    Capability.SAMSUNG_CE_WELCOME_COOLING: [
        Attribute.LATEST_REQUEST_ID,
        Attribute.OPERATING_STATE,
    ],
    Capability.SAMSUNG_CE_WELCOME_HUMIDITY: [
        Attribute.LATEST_REQUEST_ID,
        Attribute.OPERATING_STATE,
    ],
    Capability.SAMSUNG_CE_WELCOME_MESSAGE: [Attribute.WELCOME_MESSAGE],
    Capability.SAMSUNG_CE_WIFI_KIT_SUB_DEVICES: [
        Attribute.NUMBER_OF_CONNECTED_DEVICES,
        Attribute.SUB_DEVICES,
    ],
    Capability.SAMSUNG_VD_AI_ACTION: [
        Attribute.CURATION_SUPPORT,
        Attribute.IMAGE_SUPPORT,
    ],
    Capability.SAMSUNG_VD_AMBIENT: [Attribute.INFO],
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
        Attribute.ART_SUPPORTED,
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
    Capability.SAMSUNG_IM_CHARGER_FIRMWARE: [
        Attribute.MCU_DEVICE_FW_VER,
        Attribute.TXIC_DEVICE_FW_VER,
    ],
    Capability.SAMSUNG_IM_CHARGING_STATUS: [
        Attribute.CHARGING_STATUS,
        Attribute.STOPPED_STATUS,
    ],
    Capability.SAMSUNG_IM_DEVICESTATUS: [Attribute.STATUS],
    Capability.SAMSUNG_IM_FIND_NODE: [Attribute.DISABLED_REASON, Attribute.ENABLED],
    Capability.SAMSUNG_IM_FIND_NODE_GEOLOCATION: [
        Attribute.ACCURACY,
        Attribute.HEADING,
        Attribute.LATITUDE,
        Attribute.LONGITUDE,
        Attribute.METHOD,
        Attribute.SPEED,
    ],
    Capability.SAMSUNG_IM_FIRMWARE_AUTO_UPDATE: [Attribute.AUTO_UPDATE_ENABLED],
    Capability.SAMSUNG_IM_FIRMWARE_SERVER: [Attribute.SERVER],
    Capability.SAMSUNG_IM_FIXED_FIND_NODE: [],
    Capability.SAMSUNG_IM_HUB_ONBOARDING: [Attribute.ONBOARDING],
    Capability.SAMSUNG_IM_HUE_SYNC_MODE: [Attribute.MODE],
    Capability.SAMSUNG_IM_LED_NOTIFICATION: [Attribute.LED_NOTIFICATION],
    Capability.SAMSUNG_IM_NEARBY_DETECTION: [Attribute.STATUS],
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
    Capability.SAMSUNG_IM_REQUEST_INVITATION: [
        Attribute.DOUBLE,
        Attribute.HELD,
        Attribute.PUSHED,
        Attribute.REQUEST_INVITATION,
    ],
    Capability.SAMSUNG_IM_RING_MOBILE: [
        Attribute.DOUBLE,
        Attribute.HELD,
        Attribute.PUSHED,
        Attribute.RING_MOBILE,
    ],
    Capability.SAMSUNG_IM_SAMSUNGACCOUNT: [Attribute.SIGN_IN_STATUS],
    Capability.SAMSUNG_IM_SELF_TEST: [Attribute.REPORT],
    Capability.SAMSUNG_IM_STHUBEUI: [
        Attribute.HUB_DEVICE_ID,
        Attribute.HUB_EUI,
        Attribute.HUB_ONBOARDING_STATUS,
    ],
    Capability.SAMSUNG_IM_WIFI: [Attribute.CONNECTION_INFO, Attribute.SCAN_RESULTS],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_MUTE: [],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_DOWN: [],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_UP: [],
    Capability.ABATEACHIEVE62503_STATELESS_CHANNEL_DOWN: [],
    Capability.ABATEACHIEVE62503_STATELESS_CHANNEL_UP: [],
    Capability.ABSOLUTEWEATHER46907_LANGUAGE_SUPPORT: [Attribute.LANGUAGE],
    Capability.ABSOLUTEWEATHER46907_LOCK: [Attribute.LOCK],
    Capability.ABSOLUTEWEATHER46907_LOCKSTATERELEASE: [Attribute.LOCK],
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
    Capability.AMBERPIANO10217_MONITORED_APPROACH_DISTANCE: [
        Attribute.DISTANCE,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.AMBERPIANO10217_OBJECT: [Attribute.DATA],
    Capability.AMBERPIANO10217_PRESENCE_DETECTION_STATUS: [
        Attribute.PRESENCE_STATUS,
        Attribute.SUPPORTED_STATUSES,
    ],
    Capability.AMBERPIANO10217_SENSOR_DETECTION_SENSITIVITY: [
        Attribute.SENSITIVITY_MODE,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.AMBERPIANO10217_SENSOR_MONITORING_MODE: [
        Attribute.MONITORING_MODE,
        Attribute.SUPPORTED_MODES,
    ],
    Capability.AMBERPIANO10217_VIRTUAL_THING_TYPE: [
        Attribute.SUPPORTED_TYPES,
        Attribute.TYPE,
    ],
    Capability.EVENTFLUTE36860_DEFAULT_LEVEL_LOCAL: [Attribute.LEVEL_LOCAL],
    Capability.EVENTFLUTE36860_LED_BAR_SWITCH_OFF: [
        Attribute.LED_BAR_OFF_COLOR,
        Attribute.LED_BAR_OFF_LEVEL,
    ],
    Capability.EVENTFLUTE36860_LED_BAR_SWITCH_ON: [
        Attribute.LED_BAR_ON_COLOR,
        Attribute.LED_BAR_ON_LEVEL,
    ],
    Capability.EVENTFLUTE36860_LOCAL_CONTROL: [Attribute.LOCAL_CONTROL],
    Capability.EVENTFLUTE36860_LOG: [Attribute.LOG],
    Capability.EVENTFLUTE36860_NOTIFICATION_ALL: [
        Attribute.NOTIFICATION_COLOR,
        Attribute.NOTIFICATION_DURATION,
        Attribute.NOTIFICATION_EFFECT,
        Attribute.NOTIFICATION_LEVEL,
    ],
    Capability.EVENTFLUTE36860_NOTIFICATION_LZW31SN: [
        Attribute.NOTIFICATION_COLOR,
        Attribute.NOTIFICATION_DURATION,
        Attribute.NOTIFICATION_EFFECT,
        Attribute.NOTIFICATION_LEVEL,
    ],
    Capability.EVENTFLUTE36860_NOTIFICATION_SINGLE: [
        Attribute.NOTIFICATION_COLOR,
        Attribute.NOTIFICATION_DURATION,
        Attribute.NOTIFICATION_EFFECT,
        Attribute.NOTIFICATION_LEVEL,
        Attribute.NOTIFICATION_NUMBER,
    ],
    Capability.EVENTFLUTE36860_REMOTE_CONTROL: [Attribute.REMOTE_CONTROL],
    Capability.HCA_DRYER_MODE: [Attribute.MODE, Attribute.SUPPORTED_MODES],
    Capability.HCA_WASHER_MODE: [Attribute.MODE, Attribute.SUPPORTED_MODES],
    Capability.LEGENDABSOLUTE60149_ACTIONBUTTON2: [],
    Capability.LEGENDABSOLUTE60149_ATMOS_PRESSURE: [Attribute.ATMOS_PRESSURE],
    Capability.LEGENDABSOLUTE60149_BELL_SOUNDS: [Attribute.BELL_SOUNDS],
    Capability.LEGENDABSOLUTE60149_CIRCADIAN: [Attribute.CIRCADIAN],
    Capability.LEGENDABSOLUTE60149_COLOR_CHANGE_MODE1: [Attribute.COLOR_CHANGE_MODE],
    Capability.LEGENDABSOLUTE60149_COLOR_CHANGE_TIMER: [Attribute.COLOR_CHANGE_TIMER],
    Capability.LEGENDABSOLUTE60149_COLOR_CHANGING: [Attribute.COLOR_CHANGING],
    Capability.LEGENDABSOLUTE60149_COLOR_TEMPERATURE_STEPS: [
        Attribute.COLOR_TEMP_STEPS
    ],
    Capability.LEGENDABSOLUTE60149_COMMAND_CLASS: [Attribute.COMMAND_CLASS],
    Capability.LEGENDABSOLUTE60149_CREATE_DEVICE2: [Attribute.CREATE_DEVICE],
    Capability.LEGENDABSOLUTE60149_CURRENT_LOOP: [Attribute.CURRENT_LOOP],
    Capability.LEGENDABSOLUTE60149_CURRENT_TIME_PERIOD: [Attribute.CURRENT_TIME_PERIOD],
    Capability.LEGENDABSOLUTE60149_CURRENT_TWILIGHT: [Attribute.CURRENT_TWILIGHT],
    Capability.LEGENDABSOLUTE60149_DAY_LENGTH: [Attribute.DAY_LENGTH],
    Capability.LEGENDABSOLUTE60149_DEVICE_ASSOCIATION_TYPE: [
        Attribute.DEVICE_ASSOCIATION_TYPE
    ],
    Capability.LEGENDABSOLUTE60149_DEVICE_INFO: [Attribute.DEVICE_INFO],
    Capability.LEGENDABSOLUTE60149_DRIVER_VERSION1: [Attribute.DRIVER_VERSION],
    Capability.LEGENDABSOLUTE60149_EFFECTS_SET_COMMAND: [Attribute.EFFECTS_SET_COMMAND],
    Capability.LEGENDABSOLUTE60149_ENERGY_RESET1: [Attribute.ENERGY_RESET],
    Capability.LEGENDABSOLUTE60149_EVEN_ODD_DAY: [Attribute.EVEN_ODD_DAY],
    Capability.LEGENDABSOLUTE60149_FAN_CYCLIC_MODE: [Attribute.FAN_CYCLIC_MODE],
    Capability.LEGENDABSOLUTE60149_FAN_NEXT_CHANGE: [Attribute.FAN_NEXT_CHANGE],
    Capability.LEGENDABSOLUTE60149_FORCED_ON_LEVEL: [Attribute.FORCED_ON_LEVEL],
    Capability.LEGENDABSOLUTE60149_GET_GROUPS: [Attribute.GET_GROUPS],
    Capability.LEGENDABSOLUTE60149_GROUP_COMMAND_OPTION: [
        Attribute.GROUP_COMMAND_OPTION
    ],
    Capability.LEGENDABSOLUTE60149_GROUP_NUMBER: [Attribute.GROUP_NUMBER],
    Capability.LEGENDABSOLUTE60149_HUE_STEPS: [Attribute.HUE_STEPS],
    Capability.LEGENDABSOLUTE60149_HUMIDITY_CONDITION: [Attribute.HUMIDITY_CONDITION],
    Capability.LEGENDABSOLUTE60149_HUMIDITY_TARGET: [Attribute.HUMIDITY_TARGET],
    Capability.LEGENDABSOLUTE60149_INFO_PANEL: [Attribute.INFO_PANEL],
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
    Capability.LEGENDABSOLUTE60149_LOOPS_NUMBER: [Attribute.LOOPS_NUMBER],
    Capability.LEGENDABSOLUTE60149_MIRROR_GROUP_FUNCTION: [
        Attribute.MIRROR_GROUP_FUNCTION
    ],
    Capability.LEGENDABSOLUTE60149_MIRROR_IN: [Attribute.MIRROR_IN],
    Capability.LEGENDABSOLUTE60149_MIRROR_OUT: [Attribute.MIRROR_OUT],
    Capability.LEGENDABSOLUTE60149_MOTION_SENSOR_ENABLE: [
        Attribute.MOTION_SENSOR_ENABLE
    ],
    Capability.LEGENDABSOLUTE60149_NODE_END_POINT: [Attribute.NODE_END_POINT],
    Capability.LEGENDABSOLUTE60149_NODE_TO_WRITE_HEX: [Attribute.NODE_TO_WRITE],
    Capability.LEGENDABSOLUTE60149_PARAMETER_START: [Attribute.PARAMETER_START],
    Capability.LEGENDABSOLUTE60149_PARAMETEREND: [Attribute.PARAMETER_END],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_OFF1: [Attribute.PROG_OFF],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_ON1: [Attribute.PROG_ON],
    Capability.LEGENDABSOLUTE60149_RANDOM_MAXIMUM_TIMER: [
        Attribute.RANDOM_MAXIMUM_TIMER
    ],
    Capability.LEGENDABSOLUTE60149_RANDOM_MINIMUM_TIMER: [
        Attribute.RANDOM_MINIMUM_TIMER
    ],
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP: [Attribute.RANDOM_NEXT],
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP2: [Attribute.RANDOM_NEXT],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF1: [Attribute.RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF2: [Attribute.RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_RESETBUTTON: [],
    Capability.LEGENDABSOLUTE60149_SIGNAL_METRICS: [Attribute.SIGNAL_METRICS],
    Capability.LEGENDABSOLUTE60149_SIREN_OR_BELL_ACTIVE: [
        Attribute.SIREN_OR_BELL_ACTIVE
    ],
    Capability.LEGENDABSOLUTE60149_SIREN_SOUNDS: [Attribute.SIREN_SOUNDS],
    Capability.LEGENDABSOLUTE60149_SUN_AZIMUTH_ANGLE: [Attribute.SUN_AZIMUTH_ANGLE],
    Capability.LEGENDABSOLUTE60149_SUN_ELEVATION_ANGLE: [Attribute.SUN_ELEVATION_ANGLE],
    Capability.LEGENDABSOLUTE60149_SUN_RISE: [Attribute.SUN_RISE],
    Capability.LEGENDABSOLUTE60149_SUN_RISE_OFFSET1: [Attribute.SUN_RISE_OFFSET],
    Capability.LEGENDABSOLUTE60149_SUN_SET: [Attribute.SUN_SET],
    Capability.LEGENDABSOLUTE60149_SUN_SET_OFFSET1: [Attribute.SUN_SET_OFFSET],
    Capability.LEGENDABSOLUTE60149_SWITCH_ALL_ON_OFF1: [Attribute.SWITCH_ALL_ON_OFF],
    Capability.LEGENDABSOLUTE60149_TEMP_CONDITION2: [Attribute.TEMP_CONDITION],
    Capability.LEGENDABSOLUTE60149_TEMP_TARGET: [Attribute.TEMP_TARGET],
    Capability.LEGENDABSOLUTE60149_THERMOSTAT_LOCKED: [Attribute.THERMOSTAT_LOCKED],
    Capability.LEGENDABSOLUTE60149_TIMER_NEXT_CHANGE: [Attribute.TIMER_NEXT_CHANGE],
    Capability.LEGENDABSOLUTE60149_TIMER_SECONDS: [Attribute.TIMER_SECONDS],
    Capability.LEGENDABSOLUTE60149_TIMER_TYPE: [Attribute.TIMER_TYPE],
    Capability.MIRRORHAPPY40050_COPPER_WATER_METER: [
        Attribute.ENERGY_USAGE_DAY,
        Attribute.ENERGY_USAGE_MONTH,
        Attribute.POWER_CURRENT,
    ],
    Capability.MUSICAHEAD43206_POWERMODE: [Attribute.PMODE],
    Capability.MUSICAHEAD43206_SNOOZE: [Attribute.SNOOZE],
    Capability.MUSICAHEAD43206_STAGE: [Attribute.STAGE],
    Capability.PARTYVOICE23922_ADD2: [],
    Capability.PARTYVOICE23922_AMPERAGE: [Attribute.AMPERAGE],
    Capability.PARTYVOICE23922_APIWEBREQUEST: [],
    Capability.PARTYVOICE23922_BAROMETER2: [Attribute.PRESSURE],
    Capability.PARTYVOICE23922_CASTMEDIACONTROL: [Attribute.CAST_CONTROL],
    Capability.PARTYVOICE23922_CLOSEDURATION: [Attribute.CLOSEDURATION],
    Capability.PARTYVOICE23922_CLOUDCOVER: [Attribute.CLOUDCOVER],
    Capability.PARTYVOICE23922_COUNT: [Attribute.COUNT],
    Capability.PARTYVOICE23922_CREATEANOTHER: [],
    Capability.PARTYVOICE23922_CREATEDEV8: [Attribute.DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEHTTPDEV2B: [Attribute.DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEMQTTDEV9: [Attribute.DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEQTY: [Attribute.CREATE_QTY],
    Capability.PARTYVOICE23922_DURATION2: [Attribute.DURATION],
    Capability.PARTYVOICE23922_ERRORSENSOR: [Attribute.ERRORSTATUS],
    Capability.PARTYVOICE23922_ERRORSTATUS: [Attribute.ERRORSTATUS],
    Capability.PARTYVOICE23922_ERRORSTATUSCV: [Attribute.ERRORSTATUS],
    Capability.PARTYVOICE23922_HTTPCODE: [Attribute.HTTPCODE],
    Capability.PARTYVOICE23922_HTTPRESPONSE: [Attribute.RESPONSE],
    Capability.PARTYVOICE23922_INFOTABLE: [Attribute.INFO],
    Capability.PARTYVOICE23922_INPUTPERCENT: [Attribute.PERCENT],
    Capability.PARTYVOICE23922_INPUTSTATE: [Attribute.STATE],
    Capability.PARTYVOICE23922_INVENTORY8: [Attribute.INVENTORY],
    Capability.PARTYVOICE23922_KEYNUMVALUE: [Attribute.KEYNUMVALUE],
    Capability.PARTYVOICE23922_KEYVALUE2: [Attribute.KEYVALUE],
    Capability.PARTYVOICE23922_LOCATION: [Attribute.LOCATION],
    Capability.PARTYVOICE23922_MEDIASUBTITLE: [Attribute.SUBTITLE],
    Capability.PARTYVOICE23922_MEDIATITLE: [Attribute.TITLE],
    Capability.PARTYVOICE23922_MQTTPUBLISH: [],
    Capability.PARTYVOICE23922_NAMEINPUT: [Attribute.NAME_TEXT],
    Capability.PARTYVOICE23922_ONVIFINFO: [Attribute.INFO],
    Capability.PARTYVOICE23922_ONVIFSTATUS: [Attribute.STATUS],
    Capability.PARTYVOICE23922_OPENDURATION: [Attribute.OPENDURATION],
    Capability.PARTYVOICE23922_POWERFACTOR2: [Attribute.POWERFACTOR],
    Capability.PARTYVOICE23922_PRECIPPROB: [Attribute.PROBABILITY],
    Capability.PARTYVOICE23922_PRECIPRATE: [Attribute.PRECIP],
    Capability.PARTYVOICE23922_REACTIVEPOWER: [Attribute.REACTIVE],
    Capability.PARTYVOICE23922_REFRESH: [],
    Capability.PARTYVOICE23922_RESETALT: [],
    Capability.PARTYVOICE23922_RESETSELECT: [Attribute.CMD_SELECT],
    Capability.PARTYVOICE23922_ROKUCURRENTAPP: [Attribute.CURRENT_APP],
    Capability.PARTYVOICE23922_ROKUMEDIASTATUS: [Attribute.MEDIA_STATUS],
    Capability.PARTYVOICE23922_SETILLUMINANCE: [Attribute.ILLUMVALUE],
    Capability.PARTYVOICE23922_SHADEPAUSE: [],
    Capability.PARTYVOICE23922_SHELLYDEVS4: [Attribute.DEVICE_TYPE],
    Capability.PARTYVOICE23922_STATEFIELD2: [Attribute.TEXT],
    Capability.PARTYVOICE23922_STATUS: [Attribute.STATUS],
    Capability.PARTYVOICE23922_SUBTRACT2: [],
    Capability.PARTYVOICE23922_SUMMARY: [Attribute.SUMMARY],
    Capability.PARTYVOICE23922_TEMPMAX: [Attribute.MAXTEMP],
    Capability.PARTYVOICE23922_TEMPMIN: [Attribute.MINTEMP],
    Capability.PARTYVOICE23922_TOPICLIST: [Attribute.TOPICLIST],
    Capability.PARTYVOICE23922_TVCHANNEL: [Attribute.TVCHANNEL],
    Capability.PARTYVOICE23922_VHUMIDITYSET: [Attribute.VHUMIDITY],
    Capability.PARTYVOICE23922_VOLUMEDOWN: [],
    Capability.PARTYVOICE23922_VOLUMEUP: [],
    Capability.PARTYVOICE23922_VTEMPSET: [Attribute.VTEMP],
    Capability.PARTYVOICE23922_WATTAGE4: [Attribute.WATTS],
    Capability.PARTYVOICE23922_WEBREQUEST: [],
    Capability.PARTYVOICE23922_WEBREQUESTSELECT: [Attribute.SELECTION],
    Capability.PARTYVOICE23922_WINDDIRDEG: [Attribute.WINDDEG],
    Capability.PARTYVOICE23922_WINDDIRECTION2: [Attribute.DIRECTION],
    Capability.PARTYVOICE23922_WINDGUST: [Attribute.WINDGUST],
    Capability.PARTYVOICE23922_WINDSPEED5: [Attribute.W_SPEED],
    Capability.PARTYVOICE23922_WLEDEFFECTMODE2: [Attribute.EFFECT_MODE],
    Capability.PLATEMUSIC11009_AMPERAGE_MEASUREMENT: [Attribute.AMPERAGE],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_FOUR: [
        Attribute.ASSOCIATION_GROUP_FOUR
    ],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_THREE: [
        Attribute.ASSOCIATION_GROUP_THREE
    ],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_TWO: [Attribute.ASSOCIATION_GROUP_TWO],
    Capability.PLATEMUSIC11009_BASIC_SET_ASSOCIATION_GROUP: [
        Attribute.BASIC_SET_ASSOCIATION_GROUP
    ],
    Capability.PLATEMUSIC11009_DEVICE_NETWORK_ID: [Attribute.DEVICE_NETWORK_ID],
    Capability.PLATEMUSIC11009_FIRMWARE: [Attribute.FIRMWARE_VERSION],
    Capability.PLATEMUSIC11009_HS_LED_MODE: [Attribute.LED_MODE],
    Capability.PLATEMUSIC11009_HS_NORMAL_LED_COLOR: [Attribute.NORMAL_LED_COLOR],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_BLINKING_COLOR: [
        Attribute.STATUS_LED_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_BLINKING_FREQ: [
        Attribute.STATUS_LED_BLINKING_FREQ
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_FIVE_COLOR: [
        Attribute.STATUS_LED_FIVE_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_FOUR_COLOR: [
        Attribute.STATUS_LED_FOUR_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_ONE_COLOR: [
        Attribute.STATUS_LED_ONE_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_SEVEN_COLOR: [
        Attribute.STATUS_LED_SEVEN_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_SIX_COLOR: [
        Attribute.STATUS_LED_SIX_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_THREE_COLOR: [
        Attribute.STATUS_LED_THREE_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_TWO_COLOR: [
        Attribute.STATUS_LED_TWO_COLOR
    ],
    Capability.PLATEMUSIC11009_HUMIDITY_ALARM: [Attribute.HUMIDITY_ALARM],
    Capability.PLATEMUSIC11009_TEMPERATURE_HUMIDITY_SENSOR: [
        Attribute.TEMPERATURE_HUMIDITY
    ],
    Capability.PLATEMUSIC11009_ZOOZ_LED_BRIGHTNESS: [Attribute.LED_BRIGHTNESS],
    Capability.PLATEMUSIC11009_ZOOZ_LED_COLOR: [Attribute.LED_COLOR],
    Capability.PLATEMUSIC11009_ZOOZ_LED_MODE: [Attribute.LED_MODE],
    Capability.PLATINUMMASSIVE43262_AUTO_LOCK: [Attribute.AUTO_LOCK],
    Capability.PLATINUMMASSIVE43262_JASCO_DEFAULT_LEVEL: [Attribute.DEFAULT_LEVEL],
    Capability.PLATINUMMASSIVE43262_JASCO_LIGHT_SENSING: [Attribute.LIGHT_SENSING],
    Capability.PLATINUMMASSIVE43262_JASCO_MOTION_SENSITIVITY: [
        Attribute.MOTION_SENSITIVITY
    ],
    Capability.PLATINUMMASSIVE43262_JASCO_OPERATION_MODE: [Attribute.OPERATION_MODE],
    Capability.PLATINUMMASSIVE43262_JASCO_TIMEOUT_DURATION: [
        Attribute.TIMEOUT_DURATION
    ],
    Capability.PLATINUMMASSIVE43262_KEYPAD_BEEP: [Attribute.KEYPAD_BEEP],
    Capability.PLATINUMMASSIVE43262_LOCK_AND_LEAVE: [Attribute.LOCK_AND_LEAVE],
    Capability.PLATINUMMASSIVE43262_SCHLAGE_INTERIOR_BUTTON: [
        Attribute.INTERIOR_BUTTON
    ],
    Capability.PLATINUMMASSIVE43262_SCHLAGE_LOCK_ALARM: [
        Attribute.ACTIVITY_SENSITIVITY,
        Attribute.ALARM_MODE,
        Attribute.FORCED_ENTRY_SENSITIVITY,
        Attribute.TAMPER_SENSITIVITY,
    ],
    Capability.PLATINUMMASSIVE43262_STATUS_MESSAGE: [Attribute.STATUS_MESSAGE],
    Capability.PLATINUMMASSIVE43262_UNLOCK_CODE_NAME: [Attribute.UNLOCK_CODE_NAME],
    Capability.PLATINUMMASSIVE43262_VACATION_MODE: [Attribute.VACATION_MODE],
    Capability.RBOYAPPS_LOCK_AUDIO: [Attribute.AUDIO],
    Capability.RBOYAPPS_LOCK_AUTOLOCK: [Attribute.AUTOLOCK],
    Capability.RBOYAPPS_LOCK_EXTENDED: [
        Attribute.INVALID_CODE,
        Attribute.LOCK_STATUS,
        Attribute.LOCK_TYPE,
        Attribute.USER_CODE,
        Attribute.USER_ID,
        Attribute.USER_NAME,
    ],
    Capability.RBOYAPPS_LOCK_KEYPAD: [Attribute.KEYPAD],
    Capability.RBOYAPPS_LOCK_ONE_TOUCH_LOCK: [Attribute.ONETOUCHLOCK],
    Capability.RBOYAPPS_LOCK_TAMPER: [Attribute.ALARM],
    Capability.RBOYAPPS_LOCK_TAMPER_SENSITIVITY: [Attribute.SENSITIVE],
    Capability.RIVERTALENT14263_ADAPTIVE_ENERGY_USAGE_STATE: [
        Attribute.ENERGY_USAGE_STATE,
        Attribute.GRID_STATUS_STATUS,
        Attribute.GRID_STATUS_SUPPORT,
        Attribute.STORM_WATCH_ACTIVE,
        Attribute.STORM_WATCH_ENABLED,
        Attribute.STORM_WATCH_SUPPORT,
    ],
    Capability.RIVERTALENT14263_BATCH_GAS_CONSUMPTION_REPORT: [
        Attribute.GAS_CONSUMPTIONS
    ],
    Capability.RIVERTALENT14263_BATCH_POWER_CONSUMPTION_REPORT: [
        Attribute.POWER_CONSUMPTIONS
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
    Capability.RIVERTALENT14263_GAS_CONSUMPTION_REPORT: [Attribute.GAS_CONSUMPTION],
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
    Capability.SEC_SMARTTHINGS_HUB: [
        Attribute.AVAILABILITY,
        Attribute.DEVICE_ID,
        Attribute.EUI,
        Attribute.LAST_ONBOARDING_ERROR_CODE,
        Attribute.LAST_ONBOARDING_RESULT,
        Attribute.ONBOARDING_PROGRESS,
        Attribute.STATE,
        Attribute.THREAD_HARDWARE_AVAILABILITY,
        Attribute.THREAD_REQUIRES_EXTERNAL_HARDWARE,
        Attribute.VERSION,
        Attribute.ZIGBEE_HARDWARE_AVAILABILITY,
        Attribute.ZIGBEE_REQUIRES_EXTERNAL_HARDWARE,
        Attribute.ZWAVE_HARDWARE_AVAILABILITY,
        Attribute.ZWAVE_REQUIRES_EXTERNAL_HARDWARE,
    ],
    Capability.SEC_WIFI_CONFIGURATION: [
        Attribute.AUTO_RECONNECTION,
        Attribute.MIN_VERSION,
        Attribute.PROTOCOL_TYPE,
        Attribute.SUPPORTED_AUTH_TYPE,
        Attribute.SUPPORTED_WI_FI_FREQ,
    ],
    Capability.SIGNALAHEAD13665_APPLIANCEOPERATIONSTATESV2: [Attribute.OPERATION_STATE],
    Capability.SIGNALAHEAD13665_DISHWASHERPROGRAMSV2: [
        Attribute.AVAILABLE_PROGRAMS,
        Attribute.PROGRAM,
    ],
    Capability.SIGNALAHEAD13665_STARTSTOPPROGRAMV2: [Attribute.STARTSTOP],
    Capability.STSE_DEVICE_MODE: [Attribute.MODE],
    Capability.STSOLUTIONS_DEMAND_RESPONSE_MODE: [Attribute.MODE],
    Capability.STSOLUTIONS_DEMAND_RESPONSE_STATUS: [
        Attribute.CURRENT_STATUS,
        Attribute.ENROLLMENT_STATUS,
        Attribute.ENROLLMENT_STATUS_CODE,
    ],
    Capability.STSOLUTIONS_MESSAGE: [Attribute.TEXT],
    Capability.STUS_SOFTWARE_GENERATION: [Attribute.GENERATION],
    Capability.SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT: [Attribute.CIRCADIAN],
    Capability.SYNTHETIC_FADE_LIGHTNING_EFFECT: [Attribute.FADE],
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
    Capability.VALLEYBOARD16460_DEBUG: [Attribute.VALUE],
    Capability.VALLEYBOARD16460_HTTPREQUESTPATH: [Attribute.PATH],
    Capability.VALLEYBOARD16460_INFO: [Attribute.VALUE],
    Capability.WATCHDIGIT58804_ACTUALFANSPEED: [Attribute.ACTUAL_FAN_SPEED],
    Capability.WATCHDIGIT58804_AUTOMODE: [Attribute.AUTO_MODE],
    Capability.WATCHDIGIT58804_ERRORSTRING: [Attribute.ERROR],
    Capability.WATCHDIGIT58804_FILTERCHANGENEEDED: [Attribute.FILTER_CHANGE_NEEDED],
    Capability.WATCHDIGIT58804_OUTDOORUNITDEFROSTING: [
        Attribute.OUTDOOR_UNIT_DEFROSTING
    ],
    Capability.WATCHDIGIT58804_STANDBYMODE: [Attribute.STANDBY_MODE],
    Capability.WATCHDIGIT58804_SYSTEMPREHEATING: [Attribute.SYSTEM_PREHEATING],
    Capability.WATCHDIGIT58804_THERMOSTATFANSETTING: [Attribute.THERMOSTAT_FAN_SETTING],
    Capability.WATCHPANEL55613_LCCTHERMOSTAT: [Attribute.DRCAPABLE],
    Capability.WATCHPANEL55613_TCCTHERMOSTAT: [Attribute.DRCAPABLE],
}
