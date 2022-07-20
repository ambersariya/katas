from shopping_basket.src.shopping_basket.basketitem import BasketItem
from shopping_basket.src.shopping_basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.src.shopping_basket.user import UserID


class InMemoryShoppingBasketRepository(ShoppingBasketRepository):
    def __init__(self):
        self.__items = []

    def add_item(self, item: BasketItem):
        self.__items.append(item)

    def basket_for(self, user_id: UserID):
        return [item for item in self.__items if item.user_id == user_id]
