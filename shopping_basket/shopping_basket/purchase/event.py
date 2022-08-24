from dataclasses import dataclass

from shopping_basket.core.event import Event
from shopping_basket.product.product_id import ProductId


@dataclass(init=True, frozen=True)
class StockPurchased(Event):
    product_id: ProductId
    quantity_purchased: int

    @staticmethod
    def name() -> str:
        return "StockPurchased"
