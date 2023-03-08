from abc import abstractmethod
from typing import Optional, Protocol

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from core.value_objects import UserId


class ShoppingBasketRepository(Protocol):
    @abstractmethod
    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        pass

    @abstractmethod
    def add_item(self, item: ShoppingBasketItem, user_id: UserId) -> None:
        pass
