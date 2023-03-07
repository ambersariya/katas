from tests.constants import PRODUCT_ID_LORD_OF_THE_RINGS
from shopping_basket.purchase.event import StockPurchased
from shopping_basket.stock.handler import StockPurchasedHandler


class TestStockPurchaseHandlerShould:
    def test_handle_stock_purchase_event(self, mocked_stock_management_service):
        event = StockPurchased(quantity_purchased=5, product_id=PRODUCT_ID_LORD_OF_THE_RINGS)
        handler = StockPurchasedHandler(stock_management_service=mocked_stock_management_service)
        handler(event=event)

        mocked_stock_management_service.increase_stock.assert_called_once_with(
            product_id=PRODUCT_ID_LORD_OF_THE_RINGS, quantity=5
        )
