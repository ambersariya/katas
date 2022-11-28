from merchants_guide_to_galaxy.domain.symbol_repo import SymbolRepo
from merchants_guide_to_galaxy.domain.error import NonExistingCurrency
from merchants_guide_to_galaxy.domain.intergalactic_symbols import IntergalacticSymbol


class InMemorySymbolRepo(SymbolRepo):
    def __init__(self):
        self.repo: dict = {}

    def __len__(self):
        return len(self.repo)

    def add(self, symbol: IntergalacticSymbol):
        self.repo[symbol.name] = symbol

    def symbol_value(self, symbol: str) -> str:
        if symbol not in self.repo:
            raise NonExistingCurrency()
        return self.repo[symbol].value
