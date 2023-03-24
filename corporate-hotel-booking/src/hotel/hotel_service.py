from src.hotel.hotel import Hotel, RoomType, Room
from src.hotel.hotel_repository import HotelRepository


class HotelService:
    def __init__(self, hotel_repository: HotelRepository):
        self.__hotel_repository = hotel_repository

    def add_hotel(self, hotel_id: str, hotel_name: str):
        self.__hotel_repository.add_hotel(hotel=Hotel(id=hotel_id, name=hotel_name))

    def set_room(self, hotel_id: str, room_number: int, room_type: RoomType):
        hotel = self.__hotel_repository.find_hotel_by_id(hotel_id=hotel_id)
        hotel.add_room(room=Room(number=room_number, type=room_type))
        self.__hotel_repository.save(hotel=hotel)

    def find_hotel_by(self, hotel_id: str):
        return self.__hotel_repository.find_hotel_by_id(hotel_id=hotel_id)
