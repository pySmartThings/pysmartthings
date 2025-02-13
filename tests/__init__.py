"""Asynchronous Python client for SmartThings."""

from pathlib import Path
from typing import Any

import orjson


def load_fixture(filename: str) -> str:
    """Load a fixture."""
    path = Path(__package__) / "fixtures" / filename
    return path.read_text(encoding="utf-8")


def load_json_fixture(filename: str) -> Any:
    """Load a JSON fixture."""
    return orjson.loads(load_fixture(filename))  # pylint: disable=no-member
