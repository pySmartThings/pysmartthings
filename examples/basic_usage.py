"""Basic usage examples for pysmartthings.

This example demonstrates:
- Creating and authenticating a SmartThings client
- Listing all devices
- Getting detailed device information
- Checking device status
- Listing locations and rooms
"""

import asyncio

from aiohttp import ClientSession

from pysmartthings import SmartThings


async def main() -> None:
    """Demonstrate basic pysmartthings usage."""
    # Replace with your SmartThings Personal Access Token
    # Get one at: https://account.smartthings.com/tokens
    token = "YOUR_TOKEN_HERE"

    # Create a client session (recommended for production)
    async with ClientSession() as session:
        # Initialize SmartThings API client
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)
        print("SmartThings Basic Usage Example")
        print("=" * 60)

        # List all locations
        print("\n1. Listing Locations:")
        print("-" * 60)
        locations = await api.get_locations()
        print(f"Found {len(locations)} location(s)")

        for location in locations:
            print(f"\n  Location: {location.name}")
            print(f"  ID: {location.location_id}")
            print(f"  Country: {location.country_code}")
            if location.latitude and location.longitude:
                print(
                    f"  Coordinates: {location.latitude}, {location.longitude}"
                )

        # Get detailed location information
        if locations:
            location_id = locations[0].location_id
            print(f"\n2. Getting Detailed Location Info for: {locations[0].name}")
            print("-" * 60)
            location = await api.get_location(location_id)
            print(f"  Name: {location.name}")
            print(f"  Time Zone: {location.time_zone_id}")
            print(f"  Temperature Scale: {location.temperature_scale}")
            print(f"  Locale: {location.locale}")

            # List rooms in this location
            print(f"\n3. Listing Rooms in {location.name}:")
            print("-" * 60)
            rooms = await api.get_rooms(location_id)
            print(f"Found {len(rooms)} room(s)")

            for room in rooms:
                print(f"\n  Room: {room.name}")
                print(f"  ID: {room.room_id}")

        # List all devices
        print("\n4. Listing All Devices:")
        print("-" * 60)
        devices = await api.get_devices()
        print(f"Found {len(devices)} device(s)")

        for device in devices:
            print(f"\n  Device: {device.label}")
            print(f"  ID: {device.device_id}")
            print(f"  Name: {device.name}")
            print(f"  Type: {device.type}")

            # Show capabilities
            if device.capabilities:
                print(f"  Capabilities ({len(device.capabilities)}):")
                for cap in device.capabilities[:5]:  # Show first 5
                    print(f"    - {cap}")
                if len(device.capabilities) > 5:
                    print(
                        f"    ... and {len(device.capabilities) - 5} more"
                    )

        # Get detailed device information
        if devices:
            device = devices[0]
            print(f"\n5. Getting Detailed Info for: {device.label}")
            print("-" * 60)
            detailed_device = await api.get_device(device.device_id)
            print(f"  Label: {detailed_device.label}")
            print(f"  Device ID: {detailed_device.device_id}")
            print(f"  Device Type: {detailed_device.type}")
            print(f"  Network Type: {detailed_device.device_network_type}")

            if detailed_device.room_id:
                print(f"  Room ID: {detailed_device.room_id}")
            if detailed_device.location_id:
                print(f"  Location ID: {detailed_device.location_id}")

            # Show components (main, secondary, etc.)
            if detailed_device.components:
                print(
                    f"  Components ({len(detailed_device.components)}):"
                )
                for component in detailed_device.components:
                    print(f"    - {component.id}: {len(component.capabilities)} capabilities")

            # Get current device status
            print(f"\n6. Getting Current Status for: {device.label}")
            print("-" * 60)
            status = await api.get_device_status(device.device_id)
            print(f"  Device ID: {status.device_id}")

            # Show status for main component
            if status.components and "main" in status.components:
                main = status.components["main"]
                print("  Main Component Status:")

                # Show a few key capabilities if available
                common_capabilities = [
                    "switch",
                    "switchLevel",
                    "temperatureMeasurement",
                    "contactSensor",
                    "motionSensor",
                ]

                for cap_name in common_capabilities:
                    if cap_name in main:
                        cap = main[cap_name]
                        print(f"\n    {cap_name}:")
                        # Show all attributes for this capability
                        for attr_name, attr_value in cap.items():
                            if hasattr(attr_value, "value"):
                                print(f"      {attr_name}: {attr_value.value}")

        print("\n" + "=" * 60)
        print("Example completed successfully!")
        print("=" * 60)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
