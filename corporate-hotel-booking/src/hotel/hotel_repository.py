from abc import abstractmethod
from typing import Protocol

from src.hotel.exceptions import HotelAlreadyExists, HotelNotFound
from src.hotel.hotel import Hotel


class HotelRepository(Protocol):
    @abstractmethod
    def add_hotel(self, hotel: Hotel) -> None:
        pass

    @abstractmethod
    def find_hotel_by_id(self, hotel_id) -> Hotel:
        pass

    @abstractmethod
    def save(self, hotel: Hotel):
        pass


class InMemoryHotelRepository(HotelRepository):
    def __init__(self):
        self.__hotels = {}

    def add_hotel(self, hotel: Hotel) -> None:
        if self.hotel_exists(hotel_id=hotel.id):
            raise HotelAlreadyExists()
        self.save(hotel)

    def find_hotel_by_id(self, hotel_id) -> Hotel:
        if hotel_id not in self.__hotels:
            raise HotelNotFound()
        return self.__hotels[hotel_id]

    def save(self, hotel: Hotel) -> None:
        self.__hotels[hotel.id] = hotel

    def hotel_exists(self, hotel_id):
        return hotel_id in self.__hotels
