from typing import List

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.discount.discount import Discount
from shopping_basket.discount.discount_strategy import DiscountStrategy
from shopping_basket.discount.discounted_shopping_basket import DiscountedShoppingBasket


class DiscountCalculator:
    def __init__(self, strategies: List[DiscountStrategy]):
        self.strategies = strategies

    def apply_discount(self, basket: ShoppingBasket) -> ShoppingBasket:
        applicable_discounts: List[Discount] = []
        for strategy in self.strategies:
            discount = strategy.apply(basket)
            if discount is not None:
                applicable_discounts.append(discount)
        if len(applicable_discounts) == 0:
            return basket
        return DiscountedShoppingBasket(
            user_id=basket.user_id,
            created_at=basket.created_at,
            items=basket.items,
            discount=max(applicable_discounts),
        )
