from unittest.mock import MagicMock

import pytest

from src.account_service import AccountService
from src.date_provider import DateProvider
from src.statement_printer import StatementPrinter
from src.transaction import Transaction, Deposit, Withdraw
from src.transaction_repository import TransactionRepository


@pytest.fixture()
def empty_transactions():
    return []


@pytest.fixture()
def transactions() -> list[Transaction]:
    return [
        Deposit(amount=100, date='01/08/2022'),
        Deposit(amount=200, date='02/08/2022'),
        Withdraw(amount=50, date='03/08/2022')
    ]


@pytest.fixture()
def mocked_date_provider():
    date_provider = MagicMock(DateProvider)
    date_provider.today.return_value = '01/08/2022'
    return date_provider


@pytest.fixture()
def mocked_transaction_repository():
    return MagicMock(TransactionRepository)


@pytest.fixture()
def mocked_statement_printer():
    return MagicMock(StatementPrinter)


@pytest.fixture()
def account_service(mocked_transaction_repository, mocked_statement_printer, mocked_date_provider):
    return AccountService(
        transaction_repository=mocked_transaction_repository,
        statement_printer=mocked_statement_printer,
        date_provider=mocked_date_provider
    )
