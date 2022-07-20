from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class RoomType:
    # STANDARD = 'standard'
    # JUNIOR_SUITE = 'junior suite'
    type: str
