from typing import List

from src.flight import Flight, FlightPairing
from src.pilot import Pilot
from src.schedule import Schedule


class FlightScheduler:
    def generate_schedule(self, pilots: list[Pilot], unscheduled_flights: List[Flight]) -> Schedule:
        scheduled_flights = [self.__make_flight(flight, pilots) for flight in unscheduled_flights]
        return Schedule(flights=scheduled_flights)

    def __make_flight(self, flight: Flight, pilots: list[Pilot]) -> Flight:
        return Flight(flight.origin, flight.destination, flight.date, FlightPairing(pilots[0], pilots[1]))
