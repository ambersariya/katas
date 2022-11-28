from unittest.mock import MagicMock

import pytest

from merchants_guide_to_galaxy.repository.in_memory_symbol_repo import InMemorySymbolRepo
from merchants_guide_to_galaxy.domain.currency import CurrencyValue, Currency
from merchants_guide_to_galaxy.domain.symbol_repo import SymbolRepo
from merchants_guide_to_galaxy.app import IntergalacticCurrencyConverter


@pytest.fixture
def mocked_symbol_repo():
    return MagicMock(SymbolRepo)


@pytest.fixture
def intergalactic_currency_converter(in_memory_currency_repo):
    return IntergalacticCurrencyConverter(symbol_repo=in_memory_currency_repo)


@pytest.fixture
def in_memory_currency_repo():
    return InMemorySymbolRepo()


@pytest.fixture
def intergalactic_currencies():
    return [Currency(name="glob", value=CurrencyValue.I),
            Currency(name="prok", value=CurrencyValue.V),
            Currency(name="pish", value=CurrencyValue.X),
            Currency(name="tegj", value=CurrencyValue.L)]
