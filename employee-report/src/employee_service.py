from typing import Optional

from src.employee_repository import EmployeeRepository
from src.employees import Employee
from src.filter import FilterCriteria
from src.sort import SortCriteria


class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def list_employees(
        self,
        filter_by: Optional[FilterCriteria] = None,
        sort_by: Optional[SortCriteria] = None
    ) -> list[Employee]:
        employees = self.employee_repository.fetch_all(filter_by=filter_by, sort_by=sort_by)
        return employees
