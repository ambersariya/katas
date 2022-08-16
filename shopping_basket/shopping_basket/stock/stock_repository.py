from typing import Protocol

from shopping_basket.product.product_id import ProductId
from shopping_basket.stock.stock import Stock


class StockRepository(Protocol):
    def save_stock(self, stock: Stock):
        pass

    def find_by_id(self, product_id: ProductId) -> Stock:
        pass


