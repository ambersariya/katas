import pytest

from merchants_guide_to_galaxy.metal_converter import MetalConverter


def test_metal_converter_should_convert_silver_to_arabic_number(metal_converter: MetalConverter):
    data = "glob glob Silver is 34 Credits"
    numeral = "II"
    metal = "Silver"
    credit = 34
    result = metal_converter.calculate_metal_value(numeral, metal, credit)
    assert result == 17

