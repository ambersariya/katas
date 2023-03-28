import pytest

from booking.booking_policy_repository import InMemoryBookingPolicyRepository
from booking.booking_policy_service import BookingPolicyService
from src.hotel.hotel import RoomType

ROOM_TYPE = RoomType.STANDARD
EMPLOYEE_ID = '00bc5be8-883b-4744-a806-9df6d40ec920'
COMPANY_ID = '00bc2be4-243b-7018-a806-9df6d40ec930'
COMPANY_ROOM_TYPES = [RoomType.STANDARD, RoomType.DOUBLE]
EMPLOYEE_ROOM_TYPES = [RoomType.STANDARD]


@pytest.fixture
def booking_policy_repository():
    return InMemoryBookingPolicyRepository()


@pytest.fixture
def booking_policy_service(booking_policy_repository):
    return BookingPolicyService(booking_policy_repository=booking_policy_repository)


def test_should_allow_booking_double_room_when_allowed_by_company_policy(booking_policy_service: BookingPolicyService):
    booking_policy_service.set_company_policy(company_id=COMPANY_ID, room_types=COMPANY_ROOM_TYPES)
    assert booking_policy_service.is_booking_allowed(employee_id=EMPLOYEE_ID, room_type=ROOM_TYPE)


def test_should_allow_booking_single_room_when_allowed_by_employee_policy(booking_policy_service: BookingPolicyService):
    booking_policy_service.set_company_policy(company_id=COMPANY_ID, room_types=COMPANY_ROOM_TYPES)
    booking_policy_service.set_employee_policy(company_id=EMPLOYEE_ID, room_types=EMPLOYEE_ROOM_TYPES)
    assert booking_policy_service.is_booking_allowed(employee_id=EMPLOYEE_ID, room_type=ROOM_TYPE)
