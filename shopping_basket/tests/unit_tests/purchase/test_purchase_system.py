from unittest import TestCase
from unittest.mock import MagicMock

from constants import PRODUCT_ID_BREAKING_BAD

from shopping_basket.core.messagebus import MessageBus
from shopping_basket.purchase.event import StockPurchased
from shopping_basket.purchase.purchase_system import PurchaseSystem


class PurchaseSystemShould(TestCase):
    def test_update_available_stock_quantity_for_given_product(self):
        message_bus = MagicMock(MessageBus)

        purchase_system = PurchaseSystem(message_bus=message_bus)
        purchase_system.order_more(actual_quantity=5, product_id=PRODUCT_ID_BREAKING_BAD)

        message_bus.handle.assert_called_with(
            event=StockPurchased(quantity_purchased=5, product_id=PRODUCT_ID_BREAKING_BAD)
        )
