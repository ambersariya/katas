from dataclasses import dataclass
from enum import Enum
from typing import Protocol

from merchants_guide_to_galaxy.error import NonExistingCurrency
from merchants_guide_to_galaxy.intergalactic_symbols import IntergalacticSymbol


class CurrencyValue(Enum):
    I = 1
    V = 5
    X = 10
    L = 250
    C = 100
    D = 500
    M = 1000


@dataclass(init=True, frozen=True)
class Currency(IntergalacticSymbol):
    value: CurrencyValue


class SymbolRepo(Protocol):
    def add(self, symbol: IntergalacticSymbol):
        pass

    def symbol_value(self, symbol: str) -> IntergalacticSymbol | NonExistingCurrency:
        pass


class InMemorySymbolRepo:
    def __init__(self):
        self.repo: dict = {}

    def __len__(self):
        return len(self.repo)

    def add(self, symbol: IntergalacticSymbol):
        self.repo[symbol.name] = symbol

    def symbol_value(self, symbol: str) -> IntergalacticSymbol | NonExistingCurrency:
        if symbol not in self.repo:
            raise NonExistingCurrency()
        return self.repo[symbol]
