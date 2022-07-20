from typing import Protocol

from shopping_basket.src.shopping_basket.basketitem import BasketItem
from shopping_basket.src.shopping_basket.user import UserID


class ShoppingBasketRepository(Protocol):
    def add_item(self, item: BasketItem):
        raise NotImplementedError()

    def basket_for(self, user_id: UserID):
        raise NotImplementedError()
