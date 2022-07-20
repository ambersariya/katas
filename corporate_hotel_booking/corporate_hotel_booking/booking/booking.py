from dataclasses import dataclass

from corporate_hotel_booking.booking.booking_id import BookingId
from corporate_hotel_booking.company.employee_id import EmployeeId
from corporate_hotel_booking.hotel.hotel_id import HotelId
from corporate_hotel_booking.hotel.room_type import RoomType


@dataclass(frozen=True)
class Booking:
    id: BookingId
    employee_id: EmployeeId
    hotel_id: HotelId
    room_type: RoomType
    checkin_date: str
    checkout_date: str
