from unittest import mock
from unittest.mock import MagicMock

import shopping_basket
from shopping_basket.core.messagebus import handle
from constants import PRODUCT_ID_BREAKING_BAD
from shopping_basket.purchase.event import StockPurchased
from shopping_basket.purchase.purchase_system import PurchaseSystem


class TestPurchaseSystemShould:
    @mock.patch('shopping_basket.purchase.purchase_system.handle')
    def test_update_available_stock_quantity_for_given_product(self, event_handler):
        purchase_system = PurchaseSystem()
        purchase_system.order_more(actual_quantity=5, product_id=PRODUCT_ID_BREAKING_BAD)
        event_handler.assert_called_with(
            event=StockPurchased(quantity_purchased=5, product_id=PRODUCT_ID_BREAKING_BAD)
        )
