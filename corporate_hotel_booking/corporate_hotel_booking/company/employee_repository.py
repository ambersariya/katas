from typing import Protocol

from corporate_hotel_booking.company.employee import Employee
from corporate_hotel_booking.company.employee_id import EmployeeId


class EmployeeRepository(Protocol):
    def find_by_id(self, employee_id):
        pass

    def add(self, employee: Employee) -> None:
        pass


class InMemoryEmployeeRepository(EmployeeRepository):
    def __init__(self):
        self._employees = {}

    def find_by_id(self, employee_id: EmployeeId):
        return self._employees[employee_id] \
            if employee_id in self._employees else None

    def add(self, employee: Employee) -> None:
        self._employees[employee.id] = employee
