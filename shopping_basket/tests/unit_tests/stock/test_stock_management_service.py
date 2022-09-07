from unittest import mock
from unittest.mock import call

import pytest

from constants import (
    BASKET_ITEM_LORD_OF_THE_RINGS_QUANTITY_FIVE,
    PRODUCT_ID_BREAKING_BAD,
    PURCHASED_STOCK_VIDEO_BREAKING_BAD,
    RESERVED_STOCK_VIDEO_BREAKING_BAD,
    SOLD_STOCK_VIDEO_BREAKING_BAD,
    STOCK_VIDEO_BREAKING_BAD,
)
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.stock.event import StockIsLow
from shopping_basket.stock.stock_error import InsufficientStockError


class TestStockManagementServiceShould:
    def test_add_stock_to_repository(self, mocked_stock_repository,
                                     stock_management_service) -> None:
        stock_management_service.save_stock(STOCK_VIDEO_BREAKING_BAD)
        mocked_stock_repository.save_stock.assert_called_once_with(STOCK_VIDEO_BREAKING_BAD)

    def test_reserve_stock(self, mocked_stock_repository, stock_management_service) -> None:
        quantity = 5
        mocked_stock_repository.find_by_id.return_value = STOCK_VIDEO_BREAKING_BAD
        stock_management_service.reserve(product_id=PRODUCT_ID_BREAKING_BAD, quantity=quantity)

        mocked_stock_repository.save_stock.assert_called_once_with(
            stock=RESERVED_STOCK_VIDEO_BREAKING_BAD
        )

    def test_raise_error_when_reserving_more_stock_than_available(self,
                                                                  mocked_stock_repository,
                                                                  stock_management_service) -> None:
        quantity = 7
        mocked_stock_repository.find_by_id.return_value = STOCK_VIDEO_BREAKING_BAD

        with pytest.raises(InsufficientStockError):
            stock_management_service.reserve(product_id=PRODUCT_ID_BREAKING_BAD, quantity=quantity)
        mocked_stock_repository.save_stock.assert_not_called()

    @mock.patch('shopping_basket.stock.stock_management_service.handle')
    def test_update_stock_levels_for_items_purchased(self,
                                                     event_handler,
                                                     mocked_stock_repository,
                                                     stock_management_service) -> None:
        mocked_stock_repository.find_by_id.return_value = RESERVED_STOCK_VIDEO_BREAKING_BAD
        stock_management_service.update_stock(
            items=ShoppingBasketItems(items=[BASKET_ITEM_LORD_OF_THE_RINGS_QUANTITY_FIVE])
        )
        mocked_stock_repository.save_stock.assert_has_calls(
            [call(stock=SOLD_STOCK_VIDEO_BREAKING_BAD)]
        )
        event_handler.assert_called_once_with(
            event=StockIsLow(product_id=SOLD_STOCK_VIDEO_BREAKING_BAD.product_id, order_quantity=5)
        )

    def test_increase_stock_levels_for_product(self,
                                               mocked_stock_repository,
                                               stock_management_service) -> None:
        mocked_stock_repository.find_by_id.return_value = SOLD_STOCK_VIDEO_BREAKING_BAD
        stock_management_service.increase_stock(product_id=PRODUCT_ID_BREAKING_BAD, quantity=5)
        mocked_stock_repository.save_stock.assert_called_once_with(
            stock=PURCHASED_STOCK_VIDEO_BREAKING_BAD
        )
