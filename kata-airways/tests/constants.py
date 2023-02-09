from src.core.value_objects import PilotName, Route, Airport
from src.flight import Flight, FlightPairing
from src.pilot import Pilot

AIRPORT_LAX = Airport("LAX")
AIRPORT_LHR = Airport("LHR")

JOHN_SMITH = PilotName("John Smith")
JANE_DOE = PilotName("Jane Doe")

ROUTE_LHR_LAX = Route(origin=AIRPORT_LHR, destination=AIRPORT_LAX, duration=11)
ROUTE_LAX_LHR = Route(origin=AIRPORT_LAX, destination=AIRPORT_LHR, duration=11)

FLIGHT_PAIR_JOHN_JANE = FlightPairing(JOHN_SMITH, JANE_DOE)

FLIGHT_LHR_LAX_UNPAIRED = Flight(ROUTE_LHR_LAX, "2022-01-04")
FLIGHT_LHR_LAX_PAIRED = Flight(ROUTE_LHR_LAX, "2022-01-04", FLIGHT_PAIR_JOHN_JANE)

PILOT_JOHN_SMITH = Pilot()
PILOT_JANE_DOE = Pilot()
