from dataclasses import dataclass
from enum import Enum
from typing import Protocol

from merchants_guide_to_galaxy.error import NonExistingCurrency


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


class InMemoryCurrencyRepo:
    def __init__(self):
        self.repo: dict = {}

    def __len__(self):
        return len(self.repo)

    def add(self, currency: Currency):
        self.repo[currency.name] = currency

    def get_currency(self, currency_name: str) -> Currency | NonExistingCurrency:
        if currency_name not in self.repo:
            raise NonExistingCurrency()
        return self.repo[currency_name]
