from unittest import TestCase
from unittest.mock import MagicMock

from constants import SHOPPING_BASKET
from shopping_basket.core.event import EventListener
from shopping_basket.payment.event import PaymentCompleted
from shopping_basket.stock.handler import StockUpdateListener
from shopping_basket.stock.stock_management_service import StockManagementService


class StockUpdateListenerShould(TestCase):
    def setUp(self) -> None:
        self.stock_management_service = MagicMock(StockManagementService)
        self.handler = StockUpdateListener(stock_management_service=self.stock_management_service)

    def test_update_stock_levels_for_purchased_items(self):
        event = PaymentCompleted(items=SHOPPING_BASKET.items)
        self.handler.handle(event=event)

        self.stock_management_service.update_stock.assert_called_once_with(
            items=SHOPPING_BASKET.items
        )
