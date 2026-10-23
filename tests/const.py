"""Constants for the SmartThings tests."""

from pysmartthings.const import API_BASE, DEFAULT_USER_AGENT

MOCK_URL = f"https://{API_BASE}"


HEADERS = {
    "Authorization": "Bearer token",
    "Accept": "application/json",
    "User-Agent": DEFAULT_USER_AGENT,
}
