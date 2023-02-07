import pytest

from src.core.errors import UnknownDestination
from src.flight import Flight, FlightPairing
from src.flight_schduler import FlightScheduler
from src.pilot import Pilot
from src.schedule import Schedule

JOHN_SMITH = Pilot("John Smith")
JANE_DOE = Pilot("Jane Doe")
LHR_LAX = Flight("LHR", "LAX", "2022-01-01")


def test_generate_schedule_should_return_a_schedule():
    pilots = []
    flights = []
    flight_schedule = FlightScheduler().generate_schedule(pilots, flights)
    assert type(flight_schedule) == Schedule


def test_generate_schedule_should_create_flight_schedule_for_lax():
    pilots = [JOHN_SMITH, JANE_DOE]
    flights = [LHR_LAX]

    result = FlightScheduler().generate_schedule(pilots, flights)
    expected_schedule = Schedule([Flight("LHR", "LAX", "2022-01-01", FlightPairing(JOHN_SMITH, JANE_DOE))])
    assert result == expected_schedule


def test_raise_exception_for_unknown_destination(mock_route_map):
    pilots = [JOHN_SMITH, JANE_DOE]
    flights = [LHR_LAX]
    with pytest.raises(UnknownDestination):
        mock_route_map.is_valid_route.return_value = False
        FlightScheduler().generate_schedule(pilots, flights)

    mock_route_map.is_valid_route.assert_called_once_with("LHR", "LAX")
