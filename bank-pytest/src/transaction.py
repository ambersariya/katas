from dataclasses import dataclass
from typing import Protocol


class Transaction(Protocol):
    pass


@dataclass(init=True, frozen=True)
class Deposit(Transaction):
    amount: int


@dataclass(init=True, frozen=True)
class Withdraw(Transaction):
    amount: int
