from unittest.mock import MagicMock, call

import pytest

from merchants_guide_to_galaxy.currency_repo import Currency, CurrencyValue, CurrencyRepo
from merchants_guide_to_galaxy.intergalactic_currency_converter import IntergalacticCurrencyConverter


def test_should_store_currency_values_as_group(intergalactic_currency_converter: IntergalacticCurrencyConverter,
                                               mocked_currency_repo: CurrencyRepo | MagicMock) -> None:
    data = "blah is I"
    currency_object = Currency(name="blah", value=CurrencyValue.I)
    intergalactic_currency_converter.execute_conversion(raw_data=data)
    mocked_currency_repo.add.assert_called_with(currency=currency_object)


def test_should_store_multiple_currency_values(intergalactic_currency_converter: IntergalacticCurrencyConverter,
                                               mocked_currency_repo: CurrencyRepo):
    data = """
glob is I
prok is V
pish is X
tegj is L
"""
    first_currency_object = Currency(name="glob", value=CurrencyValue.I)
    second_currency_object = Currency(name="prok", value=CurrencyValue.V)
    third_currency_object = Currency(name="pish", value=CurrencyValue.X)
    fourth_currency_object = Currency(name="tegj", value=CurrencyValue.L)
    calls = [call(currency=first_currency_object),
             call(currency=second_currency_object),
             call(currency=third_currency_object),
             call(currency=fourth_currency_object)]

    intergalactic_currency_converter.execute_conversion(raw_data=data)
    mocked_currency_repo.add.assert_has_calls(calls=calls)
