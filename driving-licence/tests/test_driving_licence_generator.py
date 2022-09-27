import pytest

from driving_licence.generator import DrivingLicenceGenerator


@pytest.mark.parametrize('data, expected_output', [
    ("Smith", 'SMITH'),
    ("SmithRowe", 'SMITH'),
    ("Gea", 'GEA99')
])
def test_should_retrieve_surname(data, expected_output):
    driving_licence_generator = DrivingLicenceGenerator()
    result = driving_licence_generator.format_surname(surname=data)
    assert result == expected_output


@pytest.mark.parametrize('data, expected_output', [
    ("01-Jan-1980", '8'),
    ("01-Feb-1995", '9'),
    ("01-Jun-2000", '0')
])
def test_should_retrieve_decade(data, expected_output):
    driving_licence_generator = DrivingLicenceGenerator()
    result = driving_licence_generator.format_year(dob=data)
    assert result == expected_output


@pytest.mark.parametrize('data, expected_output', [
    (["01-Jan-1980", "M"], '01'),
    (["01-Feb-1995", "F"], '51'),
    (["01-Dec-2000", "F"], '62')
])
def test_should_format_month_of_birth_based_on_gender(data, expected_output):
    driving_licence_generator = DrivingLicenceGenerator()
    result = driving_licence_generator.format_month_of_birth(dob=data[0], gender=data[1])
    assert result == expected_output
