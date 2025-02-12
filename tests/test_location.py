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
