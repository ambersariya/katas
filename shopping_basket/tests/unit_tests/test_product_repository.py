from typing import Final
from unittest import TestCase

from shopping_basket.product import ProductId, Product
from shopping_basket.product_repository import InMemoryProductRepository

PRODUCT_ID: Final[ProductId] = ProductId("10001")
PRODUCT: Final[Product] = Product(PRODUCT_ID, name='Lord of the Rings', price=10)
NEW_PRODUCT: Final[Product] = Product(PRODUCT_ID, name='Lord of the Rings HD', price=10)


class ProductRepositoryShould(TestCase):

    def setUp(self):
        self.product_repo = InMemoryProductRepository()
        self.product_repo.add_product(PRODUCT)

    def test_return_product_by_id(self):
        expected_product = self.product_repo.find_product_by_id(PRODUCT_ID)

        self.assertEqual(expected_product, PRODUCT)

    def test_return_nothing_when_product_doesnt_exist(self):
        expected_product = self.product_repo.find_product_by_id(ProductId('random_id'))

        self.assertIsNone(expected_product)

    def test_return_updated_product_when_adding_new_product_with_existing_id(self):
        self.product_repo.add_product(NEW_PRODUCT)

        expected_product = self.product_repo.find_product_by_id(PRODUCT_ID)
        self.assertEqual(expected_product, NEW_PRODUCT)

