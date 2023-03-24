import pytest

from src.hotel.hotel_repository import InMemoryHotelRepository
from src.hotel.hotel_service import HotelService


@pytest.fixture(scope='session')
def hotel_repository():
    return InMemoryHotelRepository()


@pytest.fixture()
def hotel_service(hotel_repository):
    return HotelService(hotel_repository=hotel_repository)
