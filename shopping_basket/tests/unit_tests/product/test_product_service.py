from unittest import TestCase
from unittest.mock import MagicMock

from constants import PRODUCT_VIDEO, PRODUCT_ID_VIDEO
from shopping_basket.product.product import Product
from shopping_basket.product.product_error import ProductNotFoundError
from shopping_basket.product.product_repository import ProductRepository
from shopping_basket.product.product_service import ProductService
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_error import InsufficientStockError
from shopping_basket.stock.stock_management_service import StockManagementService


class ProductServiceShould(TestCase):
    def setUp(self):
        self.product_repository = MagicMock(ProductRepository)
        self.stock_manager = MagicMock(StockManagementService)
        self.product_service = ProductService(
            self.product_repository, self.stock_manager
        )

    def test_return_product_by_id(self):
        self.product_repository.find_product_by_id.return_value = PRODUCT_VIDEO

        product = self.product_service.reserve(product_id=PRODUCT_ID_VIDEO, quantity=2)

        self.assertIsInstance(product, Product)

    def test_raise_error_when_product_is_not_found(self):
        self.product_repository.find_product_by_id.return_value = None

        with self.assertRaises(ProductNotFoundError):
            self.product_service.reserve(product_id=PRODUCT_ID_VIDEO, quantity=2)

    def test_raise_error_when_product_has_less_stock_than_required(self):
        self.product_repository.find_product_by_id.return_value = PRODUCT_VIDEO
        self.stock_manager.reserve.side_effect = InsufficientStockError()

        with self.assertRaises(InsufficientStockError):
            self.product_service.reserve(product_id=PRODUCT_ID_VIDEO, quantity=5)

    def test_add_item_to_repository(self):
        stock = Stock(available=5, reserved=0, product_id=PRODUCT_ID_VIDEO)
        self.product_service.add_product(product=PRODUCT_VIDEO, stock=stock)

        self.product_repository.add_product.assert_called_once_with(product=PRODUCT_VIDEO)
        self.stock_manager.save_stock.assert_called_once_with(stock=stock)
