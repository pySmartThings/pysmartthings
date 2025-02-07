"""Asynchronous Python client for SmartThings."""


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
