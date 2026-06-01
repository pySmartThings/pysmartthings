"""Define consts for the pysmartthings package."""

import logging

API_BASE = "api.smartthings.com"
# Version required to use SSE
API_VERSION = 20250122

LOGGER = logging.getLogger(__package__)

# Maximum number of seconds we will wait for a single SSE line before assuming
# the connection is dead and triggering a reconnect. SmartThings emits a
# keepalive comment well within this interval; values larger than the keepalive
# interval avoid spurious reconnects but still detect half-open sockets.
SSE_READ_TIMEOUT = 120
