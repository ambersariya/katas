import pytest

from merchants_guide_to_galaxy.error import InvalidCurrencyValue
from merchants_guide_to_galaxy.metal import Metal
from merchants_guide_to_galaxy.metal_converter import MetalConverter


def test_metal_converter_should_convert_silver_to_arabic_number(
        metal_converter: MetalConverter,
        mocked_currency_repo
):
    data = "glob glob Silver is 34 Credits"
    metal = Metal(value=17, name="Silver")
    mocked_currency_repo.symbol_value.side_effect = ['I', 'I']

    metal_converter.calculate_metal_value(data=data)
    mocked_currency_repo.add.assert_called_once_with(symbol=metal)


def test_metal_converter_should_convert_silver_to_arabic_number_II(
        metal_converter: MetalConverter,
        mocked_currency_repo
):
    data = "glob glob glob Silver is 51 Credits"
    metal = Metal(value=17, name="Silver")
    mocked_currency_repo.symbol_value.side_effect = ['I', 'I', 'I']

    metal_converter.calculate_metal_value(data=data)
    mocked_currency_repo.add.assert_called_once_with(symbol=metal)


@pytest.mark.parametrize('input_data, metal_value, metal_name, currency_values', [
    ("glob glob glob Silver is 51 Credits", 17, "Silver", ["I", "I", "I"]),
    ("glob glob Silver is 34 Credits", 17, "Silver", ["I", "I"]),
    ("glob prok Gold is 57800 Credits", 14450, "Gold", ["I", "V"]),
    ("gLob prOk spacejunk is 57800 Credits", 14450, "spacejunk", ["I", "V"]),
    ("pish prok glob glob glob spacejunk is 306 Credits", 17, "spacejunk", ["X", "V", "I", "I", "I"])
])
def test_metal_converter(input_data, metal_value, metal_name, currency_values, metal_converter: MetalConverter,
                         mocked_currency_repo):
    metal = Metal(value=metal_value, name=metal_name)
    mocked_currency_repo.symbol_value.side_effect = currency_values

    metal_converter.calculate_metal_value(data=input_data)
    mocked_currency_repo.add.assert_called_once_with(symbol=metal)

