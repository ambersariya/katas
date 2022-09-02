from typing import Protocol

from src.exceptions import NoTransactionsToPrint


class StatementPrinter(Protocol):
    def print(self, transactions) -> None:
        pass


class ConsoleStatementPrinter(StatementPrinter):
    def print(self, transactions) -> None:
        if len(transactions) is 0:
            raise NoTransactionsToPrint("No transactions to print ")
