from abc import abstractmethod
from datetime import datetime
from typing import Protocol, Optional

from src.employees import Employee
from src.filter import FilterCriteria
from src.sort import SortCriteria, SortOrder


class EmployeeRepository(Protocol):
    @abstractmethod
    def fetch_all(self, filter_by: FilterCriteria, sort_by: Optional[SortCriteria]) -> list[
        Employee]:
        pass


employee_max = Employee(name='Max', dob=datetime.strptime('2005-01-01', '%Y-%m-%d'))  # 18
employee_sepp = Employee(name='Sepp', dob=datetime.strptime('2005-06-06', '%Y-%m-%d'))  # 17
employee_nina = Employee(name='Nina', dob=datetime.strptime('2007-06-06', '%Y-%m-%d'))  # 15
employee_mike = Employee(name='Mike', dob=datetime.strptime('1972-01-01', '%Y-%m-%d'))  # 51


class InMemoryEmployeeRepository(EmployeeRepository):
    employees = [employee_max, employee_sepp, employee_nina, employee_mike]

    def fetch_all(
        self,
        filter_by: Optional[FilterCriteria] = None,
        sort_by: Optional[SortCriteria] = None
    ) -> list[Employee]:

        _employees = self.employees.copy()
        # Filter
        if isinstance(filter_by, FilterCriteria):
            _employees = [
                emp for emp in _employees if
                getattr(emp, filter_by.field) >= filter_by.value
            ]

        # Sort
        if sort_by:
            _employees.sort(
                key=lambda emp: getattr(emp, sort_by.field),
                reverse=sort_by.order == SortOrder.DESC
            )

        # Capitalise
        _employees = [Employee(name=emp.name.upper(), dob=emp.dob) for emp in _employees]

        return _employees
