from src.filter import FilterCriteria, FilterOperation


def test_should_list_employees_18_years_and_above(employee_service, employees):
    filter_criteria = FilterCriteria(field='age', operation=FilterOperation.GTE, value=18)

    result = employee_service.list_employees(
        filter_by=filter_criteria
    )

    assert len(result) == 2
    assert result[0].age >= 18
    assert result[1].age >= 18
