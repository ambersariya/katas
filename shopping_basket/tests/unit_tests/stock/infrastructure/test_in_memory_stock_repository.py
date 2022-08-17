from unittest import TestCase

from constants import STOCK_VIDEO, PRODUCT_ID_VIDEO
from shopping_basket.stock.infrastructure.in_memory_stock_repository import (
    InMemoryStockRepository,
)


class InMemoryStockRepositoryShould(TestCase):
    def test_find_stock_by_id(self):
        self.repository = InMemoryStockRepository()
        self.repository.save_stock(stock=STOCK_VIDEO)

        retrieved_stock = self.repository.find_by_id(product_id=PRODUCT_ID_VIDEO)

        self.assertEqual(retrieved_stock, STOCK_VIDEO)
