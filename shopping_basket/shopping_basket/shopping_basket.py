from dataclasses import dataclass
from typing import List

from shopping_basket.product import Product
from shopping_basket.user import UserId


@dataclass(init=True, frozen=True, repr=True)
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

    def total(self):
        return self.price * self.quantity

    def __str__(self):
        price = "{:.2f}".format(self.price)
        total = "{:.2f}".format(self.total())
        return f"{self.quantity} x {self.name} // {self.quantity} x {price} = £{total}"

    def update_quantity(self, quantity: int) -> 'ShoppingBasketItem':
        return ShoppingBasketItem(
            id=self.id,
            price=self.price,
            name=self.name,
            quantity=quantity + self.quantity
        )


@dataclass()
class ShoppingBasketItems:
    _items: List[ShoppingBasketItem]

    def __init__(self, items: List[ShoppingBasketItem]):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index: int):
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

