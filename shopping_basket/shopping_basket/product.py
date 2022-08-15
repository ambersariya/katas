from dataclasses import dataclass

from shopping_basket.product_category import ProductCategory


@dataclass(init=True, frozen=True)
class ProductId:
    value: str

    def __str__(self):
        return self.value


@dataclass(init=True, frozen=True)
class Product:
    id: ProductId
    name: str
    price: int
    category: ProductCategory
