from dataclasses import dataclass


@dataclass(frozen=True, init=True)
class BookingId:
    _id: str
