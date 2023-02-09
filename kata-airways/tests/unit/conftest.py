import pytest

from src.core.route_map import RouteMap
from src.pilot_service import PilotService
from src.flight_scheduler import FlightScheduler
from src.pilot_repository import PilotRepository


@pytest.fixture()
def mock_route_map(mocker):
    return mocker.Mock(RouteMap)


@pytest.fixture
def mock_pilot_service(mocker):
    return mocker.Mock(PilotService)


@pytest.fixture
def mock_pilot_repository(mocker):
    return mocker.Mock(PilotRepository)


@pytest.fixture
def pilot_service(mock_pilot_repository):
    return PilotService(pilot_repository=mock_pilot_repository)


@pytest.fixture
def flight_scheduler(mock_route_map, mock_pilot_service):
    return FlightScheduler(route_map=mock_route_map, flight_pairing_generator=mock_pilot_service)


@pytest.fixture
def mock_pilot_repository(mocker):
    return mocker.Mock(PilotRepository)
