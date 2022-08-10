from shopping_basket.product import ProductId
from shopping_basket.product_repository import ProductRepository
from shopping_basket.shopping_basket import ShoppingBasket, ShoppingBasketItem
from shopping_basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.user import UserId


class ShoppingBasketService:
    def __init__(self, shopping_basket_repository: ShoppingBasketRepository, product_repository: ProductRepository):
        self.product_repository = product_repository
        self._shopping_basket_repository = shopping_basket_repository

    def basket_for(self, user_id: UserId) -> ShoppingBasket:
        basket = self._shopping_basket_repository.basket_for(user_id)
        if basket is None:
            raise self.ShoppingBasketNotFoundError()
        return basket

    def add_item(self, user_id: UserId, product_id: ProductId, quantity: int):
        product = self.product_repository.find_product_by_id(product_id=ProductId(product_id))
        self._shopping_basket_repository.add_item(ShoppingBasketItem.for_product(product, quantity=quantity))

    class ShoppingBasketNotFoundError(Exception):
        pass
