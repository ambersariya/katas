from src.company.employee import Employee
from src.company.employee_repository import EmployeeRepository


class CompanyService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.__employee_repository = employee_repository

    def add_employee(self, company_id: str, employee_id: str) -> None:
        employee = Employee(company_id=company_id, employee_id=employee_id)
        self.__employee_repository.add_employee(employee=employee)

    def delete_employee(self, employee_id: str) -> None:
        self.__employee_repository.delete_employee(employee_id=employee_id)
