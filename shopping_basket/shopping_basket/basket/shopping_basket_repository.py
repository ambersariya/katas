from abc import abstractmethod
from typing import Protocol, Optional

from shopping_basket.basket.shopping_basket import (
    ShoppingBasket,
)
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.user import UserId


class ShoppingBasketRepository(Protocol):
    @abstractmethod
    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        pass

    @abstractmethod
    def add_item(self, item: ShoppingBasketItem, user_id: UserId):
        pass


