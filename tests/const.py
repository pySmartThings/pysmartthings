"""Constants for the SmartThings tests."""

from pysmartthings.const import API_BASE

MOCK_URL = f"https://{API_BASE}"


HEADERS = {
    "Authorization": "Bearer token",
    "Accept": "application/vnd.smartthings+json;v=20250122",
}
