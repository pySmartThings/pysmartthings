"""Lock code management examples for pysmartthings.

This example demonstrates:
- Checking if a device supports lock codes
- Setting lock codes (PIN codes)
- Deleting lock codes
- Locking and unlocking doors
- Managing multiple codes

Note: This example addresses issue #69 (Set Lock Code functionality)
"""

import asyncio

from aiohttp import ClientSession

from pysmartthings import Capability, Command, Device, SmartThings, SmartThingsError


async def find_locks(api: SmartThings) -> list[Device]:
    """Find all lock devices.

    Args:
        api: SmartThings API client

    Returns:
        List of devices with lock capability

    """
    print("\nFinding Lock Devices:")  # noqa: T201
    print("-" * 60)  # noqa: T201
    devices = await api.get_devices()
    locks = [d for d in devices if Capability.LOCK in d.capabilities]  # type: ignore[attr-defined]

    print(f"Found {len(locks)} lock device(s)")  # noqa: T201
    for lock in locks:
        print(f"\n  Lock: {lock.label}")  # noqa: T201
        print(f"  ID: {lock.device_id}")  # noqa: T201# Check for lock codes capability
        if Capability.LOCK_CODES in lock.capabilities:  # type: ignore[attr-defined]
            print("  ✓ Supports lock codes")  # noqa: T201
        else:
            print("  ✗ Does not support lock codes")  # noqa: T201
    return locks


async def lock_unlock_example(
    api: SmartThings,
    device_id: str,
    device_name: str,
) -> None:
    """Lock and unlock a door.

    Args:
        api: SmartThings API client
        device_id: Lock device ID
        device_name: Lock device name for display

    """
    print(f"\nLock/Unlock: {device_name}")  # noqa: T201
    print("-" * 60)  # noqa: T201
    try:
        # Lock the door
        print("  Locking door...")  # noqa: T201
        await api.execute_device_command(
            device_id=device_id,
            capability=Capability.LOCK,
            command=Command.LOCK,
            argument=[],
        )
        print("  ✓ Door locked")  # noqa: T201# Wait a moment
        await asyncio.sleep(2)

        # Check lock status
        status = await api.get_device_status(device_id)
        if "main" in status.components:  # type: ignore[attr-defined]
            main_component = status.components["main"]  # type: ignore[attr-defined]
            if "lock" in main_component:
                lock_state = main_component["lock"].get("lock")
                if hasattr(lock_state, "value"):
                    print(f"  Current state: {lock_state.value}")  # noqa: T201# Wait before unlocking
        await asyncio.sleep(3)

        # Unlock the door
        print("  Unlocking door...")  # noqa: T201
        await api.execute_device_command(
            device_id=device_id,
            capability=Capability.LOCK,
            command=Command.UNLOCK,
            argument=[],
        )
        print("  ✓ Door unlocked")  # noqa: T201
    except SmartThingsError as err:
        print(f"  ✗ Error: {err}")  # noqa: T201


async def set_lock_code_example(  # noqa: PLR0913
    api: SmartThings,
    device_id: str,
    device_name: str,
    code_slot: int,
    pin_code: str,
    code_name: str,
) -> None:
    """Set a lock code (PIN).

    Args:
        api: SmartThings API client
        device_id: Lock device ID
        device_name: Lock device name for display
        code_slot: Code slot number (typically 1-30)
        pin_code: PIN code (typically 4-8 digits)
        code_name: Name/description for this code

    """
    print(f"\nSetting Lock Code: {device_name}")  # noqa: T201
    print("-" * 60)  # noqa: T201
    print(f"  Slot: {code_slot}")  # noqa: T201
    print(f"  Code: {pin_code}")  # noqa: T201
    print(f"  Name: {code_name}")  # noqa: T201
    try:
        # Set the lock code (slot, PIN, name)
        await api.execute_device_command(
            device_id=device_id,
            capability=Capability.LOCK_CODES,
            command=Command.SET_CODE,
            argument=[code_slot, pin_code, code_name],
        )
        print(f"  ✓ Lock code set in slot {code_slot}")  # noqa: T201
    except SmartThingsError as err:
        print(f"  ✗ Error setting lock code: {err}")  # noqa: T201
        print("  Note: Check your lock's documentation for:")  # noqa: T201
        print("    - Valid code slot numbers (usually 1-30)")  # noqa: T201
        print("    - PIN code length requirements (usually 4-8 digits)")  # noqa: T201
        print("    - Maximum number of supported codes")  # noqa: T201


async def delete_lock_code_example(
    api: SmartThings,
    device_id: str,
    device_name: str,
    code_slot: int,
) -> None:
    """Delete a lock code.

    Args:
        api: SmartThings API client
        device_id: Lock device ID
        device_name: Lock device name for display
        code_slot: Code slot number to delete

    """
    print(f"\nDeleting Lock Code: {device_name}")  # noqa: T201
    print("-" * 60)  # noqa: T201
    print(f"  Slot: {code_slot}")  # noqa: T201
    try:
        # Delete the lock code (slot number)
        await api.execute_device_command(
            device_id=device_id,
            capability=Capability.LOCK_CODES,
            command=Command.DELETE_CODE,
            argument=[code_slot],
        )
        print(f"  ✓ Lock code in slot {code_slot} deleted")  # noqa: T201
    except SmartThingsError as err:
        print(f"  ✗ Error deleting lock code: {err}")  # noqa: T201


