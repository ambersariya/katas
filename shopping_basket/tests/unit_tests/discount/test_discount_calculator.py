from unittest import TestCase

from constants import (
    SHOPPING_BASKET,
    DISCOUNTABLE_SHOPPING_BASKET,
    DISCOUNTED_SHOPPING_BASKET,
    CATEGORIES,
    STRATEGIES,
)
from shopping_basket.discount.discount_calculator import DiscountCalculator


class DiscountCalculatorShould(TestCase):
    def setUp(self) -> None:
        self.discount_calculator = DiscountCalculator(STRATEGIES)

    def test_return_shopping_basket_when_no_discount_is_applicable(self) -> None:
        non_discounted_basket = self.discount_calculator.apply_discount(SHOPPING_BASKET)
        self.assertEqual(SHOPPING_BASKET, non_discounted_basket)

    def test_return_discounted_shopping_basket_with_ten_percent_discount_when_it_contains_at_least_three_books(
        self,
    ) -> None:
        discounted_basket = self.discount_calculator.apply_discount(
            DISCOUNTABLE_SHOPPING_BASKET
        )

        self.assertEqual(DISCOUNTED_SHOPPING_BASKET, discounted_basket)

    def tearDown(self) -> None:
        self.discount_calculator = None
