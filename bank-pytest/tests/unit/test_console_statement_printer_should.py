import pytest

from src.exceptions import NoTransactionsToPrint
from src.statement_printer import ConsoleStatementPrinter


@pytest.fixture()
def empty_transactions():
    return []


@pytest.fixture()
def transactions():
    pass


def test_raise_exception_when_there_are_no_transactions(empty_transactions):
    statement_printer = ConsoleStatementPrinter()
    with pytest.raises(NoTransactionsToPrint, match=r'.* No Transaction *.'):
        statement_printer.print(transactions=empty_transactions)


# def test_print_a_list_of_transactions_in_reverse_chronological_order(transactions) -> None:
#     statement_printer = ConsoleStatementPrinter()
#     statement_printer.print(transactions=transactions)
#     pass
