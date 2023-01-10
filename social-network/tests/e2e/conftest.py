import pytest
from fastapi.testclient import TestClient

from src.social_network.domain.timeline_repository import TimelineRepository
from src.ui.rest.api import create_app
from src.ui.rest.routes import deps


@pytest.fixture()
def api(in_memory_timeline_repository):
    with deps.override_for_test() as test_container:
        test_container[TimelineRepository] = in_memory_timeline_repository
        return create_app()


@pytest.fixture()
def test_client(api, in_memory_timeline_repository):
    with deps.override_for_test() as test_container:
        test_container[TimelineRepository] = in_memory_timeline_repository
        return TestClient(api)
