from datetime import datetime

import pytest

from src.employee_repository import InMemoryEmployeeRepository
from src.employee_service import EmployeeService
from src.employees import Employee


@pytest.fixture
def in_memory_employee_repository():
    return InMemoryEmployeeRepository()


@pytest.fixture
def employee_service(in_memory_employee_repository):
    return EmployeeService(in_memory_employee_repository)


@pytest.fixture
def employee_max():
    return Employee(name='Max', dob=datetime.strptime('2005-01-01', '%Y-%m-%d'))


@pytest.fixture
def employee_sepp():
    return Employee(name='Sepp', dob=datetime.strptime('2005-06-06', '%Y-%m-%d'))


@pytest.fixture
def employee_nina():
    return Employee(name='Nina', dob=datetime.strptime('2007-06-06', '%Y-%m-%d'))


@pytest.fixture
def employee_mike():
    return Employee(name='Mike', dob=datetime.strptime('1972-01-01', '%Y-%m-%d'))


@pytest.fixture
def employees(employee_mike, employee_nina, employee_sepp, employee_max):
    return [employee_mike, employee_nina, employee_sepp, employee_max]
