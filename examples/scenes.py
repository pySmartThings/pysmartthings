"""Scene management examples for pysmartthings.

This example demonstrates:
- Listing available scenes
- Filtering scenes by location
- Executing scenes
- Error handling for scene operations
"""

import asyncio

from aiohttp import ClientSession

from pysmartthings import Scene, SmartThings, SmartThingsError


async def list_all_scenes(api: SmartThings) -> None:
    """List all scenes across all locations.

    Args:
        api: SmartThings API client

    """
    print("\nListing All Scenes:")  # noqa: T201
    print("-" * 60)  # noqa: T201
    scenes = await api.get_scenes()
    print(f"Found {len(scenes)} scene(s)")  # noqa: T201

    for scene in scenes:
        print(f"\n  Scene: {scene.name}")  # noqa: T201
        print(f"  ID: {scene.scene_id}")  # noqa: T201
        if scene.location_id:
            print(f"  Location ID: {scene.location_id}")  # noqa: T201
        if scene.icon:
            print(f"  Icon: {scene.icon}")  # noqa: T201
        if scene.color:
            print(f"  Color: {scene.color}")  # noqa: T201
        print(f"  Created By: {scene.created_by}")  # noqa: T201, type: ignore[attr-defined]


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
    print(f"\nListing Scenes for Location: {location_name}")  # noqa: T201
    print("-" * 60)  # noqa: T201
    scenes = await api.get_scenes(location_id=location_id)
    print(f"Found {len(scenes)} scene(s)")  # noqa: T201

    for scene in scenes:
        print(f"\n  Scene: {scene.name}")  # noqa: T201
        print(f"  ID: {scene.scene_id}")  # noqa: T201


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
    print(f"\nExecuting Scene: {scene_name}")  # noqa: T201
    print("-" * 60)  # noqa: T201
    try:
        print(f"  Triggering scene '{scene_name}'...")  # noqa: T201
        await api.execute_scene(scene_id)
        print(f"  ✓ Scene '{scene_name}' executed successfully!")  # noqa: T201
    except SmartThingsError as err:
        print(f"  ✗ Error executing scene: {err}")  # noqa: T201


async def find_scene_by_name(
    api: SmartThings,
    name: str,
) -> None:
    """Find and execute a scene by name.

    Args:
        api: SmartThings API client
        name: Scene name to search for (case-insensitive)

    """
    print(f"\nSearching for Scene: {name}")  # noqa: T201
    print("-" * 60)  # noqa: T201# Get all scenes
    scenes = await api.get_scenes()

    # Find matching scene (case-insensitive)
    matching_scenes = [s for s in scenes if name.lower() in s.name.lower()]

    if not matching_scenes:
        print(f"  No scenes found matching '{name}'")  # noqa: T201
        return

    print(f"  Found {len(matching_scenes)} matching scene(s):")  # noqa: T201
    for scene in matching_scenes:
        print(f"    - {scene.name} (ID: {scene.scene_id})")  # noqa: T201

    # Execute first match
    if matching_scenes:
        scene = matching_scenes[0]
        print(f"\n  Executing '{scene.name}'...")  # noqa: T201
        try:
            await api.execute_scene(scene.scene_id)
            print("  ✓ Scene executed successfully!")  # noqa: T201
        except SmartThingsError as err:
            print(f"  ✗ Error: {err}")  # noqa: T201


async def main() -> None:  # noqa: PLR0915, pylint: disable=too-many-statements
    """Demonstrate scene management with pysmartthings."""
    token = "YOUR_TOKEN_HERE"  # noqa: S105

    async with ClientSession() as session:
        api = SmartThings(session=session)
        api.authenticate(token)

        print("=" * 60)  # noqa: T201
        print("SmartThings Scene Management Example")  # noqa: T201
        print("=" * 60)  # noqa: T201# Get locations first
        locations = await api.get_locations()
        print(f"\nFound {len(locations)} location(s)")  # noqa: T201

        if not locations:
            print("No locations found. Please check your SmartThings setup.")  # noqa: T201
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
            print(f"\n{'=' * 60}")  # noqa: T201
            print("EXAMPLE: Executing Scene")  # noqa: T201
            print("=" * 60)  # noqa: T201
            await execute_scene_example(api, scene.scene_id, scene.name)

            # Example: Find and execute scene by name
            print(f"\n{'=' * 60}")  # noqa: T201
            print("EXAMPLE: Find Scene by Name")  # noqa: T201
            print("=" * 60)  # noqa: T201# Replace with a scene name from your SmartThings setup
            await find_scene_by_name(api, "good night")

        else:
            print("\nNo scenes found in your SmartThings account.")  # noqa: T201
            print("You can create scenes in the SmartThings mobile app:")  # noqa: T201
            print("  1. Open SmartThings app")  # noqa: T201
            print("  2. Go to Automations")  # noqa: T201
            print("  3. Create a new Scene")  # noqa: T201
            print("  4. Add devices and set their desired states")  # noqa: T201
            print("  5. Save the scene")  # noqa: T201# Show scene summary
        print(f"\n{'=' * 60}")  # noqa: T201
        print("Scene Summary")  # noqa: T201
        print("=" * 60)  # noqa: T201
        print(f"Total Scenes: {len(scenes)}")  # noqa: T201

        # Group by location
        scenes_by_location: dict[str, list[Scene]] = {}
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

            print(f"\n{location_name}:")  # noqa: T201
            for scene in loc_scenes:
                print(f"  - {scene.name}")  # noqa: T201
        print("\n" + "=" * 60)  # noqa: T201
        print("Example completed successfully!")  # noqa: T201
        print("=" * 60)  # noqa: T201


if __name__ == "__main__":
    asyncio.run(main())
