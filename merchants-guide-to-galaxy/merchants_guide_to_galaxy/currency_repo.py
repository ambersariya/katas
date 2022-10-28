from dataclasses import dataclass
from enum import Enum
from typing import Protocol


class CurrencyValue(Enum):
    I = 1
    V = 5
    X = 10
    L = 250
    C = 100
    D = 500
    M = 1000


@dataclass
class Currency:
    name: str
    value: CurrencyValue


class CurrencyRepo(Protocol):
    def add(self, currency: Currency):
        pass
