from fastapi.testclient import TestClient

import pytest

from src import main


@pytest.fixture(scope="session")
def app():
    """Fixture to get FastAPI app"""
    return main.app


@pytest.fixture(scope="session")
def client(app):
    """Fixture to get FastAPI client"""
    return TestClient(app)
