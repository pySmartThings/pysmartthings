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
    print("\nControlling Switch:")
    print("-" * 60)

    # Turn on
    print("  Turning switch ON...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH,
        command=Command.ON,
        args=[],
    )
    print("  ✓ Switch is ON")

    # Wait a moment
    await asyncio.sleep(2)

    # Turn off
    print("  Turning switch OFF...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH,
        command=Command.OFF,
        args=[],
    )
    print("  ✓ Switch is OFF")


async def control_dimmer(api: SmartThings, device_id: str) -> None:
    """Dim a light to different levels.

    Args:
        api: SmartThings API client
        device_id: Device ID to control
    """
    print("\nControlling Dimmer:")
    print("-" * 60)

    # Set to 100% (full brightness)
    print("  Setting brightness to 100%...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH_LEVEL,
        command=Command.SET_LEVEL,
        args=[100],  # Brightness level (0-100)
    )
    print("  ✓ Brightness set to 100%")

    await asyncio.sleep(2)

    # Dim to 50%
    print("  Dimming to 50%...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH_LEVEL,
        command=Command.SET_LEVEL,
        args=[50],
    )
    print("  ✓ Brightness set to 50%")

    await asyncio.sleep(2)

    # Dim to 10% (night light)
    print("  Setting to 10% (night light)...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.SWITCH_LEVEL,
        command=Command.SET_LEVEL,
        args=[10],
    )
    print("  ✓ Brightness set to 10%")


async def control_color_light(api: SmartThings, device_id: str) -> None:
    """Control a color-capable light.

    Args:
        api: SmartThings API client
        device_id: Device ID to control
    """
    print("\nControlling Color Light:")
    print("-" * 60)

    # Set color using hue/saturation
    # Hue: 0-360 (red=0, green=120, blue=240)
    # Saturation: 0-100 (0=white, 100=full color)
    print("  Setting color to red (hue=0, saturation=100)...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.COLOR_CONTROL,
        command=Command.SET_COLOR,
        args=[{"hue": 0, "saturation": 100}],
    )
    print("  ✓ Color set to red")

    await asyncio.sleep(2)

    print("  Setting color to blue (hue=240, saturation=100)...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.COLOR_CONTROL,
        command=Command.SET_COLOR,
        args=[{"hue": 240, "saturation": 100}],
    )
    print("  ✓ Color set to blue")

    await asyncio.sleep(2)

    # Set to warm white (low saturation)
    print("  Setting to warm white (hue=30, saturation=20)...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.COLOR_CONTROL,
        command=Command.SET_COLOR,
        args=[{"hue": 30, "saturation": 20}],
    )
    print("  ✓ Color set to warm white")

    # Set hue only (keep saturation unchanged)
    print("  Setting hue to green (120)...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.COLOR_CONTROL,
        command=Command.SET_HUE,
        args=[120],
    )
    print("  ✓ Hue set to green")


async def control_thermostat(api: SmartThings, device_id: str) -> None:
    """Control a thermostat.

    Args:
        api: SmartThings API client
        device_id: Device ID to control
    """
    print("\nControlling Thermostat:")
    print("-" * 60)

    # Set heating setpoint (in Fahrenheit)
    print("  Setting heating setpoint to 68°F...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.THERMOSTAT_HEATING_SETPOINT,
        command=Command.SET_HEATING_SETPOINT,
        args=[68],
    )
    print("  ✓ Heating setpoint set to 68°F")

    # Set cooling setpoint
    print("  Setting cooling setpoint to 74°F...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.THERMOSTAT_COOLING_SETPOINT,
        command=Command.SET_COOLING_SETPOINT,
        args=[74],
    )
    print("  ✓ Cooling setpoint set to 74°F")

    # Set thermostat mode
    # Valid modes: "auto", "cool", "heat", "off", "emergency heat"
    print("  Setting mode to 'auto'...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.THERMOSTAT_MODE,
        command=Command.SET_THERMOSTAT_MODE,
        args=["auto"],
    )
    print("  ✓ Mode set to 'auto'")

    # Set fan mode
    # Valid modes: "auto", "on", "circulate"
    print("  Setting fan mode to 'auto'...")
    await api.execute_device_command(
        device_id=device_id,
        capability=Capability.THERMOSTAT_FAN_MODE,
        command=Command.SET_THERMOSTAT_FAN_MODE,
        args=["auto"],
    )
    print("  ✓ Fan mode set to 'auto'")


async def main() -> None:
    """Demonstrate device control with pysmartthings."""
    token = "YOUR_TOKEN_HERE"

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)
        print("SmartThings Device Control Example")
        print("=" * 60)

        # Get all devices
        devices = await api.get_devices()
        print(f"\nFound {len(devices)} device(s)")

        # Find devices by capability
        switches = []
        dimmers = []
        color_lights = []
        thermostats = []

        for device in devices:
            if Capability.SWITCH in device.capabilities:
                switches.append(device)
            if Capability.SWITCH_LEVEL in device.capabilities:
                dimmers.append(device)
            if Capability.COLOR_CONTROL in device.capabilities:
                color_lights.append(device)
            if Capability.THERMOSTAT in device.capabilities:
                thermostats.append(device)

        print(f"\nFound {len(switches)} switch(es)")
        print(f"Found {len(dimmers)} dimmer(s)")
        print(f"Found {len(color_lights)} color light(s)")
        print(f"Found {len(thermostats)} thermostat(s)")

        # Control first switch if available
        if switches:
            print(f"\n{'=' * 60}")
            print(f"SWITCH: {switches[0].label}")
            print("=" * 60)
            await control_switch(api, switches[0].device_id)

        # Control first dimmer if available
        if dimmers:
            print(f"\n{'=' * 60}")
            print(f"DIMMER: {dimmers[0].label}")
            print("=" * 60)
            await control_dimmer(api, dimmers[0].device_id)

        # Control first color light if available
        if color_lights:
            print(f"\n{'=' * 60}")
            print(f"COLOR LIGHT: {color_lights[0].label}")
            print("=" * 60)
            await control_color_light(api, color_lights[0].device_id)

        # Control first thermostat if available
        if thermostats:
            print(f"\n{'=' * 60}")
            print(f"THERMOSTAT: {thermostats[0].label}")
            print("=" * 60)
            await control_thermostat(api, thermostats[0].device_id)

        # If no devices with these capabilities, show available capabilities
        if not switches and not dimmers and not color_lights and not thermostats:
            print("\nNo controllable devices found.")
            print("Available capabilities in your devices:")
            all_capabilities = set()
            for device in devices:
                all_capabilities.update(device.capabilities)
            for cap in sorted(all_capabilities):
                print(f"  - {cap}")

        print("\n" + "=" * 60)
        print("Example completed successfully!")
        print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
