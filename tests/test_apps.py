"""Tests for SmartThings apps endpoints."""

from aiohttp.hdrs import METH_DELETE, METH_POST
from aioresponses import aioresponses
import pytest
from syrupy import SnapshotAssertion

from pysmartthings import SmartThings, SmartThingsNotFoundError
from . import load_fixture

from .const import HEADERS, MOCK_URL

APP_ID = "8d3b1c1a-2f0d-4b0a-9c1e-9f1234567890"

async def test_create_app(
    client: SmartThings,
    responses: aioresponses,
    snapshot: SnapshotAssertion,
) -> None:
    """Test creating an app."""
    responses.post(
        f"{MOCK_URL}/v1/apps",
        status=200,
        body=load_fixture("app_create_response.json"),
    )
    assert (
        await client.create_app(
            app_name=f"homeassistant-{APP_ID}",
            display_name="Home Assistant",
            description="Home Assistant SmartThings integration",
            redirect_uris=["https://example.com/auth/callback"],
            scopes=["r:devices:*"],
        )
        == snapshot
    )
    responses.assert_called_once_with(
        f"{MOCK_URL}/v1/apps",
        METH_POST,
        headers=HEADERS,
        params=None,
        json={
            "appName": f"homeassistant-{APP_ID}",
            "displayName": "Home Assistant",
            "description": "Home Assistant SmartThings integration",
            "appType": "API_ONLY",
            "classifications": ["CONNECTED_SERVICE"],
            "apiOnly": {},
            "oauth": {
                "clientName": "Home Assistant",
                "scope": ["r:devices:*"],
                "redirectUris": ["https://example.com/auth/callback"],
            },
        },
    )


async def test_delete_app(
    client: SmartThings,
    responses: aioresponses,
) -> None:
    """Test deleting an app."""
    responses.delete(f"{MOCK_URL}/v1/apps/{APP_ID}", status=200)
    await client.delete_app(APP_ID)
    responses.assert_called_once_with(
        f"{MOCK_URL}/v1/apps/{APP_ID}",
        METH_DELETE,
        headers=HEADERS,
        params=None,
        json=None,
    )


async def test_delete_app_not_found(
    client: SmartThings,
    responses: aioresponses,
) -> None:
    """Test deleting an app that does not exist."""
    responses.delete(f"{MOCK_URL}/v1/apps/{APP_ID}", status=404)
    with pytest.raises(SmartThingsNotFoundError):
        await client.delete_app(APP_ID)
