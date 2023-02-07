import pytest

from src.core.value_objects import Route, Airport
from src.flight import Flight
from src.flight_schduler import FlightScheduler
from src.pilot import Pilot


def schedule_adheres_to_rules(schedule):
    assert schedule.for_pilot("John Smith").has_total_flights(24)
    assert schedule.for_pilot("John Smith").has_consecutive_days_off(1)
    assert schedule.for_pilot("John Smith").has_worked_less_than_thirty_hours_a_week()
    assert schedule.for_pilot("John Smith").has_worked_less_than_one_hundred_hours_a_week()
    assert schedule.for_pilot("John Smith").has_flight_on("TUE")
    assert schedule.for_pilot("John Smith").has_flight_on("THU")
    assert schedule.for_pilot("John Smith").has_flight_on("SAT")


@pytest.fixture
def unscheduled_flights():
    return [  # Unscheduled flights
        Flight(Route(origin=Airport("LHR"), destination=Airport("JFK"), duration=8), "2022-01-01"),
        Flight(Route(origin=Airport("JFK"), destination=Airport("LHR"), duration=8), "2022-01-02"),
        Flight(Route(origin=Airport("LHR"), destination=Airport("LAX"), duration=11), "2022-01-03"),
        Flight(Route(origin=Airport("LAX"), destination=Airport("LHR"), duration=11), "2022-01-04"),
    ]


def test_should_show_a_generated_schedule_for_pilots(route_map, unscheduled_flights):
    # Given a set of pilots and flights
    pilots = [  # unscheduled pilots
        Pilot("John Smith"),
        Pilot("Jane Doe"),
        Pilot("Bob Johnson"),
    ]

    # When I generate a schedule
    flight_scheduler = FlightScheduler(route_map=route_map)
    schedule = flight_scheduler.generate_schedule(pilots, unscheduled_flights)

    # Then the schedule should adhere to all of the above rules

    assert schedule_adheres_to_rules(schedule)
