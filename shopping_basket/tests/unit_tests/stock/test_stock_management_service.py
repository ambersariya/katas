from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.product.product_id import ProductId
from shopping_basket.stock.stock_error import InsufficientStockError
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_management_service import StockManagementService
from shopping_basket.stock.stock_repository import StockRepository

PRODUCT_ID = ProductId('10001')
STOCK = Stock(available=5, reserved=0, product_id=PRODUCT_ID)
UPDATED_STOCK = Stock(available=0, reserved=5, product_id=PRODUCT_ID)


class StockManagementServiceShould(TestCase):

    def setUp(self):
        self.stock_repository = MagicMock(StockRepository)
        self.stock_management = StockManagementService(stock_repository=self.stock_repository)

    def test_add_stock_to_repository(self):
        self.stock_management.save_stock(STOCK)

        self.stock_repository.save_stock.assert_called_once_with(STOCK)

    def test_reserve_stock(self):
        quantity = 5
        self.stock_repository.find_by_id.return_value = STOCK
        self.stock_management.reserve(product_id=PRODUCT_ID, quantity=quantity)

        self.stock_repository.save_stock.assert_called_once_with(UPDATED_STOCK)

    def test_raiser_error_when_reserving_more_stock_than_available(self):
        quantity = 7
        self.stock_repository.find_by_id.return_value = STOCK

        with self.assertRaises(InsufficientStockError):
            self.stock_management.reserve(product_id=PRODUCT_ID, quantity=quantity)
        self.stock_repository.save_stock.assert_not_called()
