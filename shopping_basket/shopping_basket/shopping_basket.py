from dataclasses import dataclass
from typing import List, Any

from shopping_basket.product import Product
from shopping_basket.user import UserId


@dataclass(init=True, frozen=True)
class ShoppingBasketItem:
    id: str
    name: str
    price: int
    quantity: int

    @staticmethod
    def for_product(product: Product, quantity: int):
        return ShoppingBasketItem(
            id=str(product.id),
            name=product.name,
            price=product.price,
            quantity=quantity
        )


@dataclass()
class ShoppingBasketItems:
    _items: List[ShoppingBasketItem]

    def __init__(self, items: List[ShoppingBasketItem]):
        self._items = items

    def __len__(self):
        return len(self._items)

    def add(self, item: ShoppingBasketItem):
        self._items.append(item)


@dataclass()
class ShoppingBasket:
    user_id: UserId
    created_at: str
    items: ShoppingBasketItems

    def __init__(self, user_id: UserId, created_at: str, items: ShoppingBasketItems):
        self.items = items
        self.created_at = created_at
        self.user_id = user_id

    def add(self, item: ShoppingBasketItem):
        self.items.add(item=item)
