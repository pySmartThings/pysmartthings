"""Command model."""

from enum import StrEnum

from pysmartthings.capability import Capability


class Command(StrEnum):
    """Command model."""

    ACT_SILENTLY = "actSilently"
    ACTIVATE = "activate"
    ADD = "add"
    ADD_AGING = "addAging"
    ADD_RESERVATION = "addReservation"
    AGREE_UPDATE = "agreeUpdate"
    ANNOUNCE = "announce"
    ARM_AWAY = "armAway"
    ARM_STAY = "armStay"
    AUTO = "auto"
    BEEP = "beep"
    BIXBY_COMMAND = "bixbyCommand"
    BOTH = "both"
    CALL = "call"
    CANCEL = "cancel"
    CANCEL_AGING = "cancelAging"
    CANCEL_REMAINING_JOB = "cancelRemainingJob"
    CANCEL_SELF_CHECK = "cancelSelfCheck"
    CAPTURE = "capture"
    CHANNEL_DOWN = "channelDown"
    CHANNEL_UP = "channelUp"
    CHECK_FOR_FIRMWARE_UPDATE = "checkForFirmwareUpdate"
    CHIME = "chime"
    CLEAR = "clear"
    CLIENT_ICE = "clientIce"
    CLOSE = "close"
    CONFIGURE = "configure"
    COOK_CUSTOM_RECIPE = "cookCustomRecipe"
    COOK_DEFINED_RECIPE = "cookDefinedRecipe"
    COOL = "cool"
    DEACTIVATE = "deactivate"
    DELETE = "delete"
    DELETE_CODE = "deleteCode"
    DELETE_RESERVATION = "deleteReservation"
    DELETE_RESERVATIONS = "deleteReservations"
    DELETE_WELCOME_MESSAGE = "deleteWelcomeMessage"
    DEVICE_NOTIFICATION = "deviceNotification"
    DISABLE = "disable"
    DISABLE_ALARM = "disableAlarm"
    DISABLE_REPEAT_MODE = "disableRepeatMode"
    DISABLE_SOUND_DETECTION = "disableSoundDetection"
    DISAGREE_UPDATE = "disagreeUpdate"
    DISARM = "disarm"
    DO_NOT_DISTURB_OFF = "doNotDisturbOff"
    DO_NOT_DISTURB_ON = "doNotDisturbOn"
    EDIT_RESERVATION = "editReservation"
    EMERGENCY_HEAT = "emergencyHeat"
    ENABLE = "enable"
    ENABLE_ALARM = "enableAlarm"
    ENABLE_EP_EVENTS = "enableEpEvents"
    ENABLE_MONITORING_AUTOMATION = "enableMonitoringAutomation"
    ENABLE_REPEAT_MODE = "enableRepeatMode"
    ENABLE_SOUND_DETECTION = "enableSoundDetection"
    END = "end"
    EP_CMD = "epCmd"
    ESTIMATE_OPERATION_TIME = "estimateOperationTime"
    EXECUTE = "execute"
    FAN_AUTO = "fanAuto"
    FAN_CIRCULATE = "fanCirculate"
    FAN_ON = "fanOn"
    FAST_FORWARD = "fastForward"
    FLIP = "flip"
    GROUP_VOLUME_DOWN = "groupVolumeDown"
    GROUP_VOLUME_UP = "groupVolumeUp"
    HEAT = "heat"
    LAUNCH_APP = "launchApp"
    LINK_DRYER_CYCLE = "linkDryerCycle"
    LINK_STEAM_CLOSET_CYCLE = "linkSteamClosetCycle"
    LOCK = "lock"
    LOWER_SETPOINT = "lowerSetpoint"
    MUTE = "mute"
    MUTE_GROUP = "muteGroup"
    MUTED = "muted"
    NAME_SLOT = "nameSlot"
    NEXT_TRACK = "nextTrack"
    OFF = "off"
    ON = "on"
    OPEN = "open"
    OVERRIDE_DEMAND_RESPONSE_LOAD_CONTROL_ACTION = "overrideDrlcAction"
    PAUSE = "pause"
    PERIODIC_SENSING_OFF = "periodicSensingOff"
    PERIODIC_SENSING_ON = "periodicSensingOn"
    PING = "ping"
    PLAY = "play"
    PLAY_PRESET = "playPreset"
    PLAY_TRACK = "playTrack"
    PLAY_TRACK_AND_RESTORE = "playTrackAndRestore"
    PLAY_TRACK_AND_RESUME = "playTrackAndResume"
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
    RESET_DUST_FILTER = "resetDustFilter"
    RESET_ELECTRIC_HEPA_FILTER = "resetElectricHepaFilter"
    RESET_ENERGY_METER = "resetEnergyMeter"
    RESET_FILTER = "resetFilter"
    RESET_FILTER_USAGE_TIME = "resetFilterUsageTime"
    RESET_HEPA_FILTER = "resetHepaFilter"
    RESET_VERY_FINE_DUST_FILTER = "resetVeryFineDustFilter"
    RESET_WATER_FILTER = "resetWaterFilter"
    RESTORE_TRACK = "restoreTrack"
    RESUME = "resume"
    RESUME_TRACK = "resumeTrack"
    RETURN_TO_HOME = "returnToHome"
    REWIND = "rewind"
    RM_COMMAND = "rmCommand"
    SCHEDULE_COOKING = "scheduleCooking"
    SDP_OFFER = "sdpOffer"
    SEARCH = "search"
    SEND = "send"
    SEND_KEY = "sendKey"
    SET_AC_OPTIONAL_MODE = "setAcOptionalMode"
    SET_AC_TROPICAL_NIGHT_MODE_LEVEL = "setAcTropicalNightModeLevel"
    SET_ACCESSIBILITY = "setAccessibility"
    SET_ACM_MODE = "setAcmMode"
    SET_ADD_RINSE = "setAddRinse"
    SET_AIR_CONDITIONER_MODE = "setAirConditionerMode"
    SET_AIR_CONDITIONER_ODOR_CONTROLLER_STATE = "setAirConditionerOdorControllerState"
    SET_AIR_PURIFIER_FAN_MODE = "setAirPurifierFanMode"
    SET_ALARM_THRESHOLD = "setAlarmThreshold"
    SET_AMBIENT_CONTENT = "setAmbientContent"
    SET_AMBIENT_ON = "setAmbientOn"
    SET_AMOUNT = "setAmount"
    SET_APP_NAME = "setAppName"
    SET_ATMOS_PRESSURE = "setAtmosPressure"
    SET_AUDIO_TRACK = "setAudioTrack"
    SET_AUTO_CLEANING_MODE = "setAutoCleaningMode"
    SET_AUTO_REPLENISHMENT = "setAutoReplenishment"
    SET_AUTOMATIC_EXECUTION_MODE = "setAutomaticExecutionMode"
    SET_AUTOMATIC_EXECUTION_SETTING = "setAutomaticExecutionSetting"
    SET_BRIGHTNESS_LEVEL = "setBrightnessLevel"
    SET_BUTTON = "setButton"
    SET_BUTTON_DOUBLE_PUSH = "setButtonDoublePush"
    SET_BUTTON_HOLD = "setButtonHold"
    SET_BUTTON_PUSH = "setButtonPush"
    SET_BUTTON_TRIPLE_PUSH = "setButtonTriplePush"
    SET_CHANNEL = "setChannel"
    SET_CIRCADIAN = "setCircadian"
    SET_CLEANING_MODE = "setCleaningMode"
    SET_CLUSTER_ID = "setClusterId"
    SET_CODE = "setCode"
    SET_CODE_LENGTH = "setCodeLength"
    SET_COLOR = "setColor"
    SET_COLOR_TEMPERATURE = "setColorTemperature"
    SET_CONTEXT = "setContext"
    SET_CONTEXT_SNAPSHOT = "setContextSnapshot"
    SET_COOLING_SETPOINT = "setCoolingSetpoint"
    SET_COORDINATES = "setCoordinates"
    SET_COURSE = "setCourse"
    SET_CREATE_DEVICE = "setCreateDevice"
    SET_CREATE_QTY = "setCreateQty"
    SET_CURRENT_TIME_PERIOD = "setCurrentTimePeriod"
    SET_CURRENT_TWILIGHT = "setCurrentTwilight"
    SET_CUSTOM_COURSE = "setCustomCourse"
    SET_DATA = "setData"
    SET_DAY_LENGTH = "setDayLength"
    SET_DEFINED_RECIPE = "setDefinedRecipe"
    SET_DEFROST = "setDefrost"
    SET_DELAY_END = "setDelayEnd"
    SET_DELAY_TIME = "setDelayTime"
    SET_DENSITY = "setDensity"
    SET_DESIRED_TEMPERATURE = "setDesiredTemperature"
    SET_DETECTION_INTERVAL = "setDetectionInterval"
    SET_DETECTION_PROXIMITY = "setDetectionProximity"
    SET_DETERGENT_TYPE = "setDetergentType"
    SET_DEVICE_EUI = "setDeviceEui"
    SET_DEVICE_TYPE = "setDeviceType"
    SET_DISHWASHER_DELAY_START_TIME = "setDishwasherDelayStartTime"
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
    SET_EFFECTS_SET_COMMAND = "setEffectsSetCommand"
    SET_ENABLE_STATE = "setEnableState"
    SET_ENERGY_RESET = "setEnergyReset"
    SET_ENERGY_SAVING_LEVEL = "setEnergySavingLevel"
    SET_ERROR = "setError"
    SET_EVEN_ODD_DAY = "setEvenOddDay"
    SET_FADE = "setFade"
    SET_FAN_MODE = "setFanMode"
    SET_FAN_OSCILLATION_MODE = "setFanOscillationMode"
    SET_FAN_SPEED = "setFanSpeed"
    SET_FIRMWARE_VERSION = "setFirmwareVersion"
    SET_FORCED_ON_LEVEL = "setForcedOnLevel"
    SET_FREEZER_CONVERT_MODE = "setFreezerConvertMode"
    SET_FRIDGE_MODE = "setFridgeMode"
    SET_GEOFENCE = "setGeofence"
    SET_GET_GROUPS = "setGetGroups"
    SET_GROUP_MUTE = "setGroupMute"
    SET_GROUP_NAME = "setGroupName"
    SET_GROUP_VOLUME = "setGroupVolume"
    SET_HEATED_DRY = "setHeatedDry"
    SET_HEATING_SETPOINT = "setHeatingSetpoint"
    SET_HIGH_TEMP_WASH = "setHighTempWash"
    SET_HOOD_FAN_SPEED = "setHoodFanSpeed"
    SET_HOT_AIR_DRY = "setHotAirDry"
    SET_HUE = "setHue"
    SET_HUMIDIFIER_MODE = "setHumidifierMode"
    SET_ILLUM = "setIllum"
    SET_INFRARED_LEVEL = "setInfraredLevel"
    SET_INITIAL_AMOUNT = "setInitialAmount"
    SET_INPUT_SOURCE = "setInputSource"
    SET_INVENTORY = "setInventory"
    SET_LEVEL = "setLevel"
    SET_LEVEL_STEPS = "setLevelSteps"
    SET_LIGHT_CONTROL_MODE = "setLightControlMode"
    SET_LIGHTING_LEVEL = "setLightingLevel"
    SET_LIGHTING_MODE = "setLightingMode"
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
    SET_MACHINE_STATE = "setMachineState"
    SET_MASTER_DI = "setMasterDi"
    SET_MASTER_NAME = "setMasterName"
    SET_METERING_DATE = "setMeteringDate"
    SET_MIRROR_GROUP_FUNCTION = "setMirrorGroupFunction"
    SET_MODE = "setMode"
    SET_MONITOR = "setMonitor"
    SET_MUTE = "setMute"
    SET_NAME = "setName"
    SET_OPERATING_STATE = "setOperatingState"
    SET_OPERATION_MODE = "setOperationMode"
    SET_OPERATION_ORIGIN = "setOperationOrigin"
    SET_OPERATION_TIME = "setOperationTime"
    SET_OPTIONS = "setOptions"
    SET_ORDER_THRESHOLD = "setOrderThreshold"
    SET_OUTING_MODE = "setOutingMode"
    SET_OVEN_MODE = "setOvenMode"
    SET_OVEN_SETPOINT = "setOvenSetpoint"
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
    SET_POWER_LEVEL = "setPowerLevel"
    SET_POWER_STATE = "setPowerState"
    SET_PROG_OFF = "setProgOff"
    SET_PROG_ON = "setProgOn"
    SET_RANDOM_NEXT = "setRandomNext"
    SET_RANDOM_ON_OFF = "setRandomOnOff"
    SET_RAPID_COOLING = "setRapidCooling"
    SET_RAPID_FREEZING = "setRapidFreezing"
    SET_RECENTLY_USED_APPS = "setRecentlyUsedApps"
    SET_RECOMMENDED_AMOUNT = "setRecommendedAmount"
    SET_REFRIGERATION_SETPOINT = "setRefrigerationSetpoint"
    SET_REMAINING_AMOUNT = "setRemainingAmount"
    SET_REPORT_STATE_PERIOD = "setReportStatePeriod"
    SET_REPORT_STATE_REALTIME = "setReportStateRealtime"
    SET_REPORT_STATE_REALTIME_PERIOD = "setReportStateRealtimePeriod"
    SET_RINSE_MODE = "setRinseMode"
    SET_RINSE_PLUS = "setRinsePlus"
    SET_ROBOT_CLEANER_CLEANING_MODE = "setRobotCleanerCleaningMode"
    SET_ROBOT_CLEANER_MOVEMENT = "setRobotCleanerMovement"
    SET_ROBOT_CLEANER_TURBO_MODE = "setRobotCleanerTurboMode"
    SET_ROLE = "setRole"
    SET_SANITIZE = "setSanitize"
    SET_SANITIZING_WASH = "setSanitizingWash"
    SET_SATURATION = "setSaturation"
    SET_SCHEDULE = "setSchedule"
    SET_SELECTED_ZONE = "setSelectedZone"
    SET_SERVICE_MESSAGE = "setServiceMessage"
    SET_SHADE_LEVEL = "setShadeLevel"
    SET_SIGNAL_METRICS = "setSignalMetrics"
    SET_SOFTENER_TYPE = "setSoftenerType"
    SET_SOUND_FROM = "setSoundFrom"
    SET_SOUND_MODE = "setSoundMode"
    SET_SOURCE = "setSource"
    SET_SPEED_BOOSTER = "setSpeedBooster"
    SET_SPI_MODE = "setSpiMode"
    SET_SPIN_SPEED = "setSpinSpeed"
    SET_START_VALUE = "setStartValue"
    SET_STATUS = "setStatus"
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
    SET_TEMPERATURE_LEVEL = "setTemperatureLevel"
    SET_TEMPERATURE_SETPOINT = "setTemperatureSetpoint"
    SET_THERMOSTAT_FAN_MODE = "setThermostatFanMode"
    SET_THERMOSTAT_MODE = "setThermostatMode"
    SET_THING_TYPE = "setThingType"
    SET_TIME_OFFSET = "setTimeOffset"
    SET_TIMED_CLEAN_DURATION = "setTimedCleanDuration"
    SET_TRACK = "setTrack"
    SET_TV_CHANNEL = "setTvChannel"
    SET_TV_CHANNEL_NAME = "setTvChannelName"
    SET_TYPE = "setType"
    SET_USER_LOCATION = "setUserLocation"
    SET_VALUE = "setValue"
    SET_VOLUME = "setVolume"
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
    SET_WATER_VALVE = "setWaterValve"
    SET_WELCOME_MESSAGE = "setWelcomeMessage"
    SET_WIND_MODE = "setWindMode"
    SET_ZONE_BOOSTER = "setZoneBooster"
    SETV_HUMIDITY = "setvHumidity"
    SETV_TEMP = "setvTemp"
    SIREN = "siren"
    SPEAK = "speak"
    START = "start"
    START_AUDIO = "startAudio"
    START_COOKING = "startCooking"
    START_LATER = "startLater"
    START_SELF_CHECK = "startSelfCheck"
    START_STREAM = "startStream"
    START_TALKBACK = "startTalkback"
    START_WASHING_COURSE = "startWashingCourse"
    START_WASHING_COURSE_WITH_OPTIONS = "startWashingCourseWithOptions"
    STOP = "stop"
    STOP_AUDIO = "stopAudio"
    STOP_STREAM = "stopStream"
    STOP_TALKBACK = "stopTalkback"
    STROBE = "strobe"
    TAKE = "take"
    TOGGLE = "toggle"
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
    UPDATE_FIRMWARE = "updateFirmware"
    UPLOAD_COMPLETE = "uploadComplete"
    UPLOAD_FAILED = "uploadFailed"
    VOLUME_DOWN = "volumeDown"
    VOLUME_UP = "volumeUp"
    ZERO_CALIBRATE = "zeroCalibrate"


