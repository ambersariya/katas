from unittest import mock

from constants import PRODUCT_ID_BREAKING_BAD
from shopping_basket.purchase.event import StockPurchased


class TestPurchaseSystemShould:
    @mock.patch("shopping_basket.purchase.purchase_system.handle")
    def test_update_available_stock_quantity_for_given_product(
        self, event_handler, purchase_system
    ):
        purchase_system.order_more(actual_quantity=5, product_id=PRODUCT_ID_BREAKING_BAD)

        event_handler.assert_called_with(
            event=StockPurchased(quantity_purchased=5, product_id=PRODUCT_ID_BREAKING_BAD)
        )
