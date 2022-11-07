import pytest

from merchants_guide_to_galaxy.currency_repo import InMemoryCurrencyRepo, Currency, CurrencyValue
from merchants_guide_to_galaxy.error import NonExistingCurrency

CURRENCY_GLOB = Currency(name="glob", value=CurrencyValue.I)
CURRENCY_PROK = Currency(name="prok", value=CurrencyValue.V)


def test_currency_repo_stores_currency(in_memory_currency_repo):
    in_memory_currency_repo.add(currency=CURRENCY_GLOB)

    currency = in_memory_currency_repo.get_currency("glob")

    assert len(in_memory_currency_repo) == 1
    assert currency == CURRENCY_GLOB


def test_raises_error_when_currency_doesnt_exist(in_memory_currency_repo):
    with pytest.raises(NonExistingCurrency):
        in_memory_currency_repo.get_currency(currency_name="prok")
