from dataclasses import dataclass

from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_id import ProductId


@dataclass(init=True, frozen=True)
class Product:
    id: ProductId
    name: str
    price: int
    category: ProductCategory
