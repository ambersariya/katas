from abc import abstractmethod
from typing import Protocol, Optional

from shopping_basket.date_provider import DateProvider
from shopping_basket.shopping_basket import ShoppingBasket, ShoppingBasketItem
from shopping_basket.user import UserId


class ShoppingBasketRepository(Protocol):
    @abstractmethod
    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        pass

    @abstractmethod
    def add_item(self, item: ShoppingBasketItem, user_id: UserId):
        pass


class InMemoryShoppingBasketRepository(ShoppingBasketRepository):
    _baskets: dict

    def __init__(self, date_provider: DateProvider):
        self._date_provider = date_provider
        self._baskets = {}

    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        if self._basket_exists(user_id=user_id):
            return self._baskets[user_id]

    def add_item(self, item: ShoppingBasketItem, user_id: UserId):
        if not self._basket_exists(user_id=user_id):
            basket = ShoppingBasket(
                items=[item],
                user_id=user_id,
                created_at=self._date_provider.current_date())
            self._baskets[user_id] = basket

    def _basket_exists(self, user_id: UserId):
        return user_id in self._baskets
