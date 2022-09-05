from typing import Any
from unittest.mock import patch

from src.account_service import AccountService
from src.date_provider import DateProvider
from src.statement_printer import StatementPrinter
from src.transaction_repository import TransactionRepository

EXPECTED_STATEMENT = \
    """Date | Amount | Balance
14/01/2012 | -500 | 2500
13/01/2012 | 2000 | 3000
10/01/2012 | 1000 | 1000"""


@patch("builtins.print")
def test_print_all_transactions(
    mocked_print: Any,
    transaction_repository: TransactionRepository,
    statement_printer: StatementPrinter,
    mocked_date_provider: DateProvider
) -> None:
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
