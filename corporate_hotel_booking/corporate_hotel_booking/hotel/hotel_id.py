from dataclasses import dataclass


@dataclass(frozen=True, init=True)
class HotelId:
    _id: str
