import pytest

from merchants_guide_to_galaxy.usecase.currency_assignment_use_case import currency_assignment_use_case
from merchants_guide_to_galaxy.domain.currency import CurrencyValue, Currency


@pytest.mark.parametrize('input_data, currency_name, currency_value', [
    ("glob is I", "glob", "I"),
    ("prok is V", "prok", "V"),
    ("pish is X", "pish", "X"),
    ("tegj is L", "tegj", "L")
])
def test_currency_assignment_use_case(input_data, currency_name, currency_value, mocked_symbol_repo):
    currency_assignment_use_case(symbol_repo=mocked_symbol_repo, raw_data=input_data)
    mocked_symbol_repo.add.assert_called_with(
        symbol=Currency(name=currency_name, value=CurrencyValue[currency_value]))
