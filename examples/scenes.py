"""Scene management examples for pysmartthings.

This example demonstrates:
- Listing available scenes
- Filtering scenes by location
- Executing scenes
- Error handling for scene operations
"""

import asyncio

from aiohttp import ClientSession

from pysmartthings import SmartThings, SmartThingsError


async def list_all_scenes(api: SmartThings) -> None:
    """List all scenes across all locations.

    Args:
        api: SmartThings API client
    """
    print("\nListing All Scenes:")
    print("-" * 60)

    scenes = await api.get_scenes()
    print(f"Found {len(scenes)} scene(s)")

    for scene in scenes:
        print(f"\n  Scene: {scene.name}")
        print(f"  ID: {scene.scene_id}")
        if scene.location_id:
            print(f"  Location ID: {scene.location_id}")
        if scene.icon:
            print(f"  Icon: {scene.icon}")
        if scene.color:
            print(f"  Color: {scene.color}")
        print(f"  Created By: {scene.created_by}")


async def list_scenes_by_location(
    api: SmartThings,
    location_id: str,
    location_name: str,
) -> None:
    """List scenes for a specific location.

    Args:
        api: SmartThings API client
        location_id: Location ID to filter by
        location_name: Location name for display
    """
    print(f"\nListing Scenes for Location: {location_name}")
    print("-" * 60)

    scenes = await api.get_scenes(location_id=location_id)
    print(f"Found {len(scenes)} scene(s)")

    for scene in scenes:
        print(f"\n  Scene: {scene.name}")
        print(f"  ID: {scene.scene_id}")


async def execute_scene_example(
    api: SmartThings,
    scene_id: str,
    scene_name: str,
) -> None:
    """Execute a scene with error handling.

    Args:
        api: SmartThings API client
        scene_id: Scene ID to execute
        scene_name: Scene name for display
    """
    print(f"\nExecuting Scene: {scene_name}")
    print("-" * 60)

    try:
        print(f"  Triggering scene '{scene_name}'...")
        await api.execute_scene(scene_id)
        print(f"  ✓ Scene '{scene_name}' executed successfully!")

    except SmartThingsError as err:
        print(f"  ✗ Error executing scene: {err}")


async def find_scene_by_name(
    api: SmartThings,
    name: str,
) -> None:
    """Find and execute a scene by name.

    Args:
        api: SmartThings API client
        name: Scene name to search for (case-insensitive)
    """
    print(f"\nSearching for Scene: {name}")
    print("-" * 60)

    # Get all scenes
    scenes = await api.get_scenes()

    # Find matching scene (case-insensitive)
    matching_scenes = [
        s for s in scenes if name.lower() in s.name.lower()
    ]

    if not matching_scenes:
        print(f"  No scenes found matching '{name}'")
        return

    print(f"  Found {len(matching_scenes)} matching scene(s):")
    for scene in matching_scenes:
        print(f"    - {scene.name} (ID: {scene.scene_id})")

    # Execute first match
    if matching_scenes:
        scene = matching_scenes[0]
        print(f"\n  Executing '{scene.name}'...")
        try:
            await api.execute_scene(scene.scene_id)
            print(f"  ✓ Scene executed successfully!")
        except SmartThingsError as err:
            print(f"  ✗ Error: {err}")


async def main() -> None:
    """Demonstrate scene management with pysmartthings."""
    token = "YOUR_TOKEN_HERE"

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)
        print("SmartThings Scene Management Example")
        print("=" * 60)

        # Get locations first
        locations = await api.get_locations()
        print(f"\nFound {len(locations)} location(s)")

        if not locations:
            print("No locations found. Please check your SmartThings setup.")
            return

        # List all scenes
        await list_all_scenes(api)

        # List scenes by location
        for location in locations:
            await list_scenes_by_location(
                api,
                location.location_id,
                location.name,
            )

        # Get all scenes
        scenes = await api.get_scenes()

        if scenes:
            # Execute first scene as example
            scene = scenes[0]
            print(f"\n{'=' * 60}")
            print("EXAMPLE: Executing Scene")
            print("=" * 60)
            await execute_scene_example(api, scene.scene_id, scene.name)

            # Example: Find and execute scene by name
            print(f"\n{'=' * 60}")
            print("EXAMPLE: Find Scene by Name")
            print("=" * 60)
            # Replace with a scene name from your SmartThings setup
            await find_scene_by_name(api, "good night")

        else:
            print("\nNo scenes found in your SmartThings account.")
            print("You can create scenes in the SmartThings mobile app:")
            print("  1. Open SmartThings app")
            print("  2. Go to Automations")
            print("  3. Create a new Scene")
            print("  4. Add devices and set their desired states")
            print("  5. Save the scene")

        # Show scene summary
        print(f"\n{'=' * 60}")
        print("Scene Summary")
        print("=" * 60)
        print(f"Total Scenes: {len(scenes)}")

        # Group by location
        scenes_by_location: dict[str, list] = {}
        for scene in scenes:
            loc_id = scene.location_id or "unknown"
            if loc_id not in scenes_by_location:
                scenes_by_location[loc_id] = []
            scenes_by_location[loc_id].append(scene)

        for loc_id, loc_scenes in scenes_by_location.items():
            # Find location name
            location_name = "Unknown"
            for loc in locations:
                if loc.location_id == loc_id:
                    location_name = loc.name
                    break

            print(f"\n{location_name}:")
            for scene in loc_scenes:
                print(f"  - {scene.name}")

        print("\n" + "=" * 60)
        print("Example completed successfully!")
        print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
