from src.sort import SortOrder, SortCriteria


def sort_criteria(order):
    return SortCriteria(field="name", order=order)


def list_is_in_order(result, expected_order) -> bool:
    expected_order = [name.lower() for name in expected_order]
    return [r.name.lower() for r in result] == expected_order


def test_should_list_employees_sorted_by_name_in_descending_order(
    employee_service,
    employee_max,
    employee_mike,
    employee_nina,
    employee_sepp
):
    result = employee_service.list_employees(sort_by=sort_criteria(SortOrder.DESC))

    assert len(result) == 4
    assert list_is_in_order(result=result, expected_order=['sepp', 'nina', 'mike', 'max'])


def test_should_list_employees_sorted_by_name_in_ascending_order(
    employee_service,
    employee_max,
    employee_mike,
    employee_nina,
    employee_sepp
):
    result = employee_service.list_employees(sort_by=sort_criteria(SortOrder.ASC))

    assert len(result) == 4
    assert list_is_in_order(result=result, expected_order=['max', 'mike', 'nina', 'sepp'])
