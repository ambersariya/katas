from typing import Protocol


class StatementPrinter(Protocol):
    def print(self, transactions) -> None:
        pass


class ConsoleStatementPrinter(StatementPrinter):
    pass
