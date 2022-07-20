from corporate_hotel_booking.booking.policy_repository import EmployeePolicyRepository, CompanyPolicyRepository
from corporate_hotel_booking.company.employee_id import EmployeeId
from corporate_hotel_booking.company.employee_repository import EmployeeRepository


class BookingPolicyService:
    def __init__(self, employee_policy_repository: EmployeePolicyRepository,
                 company_policy_repository: CompanyPolicyRepository,
                 employee_repository: EmployeeRepository
                 ):
        self.employee_repository = employee_repository
        self.company_policy_repository = company_policy_repository
        self.employee_policy_repository = employee_policy_repository

    def is_booking_allowed(self, employee_id: EmployeeId, room_type: str) -> bool:
        employee = self.employee_repository.find_by_id(employee_id=employee_id)
        employee_policy = self.employee_policy_repository.policy_for(employee_id=employee.employee_id)
        if employee_policy:
            return employee_policy.allows(room_type=room_type)

        company_policy = self.company_policy_repository.policy_for(company_id=employee.company_id)
        if company_policy:
            return company_policy.allows(room_type=room_type)

        return True
