from unittest.mock import MagicMock

import pytest

from src.date_provider import DateProvider
from src.statement_printer import ConsoleStatementPrinter
from src.transaction_repository import InMemoryTransactionRepository


@pytest.fixture()
def transaction_repository():
    return InMemoryTransactionRepository()


@pytest.fixture()
def statement_printer():
    return ConsoleStatementPrinter()


@pytest.fixture()
def mocked_date_provider():
    date_provider = MagicMock(DateProvider)
    date_provider.today.side_effect = [
        '10/01/2012',
        '13/01/2012',
        '14/01/2012',
    ]
    return date_provider
