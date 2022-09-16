import uuid
from decimal import Decimal
from uuid import UUID

from eventsourcing.application import Application, AggregateNotFound
from eventsourcing.domain import Aggregate, event


class BankAccount(Aggregate):
    @event('Opened')
    def __init__(self, full_name: str, email_address: str):
        self.email_address = email_address
        self.full_name = full_name
        self.balance = Decimal("0.00")
        self.overdraft_limit = Decimal("0.00")
        self.is_closed = False

    @event('MoneyIn.Deposit')
    def deposit(self, amount) -> None:
        self.balance += amount

    @event('MoneyOut.Withdrawn')
    def withdraw(self, amount) -> None:
        self.balance -= amount


class AccountNotFoundError(Exception):
    pass


class Bank(Application):
    def open_account(self, full_name: str, email_address: str) -> UUID:
        account = BankAccount(
            full_name=full_name,
            email_address=email_address,
        )

        self.save(account)
        return account.id

    def get_account(self, account_id: UUID) -> BankAccount:
        try:
            return self.repository.get(account_id)
        except AggregateNotFound:
            raise AccountNotFoundError(account_id)

    def deposit(self, account_id: UUID, amount: Decimal) -> None:
        account = self.get_account(account_id)
        account.deposit(amount=amount)
        self.save(account)

    def withdraw(self, account_id: UUID, amount: Decimal) -> None:
        account = self.get_account(account_id)
        account.withdraw(amount=amount)
        self.save(account)

    def print_statement(self) -> None:
        pass
