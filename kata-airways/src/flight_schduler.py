from typing import List

from src.core.route_map import RouteMap
from src.flight import Flight, FlightPairing
from src.pilot import Pilot
from src.schedule import Schedule


class FlightScheduler:
    def __init__(self, route_map: RouteMap):
        self.__route_map = route_map

    def generate_schedule(self, pilots: list[Pilot], unscheduled_flights: List[Flight]) -> Schedule:
        scheduled_flights = [self.__make_flight(flight, pilots) for flight in unscheduled_flights]
        return Schedule(flights=scheduled_flights)

    def __make_flight(self, unscheduled_flight: Flight, pilots: list[Pilot]) -> Flight:
        self.__route_map.get_route(origin=unscheduled_flight.origin, destination=unscheduled_flight.destination)
        return Flight(
            unscheduled_flight.route,
            unscheduled_flight.date,
            FlightPairing(captain=pilots[0], co_pilot=pilots[1])
        )
