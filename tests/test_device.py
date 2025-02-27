"""Tests for the Device file."""

from __future__ import annotations

import logging
import re
from typing import Any, TYPE_CHECKING

import pytest
from aiohttp.hdrs import METH_GET, METH_POST
from aioresponses import aioresponses
from yarl import URL

from pysmartthings import SmartThings, Capability, Command, SmartThingsCommandError
from . import load_fixture, load_json_fixture

from .const import MOCK_URL, HEADERS

if TYPE_CHECKING:
    from syrupy import SnapshotAssertion


@pytest.mark.parametrize(
    "fixture",
    [
        "devices_2",
        "devices_3",
        "devices_4",
        "devices_5",
        "devices_6",
        "devices_7",
        "devices_8",
        "devices_9",
        "devices_10",
        "devices_11",
        "devices_12",
        "devices_13",
        "devices_14",
        "devices_15",
        "devices_fake",
    ],
)
async def test_fetching_devices(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
    fixture: str,
) -> None:
    """Test getting devices."""
    responses.get(
        f"{MOCK_URL}/devices",
        status=200,
        body=load_fixture(f"{fixture}.json"),
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
        "da_ks_range_0101x",
        "da_ks_walloven_000003",
        "da_wm_wd_00001",
        "da_wm_dw_00001",
        "da_ks_microwave_0101x",
        "da_ref_normal_01001",
        "da_ref_normal_01011",
        "da_ref_normal_01011_1",
        "da_ref_normal_000001",
        "da_rvc_normal_000001",
        "da_wm_wm_000001",
        "da_wm_wm_000001_2",
        "da_wm_wm_000001_3",
        "da_wm_sc_000001",
        "hub",
        "im_smarttag_ble_uwb",
        "im_smarttag2_ble_uwb",
        "da_ac_rac_01001",
        "da_ac_rac_000001",
        "da_ac_rac_000003",
        "da_sac_wifikit_000001",
        "vd_network_audio_002s",
        "vd_network_audio_003s",
        "c2c_arlo_pro_3_switch",
        "switch_level",
        "centralite",
        "sengled",
        "ikea_floor_lamp",
        "ge_in_wall_smart_dimmer",
        "zooz_zen16_multirelay",
        "c2c_arlo_go_switch",
        "multipurpose_sensor",
        "yale_push_button_deadbolt_lock",
        "27_smart_monitor_m5",
        "contact_sensor",
        "ge_dimmer_assoc",
        "car_garage_door",
        "ikea_e26",
        "switch_binary_indicator",
        "ledvance_switch",
        "basic_electric_meter",
        "iphone",
        "vd_stv_2017_k",
        "vd_stv_2021",
        "vd_stv_2022",
        "vd_stv_2023",
        "vd_stv_2023_1",
        "vd_frame_2024",
        "vd_sensor_light_2023",
        "vd_sensor_sound_2023",
        "virtual_calendar",
        "c2c_arlo_siren",
        "c2c_arlo_doorbell_battery",
        "ikea_remote_control",
        "base_lock",
        "main_virtual_device",
        "soundbar_hw_q80_r",
        "sensibo_airconditioner_1",
        "aeotec_home_energy_meter_gen5",
        "virtual_water_sensor",
        "virtual_thermostat",
        "virtual_valve",
        "ecobee_thermostat",
        "ecobee_sensor",
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
    argument: int | str | list[Any] | dict[str, Any] | None,
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


async def test_executing_command_error(
    client: SmartThings,
    responses: aioresponses,
) -> None:
    """Test executing a command."""
    responses.post(
        f"{MOCK_URL}/devices/440063de-a200-40b5-8a6b-f3399eaa0370/commands",
        status=422,
        body=load_fixture("device_command_error.json"),
    )
    with pytest.raises(
        SmartThingsCommandError,
        match=re.escape(
            "SmartThingsCommandError (ConstraintViolationError, The request is malformed.) -> UnprocessableEntityError: commands[0].arguments[0]: must have a maximum value of 30000"
        ),
    ):
        await client.execute_device_command(
            "440063de-a200-40b5-8a6b-f3399eaa0370",
            Capability.COLOR_TEMPERATURE,
            Command.SET_COLOR_TEMPERATURE,
            argument=300000,
        )


async def test_fetching_unknown_capability(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test getting a single device."""
    caplog.set_level(logging.DEBUG)
    responses.get(
        f"{MOCK_URL}/devices/440063de-a200-40b5-8a6b-f3399eaa0370/status",
        status=200,
        body=load_fixture("device_status/fake.json"),
    )
    assert (
        await client.get_device_status("440063de-a200-40b5-8a6b-f3399eaa0370")
        == snapshot
    )
    assert (
        "Unknown capability fakeCapability. Please raise an issue at https://github.com/pySmartThings/pysmartthings."
        in caplog.text
    )
