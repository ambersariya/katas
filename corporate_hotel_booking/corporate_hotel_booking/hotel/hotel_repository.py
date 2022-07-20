from typing import Protocol, Optional

from corporate_hotel_booking.hotel.hotel import Hotel
from corporate_hotel_booking.hotel.hotel_id import HotelId


class HotelRepository(Protocol):
    def find_by_id(self, id: HotelId) -> Optional[Hotel]:
        raise NotImplementedError()

    def add(self, _id: HotelId, name: str) -> None:
        raise NotImplementedError()


class InMemoryHotelRepository(HotelRepository):
    def __init__(self, ):
        """An in memory repository for hotels"""
        self._hotels = {}

    def find_by_id(self, _id: HotelId) -> Optional[Hotel]:
        return self._hotels.get(_id)

    def add(self, _id: HotelId, name: str):
        self._hotels[_id] = Hotel(id=_id, name=name)

    def __len__(self):
        return len(self._hotels)
