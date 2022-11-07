from unittest.mock import MagicMock

import pytest

from merchants_guide_to_galaxy.currency_repo import SymbolRepo, InMemorySymbolRepo, Currency, CurrencyValue
from merchants_guide_to_galaxy.intergalactic_currency_converter import IntergalacticCurrencyConverter
from merchants_guide_to_galaxy.metal_converter import MetalConverter


@pytest.fixture
def mocked_currency_repo():
    return MagicMock(SymbolRepo)


@pytest.fixture
def intergalactic_currency_converter(mocked_currency_repo, mocked_metal_converter):
    return IntergalacticCurrencyConverter(currency_repo=mocked_currency_repo,
                                          metal_converter=mocked_metal_converter)


@pytest.fixture
def in_memory_currency_repo():
    return InMemorySymbolRepo()


@pytest.fixture
def intergalactic_currencies():
    return [Currency(name="glob", value=CurrencyValue.I),
            Currency(name="prok", value=CurrencyValue.V),
            Currency(name="pish", value=CurrencyValue.X),
            Currency(name="tegj", value=CurrencyValue.L)]


@pytest.fixture
def mocked_metal_converter():
    return MagicMock(MetalConverter)


@pytest.fixture
def metal_converter(mocked_currency_repo):
    return MetalConverter(currency_repo=mocked_currency_repo)
