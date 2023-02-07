import dataclasses


@dataclasses.dataclass(init=True, frozen=True)
class Pilot:
    name: str
