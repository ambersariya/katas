from shopping_basket.core.event import EventHandler, Event
from shopping_basket.payment.event import PaymentCompleted
from shopping_basket.purchase.event import StockPurchased
from shopping_basket.stock.stock_management_service import StockManagementService


class StockUpdateHandler:
    def __init__(self, stock_management_service: StockManagementService):
        self.stock_management_service = stock_management_service

    def handle(self, event: PaymentCompleted) -> None:
        self.stock_management_service.update_stock(items=event.items)


class StockPurchasedHandler:
    def __init__(self, stock_management_service: StockManagementService):
        self.stock_management_service = stock_management_service

    def handle(self, event: StockPurchased) -> None:
        self.stock_management_service.increase_stock(
            product_id=event.product_id,
            quantity=event.quantity_purchased
        )
