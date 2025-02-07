"""Tests for the Location module."""

from aiohttp.hdrs import METH_GET
from aioresponses import aioresponses
from syrupy import SnapshotAssertion

from pysmartthings import SmartThings
from . import load_fixture

from .const import MOCK_URL, HEADERS


async def test_fetching_all_locations(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting all locations."""
    responses.get(
        f"{MOCK_URL}/locations", status=200, body=load_fixture("locations.json")
    )
    assert await client.get_locations() == snapshot
    responses.assert_called_once_with(
        f"{MOCK_URL}/locations",
        METH_GET,
        headers=HEADERS,
        params=None,
        json=None,
    )


async def test_fetching_single_location(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting a single location."""
    responses.get(
        f"{MOCK_URL}/locations/397678e5-9995-4a39-9d9f-ae6ba310236b",
        status=200,
        body=load_fixture("location.json"),
    )
    assert await client.get_location("397678e5-9995-4a39-9d9f-ae6ba310236b") == snapshot
    responses.assert_called_once_with(
        f"{MOCK_URL}/locations/397678e5-9995-4a39-9d9f-ae6ba310236b",
        METH_GET,
        headers=HEADERS,
        params=None,
        json=None,
    )


# class TestLocation:
#     """Tests for the Location class."""
#
#     @staticmethod
#     def test_apply_data() -> None:
#         """Tests the apply_data function."""
#         # Arrange
#         data = get_json("location.json")
#         location = Location()
#         # Act
#         location.apply_data(data)
#         # Assert
#         assert location.location_id == LOCATION_ID
#         assert location.name == "Test Home"
#         assert location.country_code == "USA"
#         assert location.latitude == 45.00708112
#         assert location.longitude == -93.11223629
#         assert location.region_radius == 150
#         assert location.temperature_scale == "F"
#         assert location.timezone_id is None
#         assert location.locale == "en"
#
#
# class TestLocationEntity:
#     """Tests the LocationEntity class."""
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_refresh(api) -> None:
#         """Tests the refresh method."""
#         # Arrange
#         entity = LocationEntity(api, location_id=LOCATION_ID)
#         # Act
#         await entity.refresh()
#         # Assert
#         assert entity.name == "Test Home"
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_save(api) -> None:
#         """Tests the save method."""
#         # Arrange
#         entity = LocationEntity(api)
#         # Act/Assert
#         with pytest.raises(NotImplementedError):
#             await entity.save()
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_rooms(api) -> None:
#         """Tests the refresh method."""
#         # Arrange
#         entity = LocationEntity(api, location_id=LOCATION_ID)
#         # Act
#         rooms = await entity.rooms()
#         # Assert
#         assert len(rooms) == 1
