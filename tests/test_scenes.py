"""Tests for the scene module."""

from aiohttp.hdrs import METH_GET, METH_POST
from aioresponses import aioresponses
from syrupy import SnapshotAssertion

from pysmartthings import SmartThings
from tests import load_fixture
from tests.const import MOCK_URL, HEADERS


async def test_fetching_all_scenes(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting all scenes."""
    responses.get(
        f"{MOCK_URL}/scenes",
        status=200,
        body=load_fixture("scenes.json"),
    )
    assert await client.get_scenes() == snapshot
    responses.assert_called_once_with(
        f"{MOCK_URL}/scenes",
        METH_GET,
        headers=HEADERS,
        params={},
        json=None,
    )


async def test_fetch_scenes_for_location(
    client: SmartThings,
    responses: aioresponses,
) -> None:
    """Test getting all scenes."""
    responses.get(
        f"{MOCK_URL}/scenes?locationId=397678e5-9995-4a39-9d9f-ae6ba310236b",
        status=200,
        body=load_fixture("scenes.json"),
    )
    assert await client.get_scenes("397678e5-9995-4a39-9d9f-ae6ba310236b")
    responses.assert_called_once_with(
        f"{MOCK_URL}/scenes",
        METH_GET,
        headers=HEADERS,
        params={"locationId": "397678e5-9995-4a39-9d9f-ae6ba310236b"},
        json=None,
    )


async def test_executing_scene(
    client: SmartThings,
    responses: aioresponses,
) -> None:
    """Test executing a scene."""
    responses.post(
        f"{MOCK_URL}/scenes/3a570170-7c10-4e5a-bef8-0d02175798f2/execute",
        status=200,
        body=load_fixture("scene_execute.json"),
    )
    await client.execute_scene("3a570170-7c10-4e5a-bef8-0d02175798f2")
    responses.assert_called_once_with(
        f"{MOCK_URL}/scenes/3a570170-7c10-4e5a-bef8-0d02175798f2/execute",
        METH_POST,
        headers=HEADERS,
        params=None,
        json=None,
    )
