from typing import Dict, Optional

from basket.shopping_basket_item_logger import ItemLogger
from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.core.value_objects import UserId
from shopping_basket.core.date_provider import DateProvider


class InMemoryShoppingBasketRepository(ShoppingBasketRepository):
    __baskets: Dict[UserId, ShoppingBasket]

    def __init__(self, date_provider: DateProvider, item_logger: ItemLogger):
        self.__item_logger = item_logger
        self.__date_provider = date_provider
        self.__baskets = {}

    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        if self.__basket_exists(user_id=user_id):
            return self.__baskets[user_id]
        return None

    def add_item(self, item: ShoppingBasketItem, user_id: UserId) -> None:
        if not self.__basket_exists(user_id=user_id):
            basket = ShoppingBasket(
                user_id=user_id,
                created_at=self.__date_provider.current_date(),
                items=ShoppingBasketItems(items=[item]),
            )
            self.__baskets[user_id] = basket
            return
        basket = self.basket_for(user_id)  # type: ignore
        basket.add(item)
        self.__item_logger.log(user_id=user_id, item=item)

    def __basket_exists(self, user_id: UserId) -> bool:
        return user_id in self.__baskets
