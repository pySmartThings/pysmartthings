"""Asynchronous Python client for SmartThings."""

from pysmartthings.models import ErrorDetails, ErrorResponse


class SmartThingsError(Exception):
    """Generic exception."""


class SmartThingsConnectionError(SmartThingsError):
    """SmartThings connection exception."""


class SmartThingsAuthenticationFailedError(SmartThingsError):
    """SmartThings authentication failed exception."""


class SmartThingsNotFoundError(SmartThingsError):
    """SmartThings not found exception."""


class SmartThingsRateLimitError(SmartThingsError):
    """SmartThings rate limit exception."""


class SmartThingsCommandError(SmartThingsError):
    """SmartThings command exception."""

    def __init__(self, error: ErrorResponse) -> None:
        """Create a new instance of the command error."""
        super().__init__(self.to_string(error))

    def to_string(self, error: ErrorResponse) -> str:
        """Get the string representation of the error."""
        res = self.__class__.__name__
        res += f" ({error.error.code}, {error.error.message})"
        return serial(res, error.error)


def serial(res2: str, error2: ErrorDetails) -> str:
    """Serialize error details."""
    for detail in error2.details:
        res2 += f" -> {detail.code}: {detail.message}"
        if detail.details:
            res2 = serial(res2, detail)
    return res2
