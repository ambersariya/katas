from unittest.mock import patch

import pytest

from src.account_service import AccountService
from src.statement_printer import StatementPrinter, ConsoleStatementPrinter
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


@patch("builtins.print")
def test_print_all_transactions(mocked_print, transaction_repository, statement_printer):
    service = AccountService(transaction_repository=transaction_repository,
                             statement_printer=statement_printer)

    service.deposit(1000)
    service.deposit(2000)
    service.withdraw(500)

    service.print_statement()

    mocked_print.assert_called_with(EXPECTED_STATEMENT)
