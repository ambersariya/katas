from unittest import TestCase
from unittest.mock import MagicMock

from constants import PRODUCT_ID_BOOK
from shopping_basket.purchase.event import StockPurchased
from shopping_basket.stock.handler import StockPurchasedHandler
from shopping_basket.stock.stock_management_service import StockManagementService


class StockPurchaseHandlerShould(TestCase):
    def test_handle_stock_purchase_event(self):
        event = StockPurchased(quantity_purchased=5, product_id=PRODUCT_ID_BOOK)
        stock_management_service = MagicMock(StockManagementService)
        handler = StockPurchasedHandler(stock_management_service=stock_management_service)
        handler.handle(event=event)

        stock_management_service.increase_stock.assert_called_once_with(
            product_id=PRODUCT_ID_BOOK,
            quantity=5
        )
