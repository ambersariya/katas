from unittest import TestCase
from unittest.mock import MagicMock, call

from constants import STOCK_VIDEO, PRODUCT_ID_VIDEO, RESERVED_STOCK_VIDEO, SHOPPING_BASKET, \
    BASKET_ITEM_QUANTITY_FIVE, SOLD_STOCK_VIDEO, PURCHASED_STOCK_VIDEO
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.core.messagebus import MessageBus
from shopping_basket.stock.event import StockIsLow
from shopping_basket.stock.stock_error import InsufficientStockError
from shopping_basket.stock.stock_management_service import StockManagementService
from shopping_basket.stock.stock_repository import StockRepository


class StockManagementServiceShould(TestCase):
    def setUp(self):
        self.stock_repository = MagicMock(StockRepository)
        self.message_bus = MagicMock(MessageBus)
        self.stock_management = StockManagementService(
            stock_repository=self.stock_repository,
            message_bus=self.message_bus
        )

    def test_add_stock_to_repository(self):
        self.stock_management.save_stock(STOCK_VIDEO)
        self.stock_repository.save_stock.assert_called_once_with(STOCK_VIDEO)

    def test_reserve_stock(self):
        quantity = 5
        self.stock_repository.find_by_id.return_value = STOCK_VIDEO
        self.stock_management.reserve(product_id=PRODUCT_ID_VIDEO, quantity=quantity)

        self.stock_repository.save_stock.assert_called_once_with(stock=RESERVED_STOCK_VIDEO)

    def test_raise_error_when_reserving_more_stock_than_available(self):
        quantity = 7
        self.stock_repository.find_by_id.return_value = STOCK_VIDEO

        with self.assertRaises(InsufficientStockError):
            self.stock_management.reserve(
                product_id=PRODUCT_ID_VIDEO, quantity=quantity
            )
        self.stock_repository.save_stock.assert_not_called()

    def test_update_stock_levels_for_items_purchased(self):
        self.stock_repository.find_by_id.return_value = RESERVED_STOCK_VIDEO
        self.stock_management.update_stock(
            items=ShoppingBasketItems(items=[BASKET_ITEM_QUANTITY_FIVE])
        )
        self.stock_repository.save_stock.assert_has_calls([call(stock=SOLD_STOCK_VIDEO)])
        self.message_bus.handle.assert_called_once_with(
            event=StockIsLow(
                product_id=SOLD_STOCK_VIDEO.product_id,
                order_quantity=5
            )
        )

    def test_increase_stock_levels_for_product(self):
        self.stock_repository.find_by_id.return_value = SOLD_STOCK_VIDEO
        self.stock_management.increase_stock(
            product_id=PRODUCT_ID_VIDEO,
            quantity=5
        )
        self.stock_repository.save_stock.assert_called_once_with(stock=PURCHASED_STOCK_VIDEO)
