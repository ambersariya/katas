import pytest

from driving_licence.generator import DrivingLicenceGenerator


@pytest.mark.parametrize('data, expected_output', [
    (["", "", "Smith", "", ""], 'SMITH'),
    (["", "", "SmithRowe", "", ""], 'SMITH'),
    (["", "", "Gea", "", ""], 'GEA99')
])
def test_should_retrieve_surname(data, expected_output):
    driving_licence_generator = DrivingLicenceGenerator()
    result = driving_licence_generator.generate(data)
    assert result == expected_output
