import random
from typing import List

from src.core.route_map import RouteMap
from src.core.value_objects import PilotName
from src.flight import Flight, FlightPairing
from src.flight_pairing_generator import PilotService

from src.schedule import Schedule


class InsufficientPilotsForPairing(Exception):
    pass


class FlightScheduler:
    def __init__(self, route_map: RouteMap, flight_pairing_generator: PilotService):
        self.__flight_pairing_generator = flight_pairing_generator
        self.__route_map = route_map

    def generate_schedule(self, pilots: list[PilotName], unscheduled_flights: List[Flight]) -> Schedule:
        scheduled_flights = [self.__make_flight(flight, pilots) for flight in unscheduled_flights]
        return Schedule(flights=scheduled_flights)

    def __make_flight(self, unscheduled_flight: Flight, pilots: list[PilotName]) -> Flight:
        route = self.__route_map.get_route(origin=unscheduled_flight.origin, destination=unscheduled_flight.destination)
        flight_pairing = self.__flight_pairing_generator.generate_pairing(pilots, route)
        return Flight(route, unscheduled_flight.date, flight_pairing)

    @staticmethod
    def __create_flight_pairing(pilots: list[PilotName]):
        valid_num_for_pairing = len(pilots) % 2
        if valid_num_for_pairing > 0:
            raise InsufficientPilotsForPairing()
        _pilots = pilots.copy()
        random.shuffle(_pilots)

        def pick_pilots(_pilots):
            index = random.randint(0, len(_pilots) - 1)
            p = _pilots[index]
            del _pilots[index]
            return p

        captain = pick_pilots(_pilots)
        co_pilot = pick_pilots(_pilots)

        return FlightPairing(captain=captain, co_pilot=co_pilot)
