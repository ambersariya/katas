import pytest

from src.hotel.hotel_repository import HotelRepository
from src.hotel.hotel_service import HotelService


@pytest.fixture()
def mocked_hotel_repository(mocker):
    return mocker.Mock(HotelRepository)


@pytest.fixture()
def hotel_service(mocked_hotel_repository):
    return HotelService(hotel_repository=mocked_hotel_repository)
