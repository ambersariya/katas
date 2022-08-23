from dataclasses import dataclass

from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.core.event import Event


@dataclass(init=True, frozen=True)
class PaymentCompleted(Event):
    items: ShoppingBasketItems

    @staticmethod
    def name() -> str:
        return 'PaymentCompleted'
