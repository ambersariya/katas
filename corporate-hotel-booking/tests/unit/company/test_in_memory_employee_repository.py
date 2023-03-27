import pytest

from src.company.employee import Employee
from src.company.employee_repository import EmployeeNotFound
from src.company.errors import EmployeeAlreadyExists

COMPANY_ID = '3ade019b-c718-4ebc-89ff-ddc9512c96f0'
EMPLOYEE_ID = 'ae5c0343-70ec-40af-811d-94867bf1ae1b'

EMPLOYEE = Employee(company_id=COMPANY_ID, employee_id=EMPLOYEE_ID)


def test_should_be_able_add_employee(employee_repository):
    employee_repository.add_employee(employee=EMPLOYEE)
    assert employee_repository.exists(employee_id=EMPLOYEE_ID)


def test_should_be_able_delete_employee(employee_repository):
    employee_repository.add_employee(employee=EMPLOYEE)
    employee_repository.delete_employee(employee_id=EMPLOYEE_ID)
    assert not employee_repository.exists(employee_id=EMPLOYEE_ID)


def test_should_error_when_deleting_non_existent_employee(employee_repository):
    with pytest.raises(EmployeeNotFound):
        employee_repository.delete_employee(employee_id=EMPLOYEE_ID)


def test_should_error_when_adding_duplicate_employee(employee_repository):
    employee_repository.add_employee(employee=EMPLOYEE)
    with pytest.raises(EmployeeAlreadyExists):
        employee_repository.add_employee(employee=EMPLOYEE)
