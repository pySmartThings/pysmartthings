"""Device control examples for pysmartthings.

This example demonstrates:
- Controlling switches (on/off)
- Dimming lights (0-100%)
- Setting color lights (RGB and hue/saturation)
- Controlling thermostats (temperature, mode)
- Checking device capabilities before executing commands
"""

import asyncio

from aiohttp import ClientSession

from pysmartthings import Capability, Command, SmartThings


async def control_switch(api: SmartThings, device_id: str) -> None:
    """Turn a switch on and off.

    Args:
        api: SmartThings API client
        device_id: Device ID to control

    """
    print("\nControlling Switch:")  # noqa: T201
    print("-" * 60)  # noqa: T201

    # Turn on
    print("  Turning switch ON...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH,
        command=Command.ON,
        argument=[],
    )
    print("  ✓ Switch is ON")  # noqa: T201

    # Wait a moment
    await asyncio.sleep(2)

    # Turn off
    print("  Turning switch OFF...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH,
        command=Command.OFF,
        argument=[],
    )
    print("  ✓ Switch is OFF")  # noqa: T201


async def control_dimmer(api: SmartThings, device_id: str) -> None:
    """Dim a light to different levels.

    Args:
        api: SmartThings API client
        device_id: Device ID to control

    """
    print("\nControlling Dimmer:")  # noqa: T201
    print("-" * 60)  # noqa: T201

    # Set to 100% (full brightness)
    print("  Setting brightness to 100%...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH_LEVEL,
        command=Command.SET_LEVEL,
        argument=[100],  # Brightness level (0-100)
    )
    print("  ✓ Brightness set to 100%")  # noqa: T201

    await asyncio.sleep(2)

    # Dim to 50%
    print("  Dimming to 50%...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH_LEVEL,
        command=Command.SET_LEVEL,
        argument=[50],
    )
    print("  ✓ Brightness set to 50%")  # noqa: T201

    await asyncio.sleep(2)

    # Dim to 10% (night light)
    print("  Setting to 10% (night light)...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH_LEVEL,
        command=Command.SET_LEVEL,
        argument=[10],
    )
    print("  ✓ Brightness set to 10%")  # noqa: T201


async def control_color_light(api: SmartThings, device_id: str) -> None:
    """Control a color-capable light.

    Args:
        api: SmartThings API client
        device_id: Device ID to control

    """
    print("\nControlling Color Light:")  # noqa: T201
    print("-" * 60)  # noqa: T201

    # Set color using hue/saturation (0-360 for hue, 0-100 for saturation)
    print("  Setting color to red (hue=0, saturation=100)...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.COLOR_CONTROL,
        command=Command.SET_COLOR,
        argument=[{"hue": 0, "saturation": 100}],
    )
    print("  ✓ Color set to red")  # noqa: T201

    await asyncio.sleep(2)

    print("  Setting color to blue (hue=240, saturation=100)...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.COLOR_CONTROL,
        command=Command.SET_COLOR,
        argument=[{"hue": 240, "saturation": 100}],
    )
    print("  ✓ Color set to blue")  # noqa: T201

    await asyncio.sleep(2)

    # Set to warm white (low saturation)
    print("  Setting to warm white (hue=30, saturation=20)...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.COLOR_CONTROL,
        command=Command.SET_COLOR,
        argument=[{"hue": 30, "saturation": 20}],
    )
    print("  ✓ Color set to warm white")  # noqa: T201

    # Set hue only (keep saturation unchanged)
    print("  Setting hue to green (120)...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.COLOR_CONTROL,
        command=Command.SET_HUE,
        argument=[120],
    )
    print("  ✓ Hue set to green")  # noqa: T201


