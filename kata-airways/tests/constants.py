from src.core.value_objects import Route, Airport
from src.flight import Flight, FlightPairing
from src.pilot import Pilot

AIRPORT_LAX = Airport("LAX")
AIRPORT_LHR = Airport("LHR")

JOHN_SMITH = "John Smith"
JANE_DOE = "Jane Doe"

ROUTE_LHR_LAX = Route(origin=AIRPORT_LHR, destination=AIRPORT_LAX, duration=11)
ROUTE_LAX_LHR = Route(origin=AIRPORT_LAX, destination=AIRPORT_LHR, duration=11)

PILOT_JOHN_SMITH = Pilot(pilot_name=JOHN_SMITH, worked_month_hours=0.0, worked_week_hours=0.0)
PILOT_JANE_DOE = Pilot(pilot_name=JANE_DOE, worked_month_hours=0.0, worked_week_hours=0.0)
FLIGHT_PAIR_JOHN_JANE = FlightPairing(PILOT_JOHN_SMITH, PILOT_JANE_DOE)

FLIGHT_LHR_LAX_UNPAIRED = Flight(ROUTE_LHR_LAX, "2022-01-04")
FLIGHT_LHR_LAX_PAIRED = Flight(ROUTE_LHR_LAX, "2022-01-04", FLIGHT_PAIR_JOHN_JANE)
