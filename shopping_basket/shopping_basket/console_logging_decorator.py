from shopping_basket.product import ProductId
from shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.user import UserId


class ConsoleLoggingDecorator:
    def __init__(self, shopping_basket_service: ShoppingBasketService):
        self.shopping_basket_service = shopping_basket_service

    def add_item(self, user_id: UserId, product_id: ProductId, quantity: int):
        try:
            self.shopping_basket_service.add_item(
                user_id=user_id, product_id=product_id, quantity=quantity)
            _message = f'[ITEM ADDED TO SHOPPING CART]: User[{user_id}], ' \
                       f'Product[{product_id}], Quantity[{quantity}]'
            print(_message)
        except:
            pass
