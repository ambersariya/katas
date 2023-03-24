import pytest

from src.hotel.exceptions import HotelAlreadyExists, HotelNotFound
from src.hotel.hotel import Hotel
from src.hotel.hotel_repository import InMemoryHotelRepository

HOTEL = Hotel(id='hotel-id', name='Grand budapest hotel')


def test_should_be_able_to_find_a_hotel_by_id():
    hotel_repository = InMemoryHotelRepository()
    hotel_repository.add_hotel(hotel=HOTEL)

    result = hotel_repository.find_hotel_by_id(hotel_id='hotel-id')
    assert result == HOTEL


def test_should_raise_exception_when_adding_hotel_that_already_exists():
    hotel_repository = InMemoryHotelRepository()
    hotel_repository.add_hotel(hotel=HOTEL)

    with pytest.raises(HotelAlreadyExists):
        hotel_repository.add_hotel(hotel=HOTEL)


def test_should_raise_exception_when_hotel_by_id_isnt_found():
    hotel_repository = InMemoryHotelRepository()
    with pytest.raises(HotelNotFound):
        hotel_repository.find_hotel_by_id(hotel_id='unknown-hotel-id')


def test_save_existing_hotel():
    hotel_repository = InMemoryHotelRepository()
    hotel_repository.save(HOTEL)
