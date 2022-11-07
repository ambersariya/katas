from unittest.mock import MagicMock, call

from merchants_guide_to_galaxy.currency_repo import Currency, CurrencyValue, CurrencyRepo
from merchants_guide_to_galaxy.intergalactic_currency_converter import IntergalacticCurrencyConverter
from merchants_guide_to_galaxy.metal_converter import MetalConverter


def test_should_store_currency_values_as_group(intergalactic_currency_converter: IntergalacticCurrencyConverter,
                                               mocked_currency_repo: CurrencyRepo | MagicMock) -> None:
    data = "blah is I"
    currency_object = Currency(name="blah", value=CurrencyValue.I)
    intergalactic_currency_converter.execute_conversion(raw_data=data)
    mocked_currency_repo.add.assert_called_with(currency=currency_object)


def test_should_store_multiple_currency_values(intergalactic_currency_converter: IntergalacticCurrencyConverter,
                                               mocked_currency_repo: CurrencyRepo,
                                               intergalactic_currencies):
    data = """
glob is I
prok is V
pish is X
tegj is L
"""

    calls = [call(currency=currency) for currency in intergalactic_currencies]

    intergalactic_currency_converter.execute_conversion(raw_data=data)
    mocked_currency_repo.add.assert_has_calls(calls=calls)


def test_should_calculate_value_of_when_data_end_with_credits(
        intergalactic_currency_converter: IntergalacticCurrencyConverter,
        mocked_metal_converter: MetalConverter,
        mocked_currency_repo: CurrencyRepo):

    data = "glob glob Silver is 34 Credits"
    intergalactic_currency_converter.execute_conversion(raw_data=data)
    mocked_metal_converter.calculate_metal_value.assert_called_with(data=data)

