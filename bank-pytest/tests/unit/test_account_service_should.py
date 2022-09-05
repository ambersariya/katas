from unittest.mock import MagicMock

import pytest

from src.account_service import AccountService
from src.date_provider import DateProvider
from src.statement_printer import StatementPrinter
from src.transaction_repository import TransactionRepository


@pytest.fixture()
def mocked_transaction_repository():
    return MagicMock(TransactionRepository)


@pytest.fixture()
def mocked_statement_printer():
    return MagicMock(StatementPrinter)


@pytest.fixture()
def mocked_date_provider():
    date_provider = MagicMock(DateProvider)
    date_provider.today.return_value = '01/08/2022'
    return date_provider


@pytest.fixture()
def account_service(mocked_transaction_repository, mocked_statement_printer, mocked_date_provider):
    return AccountService(
        transaction_repository=mocked_transaction_repository,
        statement_printer=mocked_statement_printer,
        date_provider=mocked_date_provider
    )


def test_add_deposit(account_service, mocked_transaction_repository):
    account_service.deposit(100)
    mocked_transaction_repository.add_transaction.assert_called_once()


def test_withdraw(account_service, mocked_transaction_repository):
    account_service.withdraw(100)
    mocked_transaction_repository.add_transaction.assert_called_once()


def test_print_statement(account_service, mocked_statement_printer):
    account_service.print_statement()
    mocked_statement_printer.print.assert_called_once()
