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

    ACCELERATION_SENSOR = "accelerationSensor"
    ACTIVITY_LIGHTING_MODE = "activityLightingMode"
    ACTIVITY_SENSOR = "activitySensor"
    AIR_CONDITIONER_FAN_MODE = "airConditionerFanMode"
    AIR_CONDITIONER_MODE = "airConditionerMode"
    AIR_PURIFIER_FAN_MODE = "airPurifierFanMode"
    AIR_QUALITY_HEALTH_CONCERN = "airQualityHealthConcern"
    AIR_QUALITY_SENSOR = "airQualitySensor"
    ALARM = "alarm"
    ATMOSPHERIC_PRESSURE_MEASUREMENT = "atmosphericPressureMeasurement"
    AUDIO_MUTE = "audioMute"
    AUDIO_NOTIFICATION = "audioNotification"
    AUDIO_STREAM = "audioStream"
    AUDIO_TRACK_DATA = "audioTrackData"
    AUDIO_VOLUME = "audioVolume"
    BATTERY = "battery"
    BODY_MASS_INDEX_MEASUREMENT = "bodyMassIndexMeasurement"
    BODY_WEIGHT_MEASUREMENT = "bodyWeightMeasurement"
    BRIDGE = "bridge"
    BUTTON = "button"
    BYPASSABLE = "bypassable"
    CARBON_DIOXIDE_HEALTH_CONCERN = "carbonDioxideHealthConcern"
    CARBON_DIOXIDE_MEASUREMENT = "carbonDioxideMeasurement"
    CARBON_MONOXIDE_DETECTOR = "carbonMonoxideDetector"
    CARBON_MONOXIDE_MEASUREMENT = "carbonMonoxideMeasurement"
    CHIME = "chime"
    COLOR_CONTROL = "colorControl"
    COLOR_TEMPERATURE = "colorTemperature"
    CONFIGURATION = "configuration"
    CONTACT_SENSOR = "contactSensor"
    CURRENT_MEASUREMENT = "currentMeasurement"
    DEMAND_RESPONSE_LOAD_CONTROL = "demandResponseLoadControl"
    DEW_POINT = "dewPoint"
    DISHWASHER_OPERATING_STATE = "dishwasherOperatingState"
    DOOR_CONTROL = "doorControl"
    DRYER_MODE = "dryerMode"
    DRYER_OPERATING_STATE = "dryerOperatingState"
    DUST_HEALTH_CONCERN = "dustHealthConcern"
    DUST_SENSOR = "dustSensor"
    ELEVATOR_CALL = "elevatorCall"
    ENERGY_METER = "energyMeter"
    EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT = "equivalentCarbonDioxideMeasurement"
    EXECUTE = "execute"
    FAN_OSCILLATION_MODE = "fanOscillationMode"
    FAN_SPEED = "fanSpeed"
    FILTER_STATE = "filterState"
    FILTER_STATUS = "filterStatus"
    FINE_DUST_HEALTH_CONCERN = "fineDustHealthConcern"
    FINE_DUST_SENSOR = "fineDustSensor"
    FIRMWARE_UPDATE = "firmwareUpdate"
    FORMALDEHYDE_HEALTH_CONCERN = "formaldehydeHealthConcern"
    FORMALDEHYDE_MEASUREMENT = "formaldehydeMeasurement"
    GAS_DETECTOR = "gasDetector"
    GAS_METER = "gasMeter"
    GEOFENCE = "geofence"
    GEOLOCATION = "geolocation"
    HARDWARE_FAULT = "hardwareFault"
    HEALTH_CHECK = "healthCheck"
    HUMIDIFIER_MODE = "humidifierMode"
    ILLUMINANCE_MEASUREMENT = "illuminanceMeasurement"
    IMAGE_CAPTURE = "imageCapture"
    INFRARED_LEVEL = "infraredLevel"
    KEYPAD_INPUT = "keypadInput"
    LAUNDRY_WASHER_RINSE_MODE = "laundryWasherRinseMode"
    LAUNDRY_WASHER_SPIN_SPEED = "laundryWasherSpinSpeed"
    LOCK = "lock"
    LOCK_CODES = "lockCodes"
    MEDIA_GROUP = "mediaGroup"
    MEDIA_INPUT_SOURCE = "mediaInputSource"
    MEDIA_PLAYBACK = "mediaPlayback"
    MEDIA_PLAYBACK_REPEAT = "mediaPlaybackRepeat"
    MEDIA_PLAYBACK_SHUFFLE = "mediaPlaybackShuffle"
    MEDIA_PRESETS = "mediaPresets"
    MEDIA_TRACK_CONTROL = "mediaTrackControl"
    MODE = "mode"
    MOLD_HEALTH_CONCERN = "moldHealthConcern"
    MOMENTARY = "momentary"
    MOTION_SENSOR = "motionSensor"
    NETWORK_METER = "networkMeter"
    NITROGEN_DIOXIDE_HEALTH_CONCERN = "nitrogenDioxideHealthConcern"
    NITROGEN_DIOXIDE_MEASUREMENT = "nitrogenDioxideMeasurement"
    NOTIFICATION = "notification"
    OBJECT_DETECTION = "objectDetection"
    OCCUPANCY_SENSOR = "occupancySensor"
    OCF = "ocf"
    ODOR_SENSOR = "odorSensor"
    OVEN_MODE = "ovenMode"
    OVEN_OPERATING_STATE = "ovenOperatingState"
    OVEN_SETPOINT = "ovenSetpoint"
    OZONE_HEALTH_CONCERN = "ozoneHealthConcern"
    OZONE_MEASUREMENT = "ozoneMeasurement"
    PH_MEASUREMENT = "pHMeasurement"
    PANIC_ALARM = "panicAlarm"
    PEST_CONTROL = "pestControl"
    POWER_CONSUMPTION_REPORT = "powerConsumptionReport"
    POWER_METER = "powerMeter"
    POWER_SOURCE = "powerSource"
    PRECIPITATION_SENSOR = "precipitationSensor"
    PRESENCE_SENSOR = "presenceSensor"
    RADON_MEASUREMENT = "radonMeasurement"
    REFRESH = "refresh"
    REFRIGERATION = "refrigeration"
    REFRIGERATION_SETPOINT = "refrigerationSetpoint"
    RELATIVE_BRIGHTNESS = "relativeBrightness"
    RELATIVE_HUMIDITY_MEASUREMENT = "relativeHumidityMeasurement"
    REMOTE_CONTROL_STATUS = "remoteControlStatus"
    RICE_COOKER = "riceCooker"
    ROBOT_CLEANER_CLEANING_MODE = "robotCleanerCleaningMode"
    ROBOT_CLEANER_MOVEMENT = "robotCleanerMovement"
    ROBOT_CLEANER_OPERATING_STATE = "robotCleanerOperatingState"
    ROBOT_CLEANER_TURBO_MODE = "robotCleanerTurboMode"
    SECURITY_SYSTEM = "securitySystem"
    SIGNAL_STRENGTH = "signalStrength"
    SLEEP_SENSOR = "sleepSensor"
    SMOKE_DETECTOR = "smokeDetector"
    SOUND_DETECTION = "soundDetection"
    SOUND_PRESSURE_LEVEL = "soundPressureLevel"
    SOUND_SENSOR = "soundSensor"
    SWITCH = "switch"
    SWITCH_LEVEL = "switchLevel"
    TAMPER_ALERT = "tamperAlert"
    TEMPERATURE_ALARM = "temperatureAlarm"
    TEMPERATURE_LEVEL = "temperatureLevel"
    TEMPERATURE_MEASUREMENT = "temperatureMeasurement"
    TEMPERATURE_SETPOINT = "temperatureSetpoint"
    THERMOSTAT_COOLING_SETPOINT = "thermostatCoolingSetpoint"
    THERMOSTAT_FAN_MODE = "thermostatFanMode"
    THERMOSTAT_HEATING_SETPOINT = "thermostatHeatingSetpoint"
    THERMOSTAT_MODE = "thermostatMode"
    THERMOSTAT_OPERATING_STATE = "thermostatOperatingState"
    THERMOSTAT_SETPOINT = "thermostatSetpoint"
    THREE_AXIS = "threeAxis"
    TONE = "tone"
    TV_CHANNEL = "tvChannel"
    TVOC_MEASUREMENT = "tvocMeasurement"
    ULTRAVIOLET_INDEX = "ultravioletIndex"
    VALVE = "valve"
    VERY_FINE_DUST_HEALTH_CONCERN = "veryFineDustHealthConcern"
    VERY_FINE_DUST_SENSOR = "veryFineDustSensor"
    VIDEO_CAMERA = "videoCamera"
    VIDEO_CAPTURE = "videoCapture"
    VIDEO_STREAM = "videoStream"
    VOLTAGE_MEASUREMENT = "voltageMeasurement"
    WASHER_MODE = "washerMode"
    WASHER_OPERATING_STATE = "washerOperatingState"
    WATER_SENSOR = "waterSensor"
    WEBRTC = "webrtc"
    WIND_MODE = "windMode"
    WINDOW_SHADE = "windowShade"
    WINDOW_SHADE_LEVEL = "windowShadeLevel"
    WINDOW_SHADE_PRESET = "windowShadePreset"
    ZWAVE_MULTICHANNEL = "zwMultichannel"

    CUSTOM_ACCESSIBILITY = "custom.accessibility"
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
    CUSTOM_ERROR = "custom.error"
    CUSTOM_FRIDGE_MODE = "custom.fridgeMode"
    CUSTOM_HEPA_FILTER = "custom.hepaFilter"
    CUSTOM_JOB_BEGINNING_STATUS = "custom.jobBeginningStatus"
    CUSTOM_LAUNCH_APP = "custom.launchapp"
    CUSTOM_OCF_RESOURCE_VERSION = "custom.ocfResourceVersion"
    CUSTOM_OVEN_CAVITY_STATUS = "custom.ovenCavityStatus"
    CUSTOM_PERIODIC_SENSING = "custom.periodicSensing"
    CUSTOM_PICTURE_MODE = "custom.picturemode"
    CUSTOM_RECORDING = "custom.recording"
    CUSTOM_SOUND_MODE = "custom.soundmode"
    CUSTOM_SPI_MODE = "custom.spiMode"
    CUSTOM_STEAM_CLOSET_OPERATING_STATE = "custom.steamClosetOperatingState"
    CUSTOM_STEAM_CLOSET_WRINKLE_PREVENT = "custom.steamClosetWrinklePrevent"
    CUSTOM_SUPPORTED_OPTIONS = "custom.supportedOptions"
    CUSTOM_THERMOSTAT_SETPOINT_CONTROL = "custom.thermostatSetpointControl"
    CUSTOM_TV_SEARCH = "custom.tvsearch"
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
    SAMSUNG_CE_CLOTHING_EXTRA_CARE = "samsungce.clothingExtraCare"
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
    SAMSUNG_CE_FLEXIBLE_AUTO_DISPENSE_DETERGENT = (
        "samsungce.flexibleAutoDispenseDetergent"
    )
    SAMSUNG_CE_FOOD_DEFROST = "samsungce.foodDefrost"
    SAMSUNG_CE_FREEZER_CONVERT_MODE = "samsungce.freezerConvertMode"
    SAMSUNG_CE_FRIDGE_FOOD_LIST = "samsungce.fridgeFoodList"
    SAMSUNG_CE_FRIDGE_PANTRY_INFO = "samsungce.fridgePantryInfo"
    SAMSUNG_CE_FRIDGE_PANTRY_MODE = "samsungce.fridgePantryMode"
    SAMSUNG_CE_FRIDGE_VACATION_MODE = "samsungce.fridgeVacationMode"
    SAMSUNG_CE_FRIDGE_WELCOME_LIGHTING = "samsungce.fridgeWelcomeLighting"
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
    SAMSUNG_CE_SAC_DISPLAY_CONDITION = "samsungce.sacDisplayCondition"
    SAMSUNG_CE_SCALE_SETTINGS = "samsungce.scaleSettings"
    SAMSUNG_CE_SELF_CHECK = "samsungce.selfCheck"
    SAMSUNG_CE_SILENT_ACTION = "samsungce.silentAction"
    SAMSUNG_CE_SOFTENER_AUTO_REPLENISHMENT = "samsungce.softenerAutoReplenishment"
    SAMSUNG_CE_SOFTENER_ORDER = "samsungce.softenerOrder"
    SAMSUNG_CE_SOFTENER_STATE = "samsungce.softenerState"
    SAMSUNG_CE_SOFTWARE_UPDATE = "samsungce.softwareUpdate"
    SAMSUNG_CE_STEAM_CLOSET_AUTO_CYCLE_LINK = "samsungce.steamClosetAutoCycleLink"
    SAMSUNG_CE_STEAM_CLOSET_CYCLE = "samsungce.steamClosetCycle"
    SAMSUNG_CE_STEAM_CLOSET_CYCLE_PRESET = "samsungce.steamClosetCyclePreset"
    SAMSUNG_CE_STEAM_CLOSET_DELAY_END = "samsungce.steamClosetDelayEnd"
    SAMSUNG_CE_STEAM_CLOSET_KEEP_FRESH_MODE = "samsungce.steamClosetKeepFreshMode"
    SAMSUNG_CE_STEAM_CLOSET_SANITIZE_MODE = "samsungce.steamClosetSanitizeMode"
    SAMSUNG_CE_TEMPERATURE_SETTING = "samsungce.temperatureSetting"
    SAMSUNG_CE_UNAVAILABLE_CAPABILITIES = "samsungce.unavailableCapabilities"
    SAMSUNG_CE_VIEW_INSIDE = "samsungce.viewInside"
    SAMSUNG_CE_WASHER_BUBBLE_SOAK = "samsungce.washerBubbleSoak"
    SAMSUNG_CE_WASHER_CYCLE = "samsungce.washerCycle"
    SAMSUNG_CE_WASHER_CYCLE_PRESET = "samsungce.washerCyclePreset"
    SAMSUNG_CE_WASHER_DELAY_END = "samsungce.washerDelayEnd"
    SAMSUNG_CE_WASHER_FREEZE_PREVENT = "samsungce.washerFreezePrevent"
    SAMSUNG_CE_WASHER_LABEL_SCAN_CYCLE_PRESET = "samsungce.washerLabelScanCyclePreset"
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

    SAMSUNG_IM_FIXED_FIND_NODE = "samsungim.fixedFindNode"
    SAMSUNG_IM_HUE_SYNC_MODE = "samsungim.hueSyncMode"

    SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT = "synthetic.lightingEffectCircadian"
    SYNTHETIC_FADE_LIGHTNING_EFFECT = "synthetic.lightingEffectFade"

    HCA_DRYER_MODE = "hca.dryerMode"
    HCA_WASHER_MODE = "hca.washerMode"

    SEC_CALM_CONNECTION_CARE = "sec.calmConnectionCare"
    SEC_DEVICE_CONNECTION_STATE = "sec.deviceConnectionState"
    SEC_DIAGNOSTICS_INFORMATION = "sec.diagnosticsInformation"
    SEC_WIFI_CONFIGURATION = "sec.wifiConfiguration"

    TAG_E2E_ENCRYPTION = "tag.e2eEncryption"
    TAG_FACTORY_RESET = "tag.factoryReset"
    TAG_SEARCHING_STATUS = "tag.searchingStatus"
    TAG_TAG_BUTTON = "tag.tagButton"
    TAG_TAG_STATUS = "tag.tagStatus"
    TAG_UPDATED_INFO = "tag.updatedInfo"
    TAG_UWB_ACTIVATION = "tag.uwbActivation"

    SAMSUNG_VD_AMBIENT = "samsungvd.ambient"
    SAMSUNG_VD_AMBIENT18 = "samsungvd.ambient18"
    SAMSUNG_VD_AMBIENT_CONTENT = "samsungvd.ambientContent"
    SAMSUNG_VD_AUDIO_GROUP_INFO = "samsungvd.audioGroupInfo"
    SAMSUNG_VD_AUDIO_INPUT_SOURCE = "samsungvd.audioInputSource"
    SAMSUNG_VD_DEVICE_CATEGORY = "samsungvd.deviceCategory"
    SAMSUNG_VD_FIRMWARE_VERSION = "samsungvd.firmwareVersion"
    SAMSUNG_VD_GROUP_INFO = "samsungvd.groupInfo"
    SAMSUNG_VD_LIGHT_CONTROL = "samsungvd.lightControl"
    SAMSUNG_VD_MEDIA_INPUT_SOURCE = "samsungvd.mediaInputSource"
    SAMSUNG_VD_PICTURE_MODE = "samsungvd.pictureMode"
    SAMSUNG_VD_REMOTE_CONTROL = "samsungvd.remoteControl"
    SAMSUNG_VD_SOUND_DETECTION = "samsungvd.soundDetection"
    SAMSUNG_VD_SOUND_FROM = "samsungvd.soundFrom"
    SAMSUNG_VD_SOUND_MODE = "samsungvd.soundMode"
    SAMSUNG_VD_SUPPORTS_FEATURES = "samsungvd.supportsFeatures"
    SAMSUNG_VD_SUPPORTS_POWER_ON_BY_OCF = "samsungvd.supportsPowerOnByOcf"
    SAMSUNG_VD_THING_STATUS = "samsungvd.thingStatus"

    LEGENDABSOLUTE60149_CREATE_DEVICE2 = "legendabsolute60149.createDevice2"
    LEGENDABSOLUTE60149_CURRENT_TIME_PERIOD = "legendabsolute60149.currentTimePeriod"
    LEGENDABSOLUTE60149_CURRENT_TWILIGHT = "legendabsolute60149.currentTwilight"
    LEGENDABSOLUTE60149_DAY_LENGTH = "legendabsolute60149.dayLength"
    LEGENDABSOLUTE60149_DRIVER_VERSION1 = "legendabsolute60149.driverVersion1"
    LEGENDABSOLUTE60149_EFFECTS_SET_COMMAND = "legendabsolute60149.effectsSetCommand"
    LEGENDABSOLUTE60149_EVEN_ODD_DAY = "legendabsolute60149.evenOddDay"
    LEGENDABSOLUTE60149_FORCED_ON_LEVEL = "legendabsolute60149.forcedOnLevel"
    LEGENDABSOLUTE60149_GET_GROUPS = "legendabsolute60149.getGroups"
    LEGENDABSOLUTE60149_LEVEL_STEPS = "legendabsolute60149.levelSteps"
    LEGENDABSOLUTE60149_LOCAL_DATE = "legendabsolute60149.localDate"
    LEGENDABSOLUTE60149_LOCAL_DATE_ONE = "legendabsolute60149.localDateOne"
    LEGENDABSOLUTE60149_LOCAL_DATE_TWO1 = "legendabsolute60149.localDateTwo1"
    LEGENDABSOLUTE60149_LOCAL_DAY = "legendabsolute60149.localDay"
    LEGENDABSOLUTE60149_LOCAL_DAY_TWO = "legendabsolute60149.localDayTwo"
    LEGENDABSOLUTE60149_LOCAL_HOUR = "legendabsolute60149.localHour"
    LEGENDABSOLUTE60149_LOCAL_HOUR_OFFSET = "legendabsolute60149.localHourOffset"
    LEGENDABSOLUTE60149_LOCAL_HOUR_TWO = "legendabsolute60149.localHourTwo"
    LEGENDABSOLUTE60149_LOCAL_MONTH = "legendabsolute60149.localMonth"
    LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_ONE = "legendabsolute60149.localMonthDayOne"
    LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_TWO = "legendabsolute60149.localMonthDayTwo"
    LEGENDABSOLUTE60149_LOCAL_MONTH_TWO = "legendabsolute60149.localMonthTwo"
    LEGENDABSOLUTE60149_LOCAL_WEEK_DAY = "legendabsolute60149.localWeekDay"
    LEGENDABSOLUTE60149_LOCAL_YEAR = "legendabsolute60149.localYear"
    LEGENDABSOLUTE60149_MIRROR_GROUP_FUNCTION = (
        "legendabsolute60149.mirrorGroupFunction"
    )
    LEGENDABSOLUTE60149_PROGRESSIVE_OFF1 = "legendabsolute60149.progressiveOff1"
    LEGENDABSOLUTE60149_PROGRESSIVE_ON1 = "legendabsolute60149.progressiveOn1"
    LEGENDABSOLUTE60149_RANDOM_NEXT_STEP = "legendabsolute60149.randomNextStep"
    LEGENDABSOLUTE60149_RANDOM_ON_OFF1 = "legendabsolute60149.randomOnOff1"
    LEGENDABSOLUTE60149_SIGNAL_METRICS = "legendabsolute60149.signalMetrics"
    LEGENDABSOLUTE60149_SUN_AZIMUTH_ANGLE = "legendabsolute60149.sunAzimuthAngle"
    LEGENDABSOLUTE60149_SUN_ELEVATION_ANGLE = "legendabsolute60149.sunElevationAngle"
    LEGENDABSOLUTE60149_SUN_RISE = "legendabsolute60149.sunRise"
    LEGENDABSOLUTE60149_SUN_RISE_OFFSET1 = "legendabsolute60149.sunRiseOffset1"
    LEGENDABSOLUTE60149_SUN_SET = "legendabsolute60149.sunSet"
    LEGENDABSOLUTE60149_SUN_SET_OFFSET1 = "legendabsolute60149.sunSetOffset1"

    PLATEMUSIC11009_ASSOCIATION_GROUP_FOUR = "platemusic11009.associationGroupFour"
    PLATEMUSIC11009_ASSOCIATION_GROUP_THREE = "platemusic11009.associationGroupThree"
    PLATEMUSIC11009_ASSOCIATION_GROUP_TWO = "platemusic11009.associationGroupTwo"
    PLATEMUSIC11009_DEVICE_NETWORK_ID = "platemusic11009.deviceNetworkId"
    PLATEMUSIC11009_FIRMWARE = "platemusic11009.firmware"


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


