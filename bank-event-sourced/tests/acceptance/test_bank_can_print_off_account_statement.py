import uuid
from decimal import Decimal
from unittest.mock import patch

import pytest

from account import BankAccount, Bank

ACCOUNT_ID = 'e51a4075-eed5-4e65-bc12-cffb0a07b447'
EXPECTED_STATEMENT = \
    """Date | Amount | Balance
14/01/2012 | -500 | 2500
13/01/2012 | 2000 | 3000
10/01/2012 | 1000 | 1000"""


@pytest.fixture()
def bank() -> Bank:
    return Bank()


def test_print_all_transactions(bank) -> None:
    account_id = bank.open_account(full_name='Uncle Bob', email_address='bob@example.org')
    bank.deposit(amount=Decimal(1000), account_id=account_id)

    account = bank.get_account(account_id=account_id)
    account.collect_events()

    # bank.deposit(2000)
    # bank.withdraw(500)
    # bank.print_statement()
