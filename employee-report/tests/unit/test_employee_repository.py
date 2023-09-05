import datetime
from unittest.mock import patch

import pytest

from src.employee_repository import InMemoryEmployeeRepository
from src.filter import FilterCriteria, FilterOperation
from src.sort import SortCriteria, SortOrder

FREEZE_TIME = datetime.datetime(2023, 1, 26)


@pytest.fixture()
def in_memory_employee_repository() -> InMemoryEmployeeRepository:
    return InMemoryEmployeeRepository()


def test_employee_repo_should_fetch_employees_without_filtering_results(
    in_memory_employee_repository
):
    result = in_memory_employee_repository.fetch_all()

    assert len(result) == 4


@patch('src.employees.datetime')
def test_employee_repo_should_fetch_filtered_employees_by_age(
    mocked_datetime, in_memory_employee_repository
) -> None:
    mocked_datetime.now.return_value = FREEZE_TIME
    filter_by = FilterCriteria(field='age', operation=FilterOperation.GTE, value=18)
    result = in_memory_employee_repository.fetch_all(filter_by=filter_by, sort_by=None)

    assert len(result) == 2
    assert result[0].name == 'MAX'
    assert result[1].name == 'MIKE'


@patch('src.employees.datetime')
def test_employee_repo_should_fetch_all_employees_sorted_by_name(
    mocked_datetime, in_memory_employee_repository
) -> None:
    mocked_datetime.now.return_value = FREEZE_TIME

    sort_by = SortCriteria(field='name', order=SortOrder.ASC)
    result = in_memory_employee_repository.fetch_all(filter_by=None, sort_by=sort_by)

    assert len(result) == 4
    assert result[0].name == 'MAX'
    assert result[1].name == 'MIKE'
    assert result[2].name == 'NINA'
    assert result[3].name == 'SEPP'


@patch('src.employees.datetime')
def test_employee_repo_should_fetch_all_employees_sorted_by_age_desc_order(
    mocked_datetime, in_memory_employee_repository
) -> None:
    mocked_datetime.now.return_value = FREEZE_TIME
    sort_by = SortCriteria(field='age', order=SortOrder.DESC)

    result = in_memory_employee_repository.fetch_all(filter_by=None, sort_by=sort_by)

    assert len(result) == 4
    assert result[0].name == 'MIKE'
    assert result[1].name == 'MAX'
    assert result[2].name == 'SEPP'
    assert result[3].name == 'NINA'
