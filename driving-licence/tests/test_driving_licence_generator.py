import pytest

from driving_licence.generator import DrivingLicenceGenerator


@pytest.fixture
def driving_licence_generator():
    return DrivingLicenceGenerator()


@pytest.mark.parametrize('data, expected_output', [
    pytest.param("Smith", 'SMITH', id='when there are exact 5 chars'),
    pytest.param("SmithRowe", 'SMITH', id='when there are more than 5 chars'),
    pytest.param("Gea", 'GEA99', id='when there are less than 5 chars')
])
def test_should_format_surname_to_fixed_length(driving_licence_generator: DrivingLicenceGenerator, data, expected_output):
    result = driving_licence_generator.format_surname(surname=data)
    assert result == expected_output


@pytest.mark.parametrize('data, expected_output', [
    pytest.param("01-Jan-1980", '8', id='get 8 when year is 1980'),
    pytest.param("01-Feb-1995", '9', id='get 9 when year is 1995'),
    pytest.param("01-Jun-2000", '0', id='get 0 when year is 2000')
])
def test_should_format_decade_of_birth(driving_licence_generator: DrivingLicenceGenerator, data, expected_output):
    result = driving_licence_generator.format_year(dob=data)
    assert result == expected_output


@pytest.mark.parametrize('dob, gender, expected_output', [
    pytest.param("01-Jan-1980", "M", '01', id="get 01 when person is Male"),
    pytest.param("01-Nov-1980", "M", '11', id="get 11 when person is Male"),
    pytest.param("01-Dec-1980", "M", '12', id="get 11 when person is Male"),
    pytest.param("01-Feb-1995", "F", '52', id="get 51 when person is Female"),
    pytest.param("01-Sep-2000", "F", '59', id="get 59 when person is Female"),
    pytest.param("01-Oct-2000", "F", '60', id="get 60 when person is Female"),
    pytest.param("01-Nov-2000", "F", '61', id="get 61 when person is Female"),
    pytest.param("01-Dec-2000", "F", '62', id="get 62 when person is Female"),
])
def test_should_format_month_of_birth_based_on_gender(driving_licence_generator: DrivingLicenceGenerator, dob, gender, expected_output):
    result = driving_licence_generator.format_month_of_birth(dob=dob, gender=gender)
    assert result == expected_output


@pytest.mark.parametrize('dob, expected_output', [
    pytest.param("01-Jan-1980", '01'),
    pytest.param("11-Nov-1980", '11'),
    pytest.param("12-Nov-1980", '12'),
    pytest.param("30-Mar-1980", '30'),
    pytest.param("30-Dec-1980", '30'),
])
def test_should_format_date_in_month(driving_licence_generator: DrivingLicenceGenerator, dob, expected_output):
    result = driving_licence_generator.format_date_within_month(dob=dob)
    assert result == expected_output


@pytest.mark.parametrize('dob, expected_output', [
    pytest.param("01-Jan-1981", '1'),
    pytest.param("11-Nov-1982", '2'),
    pytest.param("12-Nov-1987", '7'),
    pytest.param("30-Mar-2022", '2'),
])
def test_should_format_year_in_date_of_birth(driving_licence_generator: DrivingLicenceGenerator, dob, expected_output):
    result = driving_licence_generator.format_year(dob=dob)
    assert result == expected_output
