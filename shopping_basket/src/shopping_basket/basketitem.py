import dataclasses

from shopping_basket.src.shopping_basket.product import ProductID
from shopping_basket.src.shopping_basket.user import UserID


@dataclasses.dataclass(frozen=True)
class BasketItem:
    user_id: UserID
    product_id: ProductID
    quantity: int
