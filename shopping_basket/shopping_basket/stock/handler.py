from shopping_basket.payment.event import OrderConfirmed
from shopping_basket.purchase.event import StockPurchased
from shopping_basket.stock.stock_management_service import StockManagementService


class StockUpdateHandler:
    def __init__(self, stock_management_service: StockManagementService):
        self.stock_management_service = stock_management_service

    def __call__(self, event: OrderConfirmed) -> None:
        self.stock_management_service.update_stock(items=event.shopping_basket.items)


class StockPurchasedHandler:
    def __init__(self, stock_management_service: StockManagementService):
        self.stock_management_service = stock_management_service

    def __call__(self, event: StockPurchased) -> None:
        self.stock_management_service.increase_stock(
            product_id=event.product_id, quantity=event.quantity_purchased
        )
