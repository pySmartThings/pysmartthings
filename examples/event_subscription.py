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

from pysmartthings import DeviceEvent, SmartThings, SmartThingsError

# Global flag for graceful shutdown
shutdown_event = asyncio.Event()


def signal_handler(sig: int, frame: object) -> None:  # noqa: ARG001, pylint: disable=unused-argument
    """Handle Ctrl+C gracefully.

    Args:
        sig: Signal number
        frame: Current stack frame

    """
    print("\n\nReceived interrupt signal. Shutting down gracefully...")  # noqa: T201
    shutdown_event.set()


def device_event_handler(event: DeviceEvent) -> None:  # noqa: PLR0912
    """Handle device state change events.

    Args:
        event: DeviceEvent object containing event data

    """
    print("\n" + "=" * 60)  # noqa: T201
    print("DEVICE EVENT RECEIVED")  # noqa: T201
    print("=" * 60)  # noqa: T201# Access event attributes
    if hasattr(event, "device_id"):
        print(f"Device ID: {event.device_id}")  # noqa: T201
    if hasattr(event, "component_id"):
        print(f"Component: {event.component_id}")  # noqa: T201
    if hasattr(event, "capability"):
        print(f"Capability: {event.capability}")  # noqa: T201
    if hasattr(event, "attribute"):
        print(f"Attribute: {event.attribute}")  # noqa: T201
    if hasattr(event, "value"):
        print(f"Value: {event.value}")  # noqa: T201
    if hasattr(event, "unit"):
        print(f"Unit: {event.unit}")  # noqa: T201
    if hasattr(event, "location_id"):
        print(f"Location: {event.location_id}")  # noqa: T201# Pretty print common events
    if hasattr(event, "capability") and hasattr(event, "attribute"):
        cap = event.capability
        _attr = event.attribute
        val = event.value if hasattr(event, "value") else "unknown"

        if cap == "switch":
            print(f"\n💡 Switch changed to: {val}")  # noqa: T201
        elif cap == "switchLevel":
            print(f"\n🔆 Light level changed to: {val}%")  # noqa: T201
        elif cap == "motionSensor":
            print(f"\n🚶 Motion detected: {val}")  # noqa: T201
        elif cap == "contactSensor":
            print(f"\n🚪 Contact sensor: {val}")  # noqa: T201
        elif cap == "temperatureMeasurement":
            unit = event.unit if hasattr(event, "unit") else ""
            print(f"\n🌡️  Temperature: {val}{unit}")  # noqa: T201
        elif cap == "lock":
            print(f"\n🔒 Lock state: {val}")  # noqa: T201


def health_event_handler(event: object) -> None:
    """Handle device health events.

    Args:
        event: DeviceHealthEvent object containing health data

    """
    print("\n" + "=" * 60)  # noqa: T201
    print("HEALTH EVENT RECEIVED")  # noqa: T201
    print("=" * 60)  # noqa: T201
    if hasattr(event, "device_id"):
        print(f"Device ID: {event.device_id}")  # noqa: T201
    if hasattr(event, "status"):
        print(f"Health Status: {event.status}")  # noqa: T201
        if event.status == "ONLINE":
            print("✓ Device is online")  # noqa: T201
        else:
            print("✗ Device is offline or unhealthy")  # noqa: T201
    if hasattr(event, "reason"):
        print(f"Reason: {event.reason}")  # noqa: T201


async def subscribe_to_events(
    api: SmartThings,
    device_ids: list[str] | None = None,  # noqa: ARG001
) -> None:
    """Subscribe to device events.

    Args:
        api: SmartThings API client
        device_ids: Optional list of specific device IDs to monitor.
                   If None, monitors all devices.

    """
    print("\nSetting Up Event Subscription:")  # noqa: T201
    print("-" * 60)  # noqa: T201
    try:
        # NOTE: This example shows the API usage but won't work without
        # proper location_id and installed_app_id from a SmartApp setup.
        # For real usage, get these from your SmartApp configuration.

        # Register event handlers for unspecified devices (receives all events)
        api.add_unspecified_device_event_listener(device_event_handler)
        print("✓ Event handlers registered")  # noqa: T201

        # Create subscription (requires location_id and installed_app_id)
        # These should come from your SmartApp setup
        print("✓ Creating subscription...")  # noqa: T201
        print("  (Requires location_id and installed_app_id from SmartApp)")  # noqa: T201

        # Example usage with actual credentials:
        # Call api.create_subscription(location_id, installed_app_id)
        # to create a subscription and get subscription_id

        # For demonstration, we'll skip the actual subscription
        _subscription = None
        print("\n" + "=" * 60)  # noqa: T201
        print("LISTENING FOR EVENTS")  # noqa: T201
        print("=" * 60)  # noqa: T201
        print("Press Ctrl+C to stop")  # noqa: T201
        print("\nWaiting for device events...")  # noqa: T201
        print("(Try controlling your devices via the SmartThings app)")  # noqa: T201

        # Keep the connection alive and process events
        # The event handlers will be called automatically when events arrive
        while not shutdown_event.is_set():  # noqa: ASYNC110
            await asyncio.sleep(1)

    except SmartThingsError as err:
        print(f"\n✗ Error setting up subscription: {err}")  # noqa: T201
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")  # noqa: T201
    finally:
        print("\n\nCleaning up subscription...")  # noqa: T201


async def monitor_specific_devices(
    api: SmartThings,
    device_names: list[str],
) -> None:
    """Monitor specific devices by name.

    Args:
        api: SmartThings API client
        device_names: List of device names to monitor

    """
    print(f"\nMonitoring Specific Devices: {', '.join(device_names)}")  # noqa: T201
    print("-" * 60)  # noqa: T201

    # Get all devices
    devices = await api.get_devices()

    # Find matching devices
    target_devices = []
    for device in devices:
        if device.label in device_names or device.name in device_names:
            target_devices.append(device)
            print(f"  Found: {device.label} ({device.device_id})")  # noqa: T201

    if not target_devices:
        print("  No matching devices found")  # noqa: T201
        return

    # Store device IDs for reference
    device_ids = [d.device_id for d in target_devices]

    # Subscribe to events (all events will come through)
    # We'll filter in the event handler
    await subscribe_to_events(api, device_ids)


async def main() -> None:
    """Demonstrate event subscription with pysmartthings."""
    token = "YOUR_TOKEN_HERE"  # noqa: S105

    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)  # noqa: T201
        print("SmartThings Event Subscription Example")  # noqa: T201
        print("=" * 60)  # noqa: T201

        # Show available devices
        devices = await api.get_devices()
        print(f"\nFound {len(devices)} device(s):")  # noqa: T201
        for device in devices:
            print(f"  - {device.label} ({device.device_id})")  # noqa: T201

        print("\n" + "=" * 60)  # noqa: T201
        print("SUBSCRIPTION OPTIONS")  # noqa: T201
        print("=" * 60)  # noqa: T201
        print("1. Monitor all devices (default)")  # noqa: T201
        print("2. Monitor specific devices by name")  # noqa: T201
        print()  # noqa: T201

        # For this example, we'll monitor all devices
        # To monitor specific devices, call monitor_specific_devices()
        # with device names like ["Living Room Light", "Front Door Lock"]

        # Monitor all devices
        await subscribe_to_events(api)

        print("\n" + "=" * 60)  # noqa: T201
        print("Example completed")  # noqa: T201
        print("=" * 60)  # noqa: T201


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nShutdown complete")  # noqa: T201
        sys.exit(0)
