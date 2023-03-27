from abc import abstractmethod
from typing import Protocol

from src.company.employee import Employee
from src.company.errors import EmployeeAlreadyExists


class EmployeeRepository(Protocol):
    @abstractmethod
    def add_employee(self, employee: Employee) -> None:
        pass

    @abstractmethod
    def delete_employee(self, employee_id: str) -> None:
        pass


class EmployeeNotFound(Exception):
    pass


class InMemoryEmployeeRepository(EmployeeRepository):
    def __init__(self):
        self.__employees = {}

    def delete_employee(self, employee_id: str) -> None:
        if not self.exists(employee_id=employee_id):
            raise EmployeeNotFound()
        del self.__employees[employee_id]

    def add_employee(self, employee: Employee) -> None:
        if self.exists(employee_id=employee.employee_id):
            raise EmployeeAlreadyExists()
        self.__employees[employee.employee_id] = employee

    def exists(self, employee_id: str) -> bool:
        return employee_id in self.__employees
