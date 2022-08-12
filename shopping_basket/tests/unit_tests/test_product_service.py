from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.errors import ProductNotFoundError
from shopping_basket.product import ProductId, Product
from shopping_basket.product_repository import ProductRepository
from shopping_basket.product_service import ProductService


class ProductServiceShould(TestCase):

    def setUp(self):
        self.product_repository = MagicMock(ProductRepository)
        self.product_service = ProductService(self.product_repository)

    def test_return_product_by_id(self):
        product_id = ProductId('10001')
        self.product_repository.find_product_by_id.return_value = Product(product_id, 'product', 5)

        product = self.product_service.find_product_by_id(product_id)

        self.assertIsInstance(product, Product)

    def test_raise_error_when_product_is_not_found(self):
        product_id = ProductId('10001')
        self.product_repository.find_product_by_id.return_value = None

        with self.assertRaises(ProductNotFoundError):
            self.product_service.find_product_by_id(product_id)
