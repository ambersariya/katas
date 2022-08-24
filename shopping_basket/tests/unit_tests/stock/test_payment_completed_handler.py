from unittest import TestCase
from unittest.mock import MagicMock

from constants import SHOPPING_BASKET_WITH_ONE_ITEM, ORDER_ID, PAYMENT_REFERENCE

from shopping_basket.payment.event import OrderConfirmed
from shopping_basket.stock.handler import StockUpdateHandler
from shopping_basket.stock.stock_management_service import StockManagementService


class PaymentCompletedHandlerShould(TestCase):
    def setUp(self) -> None:
        self.stock_management_service = MagicMock(StockManagementService)
        self.handler = StockUpdateHandler(stock_management_service=self.stock_management_service)

    def test_update_stock_levels_for_purchased_items(self):
        event = OrderConfirmed(shopping_basket=SHOPPING_BASKET_WITH_ONE_ITEM, order_id=ORDER_ID,
                               payment_reference=PAYMENT_REFERENCE)
        self.handler.handle(event=event)

        self.stock_management_service.update_stock.assert_called_once_with(
            items=SHOPPING_BASKET_WITH_ONE_ITEM.items
        )
