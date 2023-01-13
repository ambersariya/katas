from abc import abstractmethod
from typing import Protocol, Dict, List

from src.asset import Asset
from src.value_objects import StockName, StockPrice


class PortfolioPresenter(Protocol):
    @abstractmethod
    def present(self, assets: List[Asset], prices: Dict[StockName, StockPrice]):
        pass
