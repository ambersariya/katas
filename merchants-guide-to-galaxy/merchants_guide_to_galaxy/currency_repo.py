from dataclasses import dataclass
from enum import auto, Enum
from typing import Protocol

from merchants_guide_to_galaxy.error import NonExistingCurrency
from merchants_guide_to_galaxy.intergalactic_symbols import IntergalacticSymbol


class CurrencyValue(str, Enum):
    I = "I"
    V = "V"
    X = "X"
    L = "L"
    C = "C"
    D = "D"
    M = "M"


@dataclass(init=True, frozen=True)
class Currency(IntergalacticSymbol):
    value: CurrencyValue

    def __str__(self):
        return str(self.value)


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
