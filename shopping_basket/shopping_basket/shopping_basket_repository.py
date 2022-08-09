from abc import abstractmethod
from typing import Protocol, Optional

from shopping_basket.shopping_basket import ShoppingBasket, ShoppingBasketItem
from shopping_basket.user import UserId


class ShoppingBasketRepository(Protocol):
    @abstractmethod
    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        pass

    @abstractmethod
    def get_or_create(self, user_id):
        pass

    @abstractmethod
    def add_item(self, item: ShoppingBasketItem):
        pass


class InMemoryShoppingBasketRepository(ShoppingBasketRepository):
    def get_or_create(self, user_id):
        raise NotImplementedError()

    _baskets: dict

    def __init__(self):
        self._baskets = {}

    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        if user_id in self._baskets:
            return self._baskets[user_id]

    def add_item(self, item: ShoppingBasketItem):
        raise NotImplementedError()
