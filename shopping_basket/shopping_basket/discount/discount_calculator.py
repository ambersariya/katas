from shopping_basket.basket.shopping_basket import ShoppingBasket


class DiscountCalculator:

    def apply_discount(self, basket: ShoppingBasket) -> ShoppingBasket:
        raise NotImplementedError()
