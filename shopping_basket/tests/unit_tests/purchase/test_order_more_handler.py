from unittest import TestCase
from unittest.mock import MagicMock

from constants import PRODUCT_ID_BREAKING_BAD

from shopping_basket.purchase.handler import OrderMoreHandler
from shopping_basket.purchase.purchase_system import PurchaseSystem
from shopping_basket.stock.event import StockIsLow


class OrderMoreHandlerShould(TestCase):
    def test_handle_ordering_of_more_stock(self):
        purchase_system = MagicMock(PurchaseSystem)
        event = StockIsLow(product_id=PRODUCT_ID_BREAKING_BAD, order_quantity=5)
        handler = OrderMoreHandler(purchase_system=purchase_system)
        handler.handle(event=event)

        purchase_system.order_more.assert_called_once_with(
            product_id=PRODUCT_ID_BREAKING_BAD, actual_quantity=5
        )