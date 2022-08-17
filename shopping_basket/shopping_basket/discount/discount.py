from dataclasses import dataclass
from typing import Protocol

from shopping_basket.basket.shopping_basket import ShoppingBasket


@dataclass
class Discount(Protocol):
    pass


class ThreeBooksDiscount(Discount):
    _percentage: float = 10.00

    def calculate(self, basket: ShoppingBasket) -> float:
        return self.basket.total_amount() * (self._percentage / 100)


class MultiCategoryDiscount:
    pass
