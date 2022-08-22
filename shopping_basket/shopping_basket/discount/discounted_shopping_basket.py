from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.user import UserId
from shopping_basket.discount.discount import Discount


class DiscountedShoppingBasket(ShoppingBasket):

    def __init__(self, user_id: UserId, created_at: str, items: ShoppingBasketItems,
                 discount: Discount):
        super().__init__(user_id, created_at, items)
        self.discount = discount

    @classmethod
    def from_basket(cls, basket: ShoppingBasket, discount: Discount):
        return DiscountedShoppingBasket(user_id=basket.user_id,
                                        created_at=basket.created_at,
                                        items=basket.items,
                                        discount=discount)
