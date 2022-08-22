import uuid

from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.user import UserId


class ItemLogger:
    @staticmethod
    def log(user_id: UserId, item: ShoppingBasketItem) -> None:
        print(
            f"[{item.name}]: User[{user_id}], Product[{item.id}], Quantity[{item.quantity}]"
        )


class IdGenerator:
    @staticmethod
    def next() -> str:
        return str(uuid.uuid4())
