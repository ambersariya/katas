from typing import Dict

from src.repository.stock_pricing_repository import StockPricingRepository, StockUnknownError
from src.value_objects import StockName, StockPrice


class InMemoryStockPriceRepository(StockPricingRepository):
    def __init__(self) -> None:
        self.__prices: Dict[StockName, StockPrice] = {}

    def set_stock_price(self, stock: StockName, price: StockPrice) -> None:
        self.__prices[stock] = price

    def fetch_stock_price(self, stock: StockName) -> StockPrice:
        if stock not in self.__prices:
            raise StockUnknownError(f'No pricing available for stock {stock}')
        return self.__prices[stock]
