"""Async patterns and best practices for pysmartthings.

This example demonstrates:
- Running multiple operations concurrently with asyncio.gather
- Proper session management
- Error handling with specific SmartThings exceptions
- Retry logic for transient failures
- Timeout handling
- Production-ready async/await patterns
"""

import asyncio
from typing import Any

from aiohttp import ClientSession, ClientTimeout

from pysmartthings import (
    Capability,
    Command,
    Device,
    SmartThings,
    SmartThingsAuthenticationFailedError,
    SmartThingsConnectionError,
    SmartThingsError,
    SmartThingsNotFoundError,
    SmartThingsRateLimitError,
)


async def concurrent_device_status(api: SmartThings) -> None:
    """Get status of all devices concurrently.

    This demonstrates how to use asyncio.gather to run multiple
    async operations in parallel for better performance.

    Args:
        api: SmartThings API client
    """
    print("\nConcurrent Device Status:")
    print("-" * 60)

    # Get all devices
    devices = await api.get_devices()
    print(f"Found {len(devices)} devices")

    # Get all device statuses concurrently
    print("Fetching all device statuses concurrently...")
    start = asyncio.get_event_loop().time()

    # Create list of coroutines
    status_tasks = [
        api.get_device_status(device.device_id)
        for device in devices
    ]

    # Run all tasks concurrently
    statuses = await asyncio.gather(*status_tasks)

    end = asyncio.get_event_loop().time()
    print(f"✓ Retrieved {len(statuses)} statuses in {end - start:.2f}s")

    # Process results
    for device, status in zip(devices, statuses):
        print(f"\n  {device.label}:")
        if status.components and "main" in status.components:
            main = status.components["main"]

            # Show switch state if available
            if "switch" in main and "switch" in main["switch"]:
                switch_state = main["switch"]["switch"]
                if hasattr(switch_state, "value"):
                    print(f"    Switch: {switch_state.value}")

            # Show temperature if available
            if "temperatureMeasurement" in main:
                temp_cap = main["temperatureMeasurement"]
                if "temperature" in temp_cap:
                    temp = temp_cap["temperature"]
                    if hasattr(temp, "value"):
                        unit = temp.unit if hasattr(temp, "unit") else ""
                        print(f"    Temperature: {temp.value}{unit}")


async def concurrent_device_control(
    api: SmartThings,
    devices: list[Device],
) -> None:
    """Control multiple devices concurrently.

    Args:
        api: SmartThings API client
        devices: List of devices to control
    """
    print("\nConcurrent Device Control:")
    print("-" * 60)

    # Find all switches
    switches = [
        d for d in devices
        if Capability.SWITCH in d.capabilities
    ]

    if not switches:
        print("No switches found")
        return

    print(f"Turning on {len(switches)} switches concurrently...")

    # Create control tasks
    control_tasks = [
        api.execute_device_command(
            device.device_id,
            Capability.SWITCH,
            Command.ON,
            [],
        )
        for device in switches
    ]

    # Execute all commands concurrently
    try:
        await asyncio.gather(*control_tasks)
        print(f"✓ All {len(switches)} switches turned on")
    except SmartThingsError as err:
        print(f"✗ Error controlling devices: {err}")


async def error_handling_example(api: SmartThings) -> None:
    """Demonstrate proper error handling.

    Args:
        api: SmartThings API client
    """
    print("\nError Handling:")
    print("-" * 60)

    # Example 1: Handle specific exceptions
    try:
        # Try to get a non-existent device
        device = await api.get_device("non-existent-id")
    except SmartThingsNotFoundError:
        print("✓ Caught NotFoundError (expected)")
    except SmartThingsAuthenticationFailedError:
        print("✗ Authentication failed - check your token")
    except SmartThingsConnectionError as err:
        print(f"✗ Connection error: {err}")
    except SmartThingsError as err:
        print(f"✗ General SmartThings error: {err}")

    # Example 2: Rate limit handling
    print("\nRate Limit Handling:")
    try:
        # Make multiple requests (might hit rate limit)
        for i in range(10):
            await api.get_devices()
    except SmartThingsRateLimitError as err:
        print(f"✓ Rate limit hit (expected): {err}")
        print("  In production, implement exponential backoff")


async def retry_with_backoff(
    api: SmartThings,
    device_id: str,
    max_retries: int = 3,
) -> Any:
    """Retry an operation with exponential backoff.

    Args:
        api: SmartThings API client
        device_id: Device ID to fetch
        max_retries: Maximum number of retry attempts

    Returns:
        Device object if successful

    Raises:
        SmartThingsError: If all retries fail
    """
    for attempt in range(max_retries):
        try:
            return await api.get_device(device_id)
        except SmartThingsConnectionError as err:
            if attempt == max_retries - 1:
                raise
            # Exponential backoff: 1s, 2s, 4s
            wait_time = 2 ** attempt
            print(
                f"  Retry {attempt + 1}/{max_retries} "
                f"after {wait_time}s: {err}"
            )
            await asyncio.sleep(wait_time)


