from unittest.mock import MagicMock

import pytest

from merchants_guide_to_galaxy.currency_repo import CurrencyRepo
from merchants_guide_to_galaxy.intergalactic_currency_converter import IntergalacticCurrencyConverter

@pytest.fixture
def mocked_currency_repo():
    return MagicMock(CurrencyRepo)

@pytest.fixture
def intergalactic_currency_converter():
    return IntergalacticCurrencyConverter()
