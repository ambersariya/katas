import dataclasses

from src.core.value_objects import Route, PilotName


@dataclasses.dataclass(init=True, frozen=True, eq=True)
class FlightPairing:
    captain: PilotName
    co_pilot: PilotName


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