async def timeout_handling(api: SmartThings) -> None:
    """Demonstrate timeout handling.

    Args:
        api: SmartThings API client
    """
    print("\nTimeout Handling:")
    print("-" * 60)

    try:
        # Set a very short timeout (will likely fail)
        async with asyncio.timeout(0.001):
            devices = await api.get_devices()
            print(f"Got {len(devices)} devices")
    except TimeoutError:
        print("✓ Operation timed out (expected with 1ms timeout)")

    # Now try with reasonable timeout
    try:
        async with asyncio.timeout(10):  # 10 second timeout
            devices = await api.get_devices()
            print(f"✓ Got {len(devices)} devices with 10s timeout")
    except TimeoutError:
        print("✗ Operation timed out (unexpected)")


async def session_management_example() -> None:
    """Demonstrate proper session management.

    This shows the recommended pattern for production use.
    """
    print("\nSession Management:")
    print("-" * 60)

    token = "YOUR_TOKEN_HERE"

    # Pattern 1: Use async context manager (RECOMMENDED)
    print("\nPattern 1: Context manager (recommended)")
    async with ClientSession(
        timeout=ClientTimeout(total=30)
    ) as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        devices = await api.get_devices()
        print(f"  ✓ Got {len(devices)} devices")
        # Session is automatically closed when exiting context

    # Pattern 2: Let SmartThings manage session (simpler but less control)
    print("\nPattern 2: Auto-managed session")
    api = SmartThings()
    api.authenticate(token)

    devices = await api.get_devices()
    print(f"  ✓ Got {len(devices)} devices")
    # Note: Session is created automatically but not explicitly closed


async def gather_with_error_handling(api: SmartThings) -> None:
    """Use asyncio.gather with return_exceptions for robust concurrent ops.

    Args:
        api: SmartThings API client
    """
    print("\nGather with Error Handling:")
    print("-" * 60)

    # Get some device IDs (including an invalid one)
    devices = await api.get_devices()
    if not devices:
        print("No devices found")
        return

    # Mix valid and invalid device IDs
    device_ids = [devices[0].device_id, "invalid-id"]

    # Use return_exceptions=True to get results and errors
    print("Fetching devices (including invalid ID)...")
    results = await asyncio.gather(
        *[api.get_device(device_id) for device_id in device_ids],
        return_exceptions=True,
    )

    # Process results
    for device_id, result in zip(device_ids, results):
        if isinstance(result, Exception):
            print(f"  ✗ {device_id}: {type(result).__name__}")
        else:
            print(f"  ✓ {device_id}: {result.label}")


async def main() -> None:
    """Demonstrate async patterns and best practices."""
    token = "YOUR_TOKEN_HERE"

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)
        print("SmartThings Async Patterns Example")
        print("=" * 60)

        # Get devices for examples
        devices = await api.get_devices()
        print(f"\nFound {len(devices)} device(s)")

        if not devices:
            print("\nNo devices found. Please add devices to your SmartThings account.")
            return

        # Example 1: Concurrent operations
        print("\n" + "=" * 60)
        print("EXAMPLE 1: Concurrent Operations")
        print("=" * 60)
        await concurrent_device_status(api)

        # Example 2: Concurrent control
        print("\n" + "=" * 60)
        print("EXAMPLE 2: Concurrent Control")
        print("=" * 60)
        await concurrent_device_control(api, devices)

        # Example 3: Error handling
        print("\n" + "=" * 60)
        print("EXAMPLE 3: Error Handling")
        print("=" * 60)
        await error_handling_example(api)

        # Example 4: Retry with backoff
        print("\n" + "=" * 60)
        print("EXAMPLE 4: Retry with Backoff")
        print("=" * 60)
        print("Fetching device with retry logic...")
        try:
            device = await retry_with_backoff(api, devices[0].device_id)
            print(f"✓ Got device: {device.label}")
        except SmartThingsError as err:
            print(f"✗ All retries failed: {err}")

        # Example 5: Timeout handling
        print("\n" + "=" * 60)
        print("EXAMPLE 5: Timeout Handling")
        print("=" * 60)
        await timeout_handling(api)

        # Example 6: Gather with error handling
        print("\n" + "=" * 60)
        print("EXAMPLE 6: Gather with Error Handling")
        print("=" * 60)
        await gather_with_error_handling(api)

        print("\n" + "=" * 60)
        print("Best Practices Summary")
        print("=" * 60)
        print("✓ Use async context managers for sessions")
        print("✓ Use asyncio.gather for concurrent operations")
        print("✓ Handle specific exceptions (not just generic Exception)")
        print("✓ Implement retry logic with exponential backoff")
        print("✓ Use timeouts to prevent hanging operations")
        print("✓ Use return_exceptions=True in gather for resilience")

        print("\n" + "=" * 60)
        print("Example completed successfully!")
        print("=" * 60)


# Demonstrate session management as standalone example
async def session_example() -> None:
    """Show session management patterns."""
    await session_management_example()


if __name__ == "__main__":
    # Run main example
    asyncio.run(main())

    # Or run session management example
    # asyncio.run(session_example())
