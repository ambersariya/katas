from unittest import TestCase

from constants import NEW_VIDEO_PRODUCT, PRODUCT_ID_VIDEO, PRODUCT_VIDEO

from shopping_basket.product.infrastructure.in_memory_product_repository import (
    InMemoryProductRepository,
)
from shopping_basket.product.product_id import ProductId


class ProductRepositoryShould(TestCase):
    def setUp(self) -> None:
        self.product_repo = InMemoryProductRepository()
        self.product_repo.add_product(PRODUCT_VIDEO)

    def test_return_product_by_id(self) -> None:
        expected_product = self.product_repo.find_product_by_id(PRODUCT_ID_VIDEO)

        self.assertEqual(expected_product, PRODUCT_VIDEO)

    def test_return_nothing_when_product_doesnt_exist(self) -> None:
        expected_product = self.product_repo.find_product_by_id(ProductId("random_id"))

        self.assertIsNone(expected_product)

    def test_return_updated_product_when_adding_new_product_with_existing_id(
        self,
    ) -> None:
        self.product_repo.add_product(NEW_VIDEO_PRODUCT)

        expected_product = self.product_repo.find_product_by_id(PRODUCT_ID_VIDEO)
        self.assertEqual(expected_product, NEW_VIDEO_PRODUCT)