CAPABILITY_COMMANDS: dict[Capability, list[Command]] = {
    Capability.ACCELERATION_SENSOR: [],
    Capability.ACTIVITY_LIGHTING_MODE: [Command.SET_LIGHTING_MODE],
    Capability.ACTIVITY_SENSOR: [],
    Capability.AIR_CONDITIONER_FAN_MODE: [Command.SET_FAN_MODE],
    Capability.AIR_CONDITIONER_MODE: [Command.SET_AIR_CONDITIONER_MODE],
    Capability.AIR_PURIFIER_FAN_MODE: [Command.SET_AIR_PURIFIER_FAN_MODE],
    Capability.AIR_QUALITY_HEALTH_CONCERN: [],
    Capability.AIR_QUALITY_SENSOR: [],
    Capability.ALARM: [Command.BOTH, Command.OFF, Command.SIREN, Command.STROBE],
    Capability.ATMOSPHERIC_PRESSURE_MEASUREMENT: [],
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
    Capability.BATTERY: [],
    Capability.BATTERY_LEVEL: [],
    Capability.BODY_MASS_INDEX_MEASUREMENT: [],
    Capability.BODY_WEIGHT_MEASUREMENT: [],
    Capability.BRIDGE: [],
    Capability.BUTTON: [],
    Capability.BYPASSABLE: [],
    Capability.CARBON_DIOXIDE_HEALTH_CONCERN: [],
    Capability.CARBON_DIOXIDE_MEASUREMENT: [],
    Capability.CARBON_MONOXIDE_DETECTOR: [],
    Capability.CARBON_MONOXIDE_MEASUREMENT: [],
    Capability.CHIME: [Command.CHIME, Command.OFF],
    Capability.COLOR_CONTROL: [
        Command.SET_COLOR,
        Command.SET_HUE,
        Command.SET_SATURATION,
    ],
    Capability.COLOR_TEMPERATURE: [Command.SET_COLOR_TEMPERATURE],
    Capability.CONFIGURATION: [Command.CONFIGURE],
    Capability.CONTACT_SENSOR: [],
    Capability.CURRENT_MEASUREMENT: [],
    Capability.DEMAND_RESPONSE_LOAD_CONTROL: [
        Command.OVERRIDE_DEMAND_RESPONSE_LOAD_CONTROL_ACTION,
        Command.REQUEST_DEMAND_RESPONSE_LOAD_CONTROL_ACTION,
    ],
    Capability.DEW_POINT: [],
    Capability.DISHWASHER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.DOOR_CONTROL: [Command.CLOSE, Command.OPEN],
    Capability.DRYER_MODE: [Command.SET_DRYER_MODE],
    Capability.DRYER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.DUST_HEALTH_CONCERN: [],
    Capability.DUST_SENSOR: [],
    Capability.ELEVATOR_CALL: [Command.CALL],
    Capability.ENERGY_METER: [Command.RESET_ENERGY_METER],
    Capability.EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT: [],
    Capability.EXECUTE: [Command.EXECUTE],
    Capability.FAN_OSCILLATION_MODE: [Command.SET_FAN_OSCILLATION_MODE],
    Capability.FAN_SPEED: [Command.SET_FAN_SPEED],
    Capability.FAN_SPEED_PERCENT: [Command.SET_PERCENT],
    Capability.FILTER_STATE: [Command.RESET_FILTER],
    Capability.FILTER_STATUS: [],
    Capability.FINE_DUST_HEALTH_CONCERN: [],
    Capability.FINE_DUST_SENSOR: [],
    Capability.FIRMWARE_UPDATE: [
        Command.CHECK_FOR_FIRMWARE_UPDATE,
        Command.UPDATE_FIRMWARE,
    ],
    Capability.FORMALDEHYDE_HEALTH_CONCERN: [],
    Capability.FORMALDEHYDE_MEASUREMENT: [],
    Capability.GAS_DETECTOR: [],
    Capability.GAS_METER: [],
    Capability.GEOFENCE: [
        Command.SET_ENABLE_STATE,
        Command.SET_GEOFENCE,
        Command.SET_NAME,
    ],
    Capability.GEOLOCATION: [],
    Capability.HARDWARE_FAULT: [],
    Capability.HEALTH_CHECK: [Command.PING],
    Capability.HUMIDIFIER_MODE: [Command.SET_HUMIDIFIER_MODE],
    Capability.ILLUMINANCE_MEASUREMENT: [],
    Capability.IMAGE_CAPTURE: [
        Command.TAKE,
        Command.UPLOAD_COMPLETE,
        Command.UPLOAD_FAILED,
    ],
    Capability.INFRARED_LEVEL: [Command.SET_INFRARED_LEVEL],
    Capability.KEYPAD_INPUT: [Command.SEND_KEY],
    Capability.LAUNDRY_WASHER_RINSE_MODE: [Command.SET_RINSE_MODE],
    Capability.LAUNDRY_WASHER_SPIN_SPEED: [Command.SET_SPIN_SPEED],
    Capability.LOCK: [Command.LOCK, Command.UNLATCH, Command.UNLOCK],
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
    Capability.MOTION_SENSOR: [],
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
    Capability.OVEN_MODE: [Command.SET_OVEN_MODE],
    Capability.OVEN_OPERATING_STATE: [
        Command.SET_MACHINE_STATE,
        Command.START,
        Command.STOP,
    ],
    Capability.OVEN_SETPOINT: [Command.SET_OVEN_SETPOINT],
    Capability.OZONE_HEALTH_CONCERN: [],
    Capability.OZONE_MEASUREMENT: [],
    Capability.PH_MEASUREMENT: [],
    Capability.PANIC_ALARM: [],
    Capability.PEST_CONTROL: [],
    Capability.POWER_CONSUMPTION_REPORT: [],
    Capability.POWER_METER: [],
    Capability.POWER_SOURCE: [],
    Capability.PRECIPITATION_SENSOR: [],
    Capability.PRESENCE_SENSOR: [],
    Capability.RADON_MEASUREMENT: [],
    Capability.REFRESH: [Command.REFRESH],
    Capability.REFRIGERATION: [
        Command.SET_DEFROST,
        Command.SET_RAPID_COOLING,
        Command.SET_RAPID_FREEZING,
    ],
    Capability.REFRIGERATION_SETPOINT: [Command.SET_REFRIGERATION_SETPOINT],
    Capability.RELATIVE_BRIGHTNESS: [],
    Capability.RELATIVE_HUMIDITY_MEASUREMENT: [],
    Capability.REMOTE_CONTROL_STATUS: [],
    Capability.RICE_COOKER: [
        Command.SCHEDULE_COOKING,
        Command.SET_MODE,
        Command.START_COOKING,
        Command.STOP,
    ],
    Capability.ROBOT_CLEANER_CLEANING_MODE: [Command.SET_ROBOT_CLEANER_CLEANING_MODE],
    Capability.ROBOT_CLEANER_MOVEMENT: [Command.SET_ROBOT_CLEANER_MOVEMENT],
    Capability.ROBOT_CLEANER_OPERATING_STATE: [],
    Capability.ROBOT_CLEANER_TURBO_MODE: [Command.SET_ROBOT_CLEANER_TURBO_MODE],
    Capability.SECURITY_SYSTEM: [Command.ARM_AWAY, Command.ARM_STAY, Command.DISARM],
    Capability.SIGNAL_STRENGTH: [],
    Capability.SLEEP_SENSOR: [],
    Capability.SMOKE_DETECTOR: [],
    Capability.SOUND_DETECTION: [
        Command.DISABLE_SOUND_DETECTION,
        Command.ENABLE_SOUND_DETECTION,
    ],
    Capability.SOUND_PRESSURE_LEVEL: [],
    Capability.SOUND_SENSOR: [],
    Capability.SPEECH_SYNTHESIS: [Command.SPEAK],
    Capability.STATELESS_CUSTOM_BUTTON: [Command.SET_BUTTON],
    Capability.STATELESS_FANSPEED_BUTTON: [Command.SET_BUTTON],
    Capability.STATELESS_POWER_TOGGLE_BUTTON: [Command.SET_BUTTON],
    Capability.SWITCH: [Command.OFF, Command.ON],
    Capability.SWITCH_LEVEL: [Command.SET_LEVEL],
    Capability.TAMPER_ALERT: [],
    Capability.TEMPERATURE_ALARM: [],
    Capability.TEMPERATURE_LEVEL: [Command.SET_TEMPERATURE_LEVEL],
    Capability.TEMPERATURE_MEASUREMENT: [],
    Capability.TEMPERATURE_SETPOINT: [Command.SET_TEMPERATURE_SETPOINT],
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
    Capability.THERMOSTAT_SETPOINT: [],
    Capability.THREE_AXIS: [],
    Capability.TONE: [Command.BEEP],
    Capability.TV_CHANNEL: [
        Command.CHANNEL_DOWN,
        Command.CHANNEL_UP,
        Command.SET_TV_CHANNEL,
        Command.SET_TV_CHANNEL_NAME,
    ],
    Capability.TVOC_MEASUREMENT: [],
    Capability.ULTRAVIOLET_INDEX: [],
    Capability.VALVE: [Command.CLOSE, Command.OPEN],
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
    Capability.VIDEO_STREAM: [Command.START_STREAM, Command.STOP_STREAM],
    Capability.VOLTAGE_MEASUREMENT: [],
    Capability.WASHER_MODE: [Command.SET_WASHER_MODE],
    Capability.WASHER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.WATER_SENSOR: [],
    Capability.WEBRTC: [
        Command.CLIENT_ICE,
        Command.END,
        Command.REQUEST_TURN_INFO,
        Command.SDP_OFFER,
        Command.START_TALKBACK,
        Command.STOP_TALKBACK,
    ],
    Capability.WIND_MODE: [Command.SET_WIND_MODE],
    Capability.WINDOW_SHADE: [Command.CLOSE, Command.OPEN, Command.PAUSE],
    Capability.WINDOW_SHADE_LEVEL: [Command.SET_SHADE_LEVEL],
    Capability.WINDOW_SHADE_PRESET: [Command.PRESET_POSITION],
    Capability.ZWAVE_MULTICHANNEL: [Command.ENABLE_EP_EVENTS, Command.EP_CMD],
    Capability.CUSTOM_ACCESSIBILITY: [Command.SET_ACCESSIBILITY],
    Capability.CUSTOM_AIR_CONDITIONER_ODOR_CONTROLLER: [
        Command.SET_AIR_CONDITIONER_ODOR_CONTROLLER_STATE
    ],
    Capability.CUSTOM_AIR_CONDITIONER_OPTIONAL_MODE: [Command.SET_AC_OPTIONAL_MODE],
    Capability.CUSTOM_AIR_CONDITIONER_TROPICAL_NIGHT_MODE: [
        Command.SET_AC_TROPICAL_NIGHT_MODE_LEVEL
    ],
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
    Capability.CUSTOM_WASHER_AUTO_DETERGENT: [Command.SET_WASHER_AUTO_DETERGENT],
    Capability.CUSTOM_WASHER_AUTO_SOFTENER: [Command.SET_WASHER_AUTO_SOFTENER],
    Capability.CUSTOM_WASHER_RINSE_CYCLES: [Command.SET_WASHER_RINSE_CYCLES],
    Capability.CUSTOM_WASHER_SOIL_LEVEL: [Command.SET_WASHER_SOIL_LEVEL],
    Capability.CUSTOM_WASHER_SPIN_LEVEL: [Command.SET_WASHER_SPIN_LEVEL],
    Capability.CUSTOM_WASHER_WATER_TEMPERATURE: [Command.SET_WASHER_WATER_TEMPERATURE],
    Capability.CUSTOM_WATER_FILTER: [Command.RESET_WATER_FILTER],
    Capability.CUSTOM_WELCOME_CARE_MODE: [Command.TURN_WELCOME_CARE_ON],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_BEEP: [Command.OFF, Command.ON],
    Capability.SAMSUNG_CE_AIR_CONDITIONER_LIGHTING: [
        Command.OFF,
        Command.ON,
        Command.SET_LIGHTING_LEVEL,
    ],
    Capability.SAMSUNG_CE_AIR_QUALITY_HEALTH_CONCERN: [],
    Capability.SAMSUNG_CE_ALWAYS_ON_SENSING: [Command.OFF, Command.ON],
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
    Capability.SAMSUNG_CE_BUTTON_DISPLAY_CONDITION: [],
    Capability.SAMSUNG_CE_CLOTHING_EXTRA_CARE: [
        Command.SET_OPERATION_MODE,
        Command.SET_USER_LOCATION,
    ],
    Capability.SAMSUNG_CE_CONNECTION_STATE: [],
    Capability.SAMSUNG_CE_CONSUMED_ENERGY: [Command.SET_TIME_OFFSET],
    Capability.SAMSUNG_CE_COOKTOP_BURNER_MODE: [],
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
    Capability.SAMSUNG_CE_DEFINED_RECIPE: [
        Command.COOK_DEFINED_RECIPE,
        Command.SET_DEFINED_RECIPE,
    ],
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
    Capability.SAMSUNG_CE_MICROWAVE_POWER: [Command.SET_POWER_LEVEL],
    Capability.SAMSUNG_CE_MUSIC_PLAYLIST: [Command.SET_PLAYLIST],
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
    Capability.SAMSUNG_CE_REMOTE_MANAGEMENT_DATA: [Command.RM_COMMAND],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_AUDIO_CLIP: [Command.DISABLE, Command.ENABLE],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_AVP_REGISTRATION: [Command.REGISTER],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_CLEANING_MODE: [
        Command.DISABLE_REPEAT_MODE,
        Command.ENABLE_REPEAT_MODE,
        Command.SET_CLEANING_MODE,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_DRIVING_MODE: [Command.SET_DRIVING_MODE],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_DUST_BAG: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_FEATURE_VISIBILITY: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_AREA_INFO: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_CLEANING_INFO: [],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_MAP_LIST: [],
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
        Command.SET_SCHEDULE,
    ],
    Capability.SAMSUNG_CE_ROBOT_CLEANER_PET_MONITOR: [
        Command.DISABLE,
        Command.ENABLE,
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
    Capability.SAMSUNG_CE_SURFACE_RESIDUAL_HEAT: [],
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
    Capability.SAMSUNG_CE_WATER_RESERVOIR: [],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT: [],
    Capability.SAMSUNG_CE_WEIGHT_MEASUREMENT_CALIBRATION: [Command.ZERO_CALIBRATE],
    Capability.SAMSUNG_CE_WELCOME_COOLING: [Command.START],
    Capability.SAMSUNG_CE_WELCOME_MESSAGE: [
        Command.DELETE_WELCOME_MESSAGE,
        Command.SET_WELCOME_MESSAGE,
    ],
    Capability.SAMSUNG_CE_WIFI_KIT_SUB_DEVICES: [],
    Capability.SAMSUNG_VD_AMBIENT: [Command.SET_AMBIENT_ON],
    Capability.SAMSUNG_VD_AMBIENT18: [Command.SET_AMBIENT_ON],
    Capability.SAMSUNG_VD_AMBIENT_CONTENT: [Command.SET_AMBIENT_CONTENT],
    Capability.SAMSUNG_VD_AUDIO_GROUP_INFO: [],
    Capability.SAMSUNG_VD_AUDIO_INPUT_SOURCE: [],
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
    Capability.SAMSUNG_IM_FIXED_FIND_NODE: [Command.REFRESH],
    Capability.SAMSUNG_IM_HUE_SYNC_MODE: [],
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
    Capability.HCA_DRYER_MODE: [Command.SET_MODE],
    Capability.HCA_WASHER_MODE: [Command.SET_MODE],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_MUTE: [Command.MUTED],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_DOWN: [Command.VOLUME_DOWN],
    Capability.ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_UP: [Command.VOLUME_UP],
    Capability.ABATEACHIEVE62503_STATELESS_CHANNEL_DOWN: [Command.CHANNEL_DOWN],
    Capability.ABATEACHIEVE62503_STATELESS_CHANNEL_UP: [Command.CHANNEL_UP],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_FOUR: [],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_THREE: [],
    Capability.PLATEMUSIC11009_ASSOCIATION_GROUP_TWO: [],
    Capability.PLATEMUSIC11009_DEVICE_NETWORK_ID: [],
    Capability.PLATEMUSIC11009_FIRMWARE: [],
    Capability.SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT: [Command.SET_CIRCADIAN],
    Capability.SYNTHETIC_FADE_LIGHTNING_EFFECT: [Command.SET_FADE],
    Capability.WATCHPANEL55613_LCCTHERMOSTAT: [],
    Capability.LEGENDABSOLUTE60149_ATMOS_PRESSURE: [Command.SET_ATMOS_PRESSURE],
    Capability.LEGENDABSOLUTE60149_CREATE_DEVICE2: [Command.SET_CREATE_DEVICE],
    Capability.LEGENDABSOLUTE60149_CURRENT_TIME_PERIOD: [
        Command.SET_CURRENT_TIME_PERIOD
    ],
    Capability.LEGENDABSOLUTE60149_CURRENT_TWILIGHT: [Command.SET_CURRENT_TWILIGHT],
    Capability.LEGENDABSOLUTE60149_DAY_LENGTH: [Command.SET_DAY_LENGTH],
    Capability.LEGENDABSOLUTE60149_DRIVER_VERSION1: [Command.SET_DRIVER_VERSION],
    Capability.LEGENDABSOLUTE60149_EFFECTS_SET_COMMAND: [
        Command.SET_EFFECTS_SET_COMMAND
    ],
    Capability.LEGENDABSOLUTE60149_ENERGY_RESET1: [Command.SET_ENERGY_RESET],
    Capability.LEGENDABSOLUTE60149_EVEN_ODD_DAY: [Command.SET_EVEN_ODD_DAY],
    Capability.LEGENDABSOLUTE60149_FORCED_ON_LEVEL: [Command.SET_FORCED_ON_LEVEL],
    Capability.LEGENDABSOLUTE60149_GET_GROUPS: [Command.SET_GET_GROUPS],
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
    Capability.LEGENDABSOLUTE60149_MIRROR_GROUP_FUNCTION: [
        Command.SET_MIRROR_GROUP_FUNCTION
    ],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_OFF1: [Command.SET_PROG_OFF],
    Capability.LEGENDABSOLUTE60149_PROGRESSIVE_ON1: [Command.SET_PROG_ON],
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP: [Command.SET_RANDOM_NEXT],
    Capability.LEGENDABSOLUTE60149_RANDOM_NEXT_STEP2: [Command.SET_RANDOM_NEXT],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF1: [Command.SET_RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_RANDOM_ON_OFF2: [Command.SET_RANDOM_ON_OFF],
    Capability.LEGENDABSOLUTE60149_SIGNAL_METRICS: [Command.SET_SIGNAL_METRICS],
    Capability.LEGENDABSOLUTE60149_SUN_AZIMUTH_ANGLE: [Command.SET_SUN_AZIMUTH_ANGLE],
    Capability.LEGENDABSOLUTE60149_SUN_ELEVATION_ANGLE: [
        Command.SET_SUN_ELEVATION_ANGLE
    ],
    Capability.LEGENDABSOLUTE60149_SUN_RISE: [Command.SET_SUN_RISE],
    Capability.LEGENDABSOLUTE60149_SUN_RISE_OFFSET1: [Command.SET_SUN_RISE_OFFSET],
    Capability.LEGENDABSOLUTE60149_SUN_SET: [Command.SET_SUN_SET],
    Capability.LEGENDABSOLUTE60149_SUN_SET_OFFSET1: [Command.SET_SUN_SET_OFFSET],
    Capability.LEGENDABSOLUTE60149_SWITCH_ALL_ON_OFF1: [Command.SET_SWITCH_ALL_ON_OFF],
    Capability.SEC_CALM_CONNECTION_CARE: [],
    Capability.SEC_DEVICE_CONNECTION_STATE: [Command.REFRESH_CONNECTION],
    Capability.SEC_DIAGNOSTICS_INFORMATION: [],
    Capability.SEC_WIFI_CONFIGURATION: [],
    Capability.PARTYVOICE23922_BAROMETER2: [],
    Capability.PARTYVOICE23922_CLOUDCOVER: [],
    Capability.PARTYVOICE23922_CREATEANOTHER: [Command.PUSH],
    Capability.PARTYVOICE23922_CREATEDEV8: [Command.SET_DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEHTTPDEV2B: [Command.SET_DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEMQTTDEV9: [Command.SET_DEVICE_TYPE],
    Capability.PARTYVOICE23922_CREATEQTY: [Command.SET_CREATE_QTY],
    Capability.PARTYVOICE23922_HTTPCODE: [],
    Capability.PARTYVOICE23922_HTTPRESPONSE: [],
    Capability.PARTYVOICE23922_INVENTORY8: [Command.SET_INVENTORY],
    Capability.PARTYVOICE23922_MQTTPUBLISH: [Command.PUBLISH],
    Capability.PARTYVOICE23922_ONVIFINFO: [],
    Capability.PARTYVOICE23922_ONVIFSTATUS: [],
    Capability.PARTYVOICE23922_PRECIPPROB: [],
    Capability.PARTYVOICE23922_PRECIPRATE: [],
    Capability.PARTYVOICE23922_REFRESH: [Command.PUSH],
    Capability.PARTYVOICE23922_SETILLUMINANCE: [Command.SET_ILLUM],
    Capability.PARTYVOICE23922_STATUS: [],
    Capability.PARTYVOICE23922_SUMMARY: [],
    Capability.PARTYVOICE23922_TEMPMAX: [],
    Capability.PARTYVOICE23922_TEMPMIN: [],
    Capability.PARTYVOICE23922_TOPICLIST: [],
    Capability.PARTYVOICE23922_VHUMIDITYSET: [Command.SETV_HUMIDITY],
    Capability.PARTYVOICE23922_VTEMPSET: [Command.SETV_TEMP],
    Capability.PARTYVOICE23922_WINDDIRDEG: [],
    Capability.PARTYVOICE23922_WINDDIRECTION2: [],
    Capability.PARTYVOICE23922_WINDGUST: [],
    Capability.PARTYVOICE23922_WINDSPEED5: [],
    Capability.VALLEYBOARD16460_DEBUG: [Command.CLEAR, Command.SET_VALUE],
    Capability.RIVERTALENT14263_ADAPTIVE_ENERGY_USAGE_STATE: [],
    Capability.RIVERTALENT14263_ENERGY_METER_PROPERTIES: [
        Command.SET_METERING_DATE,
        Command.SET_SERVICE_MESSAGE,
    ],
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
    Capability.AMBERPIANO10217_OBJECT: [],
    Capability.AMBERPIANO10217_SENSOR_DETECTION_SENSITIVITY: [Command.SET_MODE],
    Capability.AMBERPIANO10217_VIRTUAL_THING_TYPE: [Command.SET_THING_TYPE],
}
