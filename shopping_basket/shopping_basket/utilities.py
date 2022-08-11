from shopping_basket.shopping_basket import ShoppingBasketItem
from shopping_basket.user import UserId


class ItemLogger:
    @staticmethod
    def log(user_id: UserId, item: ShoppingBasketItem) -> None:
        print(f'[{item.name}]: User[{user_id}], Product[{item.id}], Quantity[{item.quantity}]')
