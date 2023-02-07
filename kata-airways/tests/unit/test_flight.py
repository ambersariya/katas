from src.core.value_objects import Airport, Route
from src.flight import Flight


def test_flight_should_be_unscheduled_without_flight_pairing():
    flight = Flight(Route(origin=Airport("LAX"), destination=Airport("LHR"), duration=11), "2022-01-04")
    assert flight.scheduled is False
