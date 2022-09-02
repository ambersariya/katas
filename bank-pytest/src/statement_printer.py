from typing import Protocol


class StatementPrinter(Protocol):
    def print(self) -> None:
        pass
