import pytest

from merchants_guide_to_galaxy.metal import Metal
from merchants_guide_to_galaxy.metal_value_calculation_use_case import metal_value_calculation_use_case


@pytest.mark.parametrize('input_data, metal_value, metal_name, currency_values', [
    ("glob glob glob Silver is 51 Credits", 17, "Silver", ["I", "I", "I"]),
    ("glob glob Silver is 34 Credits", 17, "Silver", ["I", "I"]),
    ("glob prok Gold is 57800 Credits", 14450, "Gold", ["I", "V"]),
    ("gLob prOk spacejunk is 57800 Credits", 14450, "spacejunk", ["I", "V"]),
    ("pish prok glob glob glob spacejunk is 306 Credits", 17, "spacejunk", ["X", "V", "I", "I", "I"])
])
def test_metal_value_calculation_use_case(input_data, metal_value, metal_name, currency_values,
                                          mocked_symbol_repo):
    metal = Metal(value=metal_value, name=metal_name)
    mocked_symbol_repo.symbol_value.side_effect = currency_values

    metal_value_calculation_use_case(symbol_repo=mocked_symbol_repo, raw_data=input_data)
    mocked_symbol_repo.add.assert_called_once_with(symbol=metal)
