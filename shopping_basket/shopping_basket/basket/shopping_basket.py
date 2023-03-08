from dataclasses import dataclass

from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from core.value_objects import UserId


@dataclass
class ShoppingBasket:
    user_id: UserId
    created_at: str
    items: ShoppingBasketItems

    def __init__(self, user_id: UserId, created_at: str, items: ShoppingBasketItems):
        self.items = items
        self.created_at = created_at
        self.user_id = user_id

    def add(self, item: ShoppingBasketItem) -> None:
        self.items.add(item=item)

    def total_amount(self) -> float:
        return self.items.total_amount()

    def __str__(self) -> str:
        body = f"Creation date {self.created_at}\n"
        for item in self.items.items():
            body += f"{str(item)}\n"
        body += f"Total: £{'{:.2f}'.format(self.items.total_amount())}"
        return body
