import unittest
import uuid

from mockito import mock, when, verify

from corporate_hotel_booking.booking.booking_policy_service import BookingPolicyService
from corporate_hotel_booking.booking.policy_repository import EmployeePolicyRepository, CompanyPolicyRepository
from corporate_hotel_booking.company.company import CompanyId
from corporate_hotel_booking.company.employee import Employee
from corporate_hotel_booking.company.employee_id import EmployeeId
from corporate_hotel_booking.company.employee_repository import EmployeeRepository
from corporate_hotel_booking.policy.company_policy import CompanyPolicy
from corporate_hotel_booking.policy.employee_policy import EmployeePolicy

EMPLOYEE_ID = EmployeeId(str(uuid.uuid4()))
COMPANY_ID = CompanyId(str(uuid.uuid4()))

EMPLOYEE = Employee(id=EMPLOYEE_ID, company_id=COMPANY_ID)
ROOM_STANDARD = 'standard'
ROOM_JUNIOR_SUITE = 'junior suite'
ROOM_MASTER_SUITE = 'master suite'

EMPLOYEE_POLICY = EmployeePolicy(employee_id=EMPLOYEE_ID, room_types=[ROOM_STANDARD, ROOM_JUNIOR_SUITE])
COMPANY_POLICY = CompanyPolicy(company_id=COMPANY_ID, room_types=[ROOM_STANDARD])


class BookingPolicyServiceShould(unittest.TestCase):
    def setUp(self) -> None:
        """When neither company nor employee policy exists"""
        self.employee_policy_repository = mock(EmployeePolicyRepository)
        when(self.employee_policy_repository).policy_for(employee_id=EMPLOYEE_ID).thenReturn(None)

        self.company_policy_repository = mock(CompanyPolicyRepository)
        when(self.company_policy_repository).policy_for(company_id=COMPANY_ID).thenReturn(COMPANY_POLICY)

        self.employee_repository = mock(EmployeeRepository)
        when(self.employee_repository).find_by_id(employee_id=EMPLOYEE_ID).thenReturn(EMPLOYEE)

        self.policy_service = BookingPolicyService(employee_policy_repository=self.employee_policy_repository,
                                                   company_policy_repository=self.company_policy_repository,
                                                   employee_repository=self.employee_repository)

    def test_return_true_when_employee_is_allowed_to_book_a_room(self):
        self.assertEqual(self.policy_service.is_booking_allowed(EMPLOYEE_ID, ROOM_STANDARD), True)
        verify(self.employee_policy_repository).policy_for(...)
        verify(self.employee_repository).find_by_id(...)

    def test_return_true_when_employee_is_allowed_to_book_standard_room_on_employee_policy(self):
        when(self.employee_policy_repository).policy_for(employee_id=EMPLOYEE_ID).thenReturn(EMPLOYEE_POLICY)

        self.assertEqual(self.policy_service.is_booking_allowed(EMPLOYEE_ID, ROOM_STANDARD), True)
        verify(self.employee_policy_repository).policy_for(...)
        verify(self.employee_repository).find_by_id(...)

    def test_return_true_when_employee_is_allowed_to_book_standard_room_on_company_policy(self):
        when(self.company_policy_repository).policy_for(company_id=COMPANY_ID).thenReturn(COMPANY_POLICY)

        self.assertEqual(self.policy_service.is_booking_allowed(EMPLOYEE_ID, ROOM_STANDARD), True)
        verify(self.employee_policy_repository).policy_for(...)
        verify(self.company_policy_repository).policy_for(company_id=COMPANY_ID)
        verify(self.employee_repository).find_by_id(...)

    def test_return_true_when_employee_is_allowed_to_book_any_room_when_no_policies_exists(self):
        when(self.company_policy_repository).policy_for(company_id=COMPANY_ID).thenReturn(None)

        self.assertEqual(self.policy_service.is_booking_allowed(EMPLOYEE_ID, ROOM_MASTER_SUITE), True)
        verify(self.employee_policy_repository).policy_for(...)
        verify(self.company_policy_repository).policy_for(company_id=COMPANY_ID)
        verify(self.employee_repository).find_by_id(...)
