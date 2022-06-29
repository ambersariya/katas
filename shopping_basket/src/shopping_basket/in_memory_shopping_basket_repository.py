from shopping_basket.src.shopping_basket.basketitem import BasketItem
from shopping_basket.src.shopping_basket.shopping_basket_repository import ShoppingBasketRepository


class InMemoryShoppingBasketRepository(ShoppingBasketRepository):
    def __init__(self):
        self.__items = []

    def add_item(self, item: BasketItem):
        self.__items.append(item)
