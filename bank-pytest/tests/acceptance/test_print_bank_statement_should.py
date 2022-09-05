from unittest.mock import patch, MagicMock

import pytest

from src.account_service import AccountService
from src.date_provider import DateProvider
from src.statement_printer import ConsoleStatementPrinter
from src.transaction_repository import InMemoryTransactionRepository

EXPECTED_STATEMENT = \
    """Date | Amount | Balance
14/01/2012 | -500 | 2500
13/01/2012 | 2000 | 3000
10/01/2012 | 1000 | 1000"""


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


@patch("builtins.print")
def test_print_all_transactions(
    mocked_print, transaction_repository, statement_printer, mocked_date_provider
):
    service = AccountService(
        transaction_repository=transaction_repository,
        statement_printer=statement_printer,
        date_provider=mocked_date_provider
    )

    service.deposit(1000)
    service.deposit(2000)
    service.withdraw(500)

    service.print_statement()

    mocked_print.assert_called_with(EXPECTED_STATEMENT)
