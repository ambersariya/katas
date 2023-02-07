from src.flight import Flight


def test_flight_should_be_unscheduled_without_flight_pairing():
    flight = Flight("LHR", "LAX", "2022-01-01")
    result = flight.scheduled
    assert result == False