from unittest.mock import patch

import pytest

from src.exceptions import NoTransactionsToPrint
from src.statement_printer import ConsoleStatementPrinter


def test_raise_exception_when_there_are_no_transactions(empty_transactions) -> None:
    statement_printer = ConsoleStatementPrinter()
    with pytest.raises(NoTransactionsToPrint, match=r'No transactions to print'):
        statement_printer.print(transactions=empty_transactions)


@patch("builtins.print")
def test_print_a_list_of_transactions_in_reverse_chronological_order(
    mocked_print,
    transactions
) -> None:
    statement_printer = ConsoleStatementPrinter()
    statement_printer.print(transactions=transactions)

    expected_print = \
        "Date | Amount | Balance\n" \
        "03/08/2022 | -50 | 250\n" \
        "02/08/2022 | 200 | 300\n" \
        "01/08/2022 | 100 | 100"

    mocked_print.assert_called_with(expected_print)
