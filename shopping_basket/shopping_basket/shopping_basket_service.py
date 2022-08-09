from shopping_basket.shopping_basket import ShoppingBasket
from shopping_basket.shopping_basket_repository import ShoppingBasketRepository


class ShoppingBasketService:

    def __init__(self, shopping_basket_repository: ShoppingBasketRepository):
        self._shopping_basket_repository = shopping_basket_repository

    def basket_for(self, user_id) -> ShoppingBasket:
        basket = self._shopping_basket_repository.basket_for(user_id)
        if basket is None:
            raise self.ShoppingBasketNotFoundError()
        return basket

    def add_item(self, user_id, product_id, quantity):
        raise NotImplementedError()

    class ShoppingBasketNotFoundError(Exception):
        pass
