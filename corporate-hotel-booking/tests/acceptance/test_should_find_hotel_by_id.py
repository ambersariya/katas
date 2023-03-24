from src.hotel.hotel import Hotel, RoomType
from src.hotel.hotel_service import HotelService

HOTEL_ID = '00bc5be8-883b-4744-a806-9df6d40ec920'
HOTEL_NAME = 'Grand Budapest Hotel'
ROOM_TYPE = RoomType.STANDARD
ROOM_NUMBER = 1


def test_should_find_hotel_by_id(hotel_service: HotelService):
    hotel_service.add_hotel(hotel_id=HOTEL_ID, hotel_name=HOTEL_NAME)
    hotel_service.set_room(hotel_id=HOTEL_ID, room_type=ROOM_TYPE, room_number=ROOM_NUMBER)

    result = hotel_service.find_hotel_by(HOTEL_ID)

    assert isinstance(result, Hotel)
    assert result.id == HOTEL_ID
