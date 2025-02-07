"""Tests for the scene module."""

from aiohttp.hdrs import METH_GET
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


# class TestScene:
#     """Tests for the scene class."""
#
#     @staticmethod
#     def test_apply_data() -> None:
#         """Test the init method."""
#         # Arrange
#         data = get_json("scenes.json")
#         scene = Scene()
#         scene.apply_data(data["items"][0])
#         # Assert
#         assert scene.scene_id == "3a570170-7c10-4e5a-bef8-0d02175798f2"
#         assert scene.color == "#F7F9FF"
#         assert scene.name == "Test"
#         assert scene.location_id == "3b44ae84-a735-4fdd-8edd-fc295f4e1563"
#         assert scene.icon == "st.scenes.wand"
#
#
# class TestSceneEntity:
#     """Tests for the scene entity class."""
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_execute(api) -> None:
#         """Tests the execute method."""
#         # Arrange
#         data = get_json("scenes.json")
#         entity = SceneEntity(api, data["items"][1])
#         # Act
#         result = await entity.execute()
#         # Assert
#         assert result
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_refresh(api) -> None:
#         """Tests the refresh method."""
#         entity = SceneEntity(api)
#         with pytest.raises(NotImplementedError):
#             await entity.refresh()
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def test_save(api) -> None:
#         """Tests the refresh method."""
#         entity = SceneEntity(api)
#         with pytest.raises(NotImplementedError):
#             await entity.save()
