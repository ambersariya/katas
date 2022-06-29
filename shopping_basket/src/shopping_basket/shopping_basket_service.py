from shopping_basket.src.shopping_basket.basketitem import BasketItem
from shopping_basket.src.shopping_basket.product import ProductID
from shopping_basket.src.shopping_basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.src.shopping_basket.user import UserID


class ShoppingBasketService:
    def __init__(self, shopping_basket_repository: ShoppingBasketRepository):
        self.shopping_basket_repository = shopping_basket_repository

    def add_item(self, user_id: UserID, product_id: ProductID, quantity: int) -> None:
        item = BasketItem(user_id=user_id, product_id=product_id, quantity=quantity)
        self.shopping_basket_repository.add_item(item)

    def basket_for(self, user_id: UserID):
        raise NotImplementedError()
