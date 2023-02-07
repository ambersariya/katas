import dataclasses
from typing import NewType, Tuple

from src.pilot import Pilot


@dataclasses.dataclass(init=True, frozen=True)
class FlightPairing:
    captain: Pilot
    co_pilot: Pilot


@dataclasses.dataclass(init=True, frozen=True)
class Flight:
    origin: str
    destination: str
    date: str
    flight_pairing: FlightPairing = dataclasses.field(default=None)

    @property
    def scheduled(self):
        return self.flight_pairing is not None


