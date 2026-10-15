"""Define consts for the pysmartthings package."""

from importlib.metadata import PackageNotFoundError, version
import logging
import os

API_BASE = os.environ.get("SMARTTHINGS_API_BASE", "api.smartthings.com")

try:
    __version__ = version("pysmartthings")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

# Sent when the caller has not set a User-Agent, as the SSE Subscriptions API
# requires a human-readable one. Integrations should set their own.
DEFAULT_USER_AGENT = (
    f"pysmartthings/{__version__} (+https://github.com/pySmartThings/pysmartthings)"
)

LOGGER = logging.getLogger(__package__)

# Maximum number of seconds we will wait for a single SSE line before assuming
# the connection is dead and triggering a reconnect. SmartThings emits a
# keepalive comment well within this interval; values larger than the keepalive
# interval avoid spurious reconnects but still detect half-open sockets.
SSE_READ_TIMEOUT = 120
