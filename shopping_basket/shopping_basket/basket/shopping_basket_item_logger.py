from basket.shopping_basket_item import ShoppingBasketItem
from core.value_objects import UserId


class ItemLogger:
    @staticmethod
    def log(user_id: UserId, item: ShoppingBasketItem) -> None:
        print(f"[{item.name}]: User[{user_id}], Product[{item.id}], Quantity[{item.quantity}]")
