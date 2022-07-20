import uuid
from unittest import TestCase

import pytest
from mockito import when, mock, verify

from corporate_hotel_booking.booking.booking import Booking
from corporate_hotel_booking.booking_engine import BookingEngine
from corporate_hotel_booking.booking.booking_policy_service import BookingPolicyService
from corporate_hotel_booking.booking.company_policy_violation_error import CompanyPolicyViolation
from corporate_hotel_booking.hotel.hotel import Hotel
from corporate_hotel_booking.hotel.hotel_id import HotelId
from corporate_hotel_booking.hotel.hotel_not_found import HotelNotFound
from corporate_hotel_booking.hotel.hotel_service import HotelService

BOOKING_ID = str(uuid.uuid4())
EMPLOYEE_ID = str(uuid.uuid4())
HOTEL_ID = str(uuid.uuid4())
HOTEL_NAME = 'Hotel Transylvania'
ROOM_TYPE = 'Standard'
CHECKIN_DATE = '2020-09-05'
CHECKOUT_DATE = '2020-09-06'


class BookingEngineShould(TestCase):
    def setUp(self) -> None:
        self._hotel_service = mock(HotelService)
        self._booking_policy_service = mock(BookingPolicyService)
        when(self._hotel_service).find_hotel_by(id=HOTEL_ID).thenReturn(Hotel(id=HotelId(HOTEL_ID), name=HOTEL_NAME))
        when(self._booking_policy_service) \
            .is_booking_allowed(employee_id=EMPLOYEE_ID, room_type=ROOM_TYPE).thenReturn(True)

        self.booking_engine = BookingEngine(hotel_service=self._hotel_service,
                                            booking_policy_service=self._booking_policy_service)

    def test_make_a_booking_for_an_employee(self):
        self.booking_engine.book_for(EMPLOYEE_ID, HOTEL_ID, ROOM_TYPE, CHECKIN_DATE, CHECKOUT_DATE)
        verify(self._hotel_service, times=1).find_hotel_by(...)

    def test_make_a_booking_for_an_employee_when_hotel_exists(self):
        booking = self.booking_engine.book_for(EMPLOYEE_ID, HOTEL_ID, ROOM_TYPE, CHECKIN_DATE, CHECKOUT_DATE)
        verify(self._hotel_service, times=1).find_hotel_by(...)
        assert type(booking) == Booking

    def test_raise_exception_where_hotel_doesnt_exists_when_making_a_booking(self):
        when(self._hotel_service).find_hotel_by(...).thenReturn(None)
        with pytest.raises(HotelNotFound):
            self.booking_engine.book_for(EMPLOYEE_ID, HOTEL_ID, ROOM_TYPE, CHECKIN_DATE, CHECKOUT_DATE)
        verify(self._hotel_service, times=1).find_hotel_by(...)

    def test_not_make_a_booking_if_booking_room_type_is_not_allowed_by_company_policy(self):
        when(self._booking_policy_service) \
            .is_booking_allowed(employee_id=EMPLOYEE_ID, room_type='unknown').thenReturn(False)

        with self.assertRaises(CompanyPolicyViolation):
            self.booking_engine.book_for(EMPLOYEE_ID, HOTEL_ID, 'unknown', CHECKIN_DATE, CHECKOUT_DATE)

        verify(self._booking_policy_service, times=1).is_booking_allowed(...)
