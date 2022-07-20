import uuid

from corporate_hotel_booking.booking.booking import Booking
from corporate_hotel_booking.booking.booking_id import BookingId
from corporate_hotel_booking.booking.booking_policy_service import BookingPolicyService
from corporate_hotel_booking.booking.policy_repository import EmployeePolicyRepository, CompanyPolicyRepository
from corporate_hotel_booking.booking_engine import BookingEngine
from corporate_hotel_booking.company.employee_id import EmployeeId
from corporate_hotel_booking.company.employee_repository import InMemoryEmployeeRepository
from corporate_hotel_booking.hotel.hotel import Hotel
from corporate_hotel_booking.hotel.hotel_id import HotelId
from corporate_hotel_booking.hotel.hotel_repository import InMemoryHotelRepository
from corporate_hotel_booking.hotel.hotel_service import HotelService
from corporate_hotel_booking.hotel.room_type import RoomType

COMPANY_ID = str(uuid.uuid4())
BOOKING_ID = str(uuid.uuid4())
EMPLOYEE_ID = str(uuid.uuid4())
HOTEL_ID = str(uuid.uuid4())
ROOM_TYPE = 'Standard'
CHECKIN_DATE = '2020-09-05'
CHECKOUT_DATE = '2020-09-06'

EMPLOYEE_BOOKING = Booking(id=BookingId(BOOKING_ID), employee_id=EmployeeId(EMPLOYEE_ID), hotel_id=HotelId(HOTEL_ID),
                           room_type=RoomType(ROOM_TYPE), checkin_date=CHECKIN_DATE, checkout_date=CHECKOUT_DATE)

HOTEL = Hotel(id=HotelId(HOTEL_ID), name='Hotel for dogs')

employee_policy_repo = EmployeePolicyRepository()
employee_repository = InMemoryEmployeeRepository()
company_policy_repo = CompanyPolicyRepository()

booking_policy_service = BookingPolicyService(employee_repository=employee_repository,
                                              employee_policy_repository=employee_policy_repo,
                                              company_policy_repository=company_policy_repo)

hotel_repository = InMemoryHotelRepository()
hotel_service = HotelService(hotel_repository=hotel_repository)
booking_engine = BookingEngine(hotel_service=hotel_service, booking_policy_service=booking_policy_service)


def test_employee_can_make_a_booking():
    booking = booking_engine.book_for(EMPLOYEE_ID, HOTEL_ID, ROOM_TYPE, CHECKIN_DATE, CHECKOUT_DATE)

    assert type(booking) is Booking
    assert booking == EMPLOYEE_BOOKING
