import pytest
from fastapi.testclient import TestClient

from src.ui.rest.api import create_app


@pytest.fixture()
def api():
    return create_app()


@pytest.fixture()
def test_client(api):
    return TestClient(api)
