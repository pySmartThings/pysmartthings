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

from pysmartthings import Capability, Command, SmartThings, SmartThingsError


async def find_locks(api: SmartThings) -> list:
    """Find all lock devices.

    Args:
        api: SmartThings API client

    Returns:
        List of devices with lock capability
    """
    print("\nFinding Lock Devices:")
    print("-" * 60)

    devices = await api.get_devices()
    locks = [d for d in devices if Capability.LOCK in d.capabilities]

    print(f"Found {len(locks)} lock device(s)")
    for lock in locks:
        print(f"\n  Lock: {lock.label}")
        print(f"  ID: {lock.device_id}")

        # Check for lock codes capability
        if Capability.LOCK_CODES in lock.capabilities:
            print("  ✓ Supports lock codes")
        else:
            print("  ✗ Does not support lock codes")

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
    print(f"\nLock/Unlock: {device_name}")
    print("-" * 60)

    try:
        # Lock the door
        print("  Locking door...")
        await api.execute_device_command(
            device_id=device_id,
            capability=Capability.LOCK,
            command=Command.LOCK,
            args=[],
        )
        print("  ✓ Door locked")

        # Wait a moment
        await asyncio.sleep(2)

        # Check lock status
        status = await api.get_device_status(device_id)
        if "main" in status.components:
            main = status.components["main"]
            if "lock" in main:
                lock_state = main["lock"].get("lock")
                if hasattr(lock_state, "value"):
                    print(f"  Current state: {lock_state.value}")

        # Wait before unlocking
        await asyncio.sleep(3)

        # Unlock the door
        print("  Unlocking door...")
        await api.execute_device_command(
            device_id=device_id,
            capability=Capability.LOCK,
            command=Command.UNLOCK,
            args=[],
        )
        print("  ✓ Door unlocked")

    except SmartThingsError as err:
        print(f"  ✗ Error: {err}")


async def set_lock_code_example(
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
    print(f"\nSetting Lock Code: {device_name}")
    print("-" * 60)
    print(f"  Slot: {code_slot}")
    print(f"  Code: {pin_code}")
    print(f"  Name: {code_name}")

    try:
        # Set the lock code
        # Arguments: [code_slot, pin_code, code_name]
        await api.execute_device_command(
            device_id=device_id,
            capability=Capability.LOCK_CODES,
            command=Command.SET_CODE,
            args=[code_slot, pin_code, code_name],
        )
        print(f"  ✓ Lock code set in slot {code_slot}")

    except SmartThingsError as err:
        print(f"  ✗ Error setting lock code: {err}")
        print("  Note: Check your lock's documentation for:")
        print("    - Valid code slot numbers (usually 1-30)")
        print("    - PIN code length requirements (usually 4-8 digits)")
        print("    - Maximum number of supported codes")


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
    print(f"\nDeleting Lock Code: {device_name}")
    print("-" * 60)
    print(f"  Slot: {code_slot}")

    try:
        # Delete the lock code
        # Arguments: [code_slot]
        await api.execute_device_command(
            device_id=device_id,
            capability=Capability.LOCK_CODES,
            command=Command.DELETE_CODE,
            args=[code_slot],
        )
        print(f"  ✓ Lock code in slot {code_slot} deleted")

    except SmartThingsError as err:
        print(f"  ✗ Error deleting lock code: {err}")


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
    print(f"\nManaging Multiple Codes: {device_name}")
    print("-" * 60)

    # Example: Set up codes for family members
    codes = [
        {"slot": 1, "pin": "1234", "name": "Primary User"},
        {"slot": 2, "pin": "5678", "name": "Spouse"},
        {"slot": 3, "pin": "9012", "name": "Child"},
    ]

    print("  Setting up family codes...")
    for code in codes:
        try:
            await api.execute_device_command(
                device_id=device_id,
                capability=Capability.LOCK_CODES,
                command=Command.SET_CODE,
                args=[code["slot"], code["pin"], code["name"]],
            )
            print(
                f"    ✓ Slot {code['slot']}: {code['name']} "
                f"(PIN: {code['pin']})"
            )
            # Small delay between commands
            await asyncio.sleep(1)
        except SmartThingsError as err:
            print(f"    ✗ Failed to set {code['name']}: {err}")

    # Wait before deleting
    print("\n  Waiting 5 seconds before cleanup...")
    await asyncio.sleep(5)

    # Delete temporary codes
    print("\n  Cleaning up temporary codes...")
    for code in codes:
        try:
            await api.execute_device_command(
                device_id=device_id,
                capability=Capability.LOCK_CODES,
                command=Command.DELETE_CODE,
                args=[code["slot"]],
            )
            print(f"    ✓ Deleted slot {code['slot']}")
            await asyncio.sleep(1)
        except SmartThingsError as err:
            print(f"    ✗ Failed to delete slot {code['slot']}: {err}")


async def main() -> None:
    """Demonstrate lock code management with pysmartthings."""
    token = "YOUR_TOKEN_HERE"

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)
        print("SmartThings Lock Code Management Example")
        print("=" * 60)

        # Find all locks
        locks = await find_locks(api)

        if not locks:
            print("\nNo lock devices found in your SmartThings account.")
            print("This example requires a smart lock with the lock capability.")
            return

        # Use first lock for examples
        lock = locks[0]
        lock_id = lock.device_id
        lock_name = lock.label

        # Check if lock supports lock codes
        if Capability.LOCK_CODES not in lock.capabilities:
            print(
                f"\nWarning: {lock_name} does not support lock codes "
                f"(lockCodes capability)."
            )
            print(
                "Continuing with basic lock/unlock example only..."
            )

            # Just do lock/unlock
            print(f"\n{'=' * 60}")
            print("EXAMPLE: Basic Lock/Unlock")
            print("=" * 60)
            await lock_unlock_example(api, lock_id, lock_name)

        else:
            # Lock supports codes - do full examples
            print(f"\n{'=' * 60}")
            print("EXAMPLE 1: Basic Lock/Unlock")
            print("=" * 60)
            await lock_unlock_example(api, lock_id, lock_name)

            print(f"\n{'=' * 60}")
            print("EXAMPLE 2: Set Lock Code")
            print("=" * 60)
            # WARNING: This will set a real code on your lock!
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

            print(f"\n{'=' * 60}")
            print("EXAMPLE 3: Delete Lock Code")
            print("=" * 60)
            await delete_lock_code_example(
                api,
                lock_id,
                lock_name,
                code_slot=10,  # Delete the test code we just set
            )

            print(f"\n{'=' * 60}")
            print("EXAMPLE 4: Manage Multiple Codes")
            print("=" * 60)
            print("  Note: This will set and then delete multiple codes")
            await manage_multiple_codes_example(
                api,
                lock_id,
                lock_name,
            )

        print("\n" + "=" * 60)
        print("Example completed successfully!")
        print("=" * 60)
        print("\nIMPORTANT NOTES:")
        print("  - Lock codes are device-specific")
        print("  - Check your lock's manual for supported slot numbers")
        print("  - PIN length requirements vary by lock model")
        print("  - Some locks support 4-digit PINs, others 4-8 digits")
        print("  - Always test codes before relying on them!")
        print("  - Keep master codes in a secure location")


if __name__ == "__main__":
    asyncio.run(main())
