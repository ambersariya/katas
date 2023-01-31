def test_should_list_employees_with_capitalised_names(employee_service):
    result = employee_service.list_employees()

    assert len(result) == 4
    assert result[0].name == 'MAX'
    assert result[1].name == 'SEPP'
    assert result[2].name == 'NINA'
    assert result[3].name == 'MIKE'
