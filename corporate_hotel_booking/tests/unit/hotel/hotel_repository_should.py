import unittest
import uuid

from corporate_hotel_booking.hotel.hotel import Hotel
from corporate_hotel_booking.hotel.hotel_id import HotelId
from corporate_hotel_booking.hotel.hotel_repository import InMemoryHotelRepository

HOTEL_ID = HotelId(str(uuid.uuid4()))
HOTEL_NAME = 'Cloud Hotel & Spa'
FAKE_HOTEL = Hotel(HOTEL_ID, HOTEL_NAME)


class HotelRepositoryShould(unittest.TestCase):
    def setUp(self) -> None:
        self.hotel_repository = InMemoryHotelRepository()

    def test_return_hotel_by_id(self):
        self.hotel_repository.add(HOTEL_ID, HOTEL_NAME)

        hotel = self.hotel_repository.find_by_id(HOTEL_ID)

        self.assertEqual(len(self.hotel_repository), 1)
        self.assertEqual(hotel, FAKE_HOTEL)

    # def test_return(self):
    #     raise NotImplementedError()
