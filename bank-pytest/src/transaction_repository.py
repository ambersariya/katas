from abc import abstractmethod
from typing import Protocol

from src.transaction import Transaction


class TransactionRepository(Protocol):
    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def all_transactions(self) -> list[Transaction]:
        pass


class InMemoryTransactionRepository(TransactionRepository):

    def __init__(self) -> None:
        self._transactions: list[Transaction] = []

    def add_transaction(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)

    def all_transactions(self) -> list[Transaction]:
        return self._transactions
