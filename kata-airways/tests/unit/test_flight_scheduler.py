import pytest

from src.core.errors import UnknownDestination
from src.core.value_objects import Airport, Route
from src.flight import Flight, FlightPairing
from src.flight_schduler import FlightScheduler
from src.pilot import Pilot
from src.schedule import Schedule

JOHN_SMITH = Pilot("John Smith")
JANE_DOE = Pilot("Jane Doe")
LHR_LAX = Flight(Route(origin=Airport("LAX"), destination=Airport("LHR"), duration=11), "2022-01-04")
EXPECTED_PAIRED_FLIGHT = Flight(
    Route(origin=Airport("LAX"), destination=Airport("LHR"), duration=11),
    "2022-01-04",
    FlightPairing(JOHN_SMITH, JANE_DOE)
)


def test_generate_schedule_should_return_a_schedule(mock_route_map):
    pilots = []
    flights = []
    flight_schedule = FlightScheduler(route_map=mock_route_map).generate_schedule(pilots, flights)
    assert type(flight_schedule) == Schedule


def test_generate_schedule_should_create_flight_schedule_for_lax(mock_route_map):
    pilots = [JOHN_SMITH, JANE_DOE]
    flights = [LHR_LAX]

    result = FlightScheduler(route_map=mock_route_map).generate_schedule(pilots, flights)
    expected_schedule = Schedule([EXPECTED_PAIRED_FLIGHT])
    assert result == expected_schedule


def test_raise_exception_for_unknown_destination(mock_route_map):
    pilots = [JOHN_SMITH, JANE_DOE]
    flights = [LHR_LAX]
    mock_route_map.get_route.side_effect = UnknownDestination()
    with pytest.raises(UnknownDestination):
        FlightScheduler(route_map=mock_route_map).generate_schedule(pilots, flights)
        mock_route_map.get_route.assert_called_once_with(origin="LHR", destination="LAX")
