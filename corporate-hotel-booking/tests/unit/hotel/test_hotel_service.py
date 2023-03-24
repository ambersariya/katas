import pytest

from src.hotel.exceptions import HotelAlreadyExists, HotelNotFound
from src.hotel.hotel import Hotel, RoomType

HOTEL_ID = 'hotel-id'
HOTEL_NAME = 'Grand budapest hotel'
HOTEL = Hotel(id=HOTEL_ID, name=HOTEL_NAME)


def test_should_add_a_hotel(mocked_hotel_repository, hotel_service):
    hotel_service.add_hotel(hotel_id=HOTEL_ID, hotel_name=HOTEL_NAME)
    mocked_hotel_repository.add_hotel.assert_called_once_with(hotel=HOTEL)


def test_should_not_add_a_duplicate_hotel(mocked_hotel_repository, hotel_service):
    mocked_hotel_repository.add_hotel.side_effect = HotelAlreadyExists()

    with pytest.raises(HotelAlreadyExists):
        hotel_service.add_hotel(hotel_id=HOTEL_ID, hotel_name=HOTEL_NAME)


def test_should_find_hotel_by_id(hotel_service, mocked_hotel_repository):
    mocked_hotel_repository.find_hotel_by_id.return_value = HOTEL
    hotel = hotel_service.find_hotel_by(hotel_id=HOTEL_ID)

    mocked_hotel_repository.find_hotel_by_id.assert_called_once_with(hotel_id=HOTEL_ID)
    assert hotel == HOTEL


def test_should_raise_exception_when_hotel_by_id_isnt_found(hotel_service, mocked_hotel_repository):
    mocked_hotel_repository.find_hotel_by_id.side_effect = HotelNotFound()
    with pytest.raises(HotelNotFound):
        hotel = hotel_service.find_hotel_by(hotel_id=HOTEL_ID)
        mocked_hotel_repository.find_hotel_by_id.assert_called_once_with(hotel_id=HOTEL_ID)
        assert hotel == HOTEL


def test_should_set_room_detail_for_a_hotel(hotel_service, mocked_hotel_repository):
    mocked_hotel_repository.find_hotel_by_id.return_value = HOTEL
    hotel_service.set_room(hotel_id=HOTEL_ID, room_number=1, room_type=RoomType.STANDARD)
    mocked_hotel_repository.save.assert_called_once_with(hotel=HOTEL)


def test_should_raise_exception_when_hotel_doesnt_exist(hotel_service, mocked_hotel_repository):
    mocked_hotel_repository.find_hotel_by_id.side_effect = HotelNotFound()
    with pytest.raises(HotelNotFound):
        hotel_service.set_room(hotel_id=HOTEL_ID, room_number=1, room_type=RoomType.STANDARD)
    mocked_hotel_repository.add_hotel.assert_not_called()
