from shopping_basket.core.messagebus import MessageBus
from shopping_basket.product.product_id import ProductId
from shopping_basket.purchase.event import StockPurchased


class PurchaseSystem:
    def __init__(self, message_bus: MessageBus):
        self.message_bus = message_bus

    def order_more(self, product_id: ProductId, actual_quantity: int):
        self.message_bus.handle(
            event=StockPurchased(
                quantity_purchased=actual_quantity, product_id=product_id
            )
        )
