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
    print("\nConcurrent Device Status:")  # noqa: T201
    print("-" * 60)  # noqa: T201# Get all devices
    devices = await api.get_devices()
    print(f"Found {len(devices)} devices")  # noqa: T201

    # Get all device statuses concurrently
    print("Fetching all device statuses concurrently...")  # noqa: T201
    start = asyncio.get_event_loop().time()

    # Create list of coroutines
    status_tasks = [api.get_device_status(device.device_id) for device in devices]

    # Run all tasks concurrently
    statuses = await asyncio.gather(*status_tasks)

    end = asyncio.get_event_loop().time()
    print(f"✓ Retrieved {len(statuses)} statuses in {end - start:.2f}s")  # noqa: T201

    # Process results
    for device, status in zip(devices, statuses, strict=True):
        print(f"\n  {device.label}:")  # noqa: T201
        if status.components and "main" in status.components:  # type: ignore[attr-defined]
            main_component = status.components["main"]  # type: ignore[attr-defined]

            # Show switch state if available
            if "switch" in main_component and "switch" in main_component["switch"]:
                switch_state = main_component["switch"]["switch"]
                if hasattr(switch_state, "value"):
                    print(f"    Switch: {switch_state.value}")  # noqa: T201

            # Show temperature if available
            if "temperatureMeasurement" in main_component:
                temp_cap = main_component["temperatureMeasurement"]
                if "temperature" in temp_cap:
                    temp = temp_cap["temperature"]
                    if hasattr(temp, "value"):
                        unit = temp.unit if hasattr(temp, "unit") else ""
                        print(f"    Temperature: {temp.value}{unit}")  # noqa: T201


async def concurrent_device_control(
    api: SmartThings,
    devices: list[Device],
) -> None:
    """Control multiple devices concurrently.

    Args:
        api: SmartThings API client
        devices: List of devices to control

    """
    print("\nConcurrent Device Control:")  # noqa: T201
    print("-" * 60)  # noqa: T201# Find all switches
    switches = [d for d in devices if Capability.SWITCH in d.capabilities]  # type: ignore[attr-defined]

    if not switches:
        print("No switches found")  # noqa: T201
        return

    print(f"Turning on {len(switches)} switches concurrently...")  # noqa: T201

    # Create control tasks
    control_tasks = [
        api.execute_device_command(
            device.device_id,
            Capability.SWITCH,
            Command.ON,
        )
        for device in switches
    ]

    # Execute all commands concurrently
    try:
        await asyncio.gather(*control_tasks)
        print(f"✓ All {len(switches)} switches turned on")  # noqa: T201
    except SmartThingsError as err:
        print(f"✗ Error controlling devices: {err}")  # noqa: T201


async def error_handling_example(api: SmartThings) -> None:
    """Demonstrate proper error handling.

    Args:
        api: SmartThings API client

    """
    print("\nError Handling:")  # noqa: T201
    print("-" * 60)  # noqa: T201# Example 1: Handle specific exceptions
    try:
        # Try to get a non-existent device
        _device = await api.get_device("non-existent-id")
    except SmartThingsNotFoundError:
        print("✓ Caught NotFoundError (expected)")  # noqa: T201
    except SmartThingsAuthenticationFailedError:
        print("✗ Authentication failed - check your token")  # noqa: T201
    except SmartThingsConnectionError as err:
        print(f"✗ Connection error: {err}")  # noqa: T201
    except SmartThingsError as err:
        print(f"✗ General SmartThings error: {err}")  # noqa: T201# Example 2: Rate limit handling
    print("\nRate Limit Handling:")  # noqa: T201
    try:
        # Make multiple requests (might hit rate limit)
        for _ in range(10):
            await api.get_devices()
    except SmartThingsRateLimitError as err:
        print(f"✓ Rate limit hit (expected): {err}")  # noqa: T201
        print("  In production, implement exponential backoff")  # noqa: T201


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
        except SmartThingsConnectionError as err:  # noqa: PERF203
            if attempt == max_retries - 1:
                raise
            # Exponential backoff: 1s, 2s, 4s
            wait_time = 2**attempt
            print(f"  Retry {attempt + 1}/{max_retries} after {wait_time}s: {err}")  # noqa: T201
            await asyncio.sleep(wait_time)
    return None  # Explicit return for all paths


async def timeout_handling(api: SmartThings) -> None:
    """Demonstrate timeout handling.

    Args:
        api: SmartThings API client

    """
    print("\nTimeout Handling:")  # noqa: T201
    print("-" * 60)  # noqa: T201
    try:
        # Set a very short timeout (will likely fail)
        async with asyncio.timeout(0.001):
            devices = await api.get_devices()
            print(f"Got {len(devices)} devices")  # noqa: T201
    except TimeoutError:
        print("✓ Operation timed out (expected with 1ms timeout)")  # noqa: T201

    # Now try with reasonable timeout
    try:
        async with asyncio.timeout(10):  # 10 second timeout
            devices = await api.get_devices()
            print(f"✓ Got {len(devices)} devices with 10s timeout")  # noqa: T201
    except TimeoutError:
        print("✗ Operation timed out (unexpected)")  # noqa: T201


