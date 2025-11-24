"""Tests for SmartThings SmartApp endpoints."""

from aiohttp.hdrs import METH_DELETE
from aioresponses import aioresponses

from pysmartthings import SmartThings

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
