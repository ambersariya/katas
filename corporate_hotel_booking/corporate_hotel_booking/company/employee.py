from dataclasses import dataclass

from corporate_hotel_booking.company.company import CompanyId
from corporate_hotel_booking.company.employee_id import EmployeeId


@dataclass(init=True, frozen=True)
class Employee:
    id: EmployeeId
    company_id: CompanyId
