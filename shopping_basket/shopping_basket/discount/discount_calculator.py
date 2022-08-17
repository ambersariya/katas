from typing import List

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.discount.discount_strategy import DiscountStrategy


class DiscountCalculator:

    def __init__(self, strategies: List[DiscountStrategy]):
        self.strategies = strategies

    def apply_discount(self, basket: ShoppingBasket) -> ShoppingBasket:
        return basket
