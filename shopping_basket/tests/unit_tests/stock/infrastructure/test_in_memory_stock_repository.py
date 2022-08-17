from unittest import TestCase

from shopping_basket.product.product_id import ProductId
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.infrastructure.in_memory_stock_repository import (
    InMemoryStockRepository,
)

PRODUCT_ID = ProductId("10001")
STOCK = Stock(available=5, reserved=0, product_id=PRODUCT_ID)


class InMemoryStockRepositoryShould(TestCase):
    def test_find_stock_by_id(self):
        self.repository = InMemoryStockRepository()
        self.repository.save_stock(stock=STOCK)

        retrieved_stock = self.repository.find_by_id(product_id=PRODUCT_ID)

        self.assertEqual(retrieved_stock, STOCK)
