from src.employee_service import EmployeeService
from src.filter import FilterCriteria, FilterOperation
from src.sort import SortCriteria, SortOrder


def test_employee_service_should_return_list_of_all_employees(
    mock_employee_repository
):
    employee_service = EmployeeService(mock_employee_repository)
    employee_service.list_employees()
    mock_employee_repository.fetch_all.assert_called_once_with(filter_by=None, sort_by=None)


def test_employee_service_should_return_employees_filtered_by_given_criteria(
    mock_employee_repository
):
    filter_by = FilterCriteria(field='age', operation=FilterOperation.GTE, value=10)
    employee_service = EmployeeService(mock_employee_repository)
    employee_service.list_employees(filter_by=filter_by)

    mock_employee_repository.fetch_all.assert_called_once_with(filter_by=filter_by, sort_by=None)


def test_employee_service_should_sorted_employees_by_given_order(mock_employee_repository):
    sort_by = SortCriteria(field='name', order=SortOrder.DESC)
    employee_service = EmployeeService(mock_employee_repository)
    employee_service.list_employees(sort_by=sort_by)

    mock_employee_repository.fetch_all.assert_called_once_with(filter_by=None, sort_by=sort_by)


def test_employee_service_should_filter_and_sort_employees(
    mock_employee_repository
):
    filter_by = FilterCriteria(field='name', operation=FilterOperation.GTE, value=10)
    sort_by = SortCriteria(field='name', order=SortOrder.DESC)

    employee_service = EmployeeService(mock_employee_repository)
    employee_service.list_employees(sort_by=sort_by, filter_by=filter_by)

    mock_employee_repository.fetch_all.assert_called_once_with(filter_by=filter_by, sort_by=sort_by)
