import pytest

from merchants_guide_to_galaxy.domain.currency import Currency, CurrencyValue
from merchants_guide_to_galaxy.domain.metal import Metal
from merchants_guide_to_galaxy.usecase.metal_value_calculation_use_case import metal_value_calculation_use_case

glob_glob_glob_silver = [
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="glob", value=CurrencyValue.I),
    Metal(name='Silver', value=17)
]

glob_glob_silver = [
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="glob", value=CurrencyValue.I),
    Metal(name='Silver', value=17)
]

glob_prok_gold = [
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="prok", value=CurrencyValue.V),
    Metal(name='Gold', value=14450)
]

glob_pr0k_spacejunk = [
    Currency(name="gLob", value=CurrencyValue.I),
    Currency(name="prOk", value=CurrencyValue.V),
    Metal(name='spacejunk', value=14450)
]

pish_prok_glob_glob_glob_spacejunk = [
    Currency(name="pish", value=CurrencyValue.X),
    Currency(name="prok", value=CurrencyValue.V),
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="glob", value=CurrencyValue.I),
    Metal(name='spacejunk', value=14450)
]


@pytest.mark.parametrize('input_data, metal_value, metal_name, currency_values', [
    ("glob glob glob Silver is 51 Credits", 17, "Silver", glob_glob_glob_silver),
    ("glob glob Silver is 34 Credits", 17, "Silver", glob_glob_silver),
    ("glob prok Gold is 57800 Credits", 14450, "Gold", glob_prok_gold),
    ("gLob prOk spacejunk is 57800 Credits", 14450, "spacejunk", glob_pr0k_spacejunk),
    ("pish prok glob glob glob spacejunk is 306 Credits", 17, "spacejunk", pish_prok_glob_glob_glob_spacejunk)
])
def test_metal_value_calculation_use_case(input_data,
                                          metal_value,
                                          metal_name,
                                          currency_values,
                                          mocked_symbol_repo):
    metal = Metal(value=metal_value, name=metal_name)
    mocked_symbol_repo.find_symbol_value.side_effect = currency_values

    metal_value_calculation_use_case(symbol_repo=mocked_symbol_repo, raw_data=input_data)
    mocked_symbol_repo.add.assert_called_once_with(symbol=metal)
