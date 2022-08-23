from unittest import TestCase
from unittest.mock import MagicMock

from constants import PRODUCT_ID_VIDEO
from shopping_basket.core.event import EventListener
from shopping_basket.purchase.handler import OrderMoreHandler
from shopping_basket.purchase.purchase_system import PurchaseSystem
from shopping_basket.stock.event import StockIsLow


class OrderMoreHandlerShould(TestCase):
    def test_handle_ordering_of_more_stock(self):
        purchase_system = MagicMock(PurchaseSystem)
        event = StockIsLow(product_id=PRODUCT_ID_VIDEO, order_quantity=5)
        handler = OrderMoreHandler(purchase_system=purchase_system)
        handler.handle(event=event)

        purchase_system.order_more.assert_called_once_with(
            product_id=PRODUCT_ID_VIDEO,
            actual_quantity=5
        )
