"""Tests for SmartThings SmartApp endpoints."""

from aiohttp.hdrs import METH_DELETE, METH_GET
from aioresponses import aioresponses
from syrupy import SnapshotAssertion

from pysmartthings import SmartThings
from . import load_fixture

from .const import MOCK_URL, HEADERS


async def test_deleting_smart_app(
    client: SmartThings,
    responses: aioresponses,
) -> None:
    """Test deleting a SmartApp."""
    responses.delete(
        f"{MOCK_URL}/v1/apps/c6cde2b0-203e-44cf-a510-3b3ed4706996", status=200
    )
    await client.delete_smart_app(
        "abcabcabcabc", "c6cde2b0-203e-44cf-a510-3b3ed4706996"
    )
    responses.assert_called_once_with(
        f"{MOCK_URL}/v1/apps/c6cde2b0-203e-44cf-a510-3b3ed4706996",
        METH_DELETE,
        headers={**HEADERS, "Authorization": "Bearer abcabcabcabc"},
        params=None,
        json=None,
    )


async def test_get_installed_app(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting an installed SmartApp."""
    responses.get(
        f"{MOCK_URL}/v1/installedapps/4514eb36-f5fd-4ab2-9520-0597acd1d212",
        status=200,
        body=load_fixture("installedapp_get_response.json"),
    )
    assert (
        await client.get_installed_app(
            "abcabcabcabc", "4514eb36-f5fd-4ab2-9520-0597acd1d212"
        )
        == snapshot
    )
    responses.assert_called_once_with(
        f"{MOCK_URL}/v1/installedapps/4514eb36-f5fd-4ab2-9520-0597acd1d212",
        METH_GET,
        headers={**HEADERS, "Authorization": "Bearer abcabcabcabc"},
        params=None,
        json=None,
    )
