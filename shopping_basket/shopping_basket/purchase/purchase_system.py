from shopping_basket.core.messagebus import handle
from shopping_basket.product.product_id import ProductId
from shopping_basket.purchase.event import StockPurchased


class PurchaseSystem:

    def order_more(self, product_id: ProductId, actual_quantity: int):
        handle(
            event=StockPurchased(quantity_purchased=actual_quantity, product_id=product_id)
        )
