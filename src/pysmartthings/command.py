"""Command model."""

from enum import StrEnum

from pysmartthings.capability import Capability


class Command(StrEnum):
    """Command model."""

    ACT_SILENTLY = "actSilently"
    ACTION = "action"
    ACTIVATE = "activate"
    ACTIVITY = "activity"
    ADD = "add"
    ADD_AGING = "addAging"
    ADD_CREDENTIAL = "addCredential"
    ADD_RESERVATION = "addReservation"
    ADD_USER = "addUser"
    AGREE_UPDATE = "agreeUpdate"
    ALARM_TOGGLE = "alarmToggle"
    ANNOUNCE = "announce"
    ARM_AWAY = "armAway"
    ARM_STAY = "armStay"
    AUTO = "auto"
    AUTOLOCK = "autolock"
    BEEP = "beep"
    BIXBY_COMMAND = "bixbyCommand"
    BOTH = "both"
    CALL = "call"
    CANCEL = "cancel"
    CANCEL_AGING = "cancelAging"
    CANCEL_ONBOARDING = "cancelOnboarding"
    CANCEL_REMAINING_JOB = "cancelRemainingJob"
    CANCEL_SELF_CHECK = "cancelSelfCheck"
    CAPTURE = "capture"
    CAPTURE_CLIP = "captureClip"
    CHANNEL_DOWN = "channelDown"
    CHANNEL_UP = "channelUp"
    CHECK_FOR_FIRMWARE_UPDATE = "checkForFirmwareUpdate"
    CHIME = "chime"
    CLEAR = "clear"
    CLEAR_WEEK_DAY_SCHEDULES = "clearWeekDaySchedules"
    CLEAR_YEAR_DAY_SCHEDULES = "clearYearDaySchedules"
    CLIENT_ICE = "clientIce"
    CLOSE = "close"
    CONFIGURE = "configure"
    COOK_CUSTOM_RECIPE = "cookCustomRecipe"
    COOK_DEFINED_RECIPE = "cookDefinedRecipe"
    COOL = "cool"
    CREATE = "create"
    CREATE_ZONE = "createZone"
    DEACTIVATE = "deactivate"
    DELETE = "delete"
    DELETE_ALL_CREDENTIALS = "deleteAllCredentials"
    DELETE_ALL_USERS = "deleteAllUsers"
    DELETE_CODE = "deleteCode"
    DELETE_CREDENTIAL = "deleteCredential"
    DELETE_RESERVATION = "deleteReservation"
    DELETE_RESERVATIONS = "deleteReservations"
    DELETE_USER = "deleteUser"
    DELETE_WELCOME_MESSAGE = "deleteWelcomeMessage"
    DELETE_ZONE = "deleteZone"
    DEVICE_NOTIFICATION = "deviceNotification"
    DISABLE = "disable"
    DISABLE_ALARM = "disableAlarm"
    DISABLE_AUDIO = "disableAudio"
    DISABLE_AUTO_UPDATE = "disableAutoUpdate"
    DISABLE_AUTOLOCK = "disableAutolock"
    DISABLE_CHARGING = "disableCharging"
    DISABLE_KEYPAD = "disableKeypad"
    DISABLE_LED_NOTIFICATION = "disableLedNotification"
    DISABLE_ONE_TOUCH_LOCK = "disableOneTouchLock"
    DISABLE_REPEAT_MODE = "disableRepeatMode"
    DISABLE_SOUND_DETECTION = "disableSoundDetection"
    DISABLE_WIFI_GUEST_NETWORK = "disableWifiGuestNetwork"
    DISABLE_WIFI_NETWORK = "disableWifiNetwork"
    DISAGREE_UPDATE = "disagreeUpdate"
    DISARM = "disarm"
    DO_NOT_DISTURB_OFF = "doNotDisturbOff"
    DO_NOT_DISTURB_ON = "doNotDisturbOn"
    EDIT_RESERVATION = "editReservation"
    EMERGENCY_HEAT = "emergencyHeat"
    ENABLE = "enable"
    ENABLE_ALARM = "enableAlarm"
    ENABLE_AUDIO = "enableAudio"
    ENABLE_AUTO_UPDATE = "enableAutoUpdate"
    ENABLE_AUTOLOCK = "enableAutolock"
    ENABLE_CHARGING = "enableCharging"
    ENABLE_EP_EVENTS = "enableEpEvents"
    ENABLE_KEYPAD = "enableKeypad"
    ENABLE_LED_NOTIFICATION = "enableLedNotification"
    ENABLE_MONITORING_AUTOMATION = "enableMonitoringAutomation"
    ENABLE_ONE_TOUCH_LOCK = "enableOneTouchLock"
    ENABLE_REPEAT_MODE = "enableRepeatMode"
    ENABLE_SOUND_DETECTION = "enableSoundDetection"
    ENABLE_WIFI_GUEST_NETWORK = "enableWifiGuestNetwork"
    ENABLE_WIFI_NETWORK = "enableWifiNetwork"
    ENCRYPT_KEK = "encryptKek"
    END = "end"
    EP_CMD = "epCmd"
    ESTIMATE_OPERATION_TIME = "estimateOperationTime"
    EXECUTE = "execute"
    FAN_AUTO = "fanAuto"
    FAN_CIRCULATE = "fanCirculate"
    FAN_ON = "fanOn"
    FAST_FORWARD = "fastForward"
    FLIP = "flip"
    FORCEDENTRY = "forcedentry"
    G_E_T = "GET"
    GENERATE_NONCE = "generateNonce"
    GET_SCAN_RESULTS = "getScanResults"
    GO_HOME = "goHome"
    GROUP_VOLUME_DOWN = "groupVolumeDown"
    GROUP_VOLUME_UP = "groupVolumeUp"
    HEAT = "heat"
    INDICATOR_NEVER = "indicatorNever"
    INDICATOR_WHEN_OFF = "indicatorWhenOff"
    INDICATOR_WHEN_ON = "indicatorWhenOn"
    LAUNCH_APP = "launchApp"
    LINK_DRYER_CYCLE = "linkDryerCycle"
    LINK_STEAM_CLOSET_CYCLE = "linkSteamClosetCycle"
    LOCK = "lock"
    LOCKANDLEAVE = "lockandleave"
    LOWER_SETPOINT = "lowerSetpoint"
    MUTE = "mute"
    MUTE_GROUP = "muteGroup"
    MUTED = "muted"
    NAME_SLOT = "nameSlot"
    NEXT_INTENSITY = "nextIntensity"
    NEXT_TIME = "nextTime"
    NEXT_TRACK = "nextTrack"
    OFF = "off"
    ON = "on"
    ONBOARDING = "onboarding"
    OPEN = "open"
    OVERRIDE_DEMAND_RESPONSE_LOAD_CONTROL_ACTION = "overrideDrlcAction"
    P_O_S_T = "POST"
    PAUSE = "pause"
    PERIODIC_SENSING_OFF = "periodicSensingOff"
    PERIODIC_SENSING_ON = "periodicSensingOn"
    PING = "ping"
    PLAY = "play"
    PLAY_PRESET = "playPreset"
    PLAY_TRACK = "playTrack"
    PLAY_TRACK_AND_RESTORE = "playTrackAndRestore"
    PLAY_TRACK_AND_RESUME = "playTrackAndResume"
    POLL = "poll"
    POST_OCF_COMMAND = "postOcfCommand"
    PRESET_POSITION = "presetPosition"
    PREVIOUS_TRACK = "previousTrack"
    PUBLISH = "publish"
    PUSH = "push"
    RAISE_SETPOINT = "raiseSetpoint"
    RECORD_START = "recordStart"
    RECORD_STOP = "recordStop"
    REFRESH = "refresh"
    REFRESH_ALL = "refreshAll"
    REFRESH_CONNECTION = "refreshConnection"
    REFRESH_MINIMUM_RESERVABLE_TIME = "refreshMinimumReservableTime"
    REFRESH_SPECIFIC_AREA = "refreshSpecificArea"
    REGISTER = "register"
    RELOAD_ALL_CODES = "reloadAllCodes"
    REMOVE = "remove"
    REQUEST_CODE = "requestCode"
    REQUEST_DEMAND_RESPONSE_LOAD_CONTROL_ACTION = "requestDrlcAction"
    REQUEST_TURN_INFO = "requestTurnInfo"
    RESET = "reset"
    RESET_DEODOR_FILTER = "resetDeodorFilter"
    RESET_DRAIN_FILTER = "resetDrainFilter"
    RESET_DUST_FILTER = "resetDustFilter"
    RESET_ELECTRIC_HEPA_FILTER = "resetElectricHepaFilter"
    RESET_ENERGY_METER = "resetEnergyMeter"
    RESET_FILTER = "resetFilter"
    RESET_FILTER_USAGE_TIME = "resetFilterUsageTime"
    RESET_HEPA_FILTER = "resetHepaFilter"
    RESET_HOOD_FILTER = "resetHoodFilter"
    RESET_PRECIPITATION_LEVEL = "resetPrecipitationLevel"
    RESET_VERY_FINE_DUST_FILTER = "resetVeryFineDustFilter"
    RESET_WATER_FILTER = "resetWaterFilter"
    RESTORE_TRACK = "restoreTrack"
    RESUME = "resume"
    RESUME_TRACK = "resumeTrack"
    RETURN_TO_HOME = "returnToHome"
    REWIND = "rewind"
    RM_COMMAND = "rmCommand"
    RUN = "run"
    SCHEDULE_COOKING = "scheduleCooking"
    SDP_OFFER = "sdpOffer"
    SEARCH = "search"
    SELECT_AREAS = "selectAreas"
    SEND = "send"
    SEND_CONTENT = "sendContent"
    SEND_KEY = "sendKey"
    SENSITIVE_TOGGLE = "sensitiveToggle"
    SET_AC_OPTIONAL_MODE = "setAcOptionalMode"
    SET_AC_TROPICAL_NIGHT_MODE_LEVEL = "setAcTropicalNightModeLevel"
    SET_ACCESSIBILITY = "setAccessibility"
    SET_ACM_MODE = "setAcmMode"
    SET_ACTION_SETTING = "setActionSetting"
    SET_ACTIVITY_SENSITIVITY = "setActivitySensitivity"
    SET_ACTUAL_FAN_SPEED = "setActualFanSpeed"
    SET_ADD_RINSE = "setAddRinse"
    SET_AIR_CONDITIONER_MODE = "setAirConditionerMode"
    SET_AIR_CONDITIONER_ODOR_CONTROLLER_STATE = "setAirConditionerOdorControllerState"
    SET_AIR_PURIFIER_FAN_MODE = "setAirPurifierFanMode"
    SET_ALARM = "setAlarm"
    SET_ALARM_MODE = "setAlarmMode"
    SET_ALARM_SENSOR_STATE = "setAlarmSensorState"
    SET_ALARM_THRESHOLD = "setAlarmThreshold"
    SET_AMBIENT_CONTENT = "setAmbientContent"
    SET_AMBIENT_ON = "setAmbientOn"
    SET_AMOUNT = "setAmount"
    SET_AP_OPERATION_MODE = "setApOperationMode"
    SET_APP_NAME = "setAppName"
    SET_ATMOS_PRESSURE = "setAtmosPressure"
    SET_AUDIO = "setAudio"
    SET_AUDIO_TRACK = "setAudioTrack"
    SET_AUTO_CLEANING_MODE = "setAutoCleaningMode"
    SET_AUTO_MODE = "setAutoMode"
    SET_AUTO_REPLENISHMENT = "setAutoReplenishment"
    SET_AUTOLOCK = "setAutolock"
    SET_AUTOMATIC_EXECUTION_MODE = "setAutomaticExecutionMode"
    SET_AUTOMATIC_EXECUTION_SETTING = "setAutomaticExecutionSetting"
    SET_BELL_SOUNDS = "setBellSounds"
    SET_BRIGHTNESS_LEVEL = "setBrightnessLevel"
    SET_BUTTON = "setButton"
    SET_BUTTON_DOUBLE_PUSH = "setButtonDoublePush"
    SET_BUTTON_HOLD = "setButtonHold"
    SET_BUTTON_PUSH = "setButtonPush"
    SET_BUTTON_TRIPLE_PUSH = "setButtonTriplePush"
    SET_CHANNEL = "setChannel"
    SET_CIRCADIAN = "setCircadian"
    SET_CLEANING_MODE = "setCleaningMode"
    SET_CLEANING_TYPE = "setCleaningType"
    SET_CLOSE = "setClose"
    SET_CLUSTER_ID = "setClusterId"
    SET_CODE = "setCode"
    SET_CODE_LENGTH = "setCodeLength"
    SET_COFFEE_BREWING_RECIPE = "setCoffeeBrewingRecipe"
    SET_COLOR = "setColor"
    SET_COLOR_CHANGE_MODE = "setColorChangeMode"
    SET_COLOR_CHANGE_TIMER = "setColorChangeTimer"
    SET_COLOR_CHANGING = "setColorChanging"
    SET_COLOR_TEMP_STEPS = "setColorTempSteps"
    SET_COLOR_TEMPERATURE = "setColorTemperature"
    SET_COLOR_VALUE = "setColorValue"
    SET_COMPLETION_TIME = "setCompletionTime"
    SET_CONDITION = "setCondition"
    SET_CONTENT_TEXT = "setContentText"
    SET_CONTENT_TITLE = "setContentTitle"
    SET_CONTEXT = "setContext"
    SET_CONTEXT_SNAPSHOT = "setContextSnapshot"
    SET_CONTEXTS = "setContexts"
    SET_CONTROL = "setControl"
    SET_CONTROL_MODE = "setControlMode"
    SET_COOK_RECIPE = "setCookRecipe"
    SET_COOK_TIME = "setCookTime"
    SET_COOKTOP_COOK_RECIPE = "setCooktopCookRecipe"
    SET_COOLING_SETPOINT = "setCoolingSetpoint"
    SET_COORDINATES = "setCoordinates"
    SET_COURSE = "setCourse"
    SET_CREATE_DEVICE = "setCreateDevice"
    SET_CREATE_QTY = "setCreateQty"
    SET_CURRENT_LOOP = "setCurrentLoop"
    SET_CURRENT_TIME_PERIOD = "setCurrentTimePeriod"
    SET_CURRENT_TWILIGHT = "setCurrentTwilight"
    SET_CUSTOM_COURSE = "setCustomCourse"
    SET_DATA = "setData"
    SET_DAY_LENGTH = "setDayLength"
    SET_DEFAULT_LEVEL = "setDefaultLevel"
    SET_DEFINED_RECIPE = "setDefinedRecipe"
    SET_DEFROST = "setDefrost"
    SET_DEHUMIDIFIER_MODE = "setDehumidifierMode"
    SET_DELAY_END = "setDelayEnd"
    SET_DELAY_TIME = "setDelayTime"
    SET_DENSITY = "setDensity"
    SET_DESIRED_HUMIDITY = "setDesiredHumidity"
    SET_DESIRED_TEMPERATURE = "setDesiredTemperature"
    SET_DETECTION_INTERVAL = "setDetectionInterval"
    SET_DETECTION_PROXIMITY = "setDetectionProximity"
    SET_DETERGENT_TYPE = "setDetergentType"
    SET_DEVICE_ASSOCIATION_TYPE = "setDeviceAssociationType"
    SET_DEVICE_EUI = "setDeviceEui"
    SET_DEVICE_INFO = "setDeviceInfo"
    SET_DEVICE_TYPE = "setDeviceType"
    SET_DISHWASHER_DELAY_START_TIME = "setDishwasherDelayStartTime"
    SET_DISHWASHER_MODE = "setDishwasherMode"
    SET_DISTANCE = "setDistance"
    SET_DO_NOT_DISTURB_MODE = "setDoNotDisturbMode"
    SET_DOSAGE = "setDosage"
    SET_DRIVER_VERSION = "setDriverVersion"
    SET_DRIVING_MODE = "setDrivingMode"
    SET_DRY_PLUS = "setDryPlus"
    SET_DRYER_AUTO_CYCLE_LINK = "setDryerAutoCycleLink"
    SET_DRYER_CYCLE = "setDryerCycle"
    SET_DRYER_CYCLE_PRESET = "setDryerCyclePreset"
    SET_DRYER_DRY_LEVEL = "setDryerDryLevel"
    SET_DRYER_LABEL_SCAN_CYCLE_PRESET = "setDryerLabelScanCyclePreset"
    SET_DRYER_MODE = "setDryerMode"
    SET_DRYER_WRINKLE_PREVENT = "setDryerWrinklePrevent"
    SET_DRYING_TEMPERATURE = "setDryingTemperature"
    SET_DRYING_TIME = "setDryingTime"
    SET_DURATION = "setDuration"
    SET_EFFECT_MODE = "setEffectMode"
    SET_EFFECTS_SET_COMMAND = "setEffectsSetCommand"
    SET_ENABLE_STATE = "setEnableState"
    SET_ENABLED = "setEnabled"
    SET_ENERGY_RESET = "setEnergyReset"
    SET_ENERGY_SAVING_LEVEL = "setEnergySavingLevel"
    SET_ERROR = "setError"
    SET_EVEN_ODD_DAY = "setEvenOddDay"
    SET_EXCLUDE_HOLIDAYS = "setExcludeHolidays"
    SET_FADE = "setFade"
    SET_FAN_CYCLIC_MODE = "setFanCyclicMode"
    SET_FAN_MODE = "setFanMode"
    SET_FAN_NEXT_CHANGE = "setFanNextChange"
    SET_FAN_OSCILLATION_MODE = "setFanOscillationMode"
    SET_FAN_SPEED = "setFanSpeed"
    SET_FILTER_CHANGE_NEEDED = "setFilterChangeNeeded"
    SET_FIRMWARE_VERSION = "setFirmwareVersion"
    SET_FORCED_ON_LEVEL = "setForcedOnLevel"
    SET_FORCED_SENSITIVITY = "setForcedSensitivity"
    SET_FREEZER_CONVERT_MODE = "setFreezerConvertMode"
    SET_FRIDGE_MODE = "setFridgeMode"
    SET_GEOFENCE = "setGeofence"
    SET_GET_GROUPS = "setGetGroups"
    SET_GROUP_COMMAND_OPTION = "setGroupCommandOption"
    SET_GROUP_MUTE = "setGroupMute"
    SET_GROUP_NAME = "setGroupName"
    SET_GROUP_NUMBER = "setGroupNumber"
    SET_GROUP_VOLUME = "setGroupVolume"
    SET_HEATED_DRY = "setHeatedDry"
    SET_HEATING_SETPOINT = "setHeatingSetpoint"
    SET_HIGH_TEMP_WASH = "setHighTempWash"
    SET_HOOD_FAN_SPEED = "setHoodFanSpeed"
    SET_HOT_AIR_DRY = "setHotAirDry"
    SET_HOT_TEMPERATURE = "setHotTemperature"
    SET_HUE = "setHue"
    SET_HUE_STEPS = "setHueSteps"
    SET_HUMIDIFIER_MODE = "setHumidifierMode"
    SET_HUMIDITY_CONDITION = "setHumidityCondition"
    SET_HUMIDITY_TARGET = "setHumidityTarget"
    SET_ILLUM = "setIllum"
    SET_INFO_PANEL = "setInfoPanel"
    SET_INFRARED_LEVEL = "setInfraredLevel"
    SET_INITIAL_AMOUNT = "setInitialAmount"
    SET_INPUT = "setInput"
    SET_INPUT_SOURCE = "setInputSource"
    SET_INTENSITY_FOOT = "setIntensityFoot"
    SET_INTENSITY_HEAD = "setIntensityHead"
    SET_INTENSITY_WHOLE = "setIntensityWhole"
    SET_INVENTORY = "setInventory"
    SET_KEYPAD = "setKeypad"
    SET_LANGUAGE = "setLanguage"
    SET_LED_BAR_OFF_COLOR = "setLedBarOffColor"
    SET_LED_BAR_OFF_LEVEL = "setLedBarOffLevel"
    SET_LED_BAR_ON_COLOR = "setLedBarOnColor"
    SET_LED_BAR_ON_LEVEL = "setLedBarOnLevel"
    SET_LED_BRIGHTNESS = "setLedBrightness"
    SET_LED_COLOR = "setLedColor"
    SET_LED_MODE = "setLedMode"
    SET_LEVEL = "setLevel"
    SET_LEVEL_LOCAL = "setLevelLocal"
    SET_LEVEL_STEPS = "setLevelSteps"
    SET_LIGHT_CONTROL_MODE = "setLightControlMode"
    SET_LIGHT_CONTROLLER_MODE = "setLightControllerMode"
    SET_LIGHT_SENSING = "setLightSensing"
    SET_LIGHTING_LEVEL = "setLightingLevel"
    SET_LIGHTING_MODE = "setLightingMode"
    SET_LOC = "setLoc"
    SET_LOCAL_CONTROL = "setLocalControl"
    SET_LOCAL_DATE = "setLocalDate"
    SET_LOCAL_DATE_ONE = "setLocalDateOne"
    SET_LOCAL_DATE_TWO = "setLocalDateTwo"
    SET_LOCAL_DAY = "setLocalDay"
    SET_LOCAL_DAY_TWO = "setLocalDayTwo"
    SET_LOCAL_HOUR = "setLocalHour"
    SET_LOCAL_HOUR_OFFSET = "setLocalHourOffset"
    SET_LOCAL_HOUR_TWO = "setLocalHourTwo"
    SET_LOCAL_MONTH = "setLocalMonth"
    SET_LOCAL_MONTH_DAY_ONE = "setLocalMonthDayOne"
    SET_LOCAL_MONTH_DAY_TWO = "setLocalMonthDayTwo"
    SET_LOCAL_MONTH_TWO = "setLocalMonthTwo"
    SET_LOCAL_WEEK_DAY = "setLocalWeekDay"
    SET_LOCAL_YEAR = "setLocalYear"
    SET_LOCK = "setLock"
    SET_LOOPS_NUMBER = "setLoopsNumber"
    SET_MACHINE_STATE = "setMachineState"
    SET_MASTER_DI = "setMasterDi"
    SET_MASTER_NAME = "setMasterName"
    SET_MAX_CURRENT = "setMaxCurrent"
    SET_MEDICATION_MODE = "setMedicationMode"
    SET_METERING_DATE = "setMeteringDate"
    SET_MIN_CURRENT = "setMinCurrent"
    SET_MIRROR_GROUP_FUNCTION = "setMirrorGroupFunction"
    SET_MIRROR_IN = "setMirrorIn"
    SET_MIRROR_OUT = "setMirrorOut"
    SET_MODE = "setMode"
    SET_MONITOR = "setMonitor"
    SET_MOTION_SENSITIVITY = "setMotionSensitivity"
    SET_MOTION_SENSOR_ENABLE = "setMotionSensorEnable"
    SET_MUTE = "setMute"
    SET_NAME = "setName"
    SET_NEXT_INPUT_SOURCE = "setNextInputSource"
    SET_NODE_END_POINT = "setNodeEndPoint"
    SET_NODE_TO_WRITE = "setNodeToWrite"
    SET_NORMAL_LED_COLOR = "setNormalLedColor"
    SET_NOTIFICATION_COLOR = "setNotificationColor"
    SET_NOTIFICATION_DURATION = "setNotificationDuration"
    SET_NOTIFICATION_EFFECT = "setNotificationEffect"
    SET_NOTIFICATION_LEVEL = "setNotificationLevel"
    SET_NOTIFICATION_NUMBER = "setNotificationNumber"
    SET_ONE_TOUCH_LOCK = "setOneTouchLock"
    SET_OPEN = "setOpen"
    SET_OPERATING_STATE = "setOperatingState"
    SET_OPERATION_MODE = "setOperationMode"
    SET_OPERATION_ORIGIN = "setOperationOrigin"
    SET_OPERATION_TIME = "setOperationTime"
    SET_OPTION = "setOption"
    SET_OPTIONS = "setOptions"
    SET_ORDER_THRESHOLD = "setOrderThreshold"
    SET_OUTDOOR_UNIT_DEFROSTING = "setOutdoorUnitDefrosting"
    SET_OUTING_MODE = "setOutingMode"
    SET_OVEN_MODE = "setOvenMode"
    SET_OVEN_SETPOINT = "setOvenSetpoint"
    SET_PARAMETER_END = "setParameterEnd"
    SET_PARAMETER_START = "setParameterStart"
    SET_PATH = "setPath"
    SET_PATROL = "setPatrol"
    SET_PERCENT = "setPercent"
    SET_PERIODIC_SENSING = "setPeriodicSensing"
    SET_PERIODIC_SENSING_INTERVAL = "setPeriodicSensingInterval"
    SET_PICTURE_MODE = "setPictureMode"
    SET_PLAN = "setPlan"
    SET_PLAYBACK_REPEAT_MODE = "setPlaybackRepeatMode"
    SET_PLAYBACK_SHUFFLE = "setPlaybackShuffle"
    SET_PLAYBACK_STATUS = "setPlaybackStatus"
    SET_PLAYLIST = "setPlaylist"
    SET_PORTION = "setPortion"
    SET_POWER_LEVEL = "setPowerLevel"
    SET_POWER_STATE = "setPowerState"
    SET_PROG_OFF = "setProgOff"
    SET_PROG_ON = "setProgOn"
    SET_PROGRAM = "setProgram"
    SET_RANDOM_MAXIMUM_TIMER = "setRandomMaximumTimer"
    SET_RANDOM_MINIMUM_TIMER = "setRandomMinimumTimer"
    SET_RANDOM_NEXT = "setRandomNext"
    SET_RANDOM_ON_OFF = "setRandomOnOff"
    SET_RAPID_COOLING = "setRapidCooling"
    SET_RAPID_FREEZING = "setRapidFreezing"
    SET_RECENTLY_USED_APPS = "setRecentlyUsedApps"
    SET_RECOMMENDED_AMOUNT = "setRecommendedAmount"
    SET_REFRIGERATION_SETPOINT = "setRefrigerationSetpoint"
    SET_REMAINING_AMOUNT = "setRemainingAmount"
    SET_REMOTE_CONTROL = "setRemoteControl"
    SET_REPORT_STATE_PERIOD = "setReportStatePeriod"
    SET_REPORT_STATE_REALTIME = "setReportStateRealtime"
    SET_REPORT_STATE_REALTIME_PERIOD = "setReportStateRealtimePeriod"
    SET_RINSE_MODE = "setRinseMode"
    SET_RINSE_PLUS = "setRinsePlus"
    SET_ROBOT_CLEANER_CLEANING_MODE = "setRobotCleanerCleaningMode"
    SET_ROBOT_CLEANER_CLEANING_STATE = "setRobotCleanerCleaningState"
    SET_ROBOT_CLEANER_CONTROL_STATE = "setRobotCleanerControlState"
    SET_ROBOT_CLEANER_MOVEMENT = "setRobotCleanerMovement"
    SET_ROBOT_CLEANER_TURBO_MODE = "setRobotCleanerTurboMode"
    SET_ROBOT_CLEANER_TURBO_STATE = "setRobotCleanerTurboState"
    SET_ROLE = "setRole"
    SET_SANITIZE = "setSanitize"
    SET_SANITIZING_WASH = "setSanitizingWash"
    SET_SATURATION = "setSaturation"
    SET_SCENE = "setScene"
    SET_SCENT_INTENSITY = "setScentIntensity"
    SET_SCHEDULE = "setSchedule"
    SET_SELECT = "setSelect"
    SET_SELECTED_ZONE = "setSelectedZone"
    SET_SELECTION = "setSelection"
    SET_SENSITIVITY = "setSensitivity"
    SET_SERVER = "setServer"
    SET_SERVICE_MESSAGE = "setServiceMessage"
    SET_SHADE_LEVEL = "setShadeLevel"
    SET_SHADE_TILT_LEVEL = "setShadeTiltLevel"
    SET_SIGNAL_METRICS = "setSignalMetrics"
    SET_SIREN_OR_BELL_ACTIVE = "setSirenOrBellActive"
    SET_SIREN_SOUNDS = "setSirenSounds"
    SET_SOFTENER_TYPE = "setSoftenerType"
    SET_SOUND_FROM = "setSoundFrom"
    SET_SOUND_MODE = "setSoundMode"
    SET_SOURCE = "setSource"
    SET_SPEED_BOOSTER = "setSpeedBooster"
    SET_SPI_MODE = "setSpiMode"
    SET_SPIN_SPEED = "setSpinSpeed"
    SET_STAGE = "setStage"
    SET_STANDBY_MODE = "setStandbyMode"
    SET_START_TIME = "setStartTime"
    SET_START_VALUE = "setStartValue"
    SET_STARTSTOP = "setStartstop"
    SET_STATUS = "setStatus"
    SET_STATUS_LED_BLINKING_FREQ = "setStatusLedBlinkingFreq"
    SET_STATUS_LED_COLOR = "setStatusLedColor"
    SET_STATUS_LED_FIVE_COLOR = "setStatusLedFiveColor"
    SET_STATUS_LED_FOUR_COLOR = "setStatusLedFourColor"
    SET_STATUS_LED_ONE_COLOR = "setStatusLedOneColor"
    SET_STATUS_LED_SEVEN_COLOR = "setStatusLedSevenColor"
    SET_STATUS_LED_SIX_COLOR = "setStatusLedSixColor"
    SET_STATUS_LED_THREE_COLOR = "setStatusLedThreeColor"
    SET_STATUS_LED_TWO_COLOR = "setStatusLedTwoColor"
    SET_STEAM_CLOSET_AUTO_CYCLE_LINK = "setSteamClosetAutoCycleLink"
    SET_STEAM_CLOSET_CYCLE = "setSteamClosetCycle"
    SET_STEAM_CLOSET_CYCLE_PRESET = "setSteamClosetCyclePreset"
    SET_STEAM_CLOSET_DELAY_END_TIME = "setSteamClosetDelayEndTime"
    SET_STEAM_CLOSET_MACHINE_STATE = "setSteamClosetMachineState"
    SET_STEAM_CLOSET_WRINKLE_PREVENT = "setSteamClosetWrinklePrevent"
    SET_STEAM_SOAK = "setSteamSoak"
    SET_STEREO_TYPE = "setStereoType"
    SET_STORM_WASH = "setStormWash"
    SET_SUN_AZIMUTH_ANGLE = "setSunAzimuthAngle"
    SET_SUN_ELEVATION_ANGLE = "setSunElevationAngle"
    SET_SUN_RISE = "setSunRise"
    SET_SUN_RISE_OFFSET = "setSunRiseOffset"
    SET_SUN_SET = "setSunSet"
    SET_SUN_SET_OFFSET = "setSunSetOffset"
    SET_SWITCH_ALL_ON_OFF = "setSwitchAllOnOff"
    SET_SYSTEM_PREHEATING = "setSystemPreheating"
    SET_TAMPER_SENSITIVITY = "setTamperSensitivity"
    SET_TARGET_END_TIME = "setTargetEndTime"
    SET_TEMP_CONDITION = "setTempCondition"
    SET_TEMP_TARGET = "setTempTarget"
    SET_TEMPERATURE_LEVEL = "setTemperatureLevel"
    SET_TEMPERATURE_SETPOINT = "setTemperatureSetpoint"
    SET_THERMOSTAT_FAN_MODE = "setThermostatFanMode"
    SET_THERMOSTAT_FAN_SETTING = "setThermostatFanSetting"
    SET_THERMOSTAT_LOCKED = "setThermostatLocked"
    SET_THERMOSTAT_MODE = "setThermostatMode"
    SET_THING_TYPE = "setThingType"
    SET_TIME = "setTime"
    SET_TIME_OFFSET = "setTimeOffset"
    SET_TIMED_CLEAN_DURATION = "setTimedCleanDuration"
    SET_TIMEOUT_DURATION = "setTimeoutDuration"
    SET_TIMER_NEXT_CHANGE = "setTimerNextChange"
    SET_TIMER_SECONDS = "setTimerSeconds"
    SET_TIMER_TYPE = "setTimerType"
    SET_TRACK = "setTrack"
    SET_TV_CHANNEL = "setTvChannel"
    SET_TV_CHANNEL_NAME = "setTvChannelName"
    SET_TYPE = "setType"
    SET_USER_LOCATION = "setUserLocation"
    SET_VALUE = "setValue"
    SET_VIRUS_DOCTOR_MODE = "setVirusDoctorMode"
    SET_VOLUME = "setVolume"
    SET_VOLUME_LEVEL = "setVolumeLevel"
    SET_WASHER_AUTO_DETERGENT = "setWasherAutoDetergent"
    SET_WASHER_AUTO_SOFTENER = "setWasherAutoSoftener"
    SET_WASHER_CYCLE = "setWasherCycle"
    SET_WASHER_CYCLE_PRESET = "setWasherCyclePreset"
    SET_WASHER_LABEL_SCAN_CYCLE_PRESET = "setWasherLabelScanCyclePreset"
    SET_WASHER_MODE = "setWasherMode"
    SET_WASHER_RINSE_CYCLES = "setWasherRinseCycles"
    SET_WASHER_SOIL_LEVEL = "setWasherSoilLevel"
    SET_WASHER_SPIN_LEVEL = "setWasherSpinLevel"
    SET_WASHER_WATER_TEMPERATURE = "setWasherWaterTemperature"
    SET_WASHING_COURSE = "setWashingCourse"
    SET_WASHING_TIME = "setWashingTime"
    SET_WATER_LEVEL = "setWaterLevel"
    SET_WATER_SPRAY_LEVEL = "setWaterSprayLevel"
    SET_WATER_VALVE = "setWaterValve"
    SET_WATTS = "setWatts"
    SET_WEEK_DAY_SCHEDULE = "setWeekDaySchedule"
    SET_WELCOME_MESSAGE = "setWelcomeMessage"
    SET_WIND_MODE = "setWindMode"
    SET_WIRELESS_OPERATING_MODE = "setWirelessOperatingMode"
    SET_YEAR_DAY_SCHEDULE = "setYearDaySchedule"
    SET_ZONE_BOOSTER = "setZoneBooster"
    SETV_HUMIDITY = "setvHumidity"
    SETV_TEMP = "setvTemp"
    SHOW_MESSAGE = "showMessage"
    SIGN_IN = "signIn"
    SIGN_OUT = "signOut"
    SIREN = "siren"
    SPEAK = "speak"
    START = "start"
    START_ACTIVITY = "startActivity"
    START_AUDIO = "startAudio"
    START_COOKING = "startCooking"
    START_EMPTYING = "startEmptying"
    START_ENGINE = "startEngine"
    START_FEEDING = "startFeeding"
    START_LATER = "startLater"
    START_SELF_CHECK = "startSelfCheck"
    START_STREAM = "startStream"
    START_TALKBACK = "startTalkback"
    START_WASHING_COURSE = "startWashingCourse"
    START_WASHING_COURSE_WITH_OPTIONS = "startWashingCourseWithOptions"
    STF_INSTALLED = "stfInstalled"
    STF_UNINSTALLED = "stfUninstalled"
    STOP = "stop"
    STOP_AUDIO = "stopAudio"
    STOP_CAPTURE = "stopCapture"
    STOP_EMPTYING = "stopEmptying"
    STOP_ENGINE = "stopEngine"
    STOP_STREAM = "stopStream"
    STOP_TALKBACK = "stopTalkback"
    STROBE = "strobe"
    TAKE = "take"
    TAMPER = "tamper"
    TOGGLE = "toggle"
    TRIGGER_LOG = "triggerLog"
    TRIGGER_LOG_WITH_LOG_INFO = "triggerLogWithLogInfo"
    TRIGGER_LOG_WITH_URL = "triggerLogWithUrl"
    TRIGGER_MANUAL_SENSING = "triggerManualSensing"
    TURN_WELCOME_CARE_ON = "turnWelcomeCareOn"
    UNLATCH = "unlatch"
    UNLOCK = "unlock"
    UNLOCK_WITH_TIMEOUT = "unlockWithTimeout"
    UNMUTE = "unmute"
    UNMUTE_GROUP = "unmuteGroup"
    UNSET_RECOMMENDED_AMOUNT = "unsetRecommendedAmount"
    UPDATE = "update"
    UPDATE_AGING = "updateAging"
    UPDATE_CODES = "updateCodes"
    UPDATE_CREDENTIAL = "updateCredential"
    UPDATE_FIRMWARE = "updateFirmware"
    UPDATE_USER = "updateUser"
    UPDATE_ZONE_NAME = "updateZoneName"
    UPLOAD_COMPLETE = "uploadComplete"
    UPLOAD_FAILED = "uploadFailed"
    VACATION = "vacation"
    VOLUME_DOWN = "volumeDown"
    VOLUME_UP = "volumeUp"
    ZERO_CALIBRATE = "zeroCalibrate"


