from corporate_hotel_booking.booking.booking import Booking
from corporate_hotel_booking.booking.booking_policy_service import BookingPolicyService
from corporate_hotel_booking.booking.company_policy_violation_error import CompanyPolicyViolation
from corporate_hotel_booking.company.employee_id import EmployeeId
from corporate_hotel_booking.hotel.hotel_not_found import HotelNotFound
from corporate_hotel_booking.hotel.hotel_service import HotelService


class BookingEngine:
    def __init__(self, hotel_service: HotelService, booking_policy_service: BookingPolicyService):
        self._booking_policy_service = booking_policy_service
        self._hotel_service = hotel_service

    def book_for(self,
                 employee_id: str,
                 hotel_id: str,
                 room_type: str,
                 checkin_date: str,
                 checkout_date: str) -> Booking:

        if not self._booking_policy_service.is_booking_allowed(employee_id=EmployeeId(employee_id), room_type=room_type):
            raise CompanyPolicyViolation()

        hotel = self._hotel_service.find_hotel_by(hotel_id)

        if hotel is None:
            raise HotelNotFound

        return Booking('some id', employee_id, hotel.id, room_type, checkin_date, checkout_date)
