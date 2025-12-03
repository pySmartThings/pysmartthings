"""Quick test script to verify SmartThings API connection."""

import asyncio
from pathlib import Path

from aiohttp import ClientSession

from pysmartthings import SmartThings


async def test_connection() -> None:
    """Test connection to SmartThings API and list devices."""
    # Load token from .env.local
    env_file = Path(__file__).parent / ".env.local"
    token = None

    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("SMARTTHINGS_TOKEN="):
                token = line.split("=", 1)[1]
                break

    if not token:
        print("❌ No token found in .env.local")  # noqa: T201
        return

    print(f"✅ Token loaded: {token[:8]}...")  # noqa: T201

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        try:
            # Test API connection by getting locations
            print("\n🔍 Testing API connection...")  # noqa: T201
            locations = await api.get_locations()
            print(f"✅ Connected! Found {len(locations)} location(s)")  # noqa: T201

            for location in locations:
                print(f"\n📍 Location: {location.name}")  # noqa: T201
                print(f"   ID: {location.location_id}")  # noqa: T201

            # Get devices
            print("\n🔍 Fetching devices...")  # noqa: T201
            devices = await api.get_devices()
            print(f"✅ Found {len(devices)} device(s)")  # noqa: T201

            if devices:
                print("\n📱 Your devices:")  # noqa: T201
                for device in devices:
                    print(f"   • {device.label or device.name}")  # noqa: T201
                    print(f"     Type: {device.device_type_name or 'Unknown'}")  # noqa: T201
                    print(f"     ID: {device.device_id}")  # noqa: T201
                    # Capabilities are in components (main component typically)
                    if device.components and "main" in device.components:
                        main_component = device.components["main"]
                        if main_component.capabilities:
                            caps = ", ".join(
                                str(c) for c in main_component.capabilities[:5]
                            )
                            if len(main_component.capabilities) > 5:
                                num_more = len(main_component.capabilities) - 5
                                caps += f", ... (+{num_more} more)"
                            print(f"     Capabilities: {caps}")  # noqa: T201
                    print()  # noqa: T201
            else:
                msg = "No devices found. "
                msg += "Make sure devices are connected to your SmartThings hub."
                print(f"   {msg}")  # noqa: T201

        except Exception as e:  # noqa: BLE001  # pylint: disable=broad-exception-caught
            print(f"❌ Error: {e}")  # noqa: T201
            print(f"   Type: {type(e).__name__}")  # noqa: T201


if __name__ == "__main__":
    asyncio.run(test_connection())
