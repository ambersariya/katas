from shopping_basket.core.event import EventListener, Event
from shopping_basket.payment.event import PaymentCompleted
from shopping_basket.stock.stock_management_service import StockManagementService


class StockUpdateListener:
    def __init__(self, stock_management_service: StockManagementService):
        self.stock_management_service = stock_management_service

    def handle(self, event: PaymentCompleted) -> None:
        self.stock_management_service.update_stock(items=event.items)
