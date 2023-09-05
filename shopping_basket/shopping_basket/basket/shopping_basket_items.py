from dataclasses import dataclass
from typing import List

from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem


@dataclass()
class ShoppingBasketItems:
    _items: List[ShoppingBasketItem]

    def __init__(self, items: List[ShoppingBasketItem]) -> None:
        self._items = items

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> "ShoppingBasketItem":
        return self._items[index]

    def add(self, item: ShoppingBasketItem) -> None:
        for index, existing_item in enumerate(self._items):
            if existing_item.id == item.id:
                updated_item = existing_item.update_quantity(item.quantity)
                self._items[index] = updated_item
                return
        self._items.append(item)

    def items(self) -> List[ShoppingBasketItem]:
        return self._items

    def total_amount(self) -> float:
        total = 0
        for item in self._items:
            total += item.total()
        return total
