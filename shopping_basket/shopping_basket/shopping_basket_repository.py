from typing import Protocol, Optional

from shopping_basket.shopping_basket import ShoppingBasket
from shopping_basket.user import UserId


class ShoppingBasketRepository(Protocol):
    def basket_for(self, user_id: UserId) -> Optional[ShoppingBasket]:
        pass