class Command(StrEnum):
    """Command model."""

    ARM_AWAY = "armAway"
    ARM_STAY = "armStay"
    AUTO = "auto"
    BEEP = "beep"
    BOTH = "both"
    CALL = "call"
    CAPTURE = "capture"
    CHANNEL_DOWN = "channelDown"
    CHANNEL_UP = "channelUp"
    CHECK_FOR_FIRMWARE_UPDATE = "checkForFirmwareUpdate"
    CHIME = "chime"
    CLIENT_ICE = "clientIce"
    CLOSE = "close"
    CONFIGURE = "configure"
    COOL = "cool"
    DELETE_CODE = "deleteCode"
    DEVICE_NOTIFICATION = "deviceNotification"
    DISABLE_SOUND_DETECTION = "disableSoundDetection"
    DISARM = "disarm"
    EMERGENCY_HEAT = "emergencyHeat"
    ENABLE_EP_EVENTS = "enableEpEvents"
    ENABLE_SOUND_DETECTION = "enableSoundDetection"
    END = "end"
    EP_CMD = "epCmd"
    FAN_AUTO = "fanAuto"
    FAN_CIRCULATE = "fanCirculate"
    FAN_ON = "fanOn"
    FAST_FORWARD = "fastForward"
    FLIP = "flip"
    HEAT = "heat"
    LOCK = "lock"
    MUTE = "mute"
    NAME_SLOT = "nameSlot"
    NEXT_TRACK = "nextTrack"
    OFF = "off"
    ON = "on"
    OPEN = "open"
    OVERRIDE_DEMAND_RESPONSE_LOAD_CONTROL_ACTION = "overrideDrlcAction"
    PAUSE = "pause"
    PING = "ping"
    PLAY = "play"
    PLAY_TRACK = "playTrack"
    PLAY_TRACK_AND_RESTORE = "playTrackAndRestore"
    PLAY_TRACK_AND_RESUME = "playTrackAndResume"
    PRESET_POSITION = "presetPosition"
    PREVIOUS_TRACK = "previousTrack"
    PUSH = "push"
    REFRESH = "refresh"
    RELOAD_ALL_CODES = "reloadAllCodes"
    REQUEST_CODE = "requestCode"
    REQUEST_DEMAND_RESPONSE_LOAD_CONTROL_ACTION = "requestDrlcAction"
    REQUEST_TURN_INTO = "requestTurnInto"
    RESET_ENERGY_METER = "resetEnergyMeter"
    RESET_FILTER = "resetFilter"
    REWIND = "rewind"
    SCHEDULE_COOKING = "scheduleCooking"
    SDP_OFFER = "sdpOffer"
    SEND_KEY = "sendKey"
    SET_AC_OPTIONAL_MODE = "setAcOptionalMode"
    SET_AIR_CONDITIONER_MODE = "setAirConditionerMode"
    SET_AIR_PURIFIER_FAN_MODE = "setAirPurifierFanMode"
    SET_CODE = "setCode"
    SET_CODE_LENGTH = "setCodeLength"
    SET_COLOR = "setColor"
    SET_COLOR_TEMPERATURE = "setColorTemperature"
    SET_COOLING_SETPOINT = "setCoolingSetpoint"
    SET_DEFROST = "setDefrost"
    SET_DRYER_MODE = "setDryerMode"
    SET_FAN_MODE = "setFanMode"
    SET_FAN_OSCILLATION_MODE = "setFanOscillationMode"
    SET_FAN_SPEED = "setFanSpeed"
    SET_HEATING_SETPOINT = "setHeatingSetpoint"
    SET_HUE = "setHue"
    SET_HUMIDIFIER_MODE = "setHumidifierMode"
    SET_INFRARED_LEVEL = "setInfraredLevel"
    SET_INPUT_SOURCE = "setInputSource"
    SET_LEVEL = "setLevel"
    SET_LIGHTNING_MODE = "setLightningMode"
    SET_MACHINE_STATE = "setMachineState"
    SET_MODE = "setMode"
    SET_MUTE = "setMute"
    SET_OVEN_MODE = "setOvenMode"
    SET_OVEN_SETPOINT = "setOvenSetpoint"
    SET_PLAYBACK_REPEAT_MODE = "setPlaybackRepeatMode"
    SET_PLAYBACK_SHUFFLE = "setPlaybackShuffle"
    SET_PLAYBACK_STATUS = "setPlaybackStatus"
    SET_RAPID_COOLING = "setRapidCooling"
    SET_RAPID_FREEZING = "setRapidFreezing"
    SET_REFRIGERATION_SETPOINT = "setRefrigerationSetpoint"
    SET_RINSE_MODE = "setRinseMode"
    SET_ROBOT_CLEANER_CLEANING_MODE = "setRobotCleanerCleaningMode"
    SET_ROBOT_CLEANER_MOVEMENT = "setRobotCleanerMovement"
    SET_ROBOT_CLEANER_TURBO_MODE = "setRobotCleanerTurboMode"
    SET_SATURATION = "setSaturation"
    SET_SHADE_LEVEL = "setShadeLevel"
    SET_SPIN_SPEED = "setSpinSpeed"
    SET_TEMPERATURE_LEVEL = "setTemperatureLevel"
    SET_TEMPERATURE_SETPOINT = "setTemperatureSetpoint"
    SET_THERMOSTAT_FAN_MODE = "setThermostatFanMode"
    SET_THERMOSTAT_MODE = "setThermostatMode"
    SET_TV_CHANNEL = "setTvChannel"
    SET_TV_CHANNEL_NAME = "setTvChannelName"
    SET_VOLUME = "setVolume"
    SET_WASHER_MODE = "setWasherMode"
    SET_WIND_MODE = "setWindMode"
    SIREN = "siren"
    START = "start"
    START_AUDIO = "startAudio"
    START_COOKING = "startCooking"
    START_STREAM = "startStream"
    START_TALKBACK = "startTalkback"
    STOP = "stop"
    STOP_AUDIO = "stopAudio"
    STOP_STREAM = "stopStream"
    STOP_TALKBACK = "stopTalkback"
    STROBE = "strobe"
    TAKE = "take"
    UNLATCH = "unlatch"
    UNLOCK = "unlock"
    UNMUTE = "unmute"
    UPDATE_CODES = "updateCodes"
    UPDATE_FIRMWARE = "updateFirmware"
    UPLOAD_COMPLETE = "uploadComplete"
    UPLOAD_FAILED = "uploadFailed"
    VOLUME_DOWN = "volumeDown"
    VOLUME_UP = "volumeUp"


