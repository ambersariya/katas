from dataclasses import dataclass


@dataclass
class BookingRequest:
    employee_id: str
    hotel_id: str
    room_type: str
    checkin_date: str
    checkout_date: str
