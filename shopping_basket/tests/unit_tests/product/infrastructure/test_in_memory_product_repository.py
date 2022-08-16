from typing import Final
from unittest import TestCase

from shopping_basket.product.product import Product
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.infrastructure.in_memory_product_repository import InMemoryProductRepository

PRODUCT_ID: Final[ProductId] = ProductId("10001")
PRODUCT: Final[Product] = Product(PRODUCT_ID, name='Lord of the Rings', price=10, category=ProductCategory.BOOK)
NEW_PRODUCT: Final[Product] = Product(PRODUCT_ID, name='Lord of the Rings HD', price=10, category=ProductCategory.VIDEO)


class ProductRepositoryShould(TestCase):
    def setUp(self) -> None:
        self.product_repo = InMemoryProductRepository()
        self.product_repo.add_product(PRODUCT)

    def test_return_product_by_id(self) -> None:
        expected_product = self.product_repo.find_product_by_id(PRODUCT_ID)

        self.assertEqual(expected_product, PRODUCT)

    def test_return_nothing_when_product_doesnt_exist(self) -> None:
        expected_product = self.product_repo.find_product_by_id(ProductId('random_id'))

        self.assertIsNone(expected_product)

    def test_return_updated_product_when_adding_new_product_with_existing_id(self) -> None:
        self.product_repo.add_product(NEW_PRODUCT)

        expected_product = self.product_repo.find_product_by_id(PRODUCT_ID)
        self.assertEqual(expected_product, NEW_PRODUCT)