async def session_management_example() -> None:
    """Demonstrate proper session management.

    This shows the recommended pattern for production use.
    """
    print("\nSession Management:")  # noqa: T201
    print("-" * 60)  # noqa: T201
    token = "YOUR_TOKEN_HERE"  # noqa: S105

    # Pattern 1: Use async context manager (RECOMMENDED)
    print("\nPattern 1: Context manager (recommended)")  # noqa: T201
    async with ClientSession(timeout=ClientTimeout(total=30)) as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        devices = await api.get_devices()
        print(f"  ✓ Got {len(devices)} devices")  # noqa: T201
        # Session is automatically closed when exiting context

    # Pattern 2: Let SmartThings manage session (simpler but less control)
    print("\nPattern 2: Auto-managed session")  # noqa: T201
    api = SmartThings()
    api.authenticate(token)

    devices = await api.get_devices()
    print(f"  ✓ Got {len(devices)} devices")  # noqa: T201
    # Note: Session is created automatically but not explicitly closed


async def gather_with_error_handling(api: SmartThings) -> None:
    """Use asyncio.gather with return_exceptions for robust concurrent ops.

    Args:
        api: SmartThings API client

    """
    print("\nGather with Error Handling:")  # noqa: T201
    print("-" * 60)  # noqa: T201# Get some device IDs (including an invalid one)
    devices = await api.get_devices()
    if not devices:
        print("No devices found")  # noqa: T201
        return

    # Mix valid and invalid device IDs
    device_ids = [devices[0].device_id, "invalid-id"]

    # Use return_exceptions=True to get results and errors
    print("Fetching devices (including invalid ID)...")  # noqa: T201
    results = await asyncio.gather(
        *[api.get_device(device_id) for device_id in device_ids],
        return_exceptions=True,
    )

    # Process results
    for device_id, result in zip(device_ids, results, strict=True):
        if isinstance(result, Exception):
            print(f"  ✗ {device_id}: {type(result).__name__}")  # noqa: T201
        elif hasattr(result, "label"):
            print(f"  ✓ {device_id}: {result.label}")  # noqa: T201


async def main() -> None:  # noqa: PLR0915, pylint: disable=too-many-statements
    """Demonstrate async patterns and best practices."""
    token = "YOUR_TOKEN_HERE"  # noqa: S105

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)  # noqa: T201
        print("SmartThings Async Patterns Example")  # noqa: T201
        print("=" * 60)  # noqa: T201# Get devices for examples
        devices = await api.get_devices()
        print(f"\nFound {len(devices)} device(s)")  # noqa: T201

        if not devices:
            print("\nNo devices found. Please add devices to your SmartThings account.")  # noqa: T201
            return

        # Example 1: Concurrent operations
        print("\n" + "=" * 60)  # noqa: T201
        print("EXAMPLE 1: Concurrent Operations")  # noqa: T201
        print("=" * 60)  # noqa: T201
        await concurrent_device_status(api)

        # Example 2: Concurrent control
        print("\n" + "=" * 60)  # noqa: T201
        print("EXAMPLE 2: Concurrent Control")  # noqa: T201
        print("=" * 60)  # noqa: T201
        await concurrent_device_control(api, devices)

        # Example 3: Error handling
        print("\n" + "=" * 60)  # noqa: T201
        print("EXAMPLE 3: Error Handling")  # noqa: T201
        print("=" * 60)  # noqa: T201
        await error_handling_example(api)

        # Example 4: Retry with backoff
        print("\n" + "=" * 60)  # noqa: T201
        print("EXAMPLE 4: Retry with Backoff")  # noqa: T201
        print("=" * 60)  # noqa: T201
        print("Fetching device with retry logic...")  # noqa: T201
        try:
            fetched_device = await retry_with_backoff(api, devices[0].device_id)
            print(f"✓ Got device: {fetched_device.label}")  # noqa: T201
        except SmartThingsError as err:
            print(f"✗ All retries failed: {err}")  # noqa: T201# Example 5: Timeout handling
        print("\n" + "=" * 60)  # noqa: T201
        print("EXAMPLE 5: Timeout Handling")  # noqa: T201
        print("=" * 60)  # noqa: T201
        await timeout_handling(api)

        # Example 6: Gather with error handling
        print("\n" + "=" * 60)  # noqa: T201
        print("EXAMPLE 6: Gather with Error Handling")  # noqa: T201
        print("=" * 60)  # noqa: T201
        await gather_with_error_handling(api)

        print("\n" + "=" * 60)  # noqa: T201
        print("Best Practices Summary")  # noqa: T201
        print("=" * 60)  # noqa: T201
        print("✓ Use async context managers for sessions")  # noqa: T201
        print("✓ Use asyncio.gather for concurrent operations")  # noqa: T201
        print("✓ Handle specific exceptions (not just generic Exception)")  # noqa: T201
        print("✓ Implement retry logic with exponential backoff")  # noqa: T201
        print("✓ Use timeouts to prevent hanging operations")  # noqa: T201
        print("✓ Use return_exceptions=True in gather for resilience")  # noqa: T201
        print("\n" + "=" * 60)  # noqa: T201
        print("Example completed successfully!")  # noqa: T201
        print("=" * 60)  # noqa: T201# Demonstrate session management as standalone example


async def session_example() -> None:
    """Show session management patterns."""
    await session_management_example()


if __name__ == "__main__":
    # Run main example
    asyncio.run(main())

    # Or run session management example
    # Uncomment to run: asyncio.run(session_example())
