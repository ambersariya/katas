import uuid
from unittest import TestCase

from mockito import when, mock

from corporate_hotel_booking.hotel.hotel import Hotel
from corporate_hotel_booking.hotel.hotel_repository import HotelRepository
from corporate_hotel_booking.hotel.hotel_service import HotelService

HOTEL_ID = str(uuid.uuid4())
HOTEL = Hotel(HOTEL_ID)


class HotelServiceShould(TestCase):
    def setUp(self) -> None:
        self._hotel_repo = mock(HotelRepository)
        self.hotel_service = HotelService(self._hotel_repo)

    def test_return_hotel_when_finding_by_id(self):
        when(self._hotel_repo).find_by_id(...).thenReturn(HOTEL)
        self.assertEqual(self.hotel_service.find_hotel_by(id=HOTEL_ID), HOTEL)
