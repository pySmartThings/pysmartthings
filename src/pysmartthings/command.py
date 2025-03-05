"""Command models."""

from enum import StrEnum

from pysmartthings.capability import Capability


class Command(StrEnum):
    """Command model."""

    ARM_AWAY = "armAway"
    ARM_STAY = "armStay"
    AUTO = "auto"
    BEEP = "beep"
    BOTH = "both"
    CALL = "call"
    CANCEL = "cancel"
    CAPTURE = "capture"
    CHANNEL_DOWN = "channelDown"
    CHANNEL_UP = "channelUp"
    CHECK_FOR_FIRMWARE_UPDATE = "checkForFirmwareUpdate"
    CHIME = "chime"
    CLIENT_ICE = "clientIce"
    CLOSE = "close"
    CONFIGURE = "configure"
    COOL = "cool"
    DELETE = "delete"
    DELETE_CODE = "deleteCode"
    DEVICE_NOTIFICATION = "deviceNotification"
    DISABLE_SOUND_DETECTION = "disableSoundDetection"
    DISARM = "disarm"
    EMERGENCY_HEAT = "emergencyHeat"
    ENABLE_EP_EVENTS = "enableEpEvents"
    ENABLE_SOUND_DETECTION = "enableSoundDetection"
    END = "end"
    EP_CMD = "epCmd"
    ESTIMATE_OPERATION_TINE = "estimateOperationTime"
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
    RESUME = "resume"
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
    SET_DELAY_END = "setDelayEnd"
    SET_DRYER_DRY_LEVEL = "setDryerDryLevel"
    SET_DRYER_LABEL_SCAN_CYCLE_PRESET = "setDryerLabelScanCyclePreset"
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
    SET_WASHER_RINSE_CYCLES = "setWasherRinseCycles"
    SET_WASHER_SOIL_LEVEL = "setWasherSoilLevel"
    SET_WASHER_SPIN_LEVEL = "setWasherSpinLevel"
    SET_WASHER_WATER_TEMPERATURE = "setWasherWaterTemperature"
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
    Capability.CUSTOM_DRYER_DRY_LEVEL: [Command.SET_DRYER_DRY_LEVEL],
    Capability.CUSTOM_WASHER_RINSE_CYCLES: [Command.SET_WASHER_RINSE_CYCLES],
    Capability.CUSTOM_WASHER_SOIL_LEVEL: [Command.SET_WASHER_SOIL_LEVEL],
    Capability.CUSTOM_WASHER_SPIN_LEVEL: [Command.SET_WASHER_SPIN_LEVEL],
    Capability.CUSTOM_WASHER_WATER_TEMPERATURE: [Command.SET_WASHER_WATER_TEMPERATURE],
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
    Capability.SAMSUNG_CE_WASHER_BUBBLE_SOAK: [Command.ON, Command.OFF],
    Capability.SAMSUNG_CE_WASHER_OPERATING_STATE: [
        Command.START,
        Command.CANCEL,
        Command.PAUSE,
        Command.RESUME,
        Command.ESTIMATE_OPERATION_TINE,
        Command.SET_DELAY_END,
    ],
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
    Capability.SAMSUNG_CE_DRYER_LABEL_SCAN_CYCLE_PRESET: [
        Command.SET_DRYER_LABEL_SCAN_CYCLE_PRESET,
        Command.DELETE,
    ],
}
