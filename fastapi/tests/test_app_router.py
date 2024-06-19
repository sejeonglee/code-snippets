import pytest
from httpx import AsyncClient
from router import app


@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url