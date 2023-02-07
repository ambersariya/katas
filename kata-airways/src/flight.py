import dataclasses

from src.core.value_objects import Route
from src.pilot import Pilot


@dataclasses.dataclass(init=True, frozen=True)
class FlightPairing:
    captain: Pilot
    co_pilot: Pilot


@dataclasses.dataclass(init=True)
class Flight:
    route: Route
    date: str
    flight_pairing: FlightPairing = dataclasses.field(default=None)

    @property
    def scheduled(self):
        return self.flight_pairing is not None

    @property
    def origin(self):
        return self.route.origin

    @property
    def destination(self):
        return self.route.destination

    def schedule(self, flight_pairing: FlightPairing):
        self.flight_pairing = flight_pairing
