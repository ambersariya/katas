from abc import abstractmethod
from typing import Protocol

from src.transaction import Transaction


class TransactionRepository(Protocol):
    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> None:
        raise NotImplementedError()


class InMemoryTransactionRepository(TransactionRepository):

    def __init__(self):
        self._transactions = []

    def add_transaction(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)
