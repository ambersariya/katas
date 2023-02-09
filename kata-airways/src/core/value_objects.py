import dataclasses
from typing import NewType, Union, TypeAlias

Airport = NewType('Airport', str)
PilotName = NewType('PilotName', str)
FlightDuration: TypeAlias = Union[int, float]

make_route_key = lambda origin, destination: f"{origin}-{destination}"


@dataclasses.dataclass(init=True, frozen=True)
class Route:
    origin: Airport
    destination: Airport
    duration: FlightDuration

    def id(self) -> str:
        return make_route_key(self.origin, self.destination)
