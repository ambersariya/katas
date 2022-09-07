from constants import PRODUCT_ID_BREAKING_BAD
from shopping_basket.purchase.handler import OrderMoreHandler
from shopping_basket.stock.event import StockIsLow


class TestOrderMoreHandlerShould:
    def test_handle_ordering_of_more_stock(self, mocked_purchase_system):
        event = StockIsLow(product_id=PRODUCT_ID_BREAKING_BAD, order_quantity=5)
        handle = OrderMoreHandler(purchase_system=mocked_purchase_system)
        handle(event=event)

        mocked_purchase_system.order_more.assert_called_once_with(
            product_id=PRODUCT_ID_BREAKING_BAD, actual_quantity=5
        )
