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


async def main() -> None:  # noqa: PLR0912, PLR0915, pylint: disable=too-many-locals,too-many-statements
    """Demonstrate basic pysmartthings usage."""
    # Replace with your SmartThings Personal Access Token
    # Get one at: https://account.smartthings.com/tokens
    token = "YOUR_TOKEN_HERE"  # noqa: S105

    # Create a client session (recommended for production)
    async with ClientSession() as session:
        # Initialize SmartThings API client
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)  # noqa: T201
        print("SmartThings Basic Usage Example")  # noqa: T201
        print("=" * 60)  # noqa: T201

        # List all locations
        print("\n1. Listing Locations:")  # noqa: T201
        print("-" * 60)  # noqa: T201
        locations = await api.get_locations()
        print(f"Found {len(locations)} location(s)")  # noqa: T201

        for location in locations:
            print(f"\n  Location: {location.name}")  # noqa: T201
            print(f"  ID: {location.location_id}")  # noqa: T201
            print(f"  Country: {location.country_code}")  # noqa: T201, type: ignore[attr-defined]
            if location.latitude and location.longitude:  # type: ignore[attr-defined]
                print(f"  Coordinates: {location.latitude}, {location.longitude}")  # noqa: T201, type: ignore[attr-defined]

        # Get detailed location information
        if locations:
            location_id = locations[0].location_id
            print(f"\n2. Getting Detailed Location Info for: {locations[0].name}")  # noqa: T201
            print("-" * 60)  # noqa: T201
            location = await api.get_location(location_id)
            print(f"  Name: {location.name}")  # noqa: T201
            print(f"  Time Zone: {location.time_zone_id}")  # noqa: T201, type: ignore[attr-defined]
            print(f"  Temperature Scale: {location.temperature_scale}")  # noqa: T201
            print(f"  Locale: {location.locale}")  # noqa: T201, type: ignore[attr-defined]

            # List rooms in this location
            print(f"\n3. Listing Rooms in {location.name}:")  # noqa: T201
            print("-" * 60)  # noqa: T201
            rooms = await api.get_rooms(location_id)
            print(f"Found {len(rooms)} room(s)")  # noqa: T201

            for room in rooms:
                print(f"\n  Room: {room.name}")  # noqa: T201
                print(f"  ID: {room.room_id}")  # noqa: T201

        # List all devices
        print("\n4. Listing All Devices:")  # noqa: T201
        print("-" * 60)  # noqa: T201
        devices = await api.get_devices()
        print(f"Found {len(devices)} device(s)")  # noqa: T201

        for device in devices:
            print(f"\n  Device: {device.label}")  # noqa: T201
            print(f"  ID: {device.device_id}")  # noqa: T201
            print(f"  Name: {device.name}")  # noqa: T201
            print(f"  Type: {device.type}")  # noqa: T201

            # Show capabilities
            if device.capabilities:  # type: ignore[attr-defined]
                print(f"  Capabilities ({len(device.capabilities)}):")  # noqa: T201, type: ignore[attr-defined]
                for cap in device.capabilities[  # type: ignore[attr-defined]
                    :5
                ]:  # Show first 5  # type: ignore[attr-defined]
                    print(f"    - {cap}")  # noqa: T201
                if len(device.capabilities) > 5:  # type: ignore[attr-defined]
                    print(f"    ... and {len(device.capabilities) - 5} more")  # noqa: T201, type: ignore[attr-defined]

        # Get detailed device information
        if devices:
            device = devices[0]
            print(f"\n5. Getting Detailed Info for: {device.label}")  # noqa: T201
            print("-" * 60)  # noqa: T201
            detailed_device = await api.get_device(device.device_id)
            print(f"  Label: {detailed_device.label}")  # noqa: T201
            print(f"  Device ID: {detailed_device.device_id}")  # noqa: T201
            print(f"  Device Type: {detailed_device.type}")  # noqa: T201
            print(f"  Network Type: {detailed_device.device_network_type}")  # noqa: T201

            if detailed_device.room_id:
                print(f"  Room ID: {detailed_device.room_id}")  # noqa: T201
            if detailed_device.location_id:
                print(f"  Location ID: {detailed_device.location_id}")  # noqa: T201

            # Show components (main, secondary, etc.)
            if detailed_device.components:
                print(f"  Components ({len(detailed_device.components)}):")  # noqa: T201
                for component in detailed_device.components:
                    # Show component ID and capability count
                    cap_count = len(component.capabilities)  # type: ignore[attr-defined]
                    print(f"    - {component.id}: {cap_count} capabilities")  # noqa: T201, type: ignore[attr-defined]

            # Get current device status
            print(f"\n6. Getting Current Status for: {device.label}")  # noqa: T201
            print("-" * 60)  # noqa: T201
            status = await api.get_device_status(device.device_id)
            print(f"  Device ID: {status.device_id}")  # noqa: T201, type: ignore[attr-defined]

            # Show status for main component
            if status.components and "main" in status.components:  # type: ignore[attr-defined]
                main_component = status.components["main"]  # type: ignore[attr-defined]
                print("  Main Component Status:")  # noqa: T201

                # Show a few key capabilities if available
                common_capabilities = [
                    "switch",
                    "switchLevel",
                    "temperatureMeasurement",
                    "contactSensor",
                    "motionSensor",
                ]

                for cap_name in common_capabilities:
                    if cap_name in main_component:
                        cap = main_component[cap_name]
                        print(f"\n    {cap_name}:")  # noqa: T201
                        # Show all attributes for this capability
                        for attr_name, attr_value in cap.items():
                            if hasattr(attr_value, "value"):
                                print(f"      {attr_name}: {attr_value.value}")  # noqa: T201

        print("\n" + "=" * 60)  # noqa: T201
        print("Example completed successfully!")  # noqa: T201
        print("=" * 60)  # noqa: T201


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
