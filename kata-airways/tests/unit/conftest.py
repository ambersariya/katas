import pytest

from src.core.route_map import RouteMap


@pytest.fixture()
def mock_route_map(mocker):
    return mocker.Mock(RouteMap)