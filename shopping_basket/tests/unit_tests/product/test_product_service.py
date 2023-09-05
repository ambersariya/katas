import pytest

from tests.constants import PRODUCT_ID_BREAKING_BAD, PRODUCT_VIDEO_BREAKING_BAD
from shopping_basket.product.product import Product
from shopping_basket.product.product_error import ProductNotFoundError
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_error import InsufficientStockError


class TestProductServiceShould:
    def test_return_product_by_id(self, mocked_product_repository, product_service) -> None:
        mocked_product_repository.find_product_by_id.return_value = PRODUCT_VIDEO_BREAKING_BAD
        product = product_service.reserve(product_id=PRODUCT_ID_BREAKING_BAD, quantity=2)
        assert isinstance(product, Product)

    def test_raise_error_when_product_is_not_found(
        self, mocked_product_repository, product_service
    ) -> None:
        mocked_product_repository.find_product_by_id.return_value = None

        with pytest.raises(ProductNotFoundError):
            product_service.reserve(product_id=PRODUCT_ID_BREAKING_BAD, quantity=2)

    def test_raise_error_when_product_has_less_stock_than_required(
        self, mocked_stock_management_service, mocked_product_repository, product_service
    ) -> None:
        mocked_product_repository.find_product_by_id.return_value = PRODUCT_VIDEO_BREAKING_BAD
        mocked_stock_management_service.reserve.side_effect = InsufficientStockError()

        with pytest.raises(InsufficientStockError):
            product_service.reserve(product_id=PRODUCT_ID_BREAKING_BAD, quantity=5)

    def test_add_item_to_repository(
        self, mocked_stock_management_service, mocked_product_repository, product_service
    ) -> None:
        stock = Stock(available=5, reserved=0, product_id=PRODUCT_ID_BREAKING_BAD, min_available=5)
        product_service.add_product(product=PRODUCT_VIDEO_BREAKING_BAD, stock=stock)

        mocked_product_repository.add_product.assert_called_once_with(
            product=PRODUCT_VIDEO_BREAKING_BAD
        )
        mocked_stock_management_service.save_stock.assert_called_once_with(stock=stock)
