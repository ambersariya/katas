from src.transaction import Deposit
from src.transaction_repository import TransactionRepository


class AccountService:

    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    def deposit(self, amount: int) -> None:
        self.transaction_repository.add_transaction(transaction=Deposit(amount=amount))

    def withdraw(self, amount: int) -> None:
        raise NotImplementedError()

    def print_statement(self) -> None:
        raise NotImplementedError()
