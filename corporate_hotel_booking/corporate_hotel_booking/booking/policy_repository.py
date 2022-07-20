from typing import Optional

from corporate_hotel_booking.policy.company_policy import CompanyPolicy
from corporate_hotel_booking.policy.employee_policy import EmployeePolicy


class CompanyPolicyRepository:
    def policy_for(self, company_id: str) -> Optional[CompanyPolicy]:
        raise NotImplementedError()


class EmployeePolicyRepository:
    def policy_for(self, employee_id: str) -> Optional[EmployeePolicy]:
        raise NotImplementedError()
