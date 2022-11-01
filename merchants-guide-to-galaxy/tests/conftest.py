from unittest.mock import MagicMock

import pytest

from merchants_guide_to_galaxy.currency_repo import CurrencyRepo, InMemoryCurrencyRepo
from merchants_guide_to_galaxy.intergalactic_currency_converter import IntergalacticCurrencyConverter


@pytest.fixture
def mocked_currency_repo():
    return MagicMock(CurrencyRepo)


@pytest.fixture
def intergalactic_currency_converter(mocked_currency_repo):
    return IntergalacticCurrencyConverter(currency_repo=mocked_currency_repo)


@pytest.fixture
def in_memory_currency_repo():
    return InMemoryCurrencyRepo()
