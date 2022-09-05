from abc import ABC
from datetime import datetime

TRANSACTION_DATE_FORMAT = '%d/%m/%Y'


class Transaction(ABC):
    def __init__(self, date: str, amount: int):
        self._amount: int = amount
        self._date: datetime = datetime.strptime(date, TRANSACTION_DATE_FORMAT)

    @property
    def date(self) -> str:
        return self._date.strftime(TRANSACTION_DATE_FORMAT)

    @property
    def amount(self) -> int:
        return self._amount


class Deposit(Transaction):
    def __init__(self, amount: int, date: str):
        super().__init__(amount=amount, date=date)


class Withdraw(Transaction):

    def __init__(self, amount: int, date: str):
        super().__init__(amount=amount, date=date)
