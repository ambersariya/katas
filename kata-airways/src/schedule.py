import dataclasses

from src.flight import Flight


@dataclasses.dataclass(init=True, frozen=True)
class Schedule:
    flights: list[Flight]
