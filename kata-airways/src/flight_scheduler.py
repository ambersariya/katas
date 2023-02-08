import random
from typing import List

from src.core.route_map import RouteMap
from src.flight import Flight, FlightPairing
from src.pilot import Pilot
from src.schedule import Schedule
from itertools import _grouper


class InsufficientPilotsForPairing(Exception):
    pass


class FlightScheduler:
    def __init__(self, route_map: RouteMap):
        self.__route_map = route_map

    def generate_schedule(self, pilots: list[Pilot], unscheduled_flights: List[Flight]) -> Schedule:
        scheduled_flights = [self.__make_flight(flight, pilots) for flight in unscheduled_flights]
        return Schedule(flights=scheduled_flights)

    def __make_flight(self, unscheduled_flight: Flight, pilots: list[Pilot]) -> Flight:
        route = self.__route_map.get_route(origin=unscheduled_flight.origin, destination=unscheduled_flight.destination)
        return Flight(
            route,
            unscheduled_flight.date,
            self.__create_flight_pairing(pilots=pilots)
        )

    def  __create_flight_pairing(self, pilots: list[Pilot]):
        valid_num_for_pairing = len(pilots) % 2
        pilot_pairs = _grouper(pilots, 2)
        print(pilot_pairs)
        if valid_num_for_pairing > 0:
            raise InsufficientPilotsForPairing()

        # Step 1: Group pilots into pairings of twos randomly
        # Step 2: Select a pairing randomly to be chosen for flight pairing

        random.shuffle(pilots)
        return FlightPairing(captain=pilots[0], co_pilot=pilots[1])
