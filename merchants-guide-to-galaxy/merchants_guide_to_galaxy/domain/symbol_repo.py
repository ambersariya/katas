from typing import Protocol

from merchants_guide_to_galaxy.domain.currency import Currency
from merchants_guide_to_galaxy.domain.intergalactic_symbols import IntergalacticSymbol


class SymbolRepo(Protocol):
    def add(self, symbol: IntergalacticSymbol):
        pass

    def find_symbol_value(self, symbol: str) -> IntergalacticSymbol | Currency:
        pass
