from dataclasses import dataclass
from enum import Enum

from merchants_guide_to_galaxy.domain.intergalactic_symbols import IntergalacticSymbol


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
