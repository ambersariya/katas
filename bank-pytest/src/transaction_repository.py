from abc import abstractmethod
from typing import Protocol

from src.transaction import Transaction


class TransactionRepository(Protocol):
    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def all_transactions(self) -> list[Transaction]:
        pass  # pragma: no cover


class InMemoryTransactionRepository(TransactionRepository):

    def __init__(self) -> None:
        self._transactions: list[Transaction] = []

    def add_transaction(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)

    def all_transactions(self) -> list[Transaction]:
        return self._transactions
