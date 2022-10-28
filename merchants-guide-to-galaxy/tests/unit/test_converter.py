import pytest

from merchants_guide_to_galaxy.currency_repo import Currency, CurrencyValue
from merchants_guide_to_galaxy.intergalactic_currency_converter import IntergalacticCurrencyConverter


def test_should_store_currency_values_as_group(intergalactic_currency_converter: IntergalacticCurrencyConverter,
                                               mocked_currency_repo) -> None:
    data = "blah is I"
    currency_object = Currency(name="blah", value=CurrencyValue.I)
    intergalactic_currency_converter.execute_conversion(raw_data=data)
    mocked_currency_repo.add.assert_called_with(currency_object)
