from abc import abstractmethod
from string import Template
from typing import Protocol

from src.exceptions import NoTransactionsToPrint
from src.transaction import Transaction, Deposit, Withdraw


class StatementPrinter(Protocol):
    @abstractmethod
    def print(self, transactions: list[Transaction]) -> None:
        pass  # pragma: no cover


class ConsoleStatementPrinter(StatementPrinter):
    def print(self, transactions: list[Transaction]) -> None:
        self.__ensure_has_transactions(transactions)
        header = 'Date | Amount | Balance'
        transaction_template = Template('$date | $amount | $balance')
        transaction_statements = []
        running_balance = 0
        for _transaction in transactions:
            amount = -_transaction.amount if isinstance(_transaction, Withdraw) \
                else _transaction.amount
            running_balance = self.__calculate_running_balance(running_balance, _transaction)
            transaction_statements.append(transaction_template.safe_substitute(
                date=_transaction.date,
                amount=amount,
                balance=running_balance,
            ))
        transaction_statements.append(header)
        transaction_statements.reverse()

        print('\n'.join(transaction_statements))

    @staticmethod
    def __calculate_running_balance(running_balance: int, transaction: Transaction) -> int:
        if isinstance(transaction, Deposit):
            running_balance += transaction.amount
        else:
            running_balance -= transaction.amount
        return running_balance

    @staticmethod
    def __ensure_has_transactions(transactions: list[Transaction]) -> None:
        if len(transactions) == 0:
            raise NoTransactionsToPrint("No transactions to print")
