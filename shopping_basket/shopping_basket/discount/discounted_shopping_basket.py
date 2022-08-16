from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.discount.discount import Discount


class DiscountedShoppingBasket:
    @classmethod
    def from_basket(cls, basket: ShoppingBasket, discount: Discount):
        pass
