import pytest

from src.company.company_service import CompanyService
from src.company.employee import Employee
from src.company.employee_repository import EmployeeRepository
from src.company.errors import EmployeeAlreadyExists

COMPANY_ID = '3ade019b-c718-4ebc-89ff-ddc9512c96f0'
EMPLOYEE_ID = 'ae5c0343-70ec-40af-811d-94867bf1ae1b'

EMPLOYEE = Employee(company_id=COMPANY_ID, employee_id=EMPLOYEE_ID)


@pytest.fixture()
def mocked_employee_repository(mocker):
    return mocker.Mock(EmployeeRepository)


def test_should_be_able_to_add_an_employee(mocked_employee_repository):
    company_service = CompanyService(employee_repository=mocked_employee_repository)
    company_service.add_employee(company_id=COMPANY_ID, employee_id=EMPLOYEE_ID)

    mocked_employee_repository.add_employee.assert_called_once_with(employee=EMPLOYEE)


def test_should_raise_error_when_adding_duplicate_employee(mocked_employee_repository):
    mocked_employee_repository.add_employee.side_effect = EmployeeAlreadyExists()
    company_service = CompanyService(employee_repository=mocked_employee_repository)
    with pytest.raises(EmployeeAlreadyExists):
        company_service.add_employee(company_id=COMPANY_ID, employee_id=EMPLOYEE_ID)
    mocked_employee_repository.add_employee.assert_called_once_with(employee=EMPLOYEE)


def test_should_be_able_to_delete_employee(mocked_employee_repository):
    company_service = CompanyService(employee_repository=mocked_employee_repository)
    company_service.delete_employee(employee_id=EMPLOYEE_ID)

    mocked_employee_repository.delete_employee.assert_called_once_with(employee_id=EMPLOYEE_ID)