CAPABILITY_COMMANDS: dict[Capability, list[Command]] = {
    Capability.ACCELERATION_SENSOR: [],
    Capability.ACTIVITY_LIGHTING_MODE: [Command.SET_LIGHTING_MODE],
    Capability.ACTIVITY_SENSOR: [],
    Capability.ACTUATOR: [],
    Capability.AIR_CONDITIONER_FAN_MODE: [Command.SET_FAN_MODE],
    Capability.AIR_CONDITIONER_MODE: [Command.SET_AIR_CONDITIONER_MODE],
    Capability.AIR_PURIFIER_FAN_MODE: [Command.SET_AIR_PURIFIER_FAN_MODE],
    Capability.AIR_QUALITY_HEALTH_CONCERN: [],
    Capability.AIR_QUALITY_SENSOR: [],
    Capability.ALARM: [Command.BOTH, Command.OFF, Command.SIREN, Command.STROBE],
    Capability.ALARM_SENSOR: [Command.SET_ALARM_SENSOR_STATE],
    Capability.APPLIANCE_UTILIZATION: [],
    Capability.ATMOSPHERIC_PRESSURE_MEASUREMENT: [],
    Capability.AUDIO_CAPTURE: [Command.CAPTURE],
    Capability.AUDIO_MUTE: [Command.MUTE, Command.SET_MUTE, Command.UNMUTE],
    Capability.AUDIO_NOTIFICATION: [
        Command.PLAY_TRACK,
        Command.PLAY_TRACK_AND_RESTORE,
        Command.PLAY_TRACK_AND_RESUME,
    ],
    Capability.AUDIO_STREAM: [Command.START_AUDIO, Command.STOP_AUDIO],
    Capability.AUDIO_TRACK_ADDRESSING: [Command.SET_AUDIO_TRACK],
    Capability.AUDIO_TRACK_DATA: [],
    Capability.AUDIO_VOLUME: [
        Command.SET_VOLUME,
        Command.VOLUME_DOWN,
        Command.VOLUME_UP,
    ],
    Capability.BATCH_GAS_CONSUMPTION_REPORT: [],
    Capability.BATTERY: [],
    Capability.BATTERY_LEVEL: [],
    Capability.BEACON: [],
    Capability.BODY_MASS_INDEX_MEASUREMENT: [],
    Capability.BODY_WEIGHT_MEASUREMENT: [],
    Capability.BRIDGE: [],
    Capability.BUFFERED_VIDEO_CAPTURE: [Command.CAPTURE],
    Capability.BUTTON: [],
    Capability.BYPASSABLE: [],
    Capability.CAMERA_EVENT: [],
    Capability.CAMERA_PRESET: [
        Command.CREATE,
        Command.DELETE,
        Command.EXECUTE,
        Command.UPDATE,
    ],
    Capability.CARBON_DIOXIDE_HEALTH_CONCERN: [],
    Capability.CARBON_DIOXIDE_MEASUREMENT: [],
    Capability.CARBON_MONOXIDE_DETECTOR: [],
    Capability.CARBON_MONOXIDE_HEALTH_CONCERN: [],
    Capability.CARBON_MONOXIDE_MEASUREMENT: [],
    Capability.CHARGE_POINT_STATE: [],
    Capability.CHARGING_STATE: [],
    Capability.CHIME: [Command.CHIME, Command.OFF],
    Capability.COLOR: [Command.SET_COLOR_VALUE],
    Capability.COLOR_CONTROL: [
        Command.SET_COLOR,
        Command.SET_HUE,
        Command.SET_SATURATION,
    ],
    Capability.COLOR_MODE: [],
    Capability.COLOR_TEMPERATURE: [Command.SET_COLOR_TEMPERATURE],
    Capability.CONFIGURATION: [Command.CONFIGURE],
    Capability.CONSUMABLE: [],
    Capability.CONSUMABLE_LIFE: [Command.RESET],
    Capability.CONTACT_SENSOR: [],
    Capability.CONTAINER_STATE: [],
    Capability.COOK_TIME: [Command.SET_COOK_TIME],
    Capability.CURRENT_MEASUREMENT: [],
    Capability.DELIVERY_ROBOT_CALL: [Command.CALL, Command.CANCEL],
    Capability.DEMAND_RESPONSE_LOAD_CONTROL: [
        Command.OVERRIDE_DEMAND_RESPONSE_LOAD_CONTROL_ACTION,
        Command.REQUEST_DEMAND_RESPONSE_LOAD_CONTROL_ACTION,
    ],
    Capability.DEW_POINT: [],
    Capability.DISHWASHER_MODE: [Command.SET_DISHWASHER_MODE],
    Capability.DISHWASHER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.DISHWASHER_OPERATIONAL_STATE: [Command.SET_MACHINE_STATE],
    Capability.DOOR_CONTROL: [Command.CLOSE, Command.OPEN],
    Capability.DRIVING_STATUS: [],
    Capability.DRYER_MODE: [Command.SET_DRYER_MODE],
    Capability.DRYER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.DUST_HEALTH_CONCERN: [],
    Capability.DUST_SENSOR: [],
    Capability.ELEVATOR_CALL: [Command.CALL],
    Capability.END_TO_END_ENCRYPTION: [Command.ENCRYPT_KEK, Command.GENERATE_NONCE],
    Capability.ENERGY_METER: [Command.RESET_ENERGY_METER],
    Capability.EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT: [],
    Capability.ESTIMATED_TIME_OF_ARRIVAL: [],
    Capability.EVSE_CHARGING_SESSION: [
        Command.DISABLE_CHARGING,
        Command.ENABLE_CHARGING,
        Command.SET_MAX_CURRENT,
        Command.SET_MIN_CURRENT,
        Command.SET_TARGET_END_TIME,
    ],
    Capability.EVSE_STATE: [],
    Capability.EXECUTE: [Command.EXECUTE],
    Capability.FACE_RECOGNITION: [],
    Capability.FAN_MODE: [Command.SET_FAN_MODE],
    Capability.FAN_OSCILLATION_MODE: [Command.SET_FAN_OSCILLATION_MODE],
    Capability.FAN_SPEED: [Command.SET_FAN_SPEED],
    Capability.FAN_SPEED_PERCENT: [Command.SET_PERCENT],
    Capability.FEEDER_OPERATING_STATE: [Command.START_FEEDING],
    Capability.FEEDER_PORTION: [Command.SET_PORTION],
    Capability.FILTER_STATE: [Command.RESET_FILTER],
    Capability.FILTER_STATUS: [],
    Capability.FINE_DUST_HEALTH_CONCERN: [],
    Capability.FINE_DUST_SENSOR: [],
    Capability.FIRMWARE_UPDATE: [
        Command.CHECK_FOR_FIRMWARE_UPDATE,
        Command.UPDATE_FIRMWARE,
    ],
    Capability.FLOW_MEASUREMENT: [],
    Capability.FORMALDEHYDE_HEALTH_CONCERN: [],
    Capability.FORMALDEHYDE_MEASUREMENT: [],
    Capability.GARAGE_DOOR_CONTROL: [Command.CLOSE, Command.OPEN],
    Capability.GAS_CONSUMPTION_REPORT: [],
    Capability.GAS_DETECTOR: [],
    Capability.GAS_METER: [],
    Capability.GEOFENCE: [
        Command.SET_ENABLE_STATE,
        Command.SET_GEOFENCE,
        Command.SET_NAME,
    ],
    Capability.GEOFENCES: [],
    Capability.GEOLOCATION: [],
    Capability.GRID_STATE: [],
    Capability.HARDWARE_FAULT: [],
    Capability.HEALTH_CHECK: [Command.PING],
    Capability.HOLDABLE_BUTTON: [],
    Capability.HUMIDIFIER_MODE: [Command.SET_HUMIDIFIER_MODE],
    Capability.ILLUMINANCE_MEASUREMENT: [],
    Capability.IMAGE_CAPTURE: [
        Command.TAKE,
        Command.UPLOAD_COMPLETE,
        Command.UPLOAD_FAILED,
    ],
    Capability.INDICATOR: [
        Command.INDICATOR_NEVER,
        Command.INDICATOR_WHEN_OFF,
        Command.INDICATOR_WHEN_ON,
    ],
    Capability.INFRARED_LEVEL: [Command.SET_INFRARED_LEVEL],
    Capability.KEYPAD_INPUT: [Command.SEND_KEY],
    Capability.LANGUAGE_SETTING: [Command.SET_LANGUAGE],
    Capability.LAUNDRY_WASHER_RINSE_MODE: [Command.SET_RINSE_MODE],
    Capability.LAUNDRY_WASHER_SPIN_SPEED: [Command.SET_SPIN_SPEED],
    Capability.LEVEL: [Command.SET_LEVEL],
    Capability.LIGHT: [Command.OFF, Command.ON],
    Capability.LIGHT_CONTROLLER_MODE: [Command.SET_LIGHT_CONTROLLER_MODE],
    Capability.LOCATION_MODE: [Command.SET_MODE],
    Capability.LOCK: [Command.LOCK, Command.UNLATCH, Command.UNLOCK],
    Capability.LOCK_ALARM: [],
    Capability.LOCK_CODES: [
        Command.DELETE_CODE,
        Command.LOCK,
        Command.NAME_SLOT,
        Command.RELOAD_ALL_CODES,
        Command.REQUEST_CODE,
        Command.SET_CODE,
        Command.SET_CODE_LENGTH,
        Command.UNLOCK,
        Command.UNLOCK_WITH_TIMEOUT,
        Command.UPDATE_CODES,
    ],
    Capability.LOCK_CREDENTIALS: [
        Command.ADD_CREDENTIAL,
        Command.DELETE_ALL_CREDENTIALS,
        Command.DELETE_CREDENTIAL,
        Command.UPDATE_CREDENTIAL,
    ],
    Capability.LOCK_ONLY: [Command.LOCK],
    Capability.LOCK_SCHEDULES: [
        Command.CLEAR_WEEK_DAY_SCHEDULES,
        Command.CLEAR_YEAR_DAY_SCHEDULES,
        Command.SET_WEEK_DAY_SCHEDULE,
        Command.SET_YEAR_DAY_SCHEDULE,
    ],
    Capability.LOCK_USERS: [
        Command.ADD_USER,
        Command.DELETE_ALL_USERS,
        Command.DELETE_USER,
        Command.UPDATE_USER,
    ],
    Capability.LOG_TRIGGER: [
        Command.TRIGGER_LOG,
        Command.TRIGGER_LOG_WITH_LOG_INFO,
        Command.TRIGGER_LOG_WITH_URL,
    ],
    Capability.MASSAGE_INTENSITY_CHANGE: [Command.NEXT_INTENSITY],
    Capability.MASSAGE_INTENSITY_CONTROL: [
        Command.SET_INTENSITY_FOOT,
        Command.SET_INTENSITY_HEAD,
        Command.SET_INTENSITY_WHOLE,
    ],
    Capability.MASSAGE_OPERATING: [Command.START, Command.STOP],
    Capability.MASSAGE_OPERATING_STATE: [],
    Capability.MASSAGE_TIME_CHANGE: [Command.NEXT_TIME],
    Capability.MASSAGE_TIME_CONTROL: [Command.SET_TIME],
    Capability.MEDIA_CONTROLLER: [Command.START_ACTIVITY],
    Capability.MEDIA_GROUP: [
        Command.GROUP_VOLUME_DOWN,
        Command.GROUP_VOLUME_UP,
        Command.MUTE_GROUP,
        Command.SET_GROUP_MUTE,
        Command.SET_GROUP_VOLUME,
        Command.UNMUTE_GROUP,
    ],
    Capability.MEDIA_INPUT_SOURCE: [Command.SET_INPUT_SOURCE],
    Capability.MEDIA_PLAYBACK: [
        Command.FAST_FORWARD,
        Command.PAUSE,
        Command.PLAY,
        Command.REWIND,
        Command.SET_PLAYBACK_STATUS,
        Command.STOP,
    ],
    Capability.MEDIA_PLAYBACK_REPEAT: [Command.SET_PLAYBACK_REPEAT_MODE],
    Capability.MEDIA_PLAYBACK_SHUFFLE: [Command.SET_PLAYBACK_SHUFFLE],
    Capability.MEDIA_PRESETS: [Command.PLAY_PRESET],
    Capability.MEDIA_TRACK_CONTROL: [Command.NEXT_TRACK, Command.PREVIOUS_TRACK],
    Capability.MODE: [Command.SET_MODE],
    Capability.MOLD_HEALTH_CONCERN: [],
    Capability.MOMENTARY: [Command.PUSH],
    Capability.MOTION_BED: [Command.SET_MODE, Command.START, Command.STOP],
    Capability.MOTION_SENSOR: [],
    Capability.MOVEMENT_SENSOR: [],
    Capability.MULTIPLE_ZONE_PRESENCE: [
        Command.CREATE_ZONE,
        Command.DELETE_ZONE,
        Command.UPDATE_ZONE_NAME,
    ],
    Capability.MUSIC_PLAYER: [
        Command.MUTE,
        Command.NEXT_TRACK,
        Command.PAUSE,
        Command.PLAY,
        Command.PLAY_TRACK,
        Command.PREVIOUS_TRACK,
        Command.RESTORE_TRACK,
        Command.RESUME_TRACK,
        Command.SET_LEVEL,
        Command.SET_TRACK,
        Command.STOP,
        Command.UNMUTE,
    ],
    Capability.NETWORK_METER: [],
    Capability.NITROGEN_DIOXIDE_HEALTH_CONCERN: [],
    Capability.NITROGEN_DIOXIDE_MEASUREMENT: [],
    Capability.NOTIFICATION: [Command.DEVICE_NOTIFICATION],
    Capability.OBJECT_DETECTION: [],
    Capability.OCCUPANCY_SENSOR: [],
    Capability.OCF: [Command.POST_OCF_COMMAND],
    Capability.ODOR_SENSOR: [],
    Capability.OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.OPERATIONAL_STATE: [
        Command.PAUSE,
        Command.RESUME,
        Command.START,
        Command.STOP,
    ],
    Capability.OUTLET: [Command.OFF, Command.ON],
    Capability.OVEN_MODE: [Command.SET_OVEN_MODE],
    Capability.OVEN_OPERATING_STATE: [
        Command.SET_MACHINE_STATE,
        Command.START,
        Command.STOP,
    ],
    Capability.OVEN_OPERATIONAL_STATE: [Command.SET_MACHINE_STATE, Command.STOP],
    Capability.OVEN_SETPOINT: [Command.SET_OVEN_SETPOINT],
    Capability.OZONE_HEALTH_CONCERN: [],
    Capability.OZONE_MEASUREMENT: [],
    Capability.PH_MEASUREMENT: [],
    Capability.PANIC_ALARM: [],
    Capability.PEST_CONTROL: [],
    Capability.PET_ACTIVITY: [],
    Capability.POLLING: [Command.POLL],
    Capability.POWER_CONSUMPTION_REPORT: [],
    Capability.POWER_METER: [],
    Capability.POWER_SOURCE: [],
    Capability.PRECIPITATION_MEASUREMENT: [Command.RESET_PRECIPITATION_LEVEL],
    Capability.PRECIPITATION_RATE: [],
    Capability.PRECIPITATION_SENSOR: [],
    Capability.PRESENCE_SENSOR: [],
    Capability.PUMP_CONTROL_MODE: [Command.SET_CONTROL_MODE],
    Capability.PUMP_OPERATION_MODE: [Command.SET_OPERATION_MODE],
    Capability.RADON_HEALTH_CONCERN: [],
    Capability.RADON_MEASUREMENT: [],
    Capability.RAIN_SENSOR: [],
    Capability.RAPID_COOLING: [Command.SET_RAPID_COOLING],
    Capability.REFRESH: [Command.REFRESH],
    Capability.REFRIGERATION: [
        Command.SET_DEFROST,
        Command.SET_RAPID_COOLING,
        Command.SET_RAPID_FREEZING,
    ],
    Capability.REFRIGERATION_SETPOINT: [Command.SET_REFRIGERATION_SETPOINT],
    Capability.RELATIVE_BRIGHTNESS: [],
    Capability.RELATIVE_HUMIDITY_MEASUREMENT: [],
    Capability.RELAY_SWITCH: [Command.OFF, Command.ON],
    Capability.REMOTE_CONTROL_STATUS: [],
    Capability.RICE_COOKER: [
        Command.SCHEDULE_COOKING,
        Command.SET_MODE,
        Command.START_COOKING,
        Command.STOP,
    ],
    Capability.ROBOT_CLEANER_CLEANING_MODE: [Command.SET_ROBOT_CLEANER_CLEANING_MODE],
    Capability.ROBOT_CLEANER_MOVEMENT: [Command.SET_ROBOT_CLEANER_MOVEMENT],
    Capability.ROBOT_CLEANER_OPERATING_STATE: [
        Command.GO_HOME,
        Command.PAUSE,
        Command.START,
    ],
    Capability.ROBOT_CLEANER_STATE: [
        Command.SET_ROBOT_CLEANER_CLEANING_STATE,
        Command.SET_ROBOT_CLEANER_CONTROL_STATE,
        Command.SET_ROBOT_CLEANER_TURBO_STATE,
        Command.STOP,
    ],
    Capability.ROBOT_CLEANER_TURBO_MODE: [Command.SET_ROBOT_CLEANER_TURBO_MODE],
    Capability.SAMSUNG_T_V: [
        Command.MUTE,
        Command.OFF,
        Command.ON,
        Command.SET_PICTURE_MODE,
        Command.SET_SOUND_MODE,
        Command.SET_VOLUME,
        Command.SHOW_MESSAGE,
        Command.UNMUTE,
        Command.VOLUME_DOWN,
        Command.VOLUME_UP,
    ],
    Capability.SCENE_ACTIVITY: [],
    Capability.SCENES: [Command.SET_SCENE],
    Capability.SCENT: [Command.SET_SCENT_INTENSITY],
    Capability.SECURITY_SYSTEM: [Command.ARM_AWAY, Command.ARM_STAY, Command.DISARM],
    Capability.SENSOR: [],
    Capability.SERVICE_AREA: [Command.SELECT_AREAS],
    Capability.SHOCK_SENSOR: [],
    Capability.SIGNAL_STRENGTH: [],
    Capability.SLEEP_SENSOR: [],
    Capability.SMOKE_DETECTOR: [],
    Capability.SOUND_DETECTION: [
        Command.DISABLE_SOUND_DETECTION,
        Command.ENABLE_SOUND_DETECTION,
    ],
    Capability.SOUND_PRESSURE_LEVEL: [],
    Capability.SOUND_SENSOR: [],
    Capability.SPEECH_RECOGNITION: [],
    Capability.SPEECH_SYNTHESIS: [Command.SPEAK],
    Capability.STATELESS_CUSTOM_BUTTON: [Command.SET_BUTTON],
    Capability.STATELESS_FANSPEED_BUTTON: [Command.SET_BUTTON],
    Capability.STATELESS_POWER_BUTTON: [Command.SET_BUTTON],
    Capability.STATELESS_POWER_TOGGLE_BUTTON: [Command.SET_BUTTON],
    Capability.STEP_SENSOR: [],
    Capability.SWITCH: [Command.OFF, Command.ON],
    Capability.SWITCH_LEVEL: [Command.SET_LEVEL],
    Capability.SWITCH_STATE: [],
    Capability.T_V: [
        Command.CHANNEL_DOWN,
        Command.CHANNEL_UP,
        Command.VOLUME_DOWN,
        Command.VOLUME_UP,
    ],
    Capability.TAMPER_ALERT: [],
    Capability.TEMPERATURE_ALARM: [],
    Capability.TEMPERATURE_LEVEL: [Command.SET_TEMPERATURE_LEVEL],
    Capability.TEMPERATURE_MEASUREMENT: [],
    Capability.TEMPERATURE_SETPOINT: [Command.SET_TEMPERATURE_SETPOINT],
    Capability.THERMOSTAT: [
        Command.AUTO,
        Command.COOL,
        Command.EMERGENCY_HEAT,
        Command.FAN_AUTO,
        Command.FAN_CIRCULATE,
        Command.FAN_ON,
        Command.HEAT,
        Command.OFF,
        Command.SET_COOLING_SETPOINT,
        Command.SET_HEATING_SETPOINT,
        Command.SET_SCHEDULE,
        Command.SET_THERMOSTAT_FAN_MODE,
        Command.SET_THERMOSTAT_MODE,
    ],
    Capability.THERMOSTAT_COOLING_SETPOINT: [Command.SET_COOLING_SETPOINT],
    Capability.THERMOSTAT_FAN_MODE: [
        Command.FAN_AUTO,
        Command.FAN_CIRCULATE,
        Command.FAN_ON,
        Command.SET_THERMOSTAT_FAN_MODE,
    ],
    Capability.THERMOSTAT_HEATING_SETPOINT: [Command.SET_HEATING_SETPOINT],
    Capability.THERMOSTAT_MODE: [
        Command.AUTO,
        Command.COOL,
        Command.EMERGENCY_HEAT,
        Command.HEAT,
        Command.OFF,
        Command.SET_THERMOSTAT_MODE,
    ],
    Capability.THERMOSTAT_OPERATING_STATE: [],
    Capability.THERMOSTAT_SCHEDULE: [Command.SET_SCHEDULE],
    Capability.THERMOSTAT_SETPOINT: [],
    Capability.THERMOSTAT_WATER_HEATING_SETPOINT: [Command.SET_HEATING_SETPOINT],
    Capability.THREE_AXIS: [],
    Capability.TIMED_SESSION: [
        Command.CANCEL,
        Command.PAUSE,
        Command.SET_COMPLETION_TIME,
        Command.START,
        Command.STOP,
    ],
    Capability.TONE: [Command.BEEP],
    Capability.TOUCH_SENSOR: [],
    Capability.TV_CHANNEL: [
        Command.CHANNEL_DOWN,
        Command.CHANNEL_UP,
        Command.SET_TV_CHANNEL,
        Command.SET_TV_CHANNEL_NAME,
    ],
    Capability.TVOC_HEALTH_CONCERN: [],
    Capability.TVOC_MEASUREMENT: [],
    Capability.ULTRAVIOLET_INDEX: [],
    Capability.VALVE: [Command.CLOSE, Command.OPEN],
    Capability.VEHICLE_ENGINE: [Command.START_ENGINE, Command.STOP_ENGINE],
    Capability.VEHICLE_FUEL_LEVEL: [],
    Capability.VEHICLE_INFORMATION: [],
    Capability.VEHICLE_ODOMETER: [],
    Capability.VEHICLE_RANGE: [],
    Capability.VEHICLE_TIRE_PRESSURE_MONITOR: [],
    Capability.VERY_FINE_DUST_HEALTH_CONCERN: [],
    Capability.VERY_FINE_DUST_SENSOR: [],
    Capability.VIDEO_CAMERA: [
        Command.FLIP,
        Command.MUTE,
        Command.OFF,
        Command.ON,
        Command.UNMUTE,
    ],
    Capability.VIDEO_CAPTURE: [Command.CAPTURE],
    Capability.VIDEO_CAPTURE2: [
        Command.CAPTURE,
        Command.STOP_CAPTURE,
        Command.UPLOAD_COMPLETE,
        Command.UPLOAD_FAILED,
    ],
    Capability.VIDEO_CLIPS: [Command.CAPTURE_CLIP],
    Capability.VIDEO_STREAM: [Command.START_STREAM, Command.STOP_STREAM],
    Capability.VOLTAGE_MEASUREMENT: [],
    Capability.WASHER_MODE: [Command.SET_WASHER_MODE],
    Capability.WASHER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.WASHER_OPERATIONAL_STATE: [Command.SET_MACHINE_STATE],
    Capability.WATER_FLOW_ALARM: [],
    Capability.WATER_METER: [],
    Capability.WATER_PRESSURE_MEASUREMENT: [],
    Capability.WATER_SENSOR: [],
    Capability.WATER_TEMPERATURE_MEASUREMENT: [],
    Capability.WATER_USAGE_METER: [],
    Capability.WEBRTC: [
        Command.CLIENT_ICE,
        Command.END,
        Command.REQUEST_TURN_INFO,
        Command.SDP_OFFER,
        Command.START_TALKBACK,
        Command.STOP_TALKBACK,
    ],
    Capability.WIFI_MESH_ROUTER: [
        Command.DISABLE_WIFI_GUEST_NETWORK,
        Command.DISABLE_WIFI_NETWORK,
        Command.ENABLE_WIFI_GUEST_NETWORK,
        Command.ENABLE_WIFI_NETWORK,
    ],
    Capability.WIND_MODE: [Command.SET_WIND_MODE],
    Capability.WIND_SPEED: [],
    Capability.WINDOW_SHADE: [Command.CLOSE, Command.OPEN, Command.PAUSE],
    Capability.WINDOW_SHADE_LEVEL: [Command.SET_SHADE_LEVEL],
    Capability.WINDOW_SHADE_PRESET: [Command.PRESET_POSITION],
    Capability.WINDOW_SHADE_TILT_LEVEL: [Command.SET_SHADE_TILT_LEVEL],
    Capability.WIRELESS_OPERATING_MODE: [Command.SET_WIRELESS_OPERATING_MODE],
    Capability.ZWAVE_MULTICHANNEL: [Command.ENABLE_EP_EVENTS, Command.EP_CMD],
    Capability.CUSTOM_ACCESSIBILITY: [Command.SET_ACCESSIBILITY],
    Capability.CUSTOM_AIR_CONDITIONER_ODOR_CONTROLLER: [
        Command.SET_AIR_CONDITIONER_ODOR_CONTROLLER_STATE
    ],
    Capability.CUSTOM_AIR_CONDITIONER_OPTIONAL_MODE: [Command.SET_AC_OPTIONAL_MODE],
    Capability.CUSTOM_AIR_CONDITIONER_TROPICAL_NIGHT_MODE: [
        Command.SET_AC_TROPICAL_NIGHT_MODE_LEVEL
    ],
    Capability.CUSTOM_AIR_PURIFIER_OPERATION_MODE: [Command.SET_AP_OPERATION_MODE],
    Capability.CUSTOM_AIR_QUALITY_MAX_LEVEL: [],
    Capability.CUSTOM_AUTO_CLEANING_MODE: [
        Command.SET_AUTO_CLEANING_MODE,
        Command.SET_OPERATING_STATE,
        Command.SET_TIMED_CLEAN_DURATION,
        Command.START,
        Command.STOP,
    ],
    Capability.CUSTOM_COOKTOP_OPERATING_STATE: [],
    Capability.CUSTOM_DEODOR_FILTER: [Command.RESET_DEODOR_FILTER],
    Capability.CUSTOM_DEVICE_DEPENDENCY_STATUS: [],
    Capability.CUSTOM_DEVICE_REPORT_STATE_CONFIGURATION: [
        Command.SET_REPORT_STATE_PERIOD,
        Command.SET_REPORT_STATE_REALTIME,
        Command.SET_REPORT_STATE_REALTIME_PERIOD,
    ],
    Capability.CUSTOM_DISABLED_CAPABILITIES: [],
    Capability.CUSTOM_DISABLED_COMPONENTS: [],
    Capability.CUSTOM_DISHWASHER_DELAY_START_TIME: [
        Command.SET_DISHWASHER_DELAY_START_TIME
    ],
    Capability.CUSTOM_DISHWASHER_OPERATING_PERCENTAGE: [],
    Capability.CUSTOM_DISHWASHER_OPERATING_PROGRESS: [],
    Capability.CUSTOM_DO_NOT_DISTURB_MODE: [
        Command.DO_NOT_DISTURB_OFF,
        Command.DO_NOT_DISTURB_ON,
        Command.SET_DO_NOT_DISTURB_MODE,
    ],
    Capability.CUSTOM_DRYER_DRY_LEVEL: [Command.SET_DRYER_DRY_LEVEL],
    Capability.CUSTOM_DRYER_WRINKLE_PREVENT: [Command.SET_DRYER_WRINKLE_PREVENT],
    Capability.CUSTOM_DUST_FILTER: [Command.RESET_DUST_FILTER],
    Capability.CUSTOM_ELECTRIC_HEPA_FILTER: [Command.RESET_ELECTRIC_HEPA_FILTER],
    Capability.CUSTOM_ENERGY_TYPE: [Command.SET_ENERGY_SAVING_LEVEL],
    Capability.CUSTOM_ERROR: [Command.SET_ERROR],
    Capability.CUSTOM_FILTER_USAGE_TIME: [Command.RESET_FILTER_USAGE_TIME],
    Capability.CUSTOM_FRIDGE_MODE: [Command.SET_FRIDGE_MODE],
    Capability.CUSTOM_HEPA_FILTER: [Command.RESET_HEPA_FILTER],
    Capability.CUSTOM_JOB_BEGINNING_STATUS: [],
    Capability.CUSTOM_LAUNCH_APP: [Command.LAUNCH_APP],
    Capability.CUSTOM_LOWER_DEVICE_POWER: [Command.SET_POWER_STATE],
    Capability.CUSTOM_OCF_RESOURCE_VERSION: [],
    Capability.CUSTOM_OUTING_MODE: [Command.SET_OUTING_MODE],
    Capability.CUSTOM_OVEN_CAVITY_STATUS: [],
    Capability.CUSTOM_PERIODIC_SENSING: [
        Command.PERIODIC_SENSING_OFF,
        Command.PERIODIC_SENSING_ON,
        Command.SET_AUTOMATIC_EXECUTION_MODE,
        Command.SET_AUTOMATIC_EXECUTION_SETTING,
        Command.SET_PERIODIC_SENSING,
        Command.SET_PERIODIC_SENSING_INTERVAL,
        Command.TRIGGER_MANUAL_SENSING,
    ],
    Capability.CUSTOM_PICTURE_MODE: [Command.SET_PICTURE_MODE],
    Capability.CUSTOM_RECORDING: [Command.RECORD_START, Command.RECORD_STOP],
    Capability.CUSTOM_SOUND_MODE: [Command.SET_SOUND_MODE],
    Capability.CUSTOM_SPI_MODE: [Command.SET_SPI_MODE],
    Capability.CUSTOM_STEAM_CLOSET_OPERATING_STATE: [
        Command.SET_STEAM_CLOSET_DELAY_END_TIME,
        Command.SET_STEAM_CLOSET_MACHINE_STATE,
    ],
    Capability.CUSTOM_STEAM_CLOSET_WRINKLE_PREVENT: [
        Command.SET_STEAM_CLOSET_WRINKLE_PREVENT
    ],
    Capability.CUSTOM_SUPPORTED_OPTIONS: [Command.SET_COURSE],
    Capability.CUSTOM_THERMOSTAT_SETPOINT_CONTROL: [
        Command.LOWER_SETPOINT,
        Command.RAISE_SETPOINT,
    ],
    Capability.CUSTOM_TV_SEARCH: [Command.SEARCH],
    Capability.CUSTOM_USER_NOTIFICATION: [],
    Capability.CUSTOM_VERY_FINE_DUST_FILTER: [Command.RESET_VERY_FINE_DUST_FILTER],
    Capability.CUSTOM_VIRUS_DOCTOR_MODE: [Command.SET_VIRUS_DOCTOR_MODE],
    Capability.CUSTOM_WASHER_AUTO_DETERGENT: [Command.SET_WASHER_AUTO_DETERGENT],
    Capability.CUSTOM_WASHER_AUTO_SOFTENER: [Command.SET_WASHER_AUTO_SOFTENER],
    Capability.CUSTOM_WASHER_RINSE_CYCLES: [Command.SET_WASHER_RINSE_CYCLES],
    Capability.CUSTOM_WASHER_SOIL_LEVEL: [Command.SET_WASHER_SOIL_LEVEL],
    Capability.CUSTOM_WASHER_SPIN_LEVEL: [Command.SET_WASHER_SPIN_LEVEL],
    Capability.CUSTOM_WASHER_WATER_TEMPERATURE: [Command.SET_WASHER_WATER_TEMPERATURE],
    Capability.CUSTOM_WATER_FILTER: [Command.RESET_WATER_FILTER],
    Capability.CUSTOM_WELCOME_CARE_MODE: [Command.TURN_WELCOME_CARE_ON],
    Capability.SAMSUNG_CE_ACTIVATION_STATE: [],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_AUDIO_FEEDBACK: [Command.SET_VOLUME_LEVEL],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_BEEP: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_DISPLAY: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_LIGHTING: [
        Command.OFF,
        Command.ON,
        Command.SET_LIGHTING_LEVEL,
    ],
    Capability.SAMSUNG_CE_AIR_QUALITY_HEALTH_CONCERN: [],
    Capability.SAMSUNG_CE_ALWAYS_ON_SENSING: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_AUDIO_VOLUME_LEVEL: [
        Command.SET_VOLUME_LEVEL,
        Command.VOLUME_DOWN,
        Command.VOLUME_UP,
    ],
    Capability.SAMSUNG_CE_AUTO_DISPENSE_DETERGENT: [
        Command.SET_AMOUNT,
        Command.SET_DENSITY,
        Command.SET_RECOMMENDED_AMOUNT,
        Command.SET_TYPE,
        Command.UNSET_RECOMMENDED_AMOUNT,
    ],
    Capability.SAMSUNG_CE_AUTO_DISPENSE_SOFTENER: [
        Command.SET_AMOUNT,
        Command.SET_DENSITY,
    ],
    Capability.SAMSUNG_CE_AUTO_DOOR_RELEASE: [Command.DISABLE, Command.ENABLE],
    Capability.SAMSUNG_CE_AUTO_VENTILATION: [Command.ACTION],
    Capability.SAMSUNG_CE_BURNER_INFO: [],
    Capability.SAMSUNG_CE_BUTTON_DISPLAY_CONDITION: [],
    Capability.SAMSUNG_CE_CAMERA_STREAMING: [
        Command.CANCEL_ONBOARDING,
        Command.REGISTER,
    ],
    Capability.SAMSUNG_CE_CLEAN_STATION_STICK_STATUS: [],
    Capability.SAMSUNG_CE_CLEAN_STATION_UV_CLEANING: [],
    Capability.SAMSUNG_CE_CLOTHING_EXTRA_CARE: [
        Command.SET_OPERATION_MODE,
        Command.SET_USER_LOCATION,
    ],
    Capability.SAMSUNG_CE_COFFEE_BREWING_RECIPE: [Command.SET_COFFEE_BREWING_RECIPE],
    Capability.SAMSUNG_CE_CONNECTION_STATE: [],
    Capability.SAMSUNG_CE_CONSUMED_ENERGY: [Command.SET_TIME_OFFSET],
    Capability.SAMSUNG_CE_COOK_RECIPE: [Command.SET_COOK_RECIPE],
    Capability.SAMSUNG_CE_COOKTOP_BURNER_MODE: [],
    Capability.SAMSUNG_CE_COOKTOP_COOK_RECIPE: [Command.SET_COOKTOP_COOK_RECIPE],
    Capability.SAMSUNG_CE_COOKTOP_FLEX_ZONE: [],
    Capability.SAMSUNG_CE_COOKTOP_HEATING_POWER: [],
    Capability.SAMSUNG_CE_COOKTOP_PAN_DETECTION: [],
    Capability.SAMSUNG_CE_COUNT_DOWN_TIMER: [
        Command.CANCEL,
        Command.PAUSE,
        Command.RESUME,
        Command.SET_START_VALUE,
        Command.START,
    ],
    Capability.SAMSUNG_CE_CUSTOM_RECIPE: [Command.COOK_CUSTOM_RECIPE],
    Capability.SAMSUNG_CE_DDMS_MODE: [],
    Capability.SAMSUNG_CE_DEFINED_RECIPE: [
        Command.COOK_DEFINED_RECIPE,
        Command.SET_DEFINED_RECIPE,
    ],
    Capability.SAMSUNG_CE_DEHUMIDIFIER_BEEP: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_DEHUMIDIFIER_MODE: [Command.SET_DEHUMIDIFIER_MODE],
    Capability.SAMSUNG_CE_DETERGENT_AUTO_REPLENISHMENT: [
        Command.DISABLE_ALARM,
        Command.ENABLE_ALARM,
        Command.SET_AUTO_REPLENISHMENT,
        Command.SET_DOSAGE,
        Command.SET_INITIAL_AMOUNT,
        Command.SET_ORDER_THRESHOLD,
        Command.SET_REMAINING_AMOUNT,
        Command.SET_TYPE,
    ],
    Capability.SAMSUNG_CE_DETERGENT_ORDER: [
        Command.DISABLE_ALARM,
        Command.ENABLE_ALARM,
        Command.SET_ORDER_THRESHOLD,
    ],
    Capability.SAMSUNG_CE_DETERGENT_STATE: [
        Command.SET_DETERGENT_TYPE,
        Command.SET_DOSAGE,
        Command.SET_INITIAL_AMOUNT,
        Command.SET_REMAINING_AMOUNT,
    ],
    Capability.SAMSUNG_CE_DEVICE_IDENTIFICATION: [],
    Capability.SAMSUNG_CE_DISHWASHER_JOB_STATE: [],
    Capability.SAMSUNG_CE_DISHWASHER_OPERATION: [
        Command.CANCEL,
        Command.PAUSE,
        Command.RESUME,
        Command.SET_OPERATING_STATE,
        Command.START,
        Command.START_LATER,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_COURSE: [
        Command.SET_CUSTOM_COURSE,
        Command.SET_WASHING_COURSE,
        Command.START_WASHING_COURSE,
        Command.START_WASHING_COURSE_WITH_OPTIONS,
    ],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_COURSE_DETAILS: [],
    Capability.SAMSUNG_CE_DISHWASHER_WASHING_OPTIONS: [
        Command.SET_ADD_RINSE,
        Command.SET_DRY_PLUS,
        Command.SET_HEATED_DRY,
        Command.SET_HIGH_TEMP_WASH,
        Command.SET_HOT_AIR_DRY,
        Command.SET_OPTIONS,
        Command.SET_RINSE_PLUS,
        Command.SET_SANITIZE,
        Command.SET_SANITIZING_WASH,
        Command.SET_SELECTED_ZONE,
        Command.SET_SPEED_BOOSTER,
        Command.SET_STEAM_SOAK,
        Command.SET_STORM_WASH,
        Command.SET_ZONE_BOOSTER,
    ],
    Capability.SAMSUNG_CE_DO_NOT_DISTURB: [
        Command.ACTIVATE,
        Command.DEACTIVATE,
        Command.SET_DURATION,
    ],
    Capability.SAMSUNG_CE_DONGLE_SOFTWARE_INSTALLATION: [],
    Capability.SAMSUNG_CE_DOOR_STATE: [],
    Capability.SAMSUNG_CE_DRAIN_FILTER: [Command.RESET_DRAIN_FILTER],
    Capability.SAMSUNG_CE_DRIVER_STATE: [],
    Capability.SAMSUNG_CE_DRIVER_VERSION: [],
    Capability.SAMSUNG_CE_DRUM_SELF_CLEANING: [],
    Capability.SAMSUNG_CE_DRYER_AUTO_CYCLE_LINK: [
        Command.LINK_DRYER_CYCLE,
        Command.SET_DRYER_AUTO_CYCLE_LINK,
    ],
    Capability.SAMSUNG_CE_DRYER_CYCLE: [Command.SET_DRYER_CYCLE],
    Capability.SAMSUNG_CE_DRYER_CYCLE_PRESET: [
        Command.DELETE,
        Command.SET_DRYER_CYCLE_PRESET,
    ],
    Capability.SAMSUNG_CE_DRYER_DELAY_END: [Command.SET_DELAY_TIME],
    Capability.SAMSUNG_CE_DRYER_DRYING_TEMPERATURE: [Command.SET_DRYING_TEMPERATURE],
    Capability.SAMSUNG_CE_DRYER_DRYING_TIME: [Command.SET_DRYING_TIME],
    Capability.SAMSUNG_CE_DRYER_FREEZE_PREVENT: [],
    Capability.SAMSUNG_CE_DRYER_LABEL_SCAN_CYCLE_PRESET: [
        Command.DELETE,
        Command.SET_DRYER_LABEL_SCAN_CYCLE_PRESET,
    ],
    Capability.SAMSUNG_CE_DRYER_OPERATING_STATE: [
        Command.CANCEL,
        Command.PAUSE,
        Command.RESUME,
        Command.SET_DELAY_END,
        Command.START,
    ],
    Capability.SAMSUNG_CE_DUST_FILTER_ALARM: [Command.SET_ALARM_THRESHOLD],
    Capability.SAMSUNG_CE_EHS_BOOSTER_HEATER: [],
    Capability.SAMSUNG_CE_EHS_CYCLE_DATA: [],
    Capability.SAMSUNG_CE_EHS_DEFROST_MODE: [],
    Capability.SAMSUNG_CE_EHS_DIVERTER_VALVE: [],
    Capability.SAMSUNG_CE_EHS_FSV_SETTINGS: [Command.REFRESH, Command.SET_VALUE],
    Capability.SAMSUNG_CE_EHS_TEMPERATURE_REFERENCE: [],
    Capability.SAMSUNG_CE_EHS_THERMOSTAT: [],
    Capability.SAMSUNG_CE_ENERGY_PLANNER: [Command.SET_DATA, Command.SET_PLAN],
    Capability.SAMSUNG_CE_ERROR_AND_ALARM_STATE: [],
    Capability.SAMSUNG_CE_FLEXIBLE_AUTO_DISPENSE_DETERGENT: [
        Command.SET_AMOUNT,
        Command.SET_DENSITY,
        Command.SET_RECOMMENDED_AMOUNT,
        Command.SET_TYPE,
        Command.UNSET_RECOMMENDED_AMOUNT,
    ],
    Capability.SAMSUNG_CE_FOOD_DEFROST: [Command.SET_DEFROST],
    Capability.SAMSUNG_CE_FREEZER_CONVERT_MODE: [Command.SET_FREEZER_CONVERT_MODE],
    Capability.SAMSUNG_CE_FRIDGE_FOOD_LIST: [Command.REFRESH],
    Capability.SAMSUNG_CE_FRIDGE_PANTRY_INFO: [],
    Capability.SAMSUNG_CE_FRIDGE_PANTRY_MODE: [Command.SET_MODE],
    Capability.SAMSUNG_CE_FRIDGE_VACATION_MODE: [],
    Capability.SAMSUNG_CE_FRIDGE_WELCOME_LIGHTING: [
        Command.OFF,
        Command.ON,
        Command.SET_DETECTION_PROXIMITY,
    ],
    Capability.SAMSUNG_CE_HOOD_FAN_SPEED: [Command.SET_HOOD_FAN_SPEED],
    Capability.SAMSUNG_CE_HOOD_FILTER: [Command.RESET_HOOD_FILTER],
    Capability.SAMSUNG_CE_HOOD_LAMP_AUTOMATION: [
        Command.SET_CONDITION,
        Command.SET_SCHEDULE,
    ],
    Capability.SAMSUNG_CE_INDIVIDUAL_CONTROL_LOCK: [],
    Capability.SAMSUNG_CE_KIDS_LOCK: [],
    Capability.SAMSUNG_CE_KIDS_LOCK_CONTROL: [Command.LOCK, Command.UNLOCK],
    Capability.SAMSUNG_CE_KITCHEN_DEVICE_DEFAULTS: [],
    Capability.SAMSUNG_CE_KITCHEN_DEVICE_IDENTIFICATION: [],
    Capability.SAMSUNG_CE_KITCHEN_MODE_SPECIFICATION: [],
    Capability.SAMSUNG_CE_LAMP: [Command.SET_BRIGHTNESS_LEVEL],
    Capability.SAMSUNG_CE_MEAT_AGING: [
        Command.ADD_AGING,
        Command.CANCEL_AGING,
        Command.UPDATE_AGING,
    ],
    Capability.SAMSUNG_CE_MEAT_PROBE: [Command.SET_TEMPERATURE_SETPOINT],
    Capability.SAMSUNG_CE_MICROPHONE_SETTINGS: [Command.MUTE, Command.UNMUTE],
    Capability.SAMSUNG_CE_MICROWAVE_POWER: [Command.SET_POWER_LEVEL],
    Capability.SAMSUNG_CE_MUSIC_PLAYLIST: [Command.SET_PLAYLIST],
    Capability.SAMSUNG_CE_NOTIFICATION: [
        Command.SET_ACTION_SETTING,
        Command.SET_CONTENT_TEXT,
        Command.SET_CONTENT_TITLE,
        Command.SET_CONTEXTS,
    ],
    Capability.SAMSUNG_CE_OPERATION_ORIGIN: [Command.SET_OPERATION_ORIGIN],
    Capability.SAMSUNG_CE_OVEN_DRAINAGE_REQUIREMENT: [],
    Capability.SAMSUNG_CE_OVEN_MODE: [Command.SET_OVEN_MODE],
    Capability.SAMSUNG_CE_OVEN_OPERATING_STATE: [
        Command.PAUSE,
        Command.SET_OPERATION_TIME,
        Command.START,
        Command.STOP,
    ],
    Capability.SAMSUNG_CE_POWER_CONSUMPTION_RECORD: [],
    Capability.SAMSUNG_CE_POWER_COOL: [Command.ACTIVATE, Command.DEACTIVATE],
    Capability.SAMSUNG_CE_POWER_FREEZE: [Command.ACTIVATE, Command.DEACTIVATE],
    Capability.SAMSUNG_CE_QUICK_CONTROL: [],
    Capability.SAMSUNG_CE_RECHARGEABLE_BATTERY: [],
    Capability.SAMSUNG_CE_RELATIVE_HUMIDITY_LEVEL: [Command.SET_DESIRED_HUMIDITY],
    Capability.SAMSUNG_CE_REMOTE_MANAGEMENT_DATA: [Command.RM_COMMAND],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_AUDIO_CLIP: [Command.DISABLE, Command.ENABLE],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_AVP_REGISTRATION: [Command.REGISTER],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_CLEANING_MODE: [
        Command.DISABLE_REPEAT_MODE,
        Command.ENABLE_REPEAT_MODE,
        Command.SET_CLEANING_MODE,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_CLEANING_TYPE: [Command.SET_CLEANING_TYPE],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_DRIVING_MODE: [Command.SET_DRIVING_MODE],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_DUST_BAG: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_FEATURE_VISIBILITY: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_GUIDED_PATROL: [Command.START, Command.STOP],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_AREA_INFO: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_CLEANING_INFO: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_LIST: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_METADATA: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MONITORING_AUTOMATION: [
        Command.ENABLE_MONITORING_AUTOMATION
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MOTOR_FILTER: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_OPERATING_STATE: [
        Command.CANCEL_REMAINING_JOB,
        Command.PAUSE,
        Command.RESUME,
        Command.RETURN_TO_HOME,
        Command.SET_OPERATING_STATE,
        Command.START,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PATROL: [
        Command.DISABLE,
        Command.ENABLE,
        Command.SET_PATROL,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PET_CLEANING_SCHEDULE: [
        Command.DISABLE,
        Command.ENABLE,
        Command.SET_EXCLUDE_HOLIDAYS,
        Command.SET_SCHEDULE,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PET_MONITOR: [
        Command.DISABLE,
        Command.ENABLE,
        Command.SET_EXCLUDE_HOLIDAYS,
        Command.SET_MONITOR,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PET_MONITOR_REPORT: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_RELAY_CLEANING: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_RESERVATION: [
        Command.ADD_RESERVATION,
        Command.DELETE_RESERVATION,
        Command.DELETE_RESERVATIONS,
        Command.EDIT_RESERVATION,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_SAFETY_PATROL: [Command.START, Command.STOP],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_SYSTEM_SOUND_MODE: [Command.SET_SOUND_MODE],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_WATER_SPRAY_LEVEL: [
        Command.SET_WATER_SPRAY_LEVEL
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_WELCOME: [
        Command.SET_COORDINATES,
        Command.START,
    ],
    Capability.SAMSUNG_CE_RUNESTONE_HOME_CONTEXT: [
        Command.SET_CONTEXT,
        Command.SET_CONTEXT_SNAPSHOT,
        Command.SET_RECENTLY_USED_APPS,
    ],
    Capability.SAMSUNG_CE_SABBATH_MODE: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_SAC_DISPLAY_CONDITION: [],
    Capability.SAMSUNG_CE_SCALE_SETTINGS: [],
    Capability.SAMSUNG_CE_SELF_CHECK: [
        Command.CANCEL_SELF_CHECK,
        Command.START_SELF_CHECK,
    ],
    Capability.SAMSUNG_CE_SENSING_ON_SUSPEND_MODE: [],
    Capability.SAMSUNG_CE_SILENT_ACTION: [Command.ACT_SILENTLY],
    Capability.SAMSUNG_CE_SOFTENER_AUTO_REPLENISHMENT: [
        Command.DISABLE_ALARM,
        Command.ENABLE_ALARM,
        Command.SET_AUTO_REPLENISHMENT,
        Command.SET_DOSAGE,
        Command.SET_INITIAL_AMOUNT,
        Command.SET_ORDER_THRESHOLD,
        Command.SET_REMAINING_AMOUNT,
        Command.SET_TYPE,
    ],
    Capability.SAMSUNG_CE_SOFTENER_ORDER: [
        Command.DISABLE_ALARM,
        Command.ENABLE_ALARM,
        Command.SET_ORDER_THRESHOLD,
    ],
    Capability.SAMSUNG_CE_SOFTENER_STATE: [
        Command.SET_DOSAGE,
        Command.SET_INITIAL_AMOUNT,
        Command.SET_REMAINING_AMOUNT,
        Command.SET_SOFTENER_TYPE,
    ],
    Capability.SAMSUNG_CE_SOFTWARE_UPDATE: [
        Command.AGREE_UPDATE,
        Command.DISAGREE_UPDATE,
    ],
    Capability.SAMSUNG_CE_SOFTWARE_VERSION: [],
    Capability.SAMSUNG_CE_SOUND_DETECTION_SENSITIVITY: [Command.SET_LEVEL],
    Capability.SAMSUNG_CE_STEAM_CLOSET_AUTO_CYCLE_LINK: [
        Command.LINK_STEAM_CLOSET_CYCLE,
        Command.SET_STEAM_CLOSET_AUTO_CYCLE_LINK,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_CYCLE: [Command.SET_STEAM_CLOSET_CYCLE],
    Capability.SAMSUNG_CE_STEAM_CLOSET_CYCLE_PRESET: [
        Command.DELETE,
        Command.SET_STEAM_CLOSET_CYCLE_PRESET,
    ],
    Capability.SAMSUNG_CE_STEAM_CLOSET_DELAY_END: [Command.SET_DELAY_TIME],
    Capability.SAMSUNG_CE_STEAM_CLOSET_KEEP_FRESH_MODE: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_STEAM_CLOSET_SANITIZE_MODE: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_STICK_CLEANER_DUST_BAG: [Command.RESET],
    Capability.SAMSUNG_CE_STICK_CLEANER_DUSTBIN_STATUS: [
        Command.START_EMPTYING,
        Command.STOP_EMPTYING,
    ],
    Capability.SAMSUNG_CE_STICK_CLEANER_STATUS: [],
    Capability.SAMSUNG_CE_STICK_CLEANER_STICK_STATUS: [],
    Capability.SAMSUNG_CE_SURFACE_RESIDUAL_HEAT: [],
    Capability.SAMSUNG_CE_SYSTEM_AIR_CONDITIONER_RESERVATION: [],
    Capability.SAMSUNG_CE_TEMPERATURE_SETTING: [Command.SET_DESIRED_TEMPERATURE],
    Capability.SAMSUNG_CE_TOGGLE_SWITCH: [Command.OFF, Command.ON, Command.TOGGLE],
    Capability.SAMSUNG_CE_UNAVAILABLE_CAPABILITIES: [],
    Capability.SAMSUNG_CE_VIEW_INSIDE: [
        Command.REFRESH,
        Command.REFRESH_ALL,
        Command.REFRESH_SPECIFIC_AREA,
    ],
    Capability.SAMSUNG_CE_WASHER_BUBBLE_SOAK: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_WASHER_CYCLE: [Command.SET_WASHER_CYCLE],
    Capability.SAMSUNG_CE_WASHER_CYCLE_PRESET: [
        Command.DELETE,
        Command.SET_WASHER_CYCLE_PRESET,
    ],
    Capability.SAMSUNG_CE_WASHER_DELAY_END: [
        Command.REFRESH_MINIMUM_RESERVABLE_TIME,
        Command.SET_DELAY_TIME,
    ],
    Capability.SAMSUNG_CE_WASHER_FREEZE_PREVENT: [],
    Capability.SAMSUNG_CE_WASHER_LABEL_SCAN_CYCLE_PRESET: [
        Command.DELETE,
        Command.SET_WASHER_LABEL_SCAN_CYCLE_PRESET,
    ],
    Capability.SAMSUNG_CE_WASHER_OPERATING_STATE: [
        Command.CANCEL,
        Command.ESTIMATE_OPERATION_TIME,
        Command.PAUSE,
        Command.RESUME,
        Command.SET_DELAY_END,
        Command.START,
    ],
    Capability.SAMSUNG_CE_WASHER_WASHING_TIME: [Command.SET_WASHING_TIME],
    Capability.SAMSUNG_CE_WASHER_WATER_LEVEL: [Command.SET_WATER_LEVEL],
    Capability.SAMSUNG_CE_WASHER_WATER_VALVE: [Command.SET_WATER_VALVE],
    Capability.SAMSUNG_CE_WATER_CONSUMPTION_REPORT: [],
    Capability.SAMSUNG_CE_WATER_DISPENSER: [
        Command.SET_AMOUNT,
        Command.SET_HOT_TEMPERATURE,
        Command.SET_MODE,
    ],
    Capability.SAMSUNG_CE_WATER_PURIFIER_COLD_WATER_LOCK: [
        Command.LOCK,
        Command.UNLOCK,
    ],
    Capability.SAMSUNG_CE_WATER_PURIFIER_HOT_WATER_LOCK: [Command.LOCK, Command.UNLOCK],
    Capability.SAMSUNG_CE_WATER_PURIFIER_MEDICATION_MODE: [Command.SET_MEDICATION_MODE],
    Capability.SAMSUNG_CE_WATER_PURIFIER_OPERATING_STATE: [],
    Capability.SAMSUNG_CE_WATER_RESERVOIR: [],
    Capability.SAMSUNG_CE_WATER_STERILIZATION_OPERATING_STATE: [
        Command.START,
        Command.STOP,
    ],
    Capability.SAMSUNG_CE_WATER_STERILIZATION_SCHEDULE: [Command.SET_START_TIME],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT: [],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT_CALIBRATION: [Command.ZERO_CALIBRATE],
    Capability.SAMSUNG_CE_WELCOME_COOLING: [Command.START],
    Capability.SAMSUNG_CE_WELCOME_HUMIDITY: [Command.START],
    Capability.SAMSUNG_CE_WELCOME_MESSAGE: [
        Command.DELETE_WELCOME_MESSAGE,
        Command.SET_WELCOME_MESSAGE,
    ],
    Capability.SAMSUNG_CE_WIFI_KIT_SUB_DEVICES: [],
    Capability.SAMSUNG_VD_AI_ACTION: [Command.SEND_CONTENT],
    Capability.SAMSUNG_VD_AMBIENT: [Command.SET_AMBIENT_ON],
    Capability.SAMSUNG_VD_AMBIENT18: [Command.SET_AMBIENT_ON],
    Capability.SAMSUNG_VD_AMBIENT_CONTENT: [Command.SET_AMBIENT_CONTENT],
    Capability.SAMSUNG_VD_AUDIO_GROUP_INFO: [],
    Capability.SAMSUNG_VD_AUDIO_INPUT_SOURCE: [Command.SET_NEXT_INPUT_SOURCE],
    Capability.SAMSUNG_VD_DEVICE_CATEGORY: [],
    Capability.SAMSUNG_VD_FIRMWARE_VERSION: [Command.SET_FIRMWARE_VERSION],
    Capability.SAMSUNG_VD_GROUP_INFO: [],
    Capability.SAMSUNG_VD_LIGHT_CONTROL: [Command.SET_LIGHT_CONTROL_MODE],
    Capability.SAMSUNG_VD_MEDIA_INPUT_SOURCE: [Command.SET_INPUT_SOURCE],
    Capability.SAMSUNG_VD_PICTURE_MODE: [Command.SET_PICTURE_MODE],
    Capability.SAMSUNG_VD_REMOTE_CONTROL: [Command.SEND],
    Capability.SAMSUNG_VD_SOUND_DETECTION: [],
    Capability.SAMSUNG_VD_SOUND_FROM: [Command.SET_SOUND_FROM],
    Capability.SAMSUNG_VD_SOUND_MODE: [Command.SET_SOUND_MODE],
    Capability.SAMSUNG_VD_SUPPORTS_FEATURES: [],
    Capability.SAMSUNG_VD_SUPPORTS_POWER_ON_BY_OCF: [],
    Capability.SAMSUNG_VD_THING_STATUS: [],
    Capability.SAMSUNG_IM_ANNOUNCEMENT: [Command.ANNOUNCE, Command.SET_ENABLE_STATE],
    Capability.SAMSUNG_IM_BIXBY_CONTENT: [Command.BIXBY_COMMAND],
    Capability.SAMSUNG_IM_CHARGER_FIRMWARE: [],
    Capability.SAMSUNG_IM_CHARGING_STATUS: [],
    Capability.SAMSUNG_IM_DEVICESTATUS: [],
    Capability.SAMSUNG_IM_FIND_NODE: [
        Command.SET_ENABLED,
        Command.STF_INSTALLED,
        Command.STF_UNINSTALLED,
    ],
    Capability.SAMSUNG_IM_FIND_NODE_GEOLOCATION: [Command.UPDATE],
    Capability.SAMSUNG_IM_FIRMWARE_AUTO_UPDATE: [
        Command.DISABLE_AUTO_UPDATE,
        Command.ENABLE_AUTO_UPDATE,
    ],
    Capability.SAMSUNG_IM_FIRMWARE_SERVER: [Command.SET_SERVER],
    Capability.SAMSUNG_IM_FIXED_FIND_NODE: [Command.REFRESH],
    Capability.SAMSUNG_IM_HUB_ONBOARDING: [Command.ONBOARDING, Command.RESET],
    Capability.SAMSUNG_IM_HUE_SYNC_MODE: [],
    Capability.SAMSUNG_IM_LED_NOTIFICATION: [
        Command.DISABLE_LED_NOTIFICATION,
        Command.ENABLE_LED_NOTIFICATION,
    ],
    Capability.SAMSUNG_IM_NEARBY_DETECTION: [Command.OFF, Command.ON, Command.REFRESH],
    Capability.SAMSUNG_IM_NETWORK_AUDIO_GROUP_INFO: [
        Command.SET_ACM_MODE,
        Command.SET_CHANNEL,
        Command.SET_GROUP_NAME,
        Command.SET_MASTER_DI,
        Command.SET_MASTER_NAME,
        Command.SET_ROLE,
        Command.SET_STATUS,
        Command.SET_STEREO_TYPE,
    ],
    Capability.SAMSUNG_IM_NETWORK_AUDIO_MODE: [Command.SET_MODE],
    Capability.SAMSUNG_IM_NETWORK_AUDIO_TRACK_DATA: [
        Command.SET_APP_NAME,
        Command.SET_SOURCE,
    ],
    Capability.SAMSUNG_IM_REQUEST_INVITATION: [Command.UPDATE],
    Capability.SAMSUNG_IM_RING_MOBILE: [Command.UPDATE],
    Capability.SAMSUNG_IM_SAMSUNGACCOUNT: [Command.SIGN_IN, Command.SIGN_OUT],
    Capability.SAMSUNG_IM_SELF_TEST: [Command.RUN],
    Capability.SAMSUNG_IM_STHUBEUI: [],
    Capability.SAMSUNG_IM_WIFI: [Command.GET_SCAN_RESULTS, Command.UPDATE],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_MUTE: [Command.MUTED],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_DOWN: [Command.VOLUME_DOWN],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_UP: [Command.VOLUME_UP],
    Capability.ABATEACHIEVE62503_STATELESS_CHANNEL_DOWN: [Command.CHANNEL_DOWN],
    Capability.ABATEACHIEVE62503_STATELESS_CHANNEL_UP: [Command.CHANNEL_UP],
    Capability.ABSOLUTEWEATHER46907_LANGUAGE_SUPPORT: [Command.SET_LANGUAGE],
    Capability.ABSOLUTEWEATHER46907_LOCK: [Command.SET_OPTION, Command.UNLOCK],
    Capability.ABSOLUTEWEATHER46907_LOCKSTATERELEASE: [Command.SET_LOCK],
    Capability.AMBERPIANO10217_BINDING_INFO: [],
    Capability.AMBERPIANO10217_CLUSTER: [Command.SET_CLUSTER_ID],
    Capability.AMBERPIANO10217_CONTROLLER_STATUS: [],
    Capability.AMBERPIANO10217_DETECTION_INTERVAL: [Command.SET_DETECTION_INTERVAL],
    Capability.AMBERPIANO10217_DEVICE_EUI: [Command.SET_DEVICE_EUI],
    Capability.AMBERPIANO10217_DEVICEINFO: [],
    Capability.AMBERPIANO10217_GROUP_ADD: [Command.ADD, Command.PUSH],
    Capability.AMBERPIANO10217_GROUP_INFO: [],
    Capability.AMBERPIANO10217_GROUP_REMOVE: [Command.PUSH, Command.REMOVE],
    Capability.AMBERPIANO10217_GROUP_REMOVE_ALL: [Command.PUSH],
    Capability.AMBERPIANO10217_MONITORED_APPROACH_DISTANCE: [Command.SET_DISTANCE],
    Capability.AMBERPIANO10217_OBJECT: [],
    Capability.AMBERPIANO10217_PRESENCE_DETECTION_STATUS: [Command.SET_STATUS],
    Capability.AMBERPIANO10217_SENSOR_DETECTION_SENSITIVITY: [Command.SET_MODE],
    Capability.AMBERPIANO10217_SENSOR_MONITORING_MODE: [Command.SET_MODE],
    Capability.AMBERPIANO10217_VIRTUAL_THING_TYPE: [Command.SET_THING_TYPE],
    Capability.EVENTFLUTE36860_DEFAULT_LEVEL_LOCAL: [Command.SET_LEVEL_LOCAL],
    Capability.EVENTFLUTE36860_LED_BAR_SWITCH_OFF: [
        Command.SET_LED_BAR_OFF_COLOR,
        Command.SET_LED_BAR_OFF_LEVEL,
    ],
    Capability.EVENTFLUTE36860_LED_BAR_SWITCH_ON: [
        Command.SET_LED_BAR_ON_COLOR,
        Command.SET_LED_BAR_ON_LEVEL,
    ],
    Capability.EVENTFLUTE36860_LOCAL_CONTROL: [Command.SET_LOCAL_CONTROL],
    Capability.EVENTFLUTE36860_LOG: [],
    Capability.EVENTFLUTE36860_NOTIFICATION_ALL: [
        Command.SET_NOTIFICATION_COLOR,
        Command.SET_NOTIFICATION_DURATION,
        Command.SET_NOTIFICATION_EFFECT,
        Command.SET_NOTIFICATION_LEVEL,
    ],
    Capability.EVENTFLUTE36860_NOTIFICATION_LZW31SN: [
        Command.SET_NOTIFICATION_COLOR,
        Command.SET_NOTIFICATION_DURATION,
        Command.SET_NOTIFICATION_EFFECT,
        Command.SET_NOTIFICATION_LEVEL,
    ],
    Capability.EVENTFLUTE36860_NOTIFICATION_SINGLE: [
        Command.SET_NOTIFICATION_COLOR,
        Command.SET_NOTIFICATION_DURATION,
        Command.SET_NOTIFICATION_EFFECT,
        Command.SET_NOTIFICATION_LEVEL,
        Command.SET_NOTIFICATION_NUMBER,
    ],
    Capability.EVENTFLUTE36860_REMOTE_CONTROL: [Command.SET_REMOTE_CONTROL],
    Capability.HCA_DRYER_MODE: [Command.SET_MODE],
    Capability.HCA_WASHER_MODE: [Command.SET_MODE],
    Capability.LEGENDABSOLUTE60149_ACTIONBUTTON2: [Command.PUSH],
    Capability.LEGENDABSOLUTE60149_ATMOS_PRESSURE: [Command.SET_ATMOS_PRESSURE],
    Capability.LEGENDABSOLUTE60149_BELL_SOUNDS: [Command.SET_BELL_SOUNDS],
    Capability.LEGENDABSOLUTE60149_CIRCADIAN: [Command.SET_CIRCADIAN],
    Capability.LEGENDABSOLUTE60149_COLOR_CHANGE_MODE1: [Command.SET_COLOR_CHANGE_MODE],
    Capability.LEGENDABSOLUTE60149_COLOR_CHANGE_TIMER: [Command.SET_COLOR_CHANGE_TIMER],
    Capability.LEGENDABSOLUTE60149_COLOR_CHANGING: [Command.SET_COLOR_CHANGING],
    Capability.LEGENDABSOLUTE60149_COLOR_TEMPERATURE_STEPS: [
        Command.SET_COLOR_TEMP_STEPS
    ],
    Capability.LEGENDABSOLUTE60149_COMMAND_CLASS: [],
    Capability.LEGENDABSOLUTE60149_CREATE_DEVICE2: [Command.SET_CREATE_DEVICE],
    Capability.LEGENDABSOLUTE60149_CURRENT_LOOP: [Command.SET_CURRENT_LOOP],
    Capability.LEGENDABSOLUTE60149_CURRENT_TIME_PERIOD: [
        Command.SET_CURRENT_TIME_PERIOD
    ],
    Capability.LEGENDABSOLUTE60149_CURRENT_TWILIGHT: [Command.SET_CURRENT_TWILIGHT],
    Capability.LEGENDABSOLUTE60149_DAY_LENGTH: [Command.SET_DAY_LENGTH],
    Capability.LEGENDABSOLUTE60149_DEVICE_ASSOCIATION_TYPE: [
        Command.SET_DEVICE_ASSOCIATION_TYPE
    ],
    Capability.LEGENDABSOLUTE60149_DEVICE_INFO: [Command.SET_DEVICE_INFO],
    Capability.LEGENDABSOLUTE60149_DRIVER_VERSION1: [Command.SET_DRIVER_VERSION],
    Capability.LEGENDABSOLUTE60149_EFFECTS_SET_COMMAND: [
        Command.SET_EFFECTS_SET_COMMAND
    ],
    Capability.LEGENDABSOLUTE60149_ENERGY_RESET1: [Command.SET_ENERGY_RESET],
    Capability.LEGENDABSOLUTE60149_EVEN_ODD_DAY: [Command.SET_EVEN_ODD_DAY],
    Capability.LEGENDABSOLUTE60149_FAN_CYCLIC_MODE: [Command.SET_FAN_CYCLIC_MODE],
    Capability.LEGENDABSOLUTE60149_FAN_NEXT_CHANGE: [Command.SET_FAN_NEXT_CHANGE],
    Capability.LEGENDABSOLUTE60149_FORCED_ON_LEVEL: [Command.SET_FORCED_ON_LEVEL],
    Capability.LEGENDABSOLUTE60149_GET_GROUPS: [Command.SET_GET_GROUPS],
    Capability.LEGENDABSOLUTE60149_GROUP_COMMAND_OPTION: [
        Command.SET_GROUP_COMMAND_OPTION
    ],
    Capability.LEGENDABSOLUTE60149_GROUP_NUMBER: [Command.SET_GROUP_NUMBER],
    Capability.LEGENDABSOLUTE60149_HUE_STEPS: [Command.SET_HUE_STEPS],
    Capability.LEGENDABSOLUTE60149_HUMIDITY_CONDITION: [Command.SET_HUMIDITY_CONDITION],
    Capability.LEGENDABSOLUTE60149_HUMIDITY_TARGET: [Command.SET_HUMIDITY_TARGET],
    Capability.LEGENDABSOLUTE60149_INFO_PANEL: [Command.SET_INFO_PANEL],
    Capability.LEGENDABSOLUTE60149_LEVEL_STEPS: [Command.SET_LEVEL_STEPS],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE: [Command.SET_LOCAL_DATE],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE_ONE: [Command.SET_LOCAL_DATE_ONE],
    Capability.LEGENDABSOLUTE60149_LOCAL_DATE_TWO1: [Command.SET_LOCAL_DATE_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_DAY: [Command.SET_LOCAL_DAY],
    Capability.LEGENDABSOLUTE60149_LOCAL_DAY_TWO: [Command.SET_LOCAL_DAY_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR: [Command.SET_LOCAL_HOUR],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR_OFFSET: [Command.SET_LOCAL_HOUR_OFFSET],
    Capability.LEGENDABSOLUTE60149_LOCAL_HOUR_TWO: [Command.SET_LOCAL_HOUR_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH: [Command.SET_LOCAL_MONTH],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_ONE: [
        Command.SET_LOCAL_MONTH_DAY_ONE
    ],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_TWO: [
        Command.SET_LOCAL_MONTH_DAY_TWO
    ],
    Capability.LEGENDABSOLUTE60149_LOCAL_MONTH_TWO: [Command.SET_LOCAL_MONTH_TWO],
    Capability.LEGENDABSOLUTE60149_LOCAL_WEEK_DAY: [Command.SET_LOCAL_WEEK_DAY],
    Capability.LEGENDABSOLUTE60149_LOCAL_YEAR: [Command.SET_LOCAL_YEAR],
    Capability.LEGENDABSOLUTE60149_LOOPS_NUMBER: [Command.SET_LOOPS_NUMBER],
    Capability.LEGENDABSOLUTE60149_MIRROR_GROUP_FUNCTION: [
        Command.SET_MIRROR_GROUP_FUNCTION
    ],
    Capability.LEGENDABSOLUTE60149_MIRROR_IN: [Command.SET_MIRROR_IN],
    Capability.LEGENDABSOLUTE60149_MIRROR_OUT: [Command.SET_MIRROR_OUT],
    Capability.LEGENDABSOLUTE60149_MOTION_SENSOR_ENABLE: [
        Command.SET_MOTION_SENSOR_ENABLE
    ],
    Capability.LEGENDABSOLUTE60149_NODE_END_POINT: [Command.SET_NODE_END_POINT],
    Capability.LEGENDABSOLUTE60149_NODE_TO_WRITE_HEX: [Command.SET_NODE_TO_WRITE],
    Capability.LEGENDABSOLUTE60149_PARAMETER_START: [Command.SET_PARAMETER_START],
    Capability.LEGENDABSOLUTE60149_PARAMETEREND: [Command.SET_PARAMETER_END],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_OFF1: [Command.SET_PROG_OFF],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_ON1: [Command.SET_PROG_ON],
    Capability.LEGENDABSOLUTE60149_RANDOM_MAXIMUM_TIMER: [
        Command.SET_RANDOM_MAXIMUM_TIMER
    ],
    Capability.LEGENDABSOLUTE60149_RANDOM_MINIMUM_TIMER: [
        Command.SET_RANDOM_MINIMUM_TIMER
    ],
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP: [Command.SET_RANDOM_NEXT],
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP2: [Command.SET_RANDOM_NEXT],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF1: [Command.SET_RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF2: [Command.SET_RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_RESETBUTTON: [Command.PUSH],
    Capability.LEGENDABSOLUTE60149_SIGNAL_METRICS: [Command.SET_SIGNAL_METRICS],
    Capability.LEGENDABSOLUTE60149_SIREN_OR_BELL_ACTIVE: [
        Command.SET_SIREN_OR_BELL_ACTIVE
    ],
    Capability.LEGENDABSOLUTE60149_SIREN_SOUNDS: [Command.SET_SIREN_SOUNDS],
    Capability.LEGENDABSOLUTE60149_SUN_AZIMUTH_ANGLE: [Command.SET_SUN_AZIMUTH_ANGLE],
    Capability.LEGENDABSOLUTE60149_SUN_ELEVATION_ANGLE: [
        Command.SET_SUN_ELEVATION_ANGLE
    ],
    Capability.LEGENDABSOLUTE60149_SUN_RISE: [Command.SET_SUN_RISE],
    Capability.LEGENDABSOLUTE60149_SUN_RISE_OFFSET1: [Command.SET_SUN_RISE_OFFSET],
    Capability.LEGENDABSOLUTE60149_SUN_SET: [Command.SET_SUN_SET],
    Capability.LEGENDABSOLUTE60149_SUN_SET_OFFSET1: [Command.SET_SUN_SET_OFFSET],
    Capability.LEGENDABSOLUTE60149_SWITCH_ALL_ON_OFF1: [Command.SET_SWITCH_ALL_ON_OFF],
    Capability.LEGENDABSOLUTE60149_TEMP_CONDITION2: [Command.SET_TEMP_CONDITION],
    Capability.LEGENDABSOLUTE60149_TEMP_TARGET: [Command.SET_TEMP_TARGET],
    Capability.LEGENDABSOLUTE60149_THERMOSTAT_LOCKED: [Command.SET_THERMOSTAT_LOCKED],
    Capability.LEGENDABSOLUTE60149_TIMER_NEXT_CHANGE: [Command.SET_TIMER_NEXT_CHANGE],
    Capability.LEGENDABSOLUTE60149_TIMER_SECONDS: [Command.SET_TIMER_SECONDS],
    Capability.LEGENDABSOLUTE60149_TIMER_TYPE: [Command.SET_TIMER_TYPE],
    Capability.MIRRORHAPPY40050_COPPER_WATER_METER: [],
    Capability.MUSICAHEAD43206_POWERMODE: [Command.OFF, Command.ON],
    Capability.MUSICAHEAD43206_SNOOZE: [Command.OFF, Command.ON],
    Capability.MUSICAHEAD43206_STAGE: [Command.SET_STAGE],
    Capability.PARTYVOICE23922_ADD2: [Command.PUSH],
    Capability.PARTYVOICE23922_AMPERAGE: [],
    Capability.PARTYVOICE23922_APIWEBREQUEST: [Command.G_E_T, Command.P_O_S_T],
    Capability.PARTYVOICE23922_BAROMETER2: [],
    Capability.PARTYVOICE23922_CASTMEDIACONTROL: [Command.SET_CONTROL],
    Capability.PARTYVOICE23922_CLOSEDURATION: [Command.SET_CLOSE],
    Capability.PARTYVOICE23922_CLOUDCOVER: [],
    Capability.PARTYVOICE23922_COUNT: [],
    Capability.PARTYVOICE23922_CREATEANOTHER: [Command.PUSH],
    Capability.PARTYVOICE23922_CREATEDEV8: [Command.SET_DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEHTTPDEV2B: [Command.SET_DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEMQTTDEV9: [Command.SET_DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEQTY: [Command.SET_CREATE_QTY],
    Capability.PARTYVOICE23922_DURATION2: [],
    Capability.PARTYVOICE23922_ERRORSENSOR: [],
    Capability.PARTYVOICE23922_ERRORSTATUS: [],
    Capability.PARTYVOICE23922_ERRORSTATUSCV: [],
    Capability.PARTYVOICE23922_HTTPCODE: [],
    Capability.PARTYVOICE23922_HTTPRESPONSE: [],
    Capability.PARTYVOICE23922_INFOTABLE: [],
    Capability.PARTYVOICE23922_INPUTPERCENT: [],
    Capability.PARTYVOICE23922_INPUTSTATE: [],
    Capability.PARTYVOICE23922_INVENTORY8: [Command.SET_INVENTORY],
    Capability.PARTYVOICE23922_KEYNUMVALUE: [],
    Capability.PARTYVOICE23922_KEYVALUE2: [],
    Capability.PARTYVOICE23922_LOCATION: [Command.SET_LOC],
    Capability.PARTYVOICE23922_MEDIASUBTITLE: [],
    Capability.PARTYVOICE23922_MEDIATITLE: [],
    Capability.PARTYVOICE23922_MQTTPUBLISH: [Command.PUBLISH],
    Capability.PARTYVOICE23922_NAMEINPUT: [Command.SET_INPUT],
    Capability.PARTYVOICE23922_ONVIFINFO: [],
    Capability.PARTYVOICE23922_ONVIFSTATUS: [],
    Capability.PARTYVOICE23922_OPENDURATION: [Command.SET_OPEN],
    Capability.PARTYVOICE23922_POWERFACTOR2: [],
    Capability.PARTYVOICE23922_PRECIPPROB: [],
    Capability.PARTYVOICE23922_PRECIPRATE: [],
    Capability.PARTYVOICE23922_REACTIVEPOWER: [],
    Capability.PARTYVOICE23922_REFRESH: [Command.PUSH],
    Capability.PARTYVOICE23922_RESETALT: [Command.PUSH],
    Capability.PARTYVOICE23922_RESETSELECT: [Command.SET_SELECT],
    Capability.PARTYVOICE23922_ROKUCURRENTAPP: [],
    Capability.PARTYVOICE23922_ROKUMEDIASTATUS: [],
    Capability.PARTYVOICE23922_SETILLUMINANCE: [Command.SET_ILLUM],
    Capability.PARTYVOICE23922_SHADEPAUSE: [Command.PUSH],
    Capability.PARTYVOICE23922_SHELLYDEVS4: [Command.SET_DEVICE_TYPE],
    Capability.PARTYVOICE23922_STATEFIELD2: [],
    Capability.PARTYVOICE23922_STATUS: [],
    Capability.PARTYVOICE23922_SUBTRACT2: [Command.PUSH],
    Capability.PARTYVOICE23922_SUMMARY: [],
    Capability.PARTYVOICE23922_TEMPMAX: [],
    Capability.PARTYVOICE23922_TEMPMIN: [],
    Capability.PARTYVOICE23922_TOPICLIST: [],
    Capability.PARTYVOICE23922_TVCHANNEL: [],
    Capability.PARTYVOICE23922_VHUMIDITYSET: [Command.SETV_HUMIDITY],
    Capability.PARTYVOICE23922_VOLUMEDOWN: [Command.PUSH],
    Capability.PARTYVOICE23922_VOLUMEUP: [Command.PUSH],
    Capability.PARTYVOICE23922_VTEMPSET: [Command.SETV_TEMP],
    Capability.PARTYVOICE23922_WATTAGE4: [Command.SET_WATTS],
    Capability.PARTYVOICE23922_WEBREQUEST: [Command.G_E_T, Command.P_O_S_T],
    Capability.PARTYVOICE23922_WEBREQUESTSELECT: [Command.SET_SELECTION],
    Capability.PARTYVOICE23922_WINDDIRDEG: [],
    Capability.PARTYVOICE23922_WINDDIRECTION2: [],
    Capability.PARTYVOICE23922_WINDGUST: [],
    Capability.PARTYVOICE23922_WINDSPEED5: [],
    Capability.PARTYVOICE23922_WLEDEFFECTMODE2: [Command.SET_EFFECT_MODE],
    Capability.PLATEMUSIC11009_AMPERAGE_MEASUREMENT: [],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_FOUR: [],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_THREE: [],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_TWO: [],
    Capability.PLATEMUSIC11009_BASIC_SET_ASSOCIATION_GROUP: [],
    Capability.PLATEMUSIC11009_DEVICE_NETWORK_ID: [],
    Capability.PLATEMUSIC11009_FIRMWARE: [],
    Capability.PLATEMUSIC11009_HS_LED_MODE: [Command.SET_LED_MODE],
    Capability.PLATEMUSIC11009_HS_NORMAL_LED_COLOR: [Command.SET_NORMAL_LED_COLOR],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_BLINKING_COLOR: [
        Command.SET_STATUS_LED_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_BLINKING_FREQ: [
        Command.SET_STATUS_LED_BLINKING_FREQ
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_FIVE_COLOR: [
        Command.SET_STATUS_LED_FIVE_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_FOUR_COLOR: [
        Command.SET_STATUS_LED_FOUR_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_ONE_COLOR: [
        Command.SET_STATUS_LED_ONE_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_SEVEN_COLOR: [
        Command.SET_STATUS_LED_SEVEN_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_SIX_COLOR: [
        Command.SET_STATUS_LED_SIX_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_THREE_COLOR: [
        Command.SET_STATUS_LED_THREE_COLOR
    ],
    Capability.PLATEMUSIC11009_HS_STATUS_LED_TWO_COLOR: [
        Command.SET_STATUS_LED_TWO_COLOR
    ],
    Capability.PLATEMUSIC11009_HUMIDITY_ALARM: [],
    Capability.PLATEMUSIC11009_TEMPERATURE_HUMIDITY_SENSOR: [],
    Capability.PLATEMUSIC11009_ZOOZ_LED_BRIGHTNESS: [Command.SET_LED_BRIGHTNESS],
    Capability.PLATEMUSIC11009_ZOOZ_LED_COLOR: [Command.SET_LED_COLOR],
    Capability.PLATEMUSIC11009_ZOOZ_LED_MODE: [Command.SET_LED_MODE],
    Capability.PLATINUMMASSIVE43262_AUTO_LOCK: [Command.AUTOLOCK, Command.OFF],
    Capability.PLATINUMMASSIVE43262_JASCO_DEFAULT_LEVEL: [Command.SET_DEFAULT_LEVEL],
    Capability.PLATINUMMASSIVE43262_JASCO_LIGHT_SENSING: [Command.SET_LIGHT_SENSING],
    Capability.PLATINUMMASSIVE43262_JASCO_MOTION_SENSITIVITY: [
        Command.SET_MOTION_SENSITIVITY
    ],
    Capability.PLATINUMMASSIVE43262_JASCO_OPERATION_MODE: [Command.SET_OPERATION_MODE],
    Capability.PLATINUMMASSIVE43262_JASCO_TIMEOUT_DURATION: [
        Command.SET_TIMEOUT_DURATION
    ],
    Capability.PLATINUMMASSIVE43262_KEYPAD_BEEP: [Command.BEEP, Command.OFF],
    Capability.PLATINUMMASSIVE43262_LOCK_AND_LEAVE: [Command.LOCKANDLEAVE, Command.OFF],
    Capability.PLATINUMMASSIVE43262_SCHLAGE_INTERIOR_BUTTON: [
        Command.DISABLE,
        Command.ENABLE,
    ],
    Capability.PLATINUMMASSIVE43262_SCHLAGE_LOCK_ALARM: [
        Command.ACTIVITY,
        Command.FORCEDENTRY,
        Command.OFF,
        Command.SET_ACTIVITY_SENSITIVITY,
        Command.SET_ALARM_MODE,
        Command.SET_FORCED_SENSITIVITY,
        Command.SET_TAMPER_SENSITIVITY,
        Command.TAMPER,
    ],
    Capability.PLATINUMMASSIVE43262_STATUS_MESSAGE: [],
    Capability.PLATINUMMASSIVE43262_UNLOCK_CODE_NAME: [],
    Capability.PLATINUMMASSIVE43262_VACATION_MODE: [Command.OFF, Command.VACATION],
    Capability.RBOYAPPS_LOCK_AUDIO: [
        Command.DISABLE_AUDIO,
        Command.ENABLE_AUDIO,
        Command.SET_AUDIO,
    ],
    Capability.RBOYAPPS_LOCK_AUTOLOCK: [
        Command.DISABLE_AUTOLOCK,
        Command.ENABLE_AUTOLOCK,
        Command.SET_AUTOLOCK,
    ],
    Capability.RBOYAPPS_LOCK_EXTENDED: [],
    Capability.RBOYAPPS_LOCK_KEYPAD: [
        Command.DISABLE_KEYPAD,
        Command.ENABLE_KEYPAD,
        Command.SET_KEYPAD,
    ],
    Capability.RBOYAPPS_LOCK_ONE_TOUCH_LOCK: [
        Command.DISABLE_ONE_TOUCH_LOCK,
        Command.ENABLE_ONE_TOUCH_LOCK,
        Command.SET_ONE_TOUCH_LOCK,
    ],
    Capability.RBOYAPPS_LOCK_TAMPER: [Command.ALARM_TOGGLE, Command.SET_ALARM],
    Capability.RBOYAPPS_LOCK_TAMPER_SENSITIVITY: [
        Command.SENSITIVE_TOGGLE,
        Command.SET_SENSITIVITY,
    ],
    Capability.RIVERTALENT14263_ADAPTIVE_ENERGY_USAGE_STATE: [],
    Capability.RIVERTALENT14263_BATCH_GAS_CONSUMPTION_REPORT: [],
    Capability.RIVERTALENT14263_BATCH_POWER_CONSUMPTION_REPORT: [],
    Capability.RIVERTALENT14263_ENERGY_METER_PROPERTIES: [
        Command.SET_METERING_DATE,
        Command.SET_SERVICE_MESSAGE,
    ],
    Capability.RIVERTALENT14263_GAS_CONSUMPTION_REPORT: [],
    Capability.SEC_CALM_CONNECTION_CARE: [],
    Capability.SEC_DEVICE_CONNECTION_STATE: [Command.REFRESH_CONNECTION],
    Capability.SEC_DIAGNOSTICS_INFORMATION: [],
    Capability.SEC_SMARTTHINGS_HUB: [Command.CANCEL_ONBOARDING, Command.ONBOARDING],
    Capability.SEC_WIFI_CONFIGURATION: [],
    Capability.SIGNALAHEAD13665_APPLIANCEOPERATIONSTATESV2: [],
    Capability.SIGNALAHEAD13665_DISHWASHERPROGRAMSV2: [
        Command.SET_PROGRAM,
        Command.STOP,
    ],
    Capability.SIGNALAHEAD13665_STARTSTOPPROGRAMV2: [Command.SET_STARTSTOP],
    Capability.STSE_DEVICE_MODE: [],
    Capability.STSOLUTIONS_DEMAND_RESPONSE_MODE: [Command.SET_MODE],
    Capability.STSOLUTIONS_DEMAND_RESPONSE_STATUS: [],
    Capability.STSOLUTIONS_MESSAGE: [],
    Capability.STUS_SOFTWARE_GENERATION: [],
    Capability.SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT: [Command.SET_CIRCADIAN],
    Capability.SYNTHETIC_FADE_LIGHTNING_EFFECT: [Command.SET_FADE],
    Capability.TAG_E2E_ENCRYPTION: [Command.OFF, Command.ON],
    Capability.TAG_FACTORY_RESET: [Command.RESET],
    Capability.TAG_SEARCHING_STATUS: [],
    Capability.TAG_TAG_BUTTON: [
        Command.SET_BUTTON_DOUBLE_PUSH,
        Command.SET_BUTTON_HOLD,
        Command.SET_BUTTON_PUSH,
        Command.SET_BUTTON_TRIPLE_PUSH,
    ],
    Capability.TAG_TAG_STATUS: [],
    Capability.TAG_UPDATED_INFO: [Command.UPDATE],
    Capability.TAG_UWB_ACTIVATION: [Command.OFF, Command.ON],
    Capability.VALLEYBOARD16460_DEBUG: [Command.CLEAR, Command.SET_VALUE],
    Capability.VALLEYBOARD16460_HTTPREQUESTPATH: [Command.SET_PATH],
    Capability.VALLEYBOARD16460_INFO: [Command.CLEAR, Command.SET_VALUE],
    Capability.WATCHDIGIT58804_ACTUALFANSPEED: [Command.SET_ACTUAL_FAN_SPEED],
    Capability.WATCHDIGIT58804_AUTOMODE: [Command.SET_AUTO_MODE],
    Capability.WATCHDIGIT58804_ERRORSTRING: [Command.SET_ERROR],
    Capability.WATCHDIGIT58804_FILTERCHANGENEEDED: [Command.SET_FILTER_CHANGE_NEEDED],
    Capability.WATCHDIGIT58804_OUTDOORUNITDEFROSTING: [
        Command.SET_OUTDOOR_UNIT_DEFROSTING
    ],
    Capability.WATCHDIGIT58804_STANDBYMODE: [Command.SET_STANDBY_MODE],
    Capability.WATCHDIGIT58804_SYSTEMPREHEATING: [Command.SET_SYSTEM_PREHEATING],
    Capability.WATCHDIGIT58804_THERMOSTATFANSETTING: [
        Command.SET_THERMOSTAT_FAN_SETTING
    ],
    Capability.WATCHPANEL55613_LCCTHERMOSTAT: [],
    Capability.WATCHPANEL55613_TCCTHERMOSTAT: [],
}
