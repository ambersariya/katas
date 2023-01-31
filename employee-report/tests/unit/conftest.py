import pytest

from src.employee_repository import EmployeeRepository


@pytest.fixture
def mock_employee_repository(mocker):
    return mocker.Mock(EmployeeRepository)
