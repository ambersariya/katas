from typing import Final
from unittest import TestCase

from shopping_basket.product import ProductId, Product
from shopping_basket.product_repository import InMemoryProductRepository

PRODUCT_ID: Final[ProductId] = ProductId("10001")
PRODUCT: Final[Product] = Product(PRODUCT_ID, name='Lord of the Rings', price=10)


class ProductRepositoryShould(TestCase):
    def test_return_product_by_id(self):
        product_repo = InMemoryProductRepository()
        product_repo.add_product(PRODUCT)

        expected_product = product_repo.find_product_by_id(PRODUCT_ID)

        self.assertEqual(expected_product, PRODUCT)

    def test_return_nothing_when_product_doesnt_exist(self):
        product_repo = InMemoryProductRepository()
        product_repo.add_product(PRODUCT)

        expected_product = product_repo.find_product_by_id(ProductId('random_id'))

        self.assertIsNone(expected_product)
