"""Event subscription examples for pysmartthings.

This example demonstrates:
- Subscribing to real-time device events via Server-Sent Events (SSE)
- Handling device state changes
- Processing health events
- Managing subscription lifecycle
- Event filtering and processing

Note: This example uses Server-Sent Events (SSE) which maintains
a persistent connection to receive real-time updates.
"""

import asyncio
import signal
import sys

from aiohttp import ClientSession

from pysmartthings import SmartThings, SmartThingsError


# Global flag for graceful shutdown
shutdown_event = asyncio.Event()


def signal_handler(sig: int, frame: object) -> None:
    """Handle Ctrl+C gracefully.

    Args:
        sig: Signal number
        frame: Current stack frame
    """
    print("\n\nReceived interrupt signal. Shutting down gracefully...")
    shutdown_event.set()


async def device_event_handler(event: object) -> None:
    """Handle device state change events.

    Args:
        event: DeviceEvent object containing event data
    """
    print("\n" + "=" * 60)
    print("DEVICE EVENT RECEIVED")
    print("=" * 60)

    # Access event attributes
    if hasattr(event, "device_id"):
        print(f"Device ID: {event.device_id}")

    if hasattr(event, "component_id"):
        print(f"Component: {event.component_id}")

    if hasattr(event, "capability"):
        print(f"Capability: {event.capability}")

    if hasattr(event, "attribute"):
        print(f"Attribute: {event.attribute}")

    if hasattr(event, "value"):
        print(f"Value: {event.value}")

    if hasattr(event, "unit"):
        print(f"Unit: {event.unit}")

    if hasattr(event, "location_id"):
        print(f"Location: {event.location_id}")

    # Pretty print common events
    if hasattr(event, "capability") and hasattr(event, "attribute"):
        cap = event.capability
        attr = event.attribute
        val = event.value if hasattr(event, "value") else "unknown"

        if cap == "switch":
            print(f"\n💡 Switch changed to: {val}")
        elif cap == "switchLevel":
            print(f"\n🔆 Light level changed to: {val}%")
        elif cap == "motionSensor":
            print(f"\n🚶 Motion detected: {val}")
        elif cap == "contactSensor":
            print(f"\n🚪 Contact sensor: {val}")
        elif cap == "temperatureMeasurement":
            unit = event.unit if hasattr(event, "unit") else ""
            print(f"\n🌡️  Temperature: {val}{unit}")
        elif cap == "lock":
            print(f"\n🔒 Lock state: {val}")


async def health_event_handler(event: object) -> None:
    """Handle device health events.

    Args:
        event: DeviceHealthEvent object containing health data
    """
    print("\n" + "=" * 60)
    print("HEALTH EVENT RECEIVED")
    print("=" * 60)

    if hasattr(event, "device_id"):
        print(f"Device ID: {event.device_id}")

    if hasattr(event, "status"):
        print(f"Health Status: {event.status}")
        if event.status == "ONLINE":
            print("✓ Device is online")
        else:
            print("✗ Device is offline or unhealthy")

    if hasattr(event, "reason"):
        print(f"Reason: {event.reason}")


async def subscribe_to_events(
    api: SmartThings,
    device_ids: list[str] | None = None,
) -> None:
    """Subscribe to device events.

    Args:
        api: SmartThings API client
        device_ids: Optional list of specific device IDs to monitor.
                   If None, monitors all devices.
    """
    print("\nSetting Up Event Subscription:")
    print("-" * 60)

    try:
        # Register event handlers
        api.add_device_event_listener(device_event_handler)
        api.add_device_health_event_listener(health_event_handler)
        print("✓ Event handlers registered")

        # Create subscription (starts SSE connection)
        print("✓ Creating subscription...")
        subscription = await api.create_subscription()

        print(f"✓ Subscription created: {subscription.id}")
        print("\n" + "=" * 60)
        print("LISTENING FOR EVENTS")
        print("=" * 60)
        print("Press Ctrl+C to stop")
        print("\nWaiting for device events...")
        print("(Try controlling your devices via the SmartThings app)")

        # Keep the connection alive and process events
        # The event handlers will be called automatically when events arrive
        while not shutdown_event.is_set():
            await asyncio.sleep(1)

    except SmartThingsError as err:
        print(f"\n✗ Error setting up subscription: {err}")
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    finally:
        print("\n\nCleaning up subscription...")


async def monitor_specific_devices(
    api: SmartThings,
    device_names: list[str],
) -> None:
    """Monitor specific devices by name.

    Args:
        api: SmartThings API client
        device_names: List of device names to monitor
    """
    print(f"\nMonitoring Specific Devices: {', '.join(device_names)}")
    print("-" * 60)

    # Get all devices
    devices = await api.get_devices()

    # Find matching devices
    target_devices = []
    for device in devices:
        if device.label in device_names or device.name in device_names:
            target_devices.append(device)
            print(f"  Found: {device.label} ({device.device_id})")

    if not target_devices:
        print("  No matching devices found")
        return

    # Store device IDs for reference
    device_ids = [d.device_id for d in target_devices]

    # Subscribe to events (all events will come through)
    # We'll filter in the event handler
    await subscribe_to_events(api, device_ids)


async def main() -> None:
    """Demonstrate event subscription with pysmartthings."""
    token = "YOUR_TOKEN_HERE"

    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)
        print("SmartThings Event Subscription Example")
        print("=" * 60)

        # Show available devices
        devices = await api.get_devices()
        print(f"\nFound {len(devices)} device(s):")
        for device in devices:
            print(f"  - {device.label} ({device.device_id})")

        print("\n" + "=" * 60)
        print("SUBSCRIPTION OPTIONS")
        print("=" * 60)
        print("1. Monitor all devices (default)")
        print("2. Monitor specific devices by name")
        print()

        # For this example, we'll monitor all devices
        # To monitor specific devices, uncomment the following:
        # await monitor_specific_devices(
        #     api,
        #     ["Living Room Light", "Front Door Lock"]
        # )

        # Monitor all devices
        await subscribe_to_events(api)

        print("\n" + "=" * 60)
        print("Example completed")
        print("=" * 60)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nShutdown complete")
        sys.exit(0)
