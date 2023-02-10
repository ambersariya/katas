from src.core.value_objects import Airport, Route
from src.flight import Flight, FlightPairing
from tests.constants import PILOT_JOHN_SMITH, PILOT_JANE_DOE


def test_flight_should_be_unscheduled_without_flight_pairing():
    flight = Flight(Route(origin=Airport("LAX"), destination=Airport("LHR"), duration=11), "2022-01-04")
    assert flight.scheduled is False


def test_flight_should_be_scheduled_when_flight_pairing_is_added():
    flight = Flight(Route(origin=Airport("LAX"), destination=Airport("LHR"), duration=11), "2022-01-04")
    flight.schedule(FlightPairing(PILOT_JOHN_SMITH, PILOT_JANE_DOE))
    assert flight.scheduled is True
