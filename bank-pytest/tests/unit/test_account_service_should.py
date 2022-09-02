from unittest.mock import MagicMock

import pytest

from src.account_service import AccountService
from src.transaction_repository import TransactionRepository


@pytest.fixture()
def mocked_transaction_repository():
    return MagicMock(TransactionRepository)


def test_add_deposit(mocked_transaction_repository):
    account_service = AccountService(transaction_repository=mocked_transaction_repository)
    account_service.deposit(100)

    mocked_transaction_repository.add_transaction.assert_called_once()

def test_withdraw(mocked_transaction_repository):
    account_service = AccountService(transaction_repository=mocked_transaction_repository)
    account_service.withdraw(100)

    mocked_transaction_repository.add_transaction.assert_called_once()
