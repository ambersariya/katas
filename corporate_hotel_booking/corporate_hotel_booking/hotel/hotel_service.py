from corporate_hotel_booking.hotel.hotel_id import HotelId
from corporate_hotel_booking.hotel.hotel_repository import HotelRepository


class HotelService:
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def find_hotel_by(self, _id):
        return self.hotel_repository.find_by_id(id=HotelId(_id))
