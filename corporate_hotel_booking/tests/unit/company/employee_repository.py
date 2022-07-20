import uuid
from unittest import TestCase

from corporate_hotel_booking.company.employee import Employee
from corporate_hotel_booking.company.employee_id import EmployeeId
from corporate_hotel_booking.company.employee_repository import InMemoryEmployeeRepository

EMPLOYEE_ID_1 = EmployeeId(str(uuid.uuid4()))
EMPLOYEE_ID_2 = EmployeeId(str(uuid.uuid4()))
EMPLOYEE_1 = Employee(id=EMPLOYEE_ID_1)
EMPLOYEE_2 = Employee(id=EMPLOYEE_ID_2)


class EmployeeRepositoryShould(TestCase):
    def setUp(self) -> None:
        self.employee_repository = InMemoryEmployeeRepository()

    def test_return_employee_when_finding_by_id(self):
        self.employee_repository.add(EMPLOYEE_1)
        self.employee_repository.add(EMPLOYEE_2)
        result = self.employee_repository.find_by_id(employee_id=EMPLOYEE_ID_1)
        self.assertEqual(result, EMPLOYEE_1)

    def test_return_none_when_employee_doesnt_exist(self):
        self.assertIsNone(self.employee_repository.find_by_id(employee_id='unknown'))
