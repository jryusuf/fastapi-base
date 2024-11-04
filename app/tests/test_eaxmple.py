import pytest

from httpx import AsyncClient
from fastapi import FastAPI

from app.main import app


@pytest.mark.asyncio
async def test_read_main():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
