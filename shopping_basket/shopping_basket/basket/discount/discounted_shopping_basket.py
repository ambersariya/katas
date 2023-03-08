from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from core.value_objects import UserId
from shopping_basket.basket.discount.discount import Discount


class DiscountedShoppingBasket(ShoppingBasket):
    def __init__(
        self,
        user_id: UserId,
        created_at: str,
        items: ShoppingBasketItems,
        discount: Discount,
    ):
        super().__init__(user_id, created_at, items)
        self.discount = discount

    def __str__(self) -> str:
        total = self.items.total_amount() - self.discount.amount
        body = f"Creation date {self.created_at}\n"
        for item in self.items.items():
            body += f"{str(item)}\n"
        body += f"Discount applied: {'{:.0f}'.format(self.discount.percentage)}%\n"
        body += f"Total: £{'{:.2f}'.format(total)}"
        return body

    @classmethod
    def from_basket(cls, basket: ShoppingBasket, discount: Discount):
        return DiscountedShoppingBasket(
            user_id=basket.user_id,
            created_at=basket.created_at,
            items=basket.items,
            discount=discount,
        )
