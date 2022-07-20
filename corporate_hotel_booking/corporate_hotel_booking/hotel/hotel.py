from dataclasses import dataclass

from corporate_hotel_booking.hotel.hotel_id import HotelId


@dataclass(frozen=True, init=True)
class Hotel:
    id: HotelId
    name: str
