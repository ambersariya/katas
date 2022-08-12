from typing import Protocol

from shopping_basket.product import ProductId
from shopping_basket.stock.stock import Stock


class StockRepository(Protocol):
    def save_stock(self, stock):
        pass

    def find_by_id(self, product_id: ProductId) -> Stock:
        pass


class InMemoryStockRepository(StockRepository):
    def __init__(self):
        self._stock = {}

    def save_stock(self, stock):
        self._stock[stock.product_id] = stock

    def find_by_id(self, product_id: ProductId) -> Stock:
        return self._stock[product_id]
