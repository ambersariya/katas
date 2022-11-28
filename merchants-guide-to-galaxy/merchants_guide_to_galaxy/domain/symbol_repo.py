from typing import Protocol

from merchants_guide_to_galaxy.domain.intergalactic_symbols import IntergalacticSymbol


class SymbolRepo(Protocol):
    def add(self, symbol: IntergalacticSymbol):
        pass

    def symbol_value(self, symbol: str) -> str:
        pass
