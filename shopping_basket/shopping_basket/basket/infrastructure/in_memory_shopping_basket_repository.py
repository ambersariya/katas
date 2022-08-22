from typing import Dict, Optional

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.basket.user import UserId
from shopping_basket.core.date_provider import DateProvider


class InMemoryShoppingBasketRepository(ShoppingBasketRepository):
    _baskets: Dict[UserId, ShoppingBasket]

    def __init__(self, date_provider: DateProvider):
        self._date_provider = date_provider
        self._baskets = {}

    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        if self._basket_exists(user_id=user_id):
            return self._baskets[user_id]
        return None

    def add_item(self, item: ShoppingBasketItem, user_id: UserId) -> None:
        if not self._basket_exists(user_id=user_id):
            basket = ShoppingBasket(
                user_id=user_id,
                created_at=self._date_provider.current_date(),
                items=ShoppingBasketItems(items=[item]),
            )
            self._baskets[user_id] = basket
            return
        basket = self.basket_for(user_id)  # type: ignore
        basket.add(item)

    def _basket_exists(self, user_id: UserId) -> bool:
        return user_id in self._baskets
