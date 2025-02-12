"""Define test configuration."""

from collections.abc import AsyncGenerator, Generator

from aiohttp import ClientSession
from aioresponses import aioresponses

from pysmartthings import SmartThings
import pytest
from syrupy import SnapshotAssertion

from .syrupy import SmartThingsSnapshotExtension


@pytest.fixture(name="snapshot")
def snapshot_assertion(snapshot: SnapshotAssertion) -> SnapshotAssertion:
    """Return snapshot assertion fixture with the SmartThings extension."""
    return snapshot.use_extension(SmartThingsSnapshotExtension)


@pytest.fixture
async def client() -> AsyncGenerator[SmartThings, None]:
    """Return a SmartThings client."""
    async with (
        ClientSession() as session,
        SmartThings(
            session=session,
        ) as smartthings_client,
    ):
        smartthings_client.authenticate("token")
        yield smartthings_client


@pytest.fixture(name="responses")
def aioresponses_fixture() -> Generator[aioresponses, None, None]:
    """Return aioresponses fixture."""
    with aioresponses() as mocked_responses:
        yield mocked_responses
