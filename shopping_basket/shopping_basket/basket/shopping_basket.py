from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.user import UserId


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

    def __str__(self):
        total = 0
        body = f"Creation date {self.created_at}\n"
        for item in self.items.items():
            body += f'{str(item)}\n'
            total += item.total()
        body += f"Total: £{'{:.2f}'.format(total)}"
        return body

