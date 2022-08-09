from abc import abstractmethod
from typing import Protocol, Optional

from shopping_basket.shopping_basket import ShoppingBasket
from shopping_basket.user import UserId


class ShoppingBasketRepository(Protocol):
    @abstractmethod
    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        pass


class InMemoryShoppingBasketRepository(ShoppingBasketRepository):
    _baskets: dict

    def __init__(self):
        self._baskets = {}

    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        if user_id in self._baskets:
            return self._baskets[user_id]

    def add(self, basket: ShoppingBasket):
        self._baskets[basket.user_id] = basket
