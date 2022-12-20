from merchants_guide_to_galaxy.domain.currency import Currency
from merchants_guide_to_galaxy.domain.error import NonExistingCurrency
from merchants_guide_to_galaxy.domain.intergalactic_symbols import IntergalacticSymbol
from merchants_guide_to_galaxy.domain.symbol_repo import SymbolRepo


class InMemorySymbolRepo(SymbolRepo):
    def __init__(self):
        self.repo: dict = {}

    def __len__(self):
        return len(self.repo)

    def add(self, symbol: IntergalacticSymbol):
        self.repo[symbol.name] = symbol

    def find_symbol_value(self, symbol: str) -> IntergalacticSymbol:
        if symbol not in self.repo:
            raise NonExistingCurrency()
        return self.repo[symbol]
