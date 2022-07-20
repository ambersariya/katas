from shopping_basket.src.shopping_basket.basketitem import BasketItem
from shopping_basket.src.shopping_basket.shopping_basket import ShoppingBasket


class ShoppingBasketBuilder:
    def __init__(self):
        self._user_id = None
        self._created_at = None
        self._items = []

    def created_at(self, creation_date: str) -> 'ShoppingBasketBuilder':
        self._created_at = creation_date
        return self

    def with_item(self, item: BasketItem) -> 'ShoppingBasketBuilder':
        self._items.append(item)
        return self

    def for_user(self, user_id) -> 'ShoppingBasketBuilder':
        self._user_id = user_id
        return self

    def build(self) -> ShoppingBasket:
        basket = ShoppingBasket(self._user_id, self._created_at)
        for item in self._items:
            basket.add_item(item)

        return basket


def build_shopping_basket():
    return ShoppingBasketBuilder()
