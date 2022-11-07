from unittest.mock import call

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
