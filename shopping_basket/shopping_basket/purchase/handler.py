from shopping_basket.purchase.purchase_system import PurchaseSystem
from shopping_basket.stock.event import StockIsLow


class OrderMoreHandler:
    def __init__(self, purchase_system: PurchaseSystem):
        self.purchase_system = purchase_system

    def handle(self, event: StockIsLow) -> None:
        self.purchase_system.order_more(
            product_id=event.product_id,
            actual_quantity=event.order_quantity
        )
