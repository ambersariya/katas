from tests.constants import (
    DISCOUNTABLE_SHOPPING_BASKET_WITH_ONE_ITEM,
    DISCOUNTED_SHOPPING_BASKET,
    SHOPPING_BASKET_WITH_ONE_ITEM,
)


class TestDiscountCalculatorShould:
    def test_return_shopping_basket_when_no_discount_is_applicable(
        self, discount_calculator_with_strategies
    ) -> None:
        non_discounted_basket = discount_calculator_with_strategies.apply_discount(
            SHOPPING_BASKET_WITH_ONE_ITEM
        )

        assert SHOPPING_BASKET_WITH_ONE_ITEM == non_discounted_basket

    def test_return_discounted_shopping_basket_with_ten_percent_discount_when_it_contains_at_least_three_books(
        self, discount_calculator_with_strategies
    ) -> None:
        discounted_basket = discount_calculator_with_strategies.apply_discount(
            DISCOUNTABLE_SHOPPING_BASKET_WITH_ONE_ITEM
        )

        assert DISCOUNTED_SHOPPING_BASKET == discounted_basket