CAPABILITY_COMMANDS: dict[Capability, list[Command]] = {
    Capability.ACTIVITY_LIGHTING_MODE: [Command.SET_LIGHTNING_MODE],
    Capability.AIR_CONDITIONER_FAN_MODE: [Command.SET_FAN_MODE],
    Capability.AIR_CONDITIONER_MODE: [Command.SET_AIR_CONDITIONER_MODE],
    Capability.AIR_PURIFIER_FAN_MODE: [Command.SET_AIR_PURIFIER_FAN_MODE],
    Capability.ALARM: [Command.BOTH, Command.OFF, Command.SIREN, Command.STROBE],
    Capability.AUDIO_MUTE: [Command.MUTE, Command.UNMUTE, Command.SET_MUTE],
    Capability.AUDIO_NOTIFICATION: [
        Command.PLAY_TRACK,
        Command.PLAY_TRACK_AND_RESUME,
        Command.PLAY_TRACK_AND_RESTORE,
    ],
    Capability.AUDIO_STREAM: [Command.START_AUDIO, Command.STOP_AUDIO],
    Capability.AUDIO_VOLUME: [
        Command.SET_VOLUME,
        Command.VOLUME_UP,
        Command.VOLUME_DOWN,
    ],
    Capability.CHIME: [Command.CHIME, Command.OFF],
    Capability.COLOR_CONTROL: [
        Command.SET_COLOR,
        Command.SET_HUE,
        Command.SET_SATURATION,
    ],
    Capability.COLOR_TEMPERATURE: [Command.SET_COLOR_TEMPERATURE],
    Capability.CONFIGURATION: [Command.CONFIGURE],
    Capability.DEMAND_RESPONSE_LOAD_CONTROL: [
        Command.OVERRIDE_DEMAND_RESPONSE_LOAD_CONTROL_ACTION,
        Command.REQUEST_DEMAND_RESPONSE_LOAD_CONTROL_ACTION,
    ],
    Capability.DISHWASHER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.DOOR_CONTROL: [Command.OPEN, Command.CLOSE],
    Capability.DRYER_MODE: [Command.SET_DRYER_MODE],
    Capability.DRYER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.ELEVATOR_CALL: [Command.CALL],
    Capability.ENERGY_METER: [Command.RESET_ENERGY_METER],
    Capability.FAN_OSCILLATION_MODE: [Command.SET_FAN_OSCILLATION_MODE],
    Capability.FAN_SPEED: [Command.SET_FAN_SPEED],
    Capability.FILTER_STATE: [Command.RESET_FILTER],
    Capability.FIRMWARE_UPDATE: [
        Command.CHECK_FOR_FIRMWARE_UPDATE,
        Command.UPDATE_FIRMWARE,
    ],
    Capability.HEALTH_CHECK: [Command.PING],
    Capability.HUMIDIFIER_MODE: [Command.SET_HUMIDIFIER_MODE],
    Capability.IMAGE_CAPTURE: [
        Command.TAKE,
        Command.UPLOAD_COMPLETE,
        Command.UPLOAD_FAILED,
    ],
    Capability.INFRARED_LEVEL: [Command.SET_INFRARED_LEVEL],
    Capability.KEYPAD_INPUT: [Command.SEND_KEY],
    Capability.LAUNDRY_WASHER_RINSE_MODE: [Command.SET_RINSE_MODE],
    Capability.LAUNDRY_WASHER_SPIN_SPEED: [Command.SET_SPIN_SPEED],
    Capability.LOCK_CODES: [
        Command.DELETE_CODE,
        Command.NAME_SLOT,
        Command.RELOAD_ALL_CODES,
        Command.REQUEST_CODE,
        Command.SET_CODE,
        Command.SET_CODE_LENGTH,
        Command.UPDATE_CODES,
    ],
    Capability.LOCK: [Command.LOCK, Command.UNLOCK, Command.UNLATCH],
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
    Capability.MEDIA_TRACK_CONTROL: [Command.NEXT_TRACK, Command.PREVIOUS_TRACK],
    Capability.MODE: [Command.SET_MODE],
    Capability.MOMENTARY: [Command.PUSH],
    Capability.NOTIFICATION: [Command.DEVICE_NOTIFICATION],
    Capability.OVEN_MODE: [Command.SET_OVEN_MODE],
    Capability.OVEN_OPERATING_STATE: [
        Command.SET_MACHINE_STATE,
        Command.START,
        Command.STOP,
    ],
    Capability.OVEN_SETPOINT: [Command.SET_OVEN_SETPOINT],
    Capability.REFRESH: [Command.REFRESH],
    Capability.REFRIGERATION: [
        Command.SET_DEFROST,
        Command.SET_RAPID_COOLING,
        Command.SET_RAPID_FREEZING,
    ],
    Capability.REFRIGERATION_SETPOINT: [Command.SET_REFRIGERATION_SETPOINT],
    Capability.RICE_COOKER: [
        Command.SCHEDULE_COOKING,
        Command.SET_MODE,
        Command.START_COOKING,
        Command.STOP,
    ],
    Capability.ROBOT_CLEANER_CLEANING_MODE: [Command.SET_ROBOT_CLEANER_CLEANING_MODE],
    Capability.ROBOT_CLEANER_MOVEMENT: [Command.SET_ROBOT_CLEANER_MOVEMENT],
    Capability.ROBOT_CLEANER_TURBO_MODE: [Command.SET_ROBOT_CLEANER_TURBO_MODE],
    Capability.SECURITY_SYSTEM: [Command.ARM_AWAY, Command.ARM_STAY, Command.DISARM],
    Capability.SOUND_DETECTION: [
        Command.ENABLE_SOUND_DETECTION,
        Command.DISABLE_SOUND_DETECTION,
    ],
    Capability.SWITCH: [Command.ON, Command.OFF],
    Capability.SWITCH_LEVEL: [Command.SET_LEVEL],
    Capability.TEMPERATURE_LEVEL: [Command.SET_TEMPERATURE_LEVEL],
    Capability.TEMPERATURE_SETPOINT: [Command.SET_TEMPERATURE_SETPOINT],
    Capability.THERMOSTAT_COOLING_SETPOINT: [Command.SET_COOLING_SETPOINT],
    Capability.THERMOSTAT_FAN_MODE: [
        Command.SET_THERMOSTAT_FAN_MODE,
        Command.FAN_ON,
        Command.FAN_AUTO,
        Command.FAN_CIRCULATE,
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
    Capability.TONE: [Command.BEEP],
    Capability.TV_CHANNEL: [
        Command.CHANNEL_UP,
        Command.CHANNEL_DOWN,
        Command.SET_TV_CHANNEL,
        Command.SET_TV_CHANNEL_NAME,
    ],
    Capability.VALVE: [Command.OPEN, Command.CLOSE],
    Capability.VIDEO_CAMERA: [
        Command.FLIP,
        Command.MUTE,
        Command.OFF,
        Command.ON,
        Command.UNMUTE,
    ],
    Capability.VIDEO_CAPTURE: [Command.CAPTURE],
    Capability.VIDEO_STREAM: [Command.START_STREAM, Command.STOP_STREAM],
    Capability.WASHER_MODE: [Command.SET_WASHER_MODE],
    Capability.WASHER_OPERATING_STATE: [Command.SET_MACHINE_STATE],
    Capability.WEBRTC: [
        Command.CLIENT_ICE,
        Command.END,
        Command.REQUEST_TURN_INTO,
        Command.SDP_OFFER,
        Command.STOP_TALKBACK,
        Command.START_TALKBACK,
    ],
    Capability.WIND_MODE: [Command.SET_WIND_MODE],
    Capability.WINDOW_SHADE_LEVEL: [Command.SET_SHADE_LEVEL],
    Capability.WINDOW_SHADE_PRESET: [Command.PRESET_POSITION],
    Capability.WINDOW_SHADE: [Command.CLOSE, Command.OPEN, Command.PAUSE],
    Capability.ZWAVE_MULTICHANNEL: [Command.ENABLE_EP_EVENTS, Command.EP_CMD],
    Capability.CUSTOM_AIR_CONDITIONER_OPTIONAL_MODE: [Command.SET_AC_OPTIONAL_MODE],
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
    capabilities: list[Capability]
    manufacturer_category: Category
    label: str | None = None
    user_category: Category | None = None

    @classmethod
    def __pre_deserialize__(cls, d: dict[str, Any]) -> dict[str, Any]:
        """Pre deserialize hook."""
        d["capabilities"] = [c["id"] for c in d["capabilities"]]
        for cat in d["categories"]:
            if cat["categoryType"] == "manufacturer":
                d["manufacturer_category"] = cat["name"]
            else:
                d["user_category"] = cat["name"]
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
