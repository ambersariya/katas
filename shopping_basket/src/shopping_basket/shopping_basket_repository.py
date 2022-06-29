from typing import Protocol

from shopping_basket.src.shopping_basket.basketitem import BasketItem


class ShoppingBasketRepository(Protocol):
    def add_item(self, item: BasketItem):
        raise NotImplementedError()
