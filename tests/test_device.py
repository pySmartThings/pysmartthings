"""Tests for the Device file."""

from __future__ import annotations
from typing import Any, TYPE_CHECKING

import pytest
from aiohttp.hdrs import METH_GET, METH_POST
from aioresponses import aioresponses
from yarl import URL

from pysmartthings import SmartThings
from pysmartthings.models import Capability, Command
from . import load_fixture, load_json_fixture

from .const import MOCK_URL, HEADERS

if TYPE_CHECKING:
    from syrupy import SnapshotAssertion


async def test_fetching_devices(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting devices."""
    responses.get(
        f"{MOCK_URL}/devices",
        status=200,
        body=load_fixture("devices_2.json"),
    )
    assert await client.get_devices() == snapshot
    responses.assert_called_once_with(
        f"{MOCK_URL}/devices",
        METH_GET,
        headers=HEADERS,
        params={},
        json=None,
    )


@pytest.mark.parametrize(
    ("kwargs", "params"),
    [
        ({"device_ids": ["abc", "def"]}, {"deviceId": "abc,def"}),
        ({"device_ids": ["abc"]}, {"deviceId": "abc"}),
        ({"location_ids": ["abc", "def"]}, {"locationId": "abc,def"}),
        (
            {"capabilities": [Capability.SWITCH, Capability.SWITCH_LEVEL]},
            {"capability": "switch,switchLevel"},
        ),
    ],
)
async def test_fetching_specific_devices(
    client: SmartThings,
    responses: aioresponses,
    kwargs: dict[str, Any],
    params: dict[str, Any],
) -> None:
    """Test getting devices."""
    url = str(URL(f"{MOCK_URL}/devices").with_query(params))
    responses.get(
        url,
        status=200,
        body=load_fixture("devices_2.json"),
    )
    assert await client.get_devices(**kwargs)
    responses.assert_called_once_with(
        f"{MOCK_URL}/devices",
        METH_GET,
        headers=HEADERS,
        params=params,
        json=None,
    )


async def test_fetching_single_device(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting a single device."""
    responses.get(
        f"{MOCK_URL}/devices/440063de-a200-40b5-8a6b-f3399eaa0370",
        status=200,
        body=load_fixture("device.json"),
    )
    assert await client.get_device("440063de-a200-40b5-8a6b-f3399eaa0370") == snapshot
    responses.assert_called_once_with(
        f"{MOCK_URL}/devices/440063de-a200-40b5-8a6b-f3399eaa0370",
        METH_GET,
        headers=HEADERS,
        params=None,
        json=None,
    )


@pytest.mark.parametrize(
    "fixture",
    [
        "hue_color_temperature_bulb",
        "hue_rgbw_color_bulb",
        "c2c_shade",
        "c2c_motion_2",
        "c2c_thermostat_bridge_1",
        "c2c_humidity",
        "c2c_switch",
    ],
)
async def test_fetching_status_of_single_device(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
    fixture: str,
) -> None:
    """Test getting a single device."""
    responses.get(
        f"{MOCK_URL}/devices/440063de-a200-40b5-8a6b-f3399eaa0370/status",
        status=200,
        body=load_fixture(f"device_status/{fixture}.json"),
    )
    assert (
        await client.get_device_status("440063de-a200-40b5-8a6b-f3399eaa0370")
        == snapshot
    )
    responses.assert_called_once_with(
        f"{MOCK_URL}/devices/440063de-a200-40b5-8a6b-f3399eaa0370/status",
        METH_GET,
        headers=HEADERS,
        params=None,
        json=None,
    )


@pytest.mark.parametrize(
    ("capability", "command", "argument", "fixture"),
    [
        (
            Capability.COLOR_TEMPERATURE,
            Command.SET_COLOR_TEMPERATURE,
            3000,
            "set_color_temperature",
        )
    ],
)
async def test_executing_command(
    client: SmartThings,
    responses: aioresponses,
    capability: Capability,
    command: Command,
    argument: int | str | list | dict | None,
    fixture: str,
) -> None:
    """Test executing a command."""
    responses.post(
        f"{MOCK_URL}/devices/440063de-a200-40b5-8a6b-f3399eaa0370/commands",
        status=200,
        body=load_fixture("executed_command.json"),
    )
    await client.execute_device_command(
        "440063de-a200-40b5-8a6b-f3399eaa0370", capability, command, argument=argument
    )
    responses.assert_called_once_with(
        f"{MOCK_URL}/devices/440063de-a200-40b5-8a6b-f3399eaa0370/commands",
        METH_POST,
        headers=HEADERS,
        params=None,
        json=load_json_fixture(f"device_commands/{fixture}.json"),
    )


# class TestDevice:
#     """Tests for the Device class."""
#
#     @staticmethod
#     def test_init() -> None:
#         """Tests whether the Device class initializes correctly."""
#         # Arrange/Act
#         device = Device()
#         # Assert
#         assert device.type == DEVICE_TYPE_UNKNOWN
#         assert not device.capabilities
#         assert not device.components
#
#     @staticmethod
#     def test_apply_data() -> None:
#         """Tests the apply data method."""
#         # Arrange
#         data = get_json("device.json")
#         device = Device()
#         # Act
#         device.apply_data(data)
#         # Assert
#         assert device.device_id == DEVICE_ID
#         assert device.name == "GE In-Wall Smart Dimmer"
#         assert device.label == "Front Porch Lights"
#         assert device.location_id == LOCATION_ID
#         assert device.room_id == ROOM_ID
#         assert device.type == DEVICE_TYPE_DTH
#         assert device.device_type_id == "8a9d4b1e3b9b1fe3013b9b206a7f000d"
#         assert device.device_type_name == "Dimmer Switch"
#         assert device.device_type_network == "ZWAVE"
#         assert device.capabilities == [
#             "switch",
#             "switchLevel",
#             "refresh",
#             "indicator",
#             "sensor",
#             "actuator",
#             "healthCheck",
#             "light",
#         ]
#         assert device.components == {
#             "bottomButton": ["button"],
#             "topButton": ["button"],
#         }
#
#     @staticmethod
#     def test_get_capability() -> None:
#         """Test the capability retrieval method."""
#         # Arrange
#         data = get_json("device.json")
#         device = Device()
#         # Act
#         device.apply_data(data)
#         # Assert
#         assert device.get_capability("switch", "light") == "switch"
#         assert device.get_capability("foo", "switch") == "switch"
#         assert device.get_capability("foo", "bar") is None
#
#
# class TestDeviceEntity:
#     """Tests for the DeviceEntity class."""
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_refresh(api) -> None:
#         """Tests the refresh method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         await device.refresh()
#         # Assert
#         assert device.label == "Front Porch Lights"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_save(api) -> None:
#         """Tests the save method."""
#         # Arrange
#         device = DeviceEntity(api)
#         # Act/Assert
#         with pytest.raises(NotImplementedError):
#             await device.save()
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_switch_on(api) -> None:
#         """Tests the switch_on method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.switch_on()
#         # Assert
#         assert result
#         assert not device.status.switch
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_switch_on_update(api) -> None:
#         """Tests the switch_on method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.switch_on(True)
#         # Assert
#         assert result
#         assert device.status.switch
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_switch_off(api) -> None:
#         """Tests the switch_on method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.switch = True
#         # Act
#         result = await device.switch_off()
#         # Assert
#         assert result
#         assert device.status.switch
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_switch_off_update(api) -> None:
#         """Tests the switch_on method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.switch = True
#         # Act
#         result = await device.switch_off(True)
#         # Assert
#         assert result
#         assert not device.status.switch
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_lock(api) -> None:
#         """Tests the lock method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.lock()
#         # Assert
#         assert result
#         assert not device.status.lock
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_lock_update(api) -> None:
#         """Tests the lock method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.lock(True)
#         # Assert
#         assert result
#         assert device.status.lock == "locked"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_unlock(api) -> None:
#         """Tests the unlock method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.unlock()
#         # Assert
#         assert result
#         assert not device.status.lock
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_unlock_update(api) -> None:
#         """Tests the unlock method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.unlock(True)
#         # Assert
#         assert result
#         assert device.status.lock == "unlocked"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_level(api) -> None:
#         """Tests the set_level method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_level(75, 2)
#         # Assert
#         assert result
#         assert device.status.level == 0
#         assert not device.status.switch
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_level_invalid(api) -> None:
#         """Tests the set_level method invalid values."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Assert level
#         levels = [-1, 101]
#         for level in levels:
#             with pytest.raises(ValueError):
#                 await device.set_level(level)
#         # Assert duration
#         with pytest.raises(ValueError):
#             await device.set_level(100, -1)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_level_update(api) -> None:
#         """Tests the set_level method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_level(75, 2, True)
#         # Assert
#         assert result
#         assert device.status.level == 75
#         assert device.status.switch
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_fan_speed(api) -> None:
#         """Tests the set_fan_speed method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_fan_speed(66)
#         # Assert
#         assert result
#         assert device.status.level == 0
#         assert not device.status.switch
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_fan_speed_invalid(api) -> None:
#         """Tests the set_fan_speed method invalid values."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Assert
#         with pytest.raises(ValueError):
#             await device.set_fan_speed(-1)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_fan_speed_update(api) -> None:
#         """Tests the set_fan_speed method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_fan_speed(66, True)
#         # Assert
#         assert result
#         assert device.status.fan_speed == 66
#         assert device.status.switch
#
#     @staticmethod
#     def test_status() -> None:
#         """Tests the set_level method."""
#         # Arrange
#         device = DeviceEntity(None, device_id=DEVICE_ID)
#         # Act
#         status = device.status
#         # Assert
#         assert status.device_id == DEVICE_ID
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color_temperature(api) -> None:
#         """Tests the set_color_temperature method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_color_temperature(3000)
#         # Assert
#         assert result
#         assert device.status.color_temperature == 1
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color_temperature_invalid(api) -> None:
#         """Tests the set_color_temperature method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         values = [0, 30001]
#         for value in values:
#             with pytest.raises(ValueError):
#                 await device.set_color_temperature(value)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color_temperature_update(api) -> None:
#         """Tests the set_color_temperature method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_color_temperature(3000, True)
#         # Assert
#         assert result
#         assert device.status.color_temperature == 3000
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_hue(api) -> None:
#         """Tests the set_hue method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_hue(75)
#         # Assert
#         assert result
#         assert device.status.hue == 0
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_hue_invalid(api) -> None:
#         """Tests the set_hue method invalid values."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Assert
#         levels = [-1, 101]
#         for level in levels:
#             with pytest.raises(ValueError):
#                 await device.set_hue(level)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_hue_update(api) -> None:
#         """Tests the set_hue method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_hue(75, True)
#         # Assert
#         assert result
#         assert device.status.hue == 75
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_saturation(api) -> None:
#         """Tests the set_saturation method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_saturation(75)
#         # Assert
#         assert result
#         assert device.status.saturation == 0
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_saturation_invalid(api) -> None:
#         """Tests the set_saturation method invalid values."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Assert
#         levels = [-1, 101]
#         for level in levels:
#             with pytest.raises(ValueError):
#                 await device.set_saturation(level)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_saturation_update(api) -> None:
#         """Tests the set_saturation method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_saturation(75, True)
#         # Assert
#         assert result
#         assert device.status.saturation == 75
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color(api) -> None:
#         """Tests the set_color method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_color(25, 50)
#         # Assert
#         assert result
#         assert device.status.hue == 0
#         assert device.status.saturation == 0
#         assert device.status.color is None
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color_invalid(api) -> None:
#         """Tests the set_saturation method invalid values."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Assert
#         values = [-1, 101]
#         for value in values:
#             with pytest.raises(ValueError):
#                 await device.set_color(value, 0)
#             with pytest.raises(ValueError):
#                 await device.set_color(0, value)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color_update(api) -> None:
#         """Tests the set_saturation method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_color(25, 50, set_status=True)
#         # Assert
#         assert result
#         assert device.status.hue == 25
#         assert device.status.saturation == 50
#         assert device.status.color == "#4B6432"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color_hex(api) -> None:
#         """Tests the set_color method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_color(color_hex="#4B6432")
#         # Assert
#         assert result
#         assert device.status.hue == 0
#         assert device.status.saturation == 0
#         assert device.status.color is None
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color_hex_invalid(api) -> None:
#         """Tests the set_color method invalid values."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Assert
#         values = ["000000", "#00000", "#G00000"]
#         for value in values:
#             with pytest.raises(ValueError):
#                 await device.set_color(color_hex=value)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_color_update_hex(api) -> None:
#         """Tests the set_saturation method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_color(color_hex="#4B6432", set_status=True)
#         # Assert
#         assert result
#         assert device.status.hue == 25
#         assert device.status.saturation == 50
#         assert device.status.color == "#4B6432"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_thermostat_fan_mode_legacy(api) -> None:
#         """Tests the set_saturation method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat)
#         device.status.thermostat_fan_mode = "on"
#         # Act
#         result = await device.set_thermostat_fan_mode("auto")
#         # Assert
#         assert result
#         assert device.status.thermostat_fan_mode != "auto"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_thermostat_fan_mode(api) -> None:
#         """Tests the set_saturation method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat_fan_mode)
#         device.status.thermostat_fan_mode = "on"
#         # Act
#         result = await device.set_thermostat_fan_mode("auto")
#         # Assert
#         assert result
#         assert device.status.thermostat_fan_mode != "auto"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_thermostat_fan_mode_update(api) -> None:
#         """Tests the set_saturation method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat_fan_mode)
#         device.status.thermostat_fan_mode = "on"
#         # Act
#         result = await device.set_thermostat_fan_mode("auto", set_status=True)
#         # Assert
#         assert result
#         assert device.status.thermostat_fan_mode == "auto"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_thermostat_mode_legacy(api) -> None:
#         """Tests the set_thermostat_mode method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat)
#         device.status.thermostat_mode = "heat"
#         # Act
#         result = await device.set_thermostat_mode("auto")
#         # Assert
#         assert result
#         assert device.status.thermostat_mode != "auto"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_thermostat_mode(api) -> None:
#         """Tests the set_thermostat_mode method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat_mode)
#         device.status.thermostat_mode = "heat"
#         # Act
#         result = await device.set_thermostat_mode("auto")
#         # Assert
#         assert result
#         assert device.status.thermostat_mode != "auto"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_thermostat_mode_update(api) -> None:
#         """Tests the set_thermostat_mode method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat_mode)
#         device.status.thermostat_mode = "heat"
#         # Act
#         result = await device.set_thermostat_mode("auto", set_status=True)
#         # Assert
#         assert result
#         assert device.status.thermostat_mode == "auto"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_cooling_setpoint_legacy(api) -> None:
#         """Tests the set_cooling_setpoint method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat)
#         device.status.cooling_setpoint = 70
#         # Act
#         result = await device.set_cooling_setpoint(76)
#         # Assert
#         assert result
#         assert device.status.cooling_setpoint != 76
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_cooling_setpoint_mode(api) -> None:
#         """Tests the set_cooling_setpoint method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat_cooling_setpoint)
#         device.status.cooling_setpoint = 70
#         # Act
#         result = await device.set_cooling_setpoint(76)
#         # Assert
#         assert result
#         assert device.status.cooling_setpoint != 76
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_cooling_setpoint_update(api) -> None:
#         """Tests the set_cooling_setpoint method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat_cooling_setpoint)
#         device.status.cooling_setpoint = 70
#         # Act
#         result = await device.set_cooling_setpoint(76, set_status=True)
#         # Assert
#         assert result
#         assert device.status.cooling_setpoint == 76
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_heating_setpoint_legacy(api) -> None:
#         """Tests the set_heating_setpoint method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat)
#         device.status.heating_setpoint = 70
#         # Act
#         result = await device.set_heating_setpoint(76)
#         # Assert
#         assert result
#         assert device.status.heating_setpoint != 76
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_heating_setpoint_mode(api) -> None:
#         """Tests the set_heating_setpoint method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat_heating_setpoint)
#         device.status.heating_setpoint = 70
#         # Act
#         result = await device.set_heating_setpoint(76)
#         # Assert
#         assert result
#         assert device.status.heating_setpoint != 76
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_heating_setpoint_update(api) -> None:
#         """Tests the set_heating_setpoint method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.thermostat_heating_setpoint)
#         device.status.heating_setpoint = 70
#         # Act
#         result = await device.set_heating_setpoint(76, set_status=True)
#         # Assert
#         assert result
#         assert device.status.heating_setpoint == 76
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_open(api) -> None:
#         """Tests the open method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.door_control)
#         # Act/Assert
#         assert await device.open()
#         assert device.status.door is None
#         assert await device.open(set_status=True)
#         assert device.status.door == "opening"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_open_legacy(api) -> None:
#         """Tests the open method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.garage_door_control)
#         # Act/Assert
#         assert await device.open()
#         assert device.status.door is None
#         assert await device.open(set_status=True)
#         assert device.status.door == "opening"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_close(api) -> None:
#         """Tests the close method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.door_control)
#         # Act/Assert
#         assert await device.close()
#         assert device.status.door is None
#         assert await device.close(set_status=True)
#         assert device.status.door == "closing"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_close_legacy(api) -> None:
#         """Tests the close method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.garage_door_control)
#         # Act/Assert
#         assert await device.close()
#         assert device.status.door is None
#         assert await device.close(set_status=True)
#         assert device.status.door == "closing"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_open_window_shade(api) -> None:
#         """Tests the open method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.window_shade)
#         # Act/Assert
#         assert await device.open()
#         assert device.status.window_shade is None
#         assert await device.open(set_status=True)
#         assert device.status.window_shade == "opening"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_close_window_shade(api) -> None:
#         """Tests the close method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.capabilities.append(Capability.window_shade)
#         # Act/Assert
#         assert await device.close()
#         assert device.status.window_shade is None
#         assert await device.close(set_status=True)
#         assert device.status.window_shade == "closing"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_request_drlc_action(api) -> None:
#         """Tests the request_drlc_action method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act/Assert
#         assert await device.request_drlc_action(1, 2, "1970-01-01T00:00:00Z", 10, 1)
#         assert device.status.drlc_status is None
#         assert await device.request_drlc_action(
#             1, 2, "1970-01-01T00:00:00Z", 10, 1, set_status=True
#         )
#         assert device.status.drlc_status == {
#             "duration": 10,
#             "drlcLevel": 2,
#             "start": "1970-01-01T00:00:00Z",
#             "override": False,
#         }
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_override_drlc_action(api) -> None:
#         """Tests the override_drlc_action method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act/Assert
#         assert await device.override_drlc_action(True)
#         assert device.status.drlc_status is None
#         assert await device.override_drlc_action(True, set_status=True)
#         assert device.status.drlc_status == {"override": True}
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_execute(api) -> None:
#         """Tests the execute method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act/Assert
#         assert await device.execute("Test", {"data": "Test"})
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_preset_position(api) -> None:
#         """Tests the preset_position method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act/Assert
#         assert await device.preset_position()
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_air_conditioner_mode(api) -> None:
#         """Tests the set_air_conditioner_mode method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act/Assert
#         assert await device.set_air_conditioner_mode("auto")
#         assert device.status.air_conditioner_mode is None
#         assert await device.set_air_conditioner_mode("auto", set_status=True)
#         assert device.status.air_conditioner_mode == "auto"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_fan_mode(api) -> None:
#         """Tests the set_fan_mode method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act/Assert
#         assert await device.set_fan_mode("auto")
#         assert device.status.fan_mode is None
#         assert await device.set_fan_mode("auto", set_status=True)
#         assert device.status.fan_mode == "auto"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_fan_oscillation_mode(api) -> None:
#         """Tests the set_fan_oscillation_mode method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act/Assert
#         assert await device.set_fan_oscillation_mode("all")
#         assert device.status.fan_oscillation_mode is None
#         assert await device.set_fan_oscillation_mode("all", set_status=True)
#         assert device.status.fan_oscillation_mode == "all"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_air_flow_direction(api) -> None:
#         """Tests the set_air_flow_direction method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act/Assert
#         assert await device.set_air_flow_direction("fixed")
#         assert device.status.air_flow_direction is None
#         assert await device.set_air_flow_direction("fixed", set_status=True)
#         assert device.status.air_flow_direction == "fixed"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_mute(api) -> None:
#         """Test the mute method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.mute = False
#         # Act
#         result = await device.mute()
#         # Assert
#         assert result
#         assert not device.status.mute
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_mute_update(api) -> None:
#         """Test the mute method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.mute = False
#         # Act
#         result = await device.mute(set_status=True)
#         # Assert
#         assert result
#         assert device.status.mute
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_unmute(api) -> None:
#         """Test the unmute method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.mute = True
#         # Act
#         result = await device.unmute()
#         # Assert
#         assert result
#         assert device.status.mute
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_unmute_update(api) -> None:
#         """Test the unmute method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.mute = True
#         # Act
#         result = await device.unmute(set_status=True)
#         # Assert
#         assert result
#         assert not device.status.mute
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_volume(api) -> None:
#         """Test the set_volume method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.volume = 9
#         # Act
#         result = await device.set_volume(volume=10)
#         # Assert
#         assert result
#         assert device.status.volume == 9
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_volume_update(api) -> None:
#         """Test the set_volume method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.volume = 9
#         # Act
#         result = await device.set_volume(volume=10, set_status=True)
#         # Assert
#         assert result
#         assert device.status.volume == 10
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_volume_up(api) -> None:
#         """Test the volume_up method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.volume = 9
#         # Act
#         result = await device.volume_up()
#         # Assert
#         assert result
#         assert device.status.volume == 9
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_volume_up_update(api) -> None:
#         """Test the volume_up method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.volume = 9
#         # Act
#         result = await device.volume_up(set_status=True)
#         # Assert
#         assert result
#         assert device.status.volume == 10
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_volume_down(api) -> None:
#         """Test the volume_down method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.volume = 11
#         # Act
#         result = await device.volume_down()
#         # Assert
#         assert result
#         assert device.status.volume == 11
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_volume_down_update(api) -> None:
#         """Test the volume_down method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.volume = 11
#         # Act
#         result = await device.volume_down(set_status=True)
#         # Assert
#         assert result
#         assert device.status.volume == 10
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_play(api) -> None:
#         """Test the play method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.play()
#         # Assert
#         assert result
#         assert device.status.playback_status is None
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_play_update(api) -> None:
#         """Test the play method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.play(set_status=True)
#         # Assert
#         assert result
#         assert device.status.playback_status == "play"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_pause(api) -> None:
#         """Test the pause method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.pause()
#         # Assert
#         assert result
#         assert device.status.playback_status is None
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_pause_update(api) -> None:
#         """Test the pause method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.pause(set_status=True)
#         # Assert
#         assert result
#         assert device.status.playback_status == "pause"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_stop(api) -> None:
#         """Test the stop method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.stop()
#         # Assert
#         assert result
#         assert device.status.playback_status is None
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_stop_update(api) -> None:
#         """Test the stop method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.stop(set_status=True)
#         # Assert
#         assert result
#         assert device.status.playback_status == "stop"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_fast_forward(api) -> None:
#         """Test the fast_forward method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.fast_forward()
#         # Assert
#         assert result
#         assert device.status.playback_status is None
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_fast_forward_update(api) -> None:
#         """Test the fast_forward method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.fast_forward(set_status=True)
#         # Assert
#         assert result
#         assert device.status.playback_status == "fast forward"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_rewind(api) -> None:
#         """Test the rewind method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.rewind()
#         # Assert
#         assert result
#         assert device.status.playback_status is None
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_rewind_update(api) -> None:
#         """Test the rewind method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_status = None
#         # Act
#         result = await device.rewind(set_status=True)
#         # Assert
#         assert result
#         assert device.status.playback_status == "rewind"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_input_source(api) -> None:
#         """Test the set_input_source method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.update_attribute_value(
#             Attribute.supported_input_sources, ["Source", "OtherSource"]
#         )
#         device.status.input_source = "OtherSource"
#         # Act
#         result = await device.set_input_source("Source")
#         # Assert
#         assert result
#         assert device.status.input_source == "OtherSource"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_input_source_update(api) -> None:
#         """Test the set_input_source method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.update_attribute_value(
#             Attribute.supported_input_sources, ["Source", "OtherSource"]
#         )
#         device.status.input_source = "OtherSource"
#         # Act
#         result = await device.set_input_source("Source", set_status=True)
#         # Assert
#         assert result
#         assert device.status.input_source == "Source"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_playback_shuffle(api) -> None:
#         """Test the set_playback_shuffle method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_shuffle = False
#         # Act
#         result = await device.set_playback_shuffle(shuffle=True)
#         # Assert
#         assert result
#         assert not device.status.playback_shuffle
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_playback_shuffle_update(api) -> None:
#         """Test the set_playback_shuffle method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_shuffle = False
#         # Act
#         result = await device.set_playback_shuffle(True, set_status=True)
#         # Assert
#         assert result
#         assert device.status.playback_shuffle
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_repeat(api) -> None:
#         """Test the set_repeat method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_repeat_mode = "off"
#         # Act
#         result = await device.set_repeat("all")
#         # Assert
#         assert result
#         assert device.status.playback_repeat_mode == "off"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_repeat_update(api) -> None:
#         """Test the set_repeat method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.playback_repeat_mode = "off"
#         # Act
#         result = await device.set_repeat("all", set_status=True)
#         # Assert
#         assert result
#         assert device.status.playback_repeat_mode == "all"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_tv_channel(api) -> None:
#         """Test the tv_channel method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.tv_channel = "OtherChannel"
#         # Act
#         result = await device.set_tv_channel("Channel")
#         # Assert
#         assert result
#         assert device.status.tv_channel == "OtherChannel"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_tv_channel_update(api) -> None:
#         """Test the tv_channel method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         device.status.tv_channel = "OtherChannel"
#         # Act
#         result = await device.set_tv_channel("Channel", set_status=True)
#         # Assert
#         assert result
#         assert device.status.tv_channel == "Channel"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_channel_up(api) -> None:
#         """Test the channel_up method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.channel_up()
#         # Assert
#         assert result
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_channel_down(api) -> None:
#         """Test the channel_down method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.channel_down()
#         # Assert
#         assert result
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_window_shade_level(api) -> None:
#         """Tests the set_window_shade_level method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_window_shade_level(75)
#         # Assert
#         assert result
#         assert device.status.level == 0
#         assert not device.status.switch
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_window_shade_level_invalid(api) -> None:
#         """Tests the set_window_shade_level method invalid values."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Assert level
#         levels = [-1, 101]
#         for level in levels:
#             with pytest.raises(ValueError):
#                 await device.set_window_shade_level(level)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_set_window_shade_level_update(api) -> None:
#         """Tests the set_window_shade_level method."""
#         # Arrange
#         device = DeviceEntity(api, device_id=DEVICE_ID)
#         # Act
#         result = await device.set_window_shade_level(75, True)
#         # Assert
#         assert result
#         assert device.status.shade_level == 75
#         assert device.status.switch
#
#
# class TestDeviceStatus:
#     """Tests for the DeviceStatus class."""
#
#     @staticmethod
#     def test_init() -> None:
#         """Tests the init method."""
#         # Arrange/Act
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Assert
#         assert status.device_id == DEVICE_ID
#         assert not status.attributes
#         assert not status.switch
#         assert not status.motion
#         assert status.level == 0
#         assert status.component_id == "main"
#
#     @staticmethod
#     def test_apply_data() -> None:
#         """Tests the apply_data method."""
#         # Arrange
#         data = get_json("device_status.json")
#         # Act
#         status = DeviceStatus(None, DEVICE_ID, data)
#         # Assert
#         assert len(status.attributes) == 9
#         assert status.switch
#         assert status.level == 100
#         assert len(status.components) == 2
#         assert len(status.components["topButton"].attributes) == 3
#         assert len(status.components["bottomButton"].attributes) == 3
#
#     @staticmethod
#     def test_apply_attribute_update() -> None:
#         """Tests the apply_attribute_update method."""
#         # Arrange
#         data = get_json("device_status.json")
#         device = DeviceStatus(None, DEVICE_ID, data)
#         # Act
#         device.apply_attribute_update(
#             "main", Capability.switch_level, Attribute.level, 50, "%", {"test": "test"}
#         )
#         # Assert
#         status = device.attributes[Attribute.level]
#         assert status.value == 50
#         assert status.unit == "%"
#         assert status.data == {"test": "test"}
#
#     @staticmethod
#     def test_apply_attribute_update_preserve_unit() -> None:
#         """Tests the apply_attribute_update preserves the old unit."""
#         # Arrange
#         data = get_json("device_status.json")
#         device = DeviceStatus(None, DEVICE_ID, data)
#         device.attributes[Capability.switch_level] = Status(40, "%", None)
#         # Act
#         device.apply_attribute_update(
#             "main", Capability.switch_level, Attribute.level, 50
#         )
#         # Assert
#         status = device.attributes[Attribute.level]
#         assert status.unit == "%"
#
#     @staticmethod
#     def test_apply_attribute_update_child_status() -> None:
#         """Tests the apply_attribute_update method to a child status."""
#         # Arrange
#         data = get_json("device_status.json")
#         status = DeviceStatus(None, DEVICE_ID, data)
#         # Act
#         status.apply_attribute_update("bottomButton", "switchLevel", "level", 50)
#         # Assert
#         assert status.components["bottomButton"].level == 50
#
#     @staticmethod
#     def test_values() -> None:
#         """Test the values property."""
#         # Arrange
#         data = get_json("device_status.json")
#         status = DeviceStatus(None, DEVICE_ID, data)
#         # Act/Assert
#         assert status.values == {
#             "button": None,
#             "numberOfButtons": None,
#             "supportedButtonValues": None,
#             "indicatorStatus": "when off",
#             "switch": "on",
#             "checkInterval": 1920,
#             "healthStatus": None,
#             "DeviceWatch-DeviceStatus": None,
#             "level": 100,
#         }
#
#     @staticmethod
#     def test_attributes() -> None:
#         """Test the attributes property."""
#         # Arrange
#         data = get_json("device_status.json")
#         status = DeviceStatus(None, DEVICE_ID, data)
#         # Act/Assert
#         assert status.attributes == {
#             "button": (None, None, None),
#             "numberOfButtons": (None, None, None),
#             "supportedButtonValues": (None, None, None),
#             "indicatorStatus": ("when off", None, None),
#             "switch": ("on", None, None),
#             "checkInterval": (
#                 1920,
#                 "s",
#                 {"protocol": "zwave", "hubHardwareId": "000F"},
#             ),
#             "healthStatus": (None, None, {}),
#             "DeviceWatch-DeviceStatus": (None, None, {}),
#             "level": (100, "%", None),
#         }
#
#     @staticmethod
#     def test_attributes_default() -> None:
#         """Test the attributes property."""
#         # Arrange
#         data = get_json("device_status.json")
#         status = DeviceStatus(None, DEVICE_ID, data)
#         # Act/Assert
#         assert status.attributes["thermostatSetpoint"] == (None, None, None)
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_refresh(api) -> None:
#         """Tests the refresh method."""
#         # Arrange
#         status = DeviceStatus(api, device_id=DEVICE_ID)
#         # Act
#         await status.refresh()
#         # Assert
#         assert len(status.attributes) == 9
#
#     @staticmethod
#     def test_switch() -> None:
#         """Tests the switch property."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act
#         status.switch = True
#         # Assert
#         assert status.switch
#
#     @staticmethod
#     def test_level() -> None:
#         """Tests the level property."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act
#         status.level = 50
#         # Assert
#         assert status.level == 50
#
#     @staticmethod
#     def test_level_range() -> None:
#         """Tests the level property's range."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act/Assert
#         values = [-1, 101]
#         for value in values:
#             with pytest.raises(ValueError):
#                 status.level = value
#
#     @staticmethod
#     def test_fan_speed() -> None:
#         """Tests the fan_speed property."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act
#         status.fan_speed = 50
#         # Assert
#         assert status.fan_speed == 50
#
#     @staticmethod
#     def test_fan_speed_range() -> None:
#         """Tests the fan_speed property's range."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act/Assert
#         with pytest.raises(ValueError):
#             status.fan_speed = -1
#
#     @staticmethod
#     def test_hue_range() -> None:
#         """Tests the hue property's range."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act/Assert
#         values = [-1, 101]
#         for value in values:
#             with pytest.raises(ValueError):
#                 status.hue = value
#
#     @staticmethod
#     def test_saturation_range() -> None:
#         """Tests the hue property's range."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act/Assert
#         values = [-1, 101]
#         for value in values:
#             with pytest.raises(ValueError):
#                 status.saturation = value
#
#     @staticmethod
#     def test_color_temperature_range() -> None:
#         """Tests the hue property's range."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act/Assert
#         values = [0, 30001]
#         for value in values:
#             with pytest.raises(ValueError):
#                 status.color_temperature = value
#
#     @staticmethod
#     def test_color_format() -> None:
#         """Tests the color property's validation."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act/Assert
#         values = ["000000", "#00000", "#HH2000"]
#         for value in values:
#             with pytest.raises(ValueError):
#                 status.color = value
#
#     @staticmethod
#     def test_volume_range(api) -> None:
#         """Test the volume property's range."""
#         # Arrange
#         status = DeviceStatus(api, device_id=DEVICE_ID)
#         # Act/Assert
#         values = [-1, 101]
#         for value in values:
#             with pytest.raises(ValueError):
#                 status.volume = value
#
#     @staticmethod
#     def test_input_source(api) -> None:
#         """Test the volume property's range."""
#         # Arrange
#         status = DeviceStatus(api, device_id=DEVICE_ID)
#         status.update_attribute_value(Attribute.supported_input_sources, "Source")
#         # Act/Assert
#         with pytest.raises(ValueError):
#             status.input_source = "INVALID"
#
#     @staticmethod
#     def test_playback_repeat_mode(api) -> None:
#         """Test the volume property's range."""
#         # Arrange
#         status = DeviceStatus(api, device_id=DEVICE_ID)
#         # Act/Assert
#         with pytest.raises(ValueError):
#             status.playback_repeat_mode = "INVALID"
#
#     @staticmethod
#     def test_is_on() -> None:
#         """Tests the is_on method."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         status.update_attribute_value(Attribute.acceleration, "active")
#         status.level = 100
#         # Act/Assert
#         assert status.is_on(Attribute.acceleration)
#         assert status.is_on(Attribute.level)
#         assert not status.is_on(Attribute.switch)
#
#     @staticmethod
#     def test_well_known_attributes() -> None:
#         """Tests the humidity property."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#
#         assert status.supported_ac_modes == []
#         assert status.supported_ac_fan_modes == []
#
#         status.update_attribute_value(Attribute.humidity, 50)
#         status.update_attribute_value(Attribute.temperature, 55)
#         status.update_attribute_value(Attribute.thermostat_operating_state, "on")
#         status.update_attribute_value(
#             Attribute.supported_thermostat_fan_modes, ["on", "off"]
#         )
#         status.update_attribute_value(
#             Attribute.supported_thermostat_modes, ["auto", "off"]
#         )
#         status.update_attribute_value(Attribute.lock, "locked")
#         status.update_attribute_value(Attribute.door, "open")
#         status.update_attribute_value(Attribute.window_shade, "closed")
#         status.update_attribute_value(Attribute.data, {"test": "test"})
#         status.update_attribute_value(Attribute.three_axis, [0, 0, 0])
#         status.update_attribute_value(Attribute.supported_ac_modes, ["auto", "cool"])
#         status.update_attribute_value(Attribute.fan_mode, "low")
#         status.update_attribute_value(Attribute.fan_oscillation_mode, "fixed")
#         status.update_attribute_value(Attribute.supported_ac_fan_modes, ["auto", "low"])
#         # Act/Assert
#         assert status.humidity == 50
#         assert status.temperature == 55
#         assert status.thermostat_operating_state == "on"
#         assert status.supported_thermostat_fan_modes == ["on", "off"]
#         assert status.supported_thermostat_modes == ["auto", "off"]
#         assert status.lock == "locked"
#         assert status.door == "open"
#         assert status.window_shade == "closed"
#         assert status.data == {"test": "test"}
#         assert status.three_axis == [0, 0, 0]
#         assert status.supported_ac_modes == ["auto", "cool"]
#         assert status.supported_ac_fan_modes == ["auto", "low"]
#
#     @staticmethod
#     def test_well_known_ocf_attributes() -> None:
#         """Tests the OCF related attributes."""
#         # Arrange
#         data = get_json("device_samsungac_status.json")
#         status = DeviceStatus(None, device_id=DEVICE_ID, data=data)
#         # Act/Assert
#         assert status.ocf_data_model_version == "res.1.1.0,sh.1.1.0"
#         assert status.ocf_date_of_manufacture == "2019-02-26T02:05:55Z"
#         assert status.ocf_device_id == DEVICE_ID
#         assert status.ocf_firmware_version == "0.1.0"
#         assert status.ocf_hardware_version == "1.0"
#         assert status.ocf_manufacturer_details_link == "http://www.samsung.com"
#         assert status.ocf_manufacturer_name == "Samsung Electronics"
#         assert (
#             status.ocf_model_number
#             == "ARTIK051_KRAC_18K|10193441|60010123001111010200000000000000"
#         )
#         assert status.ocf_name == "Air Conditioner"
#         assert status.ocf_os_version == "TizenRT2.0"
#         assert status.ocf_platform_id == "d5226d90-1b4f-e59d-5f3f-027ac3b18faf"
#         assert status.ocf_platform_version == "0.1.0"
#         assert status.ocf_spec_version == "core.1.1.0"
#         assert status.ocf_support_link == "http://www.samsung.com/support"
#         assert status.ocf_system_time == "02:05:55Z"
#         assert status.ocf_vendor_id == "DA-AC-RAC-000001"
#
#     @staticmethod
#     def test_well_known_drlc_attributes() -> None:
#         """Tests the drlc related attributes."""
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # No attribute
#         assert status.drlc_status is None
#         assert status.drlc_status_duration is None
#         assert status.drlc_status_level is None
#         assert status.drlc_status_override is None
#         assert status.drlc_status_start is None
#         # Populated
#         drlc_status = {
#             "duration": 0,
#             "drlcLevel": -1,
#             "start": "1970-01-01T00:00:00Z",
#             "override": False,
#         }
#         status.update_attribute_value(Attribute.drlc_status, drlc_status)
#         assert status.drlc_status == drlc_status
#         assert status.drlc_status_duration == 0
#         assert status.drlc_status_level == -1
#         assert not status.drlc_status_override
#         assert status.drlc_status_start == "1970-01-01T00:00:00Z"
#         # Missing
#         status.update_attribute_value(Attribute.drlc_status, {})
#         assert status.drlc_status == {}
#         assert status.drlc_status_duration is None
#         assert status.drlc_status_level is None
#         assert status.drlc_status_override is None
#         assert status.drlc_status_start is None
#         # Not valid
#         drlc_status = {"duration": "Foo", "drlcLevel": "Foo"}
#         status.update_attribute_value(Attribute.drlc_status, drlc_status)
#         assert status.drlc_status == drlc_status
#         assert status.drlc_status_duration is None
#         assert status.drlc_status_level is None
#
#     @staticmethod
#     def test_well_known_power_consumption_attributes() -> None:
#         """Tests the power consumption related attributes."""
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # No attribute
#         assert status.power_consumption is None
#         assert status.power_consumption_end is None
#         assert status.power_consumption_energy is None
#         assert status.power_consumption_power is None
#         assert status.power_consumption_start is None
#         assert status.power_consumption_delta_energy is None
#         assert status.power_consumption_energy_saved is None
#         assert status.power_consumption_persisted_energy is None
#         assert status.power_consumption_power_energy is None
#         # Populated
#         data = {
#             "start": "2019-02-24T21:03:04Z",
#             "power": 0,
#             "energy": 500,
#             "end": "2019-02-26T02:05:55Z",
#             "powerEnergy": 1.5,
#             "persistedEnergy": 100,
#             "energySaved": 50,
#             "deltaEnergy": 25,
#         }
#         status.update_attribute_value(Attribute.power_consumption, data)
#         assert status.power_consumption == data
#         assert status.power_consumption_end == "2019-02-26T02:05:55Z"
#         assert status.power_consumption_energy == 500
#         assert status.power_consumption_power == 0
#         assert status.power_consumption_start == "2019-02-24T21:03:04Z"
#         assert status.power_consumption_delta_energy == 25
#         assert status.power_consumption_energy_saved == 50
#         assert status.power_consumption_persisted_energy == 100
#         assert status.power_consumption_power_energy == 1.5
#         # Missing
#         status.update_attribute_value(Attribute.power_consumption, {})
#         assert status.power_consumption == {}
#         assert status.power_consumption_end is None
#         assert status.power_consumption_energy is None
#         assert status.power_consumption_power is None
#         assert status.power_consumption_start is None
#         assert status.power_consumption_delta_energy is None
#         assert status.power_consumption_energy_saved is None
#         assert status.power_consumption_persisted_energy is None
#         assert status.power_consumption_power_energy is None
#         # Minimal
#         data = {"deltaEnergy": 0, "power": 0, "energy": 60800}
#         status.update_attribute_value(Attribute.power_consumption, data)
#         assert status.power_consumption == data
#         assert status.power_consumption_end is None
#         assert status.power_consumption_energy == 60800
#         assert status.power_consumption_power == 0
#         assert status.power_consumption_start is None
#         assert status.power_consumption_delta_energy == 0
#         assert status.power_consumption_energy_saved is None
#         assert status.power_consumption_persisted_energy is None
#         assert status.power_consumption_power_energy is None
#         # Not valid
#         data = {"power": "Foo", "energy": "Bar"}
#         status.update_attribute_value(Attribute.power_consumption, data)
#         assert status.power_consumption == data
#         assert status.power_consumption_energy is None
#         assert status.power_consumption_power is None
#         assert status.power_consumption_delta_energy is None
#         assert status.power_consumption_energy_saved is None
#         assert status.power_consumption_persisted_energy is None
#         assert status.power_consumption_power_energy is None
#
#     @staticmethod
#     def test_shade_level() -> None:
#         """Tests the shade_level property."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act
#         status.shade_level = 50
#         # Assert
#         assert status.shade_level == 50
#
#     @staticmethod
#     def test_shade_level_range() -> None:
#         """Tests the shade_level property's range."""
#         # Arrange
#         status = DeviceStatus(None, device_id=DEVICE_ID)
#         # Act/Assert
#         values = [-1, 101]
#         for value in values:
#             with pytest.raises(ValueError):
#                 status.shade_level = value
