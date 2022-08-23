from dataclasses import dataclass

from shopping_basket.core.event import Event
from shopping_basket.product.product_id import ProductId


@dataclass(init=True, frozen=True)
class StockAvailabilityUpdated(Event):
    product_id: ProductId
    order_quantity: int
