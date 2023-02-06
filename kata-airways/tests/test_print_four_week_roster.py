def schedule_adheres_to_rules(schedule):
    pass

PRINTOUT_SCHEDULE = """
Origin | Destination | Departure | Arrival | Captain | Co-Pilot
LHR | LAX | 2022-01-01T12:00Z | 2022-01-01T15:00Z-8 | John Smith | Bob Johnson
LHR | JFK | 2022-01-01T13:00Z | 2022-01-01T16:00Z-5 | John Smith |Bob Johnson
LHR | BER | 2022-01-01T14:00Z | 2022-01-01T16:40Z+1 | John Smith | Jane Doe
LHR | ATH | 2022-01-01T16:00Z | 2022-01-01T21:30Z+2 | John Smith | Jane Doe
LHR | CDG | 2022-01-01T17:00Z | 2022-01-01T19:00Z+1 | Jane Doe | John Smith
LHR | DUB | 2022-01-01T18:00Z | 2022-01-01T19:00Z+0 | Jane Doe | Bob Johnson
LHR | BCN | 2022-01-01T19:00Z | 2022-01-01T21:00Z+1 | Jane Doe | Bob Johnson
LHR | MXP | 2022-01-01T20:00Z | 2022-01-01T12:00Z+1 | Jane Doe | Bob Johnson
LHR | DXB | 2022-01-01T21:00Z | 2022-02-01T04:00Z+4 | Bob Johnson | Jane Doe
"""

def test_should_show_a_generated_schedule_for_pilots():
    # Given a set of pilots and flights
    pilots = [  # unscheduled pilots
        Pilot("John Smith"),
        Pilot("Jane Doe"),
        Pilot("Bob Johnson"),
    ]

    flights = [  # Unscheduled flights
        Flight("LAX", "JFK", "2022-01-01"),
        Flight("JFK", "LAX", "2022-01-02"),
        Flight("LAX", "JFK", "2022-01-03"),
        Flight("JFK", "LAX", "2022-01-04"),
    ]

    # When I generate a schedule
    flight_scheduler = FlightScheduler()
    schedule = flight_scheduler.generate_schedule(pilots, flights)

    # Then the schedule should adhere to all of the above rules

    assert schedule_adheres_to_rules(schedule) == PRINTOUT_SCHEDULE

