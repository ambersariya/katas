from constants import (
    UPDATED_PRODUCT_WITH_OLD_ID,
    PRODUCT_ID_BREAKING_BAD,
    PRODUCT_VIDEO_BREAKING_BAD,
)
from shopping_basket.product.product_id import ProductId


class TestProductRepositoryShould:
    def test_return_product_by_id(self, product_repository) -> None:
        product_repository.add_product(PRODUCT_VIDEO_BREAKING_BAD)
        expected_product = product_repository.find_product_by_id(PRODUCT_ID_BREAKING_BAD)
        assert expected_product == PRODUCT_VIDEO_BREAKING_BAD

    def test_return_nothing_when_product_doesnt_exist(self, product_repository) -> None:
        expected_product = product_repository.find_product_by_id(ProductId("random_id"))
        assert expected_product is None

    def test_return_updated_product_when_adding_new_product_with_existing_id(
        self, product_repository
    ) -> None:
        product_repository.add_product(UPDATED_PRODUCT_WITH_OLD_ID)

        expected_product = product_repository.find_product_by_id(PRODUCT_ID_BREAKING_BAD)
        assert expected_product == UPDATED_PRODUCT_WITH_OLD_ID