async def manage_multiple_codes_example(
    api: SmartThings,
    device_id: str,
    device_name: str,
) -> None:
    """Manage multiple lock codes.

    Args:
        api: SmartThings API client
        device_id: Lock device ID
        device_name: Lock device name for display

    """
    print(f"\nManaging Multiple Codes: {device_name}")  # noqa: T201
    print("-" * 60)  # noqa: T201# Example: Set up codes for family members
    codes = [
        {"slot": 1, "pin": "1234", "name": "Primary User"},
        {"slot": 2, "pin": "5678", "name": "Spouse"},
        {"slot": 3, "pin": "9012", "name": "Child"},
    ]

    print("  Setting up family codes...")  # noqa: T201
    for code in codes:
        try:
            await api.execute_device_command(
                device_id=device_id,
                capability=Capability.LOCK_CODES,
                command=Command.SET_CODE,
                argument=[code["slot"], code["pin"], code["name"]],
            )
            print(f"    ✓ Slot {code['slot']}: {code['name']} (PIN: {code['pin']})")  # noqa: T201
            # Small delay between commands
            await asyncio.sleep(1)
        except SmartThingsError as err:  # noqa: PERF203
            print(f"    ✗ Failed to set {code['name']}: {err}")  # noqa: T201# Wait before deleting
    print("\n  Waiting 5 seconds before cleanup...")  # noqa: T201
    await asyncio.sleep(5)

    # Delete temporary codes
    print("\n  Cleaning up temporary codes...")  # noqa: T201
    for code in codes:
        try:
            await api.execute_device_command(
                device_id=device_id,
                capability=Capability.LOCK_CODES,
                command=Command.DELETE_CODE,
                argument=[code["slot"]],
            )
            print(f"    ✓ Deleted slot {code['slot']}")  # noqa: T201
            await asyncio.sleep(1)
        except SmartThingsError as err:  # noqa: PERF203
            print(f"    ✗ Failed to delete slot {code['slot']}: {err}")  # noqa: T201


async def main() -> None:  # noqa: PLR0915, pylint: disable=too-many-statements
    """Demonstrate lock code management with pysmartthings."""
    token = "YOUR_TOKEN_HERE"  # noqa: S105

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)  # noqa: T201
        print("SmartThings Lock Code Management Example")  # noqa: T201
        print("=" * 60)  # noqa: T201# Find all locks
        locks = await find_locks(api)

        if not locks:
            print("\nNo lock devices found in your SmartThings account.")  # noqa: T201
            print("This example requires a smart lock with the lock capability.")  # noqa: T201
            return

        # Use first lock for examples
        lock = locks[0]
        lock_id = lock.device_id
        lock_name = lock.label

        # Check if lock supports lock codes
        if Capability.LOCK_CODES not in lock.capabilities:  # type: ignore[attr-defined]
            print(  # noqa: T201
                f"\nWarning: {lock_name} does not support lock codes "
                f"(lockCodes capability)."
            )
            print("Continuing with basic lock/unlock example only...")  # noqa: T201# Just do lock/unlock
            print(f"\n{'=' * 60}")  # noqa: T201
            print("EXAMPLE: Basic Lock/Unlock")  # noqa: T201
            print("=" * 60)  # noqa: T201
            await lock_unlock_example(api, lock_id, lock_name)

        else:
            # Lock supports codes - do full examples
            print(f"\n{'=' * 60}")  # noqa: T201
            print("EXAMPLE 1: Basic Lock/Unlock")  # noqa: T201
            print("=" * 60)  # noqa: T201
            await lock_unlock_example(api, lock_id, lock_name)

            print(f"\n{'=' * 60}")  # noqa: T201
            print("EXAMPLE 2: Set Lock Code")  # noqa: T201
            print("=" * 60)  # noqa: T201# WARNING: This will set a real code on your lock!
            # Change these values as needed
            await set_lock_code_example(
                api,
                lock_id,
                lock_name,
                code_slot=10,  # Use slot 10 for testing
                pin_code="9999",  # Test PIN
                code_name="Test Code",
            )

            # Wait before deleting
            await asyncio.sleep(3)

            print(f"\n{'=' * 60}")  # noqa: T201
            print("EXAMPLE 3: Delete Lock Code")  # noqa: T201
            print("=" * 60)  # noqa: T201
            await delete_lock_code_example(
                api,
                lock_id,
                lock_name,
                code_slot=10,  # Delete the test code we just set
            )

            print(f"\n{'=' * 60}")  # noqa: T201
            print("EXAMPLE 4: Manage Multiple Codes")  # noqa: T201
            print("=" * 60)  # noqa: T201
            print("  Note: This will set and then delete multiple codes")  # noqa: T201
            await manage_multiple_codes_example(
                api,
                lock_id,
                lock_name,
            )

        print("\n" + "=" * 60)  # noqa: T201
        print("Example completed successfully!")  # noqa: T201
        print("=" * 60)  # noqa: T201
        print("\nIMPORTANT NOTES:")  # noqa: T201
        print("  - Lock codes are device-specific")  # noqa: T201
        print("  - Check your lock's manual for supported slot numbers")  # noqa: T201
        print("  - PIN length requirements vary by lock model")  # noqa: T201
        print("  - Some locks support 4-digit PINs, others 4-8 digits")  # noqa: T201
        print("  - Always test codes before relying on them!")  # noqa: T201
        print("  - Keep master codes in a secure location")  # noqa: T201


if __name__ == "__main__":
    asyncio.run(main())
