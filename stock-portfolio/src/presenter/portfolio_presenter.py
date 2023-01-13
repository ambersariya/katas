from abc import abstractmethod
from typing import Protocol, Dict, List

from src.asset import Asset
from src.repository.stock_pricing_repository import StockName, StockPrice


class Presenter(Protocol):
    @abstractmethod
    def present(self, assets: List[Asset], prices: Dict[StockName, StockPrice]):
        pass
