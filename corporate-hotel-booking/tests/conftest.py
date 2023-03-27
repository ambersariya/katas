import pytest

from src.company.employee_repository import InMemoryEmployeeRepository
from src.hotel.hotel_repository import InMemoryHotelRepository
from src.hotel.hotel_service import HotelService


@pytest.fixture()
def hotel_repository():
    return InMemoryHotelRepository()


@pytest.fixture()
def employee_repository():
    return InMemoryEmployeeRepository()


@pytest.fixture()
def hotel_service(hotel_repository):
    return HotelService(hotel_repository=hotel_repository)
