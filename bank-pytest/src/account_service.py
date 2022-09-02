from src.statement_printer import StatementPrinter
from src.transaction import Deposit, Withdraw
from src.transaction_repository import TransactionRepository


class AccountService:
    def __init__(self,
                 transaction_repository: TransactionRepository,
                 statement_printer: StatementPrinter
                 ) -> None:
        self.statement_printer = statement_printer
        self.transaction_repository = transaction_repository

    def deposit(self, amount: int) -> None:
        self.transaction_repository.add_transaction(transaction=Deposit(amount=amount))

    def withdraw(self, amount: int) -> None:
        self.transaction_repository.add_transaction(transaction=Withdraw(amount=amount))

    def print_statement(self) -> None:
        transactions = self.transaction_repository.all_transactions()
        self.statement_printer.print(transactions)
