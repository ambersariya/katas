from typing import Dict

from shopping_basket.product.product_id import ProductId
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_repository import StockRepository


class InMemoryStockRepository(StockRepository):
    def __init__(self):
        self._stock: Dict[ProductId, Stock] = {}

    def save_stock(self, stock: Stock):
        self._stock[stock.product_id] = stock

    def find_by_id(self, product_id: ProductId) -> Stock:
        return self._stock[product_id]
