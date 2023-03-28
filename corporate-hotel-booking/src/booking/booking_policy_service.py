from booking.booking_policy_repository import BookingPolicyRepository
from hotel.hotel import RoomType


class BookingPolicyService:
    def __init__(self, booking_policy_repository: BookingPolicyRepository):
        self.__booking_policy_repository = booking_policy_repository

    def set_company_policy(self, company_id: str, room_types: list[RoomType]) -> None:
        raise NotImplementedError()

    def set_employee_policy(self, company_id: str, room_types: list[RoomType]) -> None:
        raise NotImplementedError()

    def is_booking_allowed(self, employee_id: str, room_type: RoomType) -> bool:
        raise NotImplementedError()
