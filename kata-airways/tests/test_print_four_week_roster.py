def schedule_adheres_to_rules(schedule):
    pass


def test_should_show_a_generated_schedule_for_pilots():
    # Given a set of pilots and flights
    pilots = [  # unscheduled pilots
        Pilot("John Smith", "Captain"),
        Pilot("Jane Doe", "Co-Pilot"),
        Pilot("Bob Johnson", "Co-Pilot"),
    ]

    flights = [  # Unscheduled flights
        Flight("LAX", "JFK", "2022-01-01", "Captain"),
        Flight("JFK", "LAX", "2022-01-02", "Co-pilot"),
        Flight("LAX", "JFK", "2022-01-03", "Captain"),
        Flight("JFK", "LAX", "2022-01-04", "Co-pilot"),
    ]

    # When I generate a schedule
    flight_scheduler = FlightScheduler()
    schedule = flight_scheduler.generate_schedule(pilots, flights)

    # Then the schedule should adhere to all of the above rules
    assert schedule_adheres_to_rules(schedule)
