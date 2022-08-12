from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.errors import ProductNotFoundError, OutOfStockError
from shopping_basket.product import ProductId, Product
from shopping_basket.product_repository import ProductRepository
from shopping_basket.product_service import ProductService
from shopping_basket.stock.stock_management_service import StockManagementService

PRODUCT_ID = ProductId('10001')


class ProductServiceShould(TestCase):

    def setUp(self):
        self.product_repository = MagicMock(ProductRepository)
        self.stock_manager = MagicMock(StockManagementService)
        self.product_service = ProductService(self.product_repository, self.stock_manager)

    def test_return_product_by_id(self):
        self.product_repository.find_product_by_id.return_value = Product(id=PRODUCT_ID, name='product', price=5)

        product = self.product_service.find_and_reserve(product_id=PRODUCT_ID, quantity=2)

        self.assertIsInstance(product, Product)

    def test_raise_error_when_product_is_not_found(self):
        self.product_repository.find_product_by_id.return_value = None

        with self.assertRaises(ProductNotFoundError):
            self.product_service.find_and_reserve(product_id=PRODUCT_ID, quantity=2)

    def test_raise_error_when_product_has_less_stock_than_required(self):
        self.product_repository.find_product_by_id.return_value = Product(id=PRODUCT_ID, name='product', price=5)
        self.stock_manager.reserve.side_effect = OutOfStockError()

        with self.assertRaises(OutOfStockError):
            self.product_service.find_and_reserve(product_id=PRODUCT_ID, quantity=5)
