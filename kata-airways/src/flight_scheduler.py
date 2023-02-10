from typing import List

from src.core.route_map import RouteMap
from src.core.value_objects import PilotName
from src.flight import Flight
from src.pilot_service import PilotService
from src.schedule import Schedule


class InsufficientPilotsForPairing(Exception):
    pass


class FlightScheduler:
    def __init__(self, route_map: RouteMap, pilot_service: PilotService):
        self.__pilot_service = pilot_service
        self.__route_map = route_map

    def generate_schedule(self, unscheduled_flights: List[Flight]) -> Schedule:
        scheduled_flights = [self.__make_flight(flight) for flight in unscheduled_flights]
        return Schedule(flights=scheduled_flights)

    def __make_flight(self, unscheduled_flight: Flight) -> Flight:
        route = self.__route_map.get_route(origin=unscheduled_flight.origin, destination=unscheduled_flight.destination)
        flight_pairing = self.__pilot_service.generate_pairing(route)
        return Flight(route, unscheduled_flight.date, flight_pairing)
