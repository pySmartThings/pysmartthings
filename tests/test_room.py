"""Tests for the room module."""

from aiohttp.hdrs import METH_GET
from aioresponses import aioresponses
from syrupy import SnapshotAssertion

from pysmartthings import SmartThings

from . import load_fixture
from .const import MOCK_URL, HEADERS


async def test_fetching_all_rooms(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting all rooms for a location."""
    responses.get(
        f"{MOCK_URL}/locations/397678e5-9995-4a39-9d9f-ae6ba310236b/rooms",
        status=200,
        body=load_fixture("rooms.json"),
    )
    assert await client.get_rooms("397678e5-9995-4a39-9d9f-ae6ba310236b") == snapshot
    responses.assert_called_once_with(
        f"{MOCK_URL}/locations/397678e5-9995-4a39-9d9f-ae6ba310236b/rooms",
        METH_GET,
        headers=HEADERS,
        params=None,
        json=None,
    )


async def test_fetching_single_room(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting a single room."""
    responses.get(
        f"{MOCK_URL}/locations/397678e5-9995-4a39-9d9f-ae6ba310236b/rooms/7715151d-0314-457a-a82c-5ce48900e065",
        status=200,
        body=load_fixture("room.json"),
    )
    assert (
        await client.get_room(
            "397678e5-9995-4a39-9d9f-ae6ba310236b",
            "7715151d-0314-457a-a82c-5ce48900e065",
        )
        == snapshot
    )
    responses.assert_called_once_with(
        f"{MOCK_URL}/locations/397678e5-9995-4a39-9d9f-ae6ba310236b/rooms/7715151d-0314-457a-a82c-5ce48900e065",
        METH_GET,
        headers=HEADERS,
        params=None,
        json=None,
    )


# class TestRoom:
#     """Tests for the Room class."""
#
#     @staticmethod
#     def test_apply_data() -> None:
#         """Test the init method."""
#         # Arrange
#         data = get_json("room.json")
#         room = Room()
#         room.apply_data(data)
#         # Assert
#         assert room.room_id == ROOM_ID
#         assert room.location_id == LOCATION_ID
#         assert room.name == "Theater"
#         assert room.background_image == "Test"
#
#
# class TestRoomEntity:
#     """Tests for the room entity class."""
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_refresh(api) -> None:
#         """Tests the refresh method."""
#         # Arrange
#         entity = RoomEntity(api, location_id=LOCATION_ID, room_id=ROOM_ID)
#         # Act
#         await entity.refresh()
#         # Assert
#         assert entity.name == "Theater"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_save(api) -> None:
#         """Tests the save method."""
#         # Arrange
#         entity = RoomEntity(api, location_id=LOCATION_ID, room_id=ROOM_ID)
#         entity.name = "Theater"
#         entity.background_image = "Test"
#         # Act
#         await entity.save()
#         # Assert
#         assert entity.name == "Theater"
#         assert entity.background_image == "Test"
