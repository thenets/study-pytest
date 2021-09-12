from fastapi.testclient import TestClient

import pytest

from src import main

# fixture to get FastAPI app
@pytest.fixture(scope="session")
def app():
    return main.app


# fixture get FastAPI client
@pytest.fixture(scope="session")
def client(app):
    return TestClient(app)
