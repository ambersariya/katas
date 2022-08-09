from dataclasses import dataclass

from shopping_basket.user import UserId


@dataclass(init=True, frozen=True)
class ShoppingBasket:
    user_id: UserId
