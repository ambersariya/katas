from abc import abstractmethod
from typing import Protocol, Dict

StockPrices = Dict[str, float]


class StockPricingRepository(Protocol):

    @abstractmethod
    def set_stock_price(self, stock: str, price: float):
        pass

    @abstractmethod
    def fetch_prices(self) -> StockPrices:
        pass