async def control_thermostat(api: SmartThings, device_id: str) -> None:
    """Control a thermostat.

    Args:
        api: SmartThings API client
        device_id: Device ID to control

    """
    print("\nControlling Thermostat:")  # noqa: T201
    print("-" * 60)  # noqa: T201

    # Set heating setpoint (in Fahrenheit)
    print("  Setting heating setpoint to 68°F...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.THERMOSTAT_HEATING_SETPOINT,
        command=Command.SET_HEATING_SETPOINT,
        argument=[68],
    )
    print("  ✓ Heating setpoint set to 68°F")  # noqa: T201

    # Set cooling setpoint
    print("  Setting cooling setpoint to 74°F...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.THERMOSTAT_COOLING_SETPOINT,
        command=Command.SET_COOLING_SETPOINT,
        argument=[74],
    )
    print("  ✓ Cooling setpoint set to 74°F")  # noqa: T201

    # Set thermostat mode
    # Valid modes: "auto", "cool", "heat", "off", "emergency heat"
    print("  Setting mode to 'auto'...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.THERMOSTAT_MODE,
        command=Command.SET_THERMOSTAT_MODE,
        argument=["auto"],
    )
    print("  ✓ Mode set to 'auto'")  # noqa: T201

    # Set fan mode
    # Valid modes: "auto", "on", "circulate"
    print("  Setting fan mode to 'auto'...")  # noqa: T201
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.THERMOSTAT_FAN_MODE,
        command=Command.SET_THERMOSTAT_FAN_MODE,
        argument=["auto"],
    )
    print("  ✓ Fan mode set to 'auto'")  # noqa: T201


async def main() -> None:  # noqa: PLR0915, pylint: disable=too-many-statements
    """Demonstrate device control with pysmartthings."""
    token = "YOUR_TOKEN_HERE"  # noqa: S105

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)  # noqa: T201
        print("SmartThings Device Control Example")  # noqa: T201
        print("=" * 60)  # noqa: T201

        # Get all devices
        devices = await api.get_devices()
        print(f"\nFound {len(devices)} device(s)")  # noqa: T201

        # Find devices by capability
        switches = []
        dimmers = []
        color_lights = []
        thermostats = []

        for device in devices:
            if Capability.SWITCH in device.capabilities:  # type: ignore[attr-defined]
                switches.append(device)
            if Capability.SWITCH_LEVEL in device.capabilities:  # type: ignore[attr-defined]
                dimmers.append(device)
            if Capability.COLOR_CONTROL in device.capabilities:  # type: ignore[attr-defined]
                color_lights.append(device)
            if Capability.THERMOSTAT in device.capabilities:  # type: ignore[attr-defined]
                thermostats.append(device)

        print(f"\nFound {len(switches)} switch(es)")  # noqa: T201
        print(f"Found {len(dimmers)} dimmer(s)")  # noqa: T201
        print(f"Found {len(color_lights)} color light(s)")  # noqa: T201
        print(f"Found {len(thermostats)} thermostat(s)")  # noqa: T201

        # Control first switch if available
        if switches:
            print(f"\n{'=' * 60}")  # noqa: T201
            print(f"SWITCH: {switches[0].label}")  # noqa: T201
            print("=" * 60)  # noqa: T201
            await control_switch(api, switches[0].device_id)

        # Control first dimmer if available
        if dimmers:
            print(f"\n{'=' * 60}")  # noqa: T201
            print(f"DIMMER: {dimmers[0].label}")  # noqa: T201
            print("=" * 60)  # noqa: T201
            await control_dimmer(api, dimmers[0].device_id)

        # Control first color light if available
        if color_lights:
            print(f"\n{'=' * 60}")  # noqa: T201
            print(f"COLOR LIGHT: {color_lights[0].label}")  # noqa: T201
            print("=" * 60)  # noqa: T201
            await control_color_light(api, color_lights[0].device_id)

        # Control first thermostat if available
        if thermostats:
            print(f"\n{'=' * 60}")  # noqa: T201
            print(f"THERMOSTAT: {thermostats[0].label}")  # noqa: T201
            print("=" * 60)  # noqa: T201
            await control_thermostat(api, thermostats[0].device_id)

        # If no devices with these capabilities, show available capabilities
        if not switches and not dimmers and not color_lights and not thermostats:
            print("\nNo controllable devices found.")  # noqa: T201
            print("Available capabilities in your devices:")  # noqa: T201
            all_capabilities = set()
            for device in devices:
                all_capabilities.update(device.capabilities)  # type: ignore[attr-defined]
            for cap in sorted(all_capabilities):
                print(f"  - {cap}")  # noqa: T201

        print("\n" + "=" * 60)  # noqa: T201
        print("Example completed successfully!")  # noqa: T201
        print("=" * 60)  # noqa: T201


if __name__ == "__main__":
    asyncio.run(main())
