from tests.constants import SHOPPING_BASKET_WITH_ONE_ITEM, ORDER_ID, PAYMENT_REFERENCE
from shopping_basket.payment.event import OrderConfirmed
from shopping_basket.stock.handler import StockUpdateHandler


class TestPaymentCompletedHandlerShould:
    def test_update_stock_levels_for_purchased_items(self, mocked_stock_management_service):
        handler = StockUpdateHandler(stock_management_service=mocked_stock_management_service)
        event = OrderConfirmed(
            shopping_basket=SHOPPING_BASKET_WITH_ONE_ITEM,
            order_id=ORDER_ID,
            payment_reference=PAYMENT_REFERENCE,
        )

        handler(event=event)

        mocked_stock_management_service.update_stock.assert_called_once_with(
            items=SHOPPING_BASKET_WITH_ONE_ITEM.items
        )
