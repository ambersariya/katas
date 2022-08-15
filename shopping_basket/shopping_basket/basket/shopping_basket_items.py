from dataclasses import dataclass
from typing import List

from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem


@dataclass()
class ShoppingBasketItems:
    _items: List[ShoppingBasketItem]

    def __init__(self, items: List[ShoppingBasketItem]):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def add(self, item: ShoppingBasketItem):
        for index, existing_item in enumerate(self._items):
            if existing_item.id == item.id:
                updated_item = existing_item.update_quantity(item.quantity)
                self._items[index] = updated_item
                return
        self._items.append(item)

    def items(self):
        return self._items
