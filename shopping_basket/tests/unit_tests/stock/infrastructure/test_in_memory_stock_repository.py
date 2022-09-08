from unittest import TestCase

from constants import PRODUCT_ID_BREAKING_BAD, STOCK_VIDEO_BREAKING_BAD
from shopping_basket.stock.infrastructure.in_memory_stock_repository import InMemoryStockRepository


class InMemoryStockRepositoryShould(TestCase):
    def test_find_stock_by_id(self):
        self.repository = InMemoryStockRepository()
        self.repository.save_stock(stock=STOCK_VIDEO_BREAKING_BAD)

        retrieved_stock = self.repository.find_by_id(product_id=PRODUCT_ID_BREAKING_BAD)

        self.assertEqual(retrieved_stock, STOCK_VIDEO_BREAKING_BAD)
