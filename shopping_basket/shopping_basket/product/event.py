from dataclasses import dataclass
from typing import List

from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.core.event import Event
from shopping_basket.product.product_id import ProductId


@dataclass(init=True, frozen=True)
class ProductLowOnStock(Event):
    product_id: ProductId
    quantity: int
