import pytest

from merchants_guide_to_galaxy.usecase.answer_queries_use_case import answer_queries_use_case
from merchants_guide_to_galaxy.domain.currency import CurrencyValue, Currency


@pytest.mark.parametrize('input_data, answer, symbol_values', [
    ("how much is pish tegj glob glob ?", "pish tegj glob glob is 42",
     [Currency(value=CurrencyValue.X.value, name="pish"),
      Currency(value=CurrencyValue.L.value, name="tegj"),
      Currency(value=CurrencyValue.I.value, name="glob"),
      Currency(value=CurrencyValue.I.value, name="glob")
      ])])
def test_answer_queries_use_case(input_data, answer, symbol_values, mocked_symbol_repo):
    mocked_symbol_repo.symbol_value.side_effect = symbol_values
    answers = answer_queries_use_case(raw_data=input_data, symbol_repo=mocked_symbol_repo)

    assert len(answers) == 1
