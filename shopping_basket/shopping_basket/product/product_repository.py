from abc import abstractmethod
from typing import Protocol, Optional

from shopping_basket.product.product import Product
from shopping_basket.product.product_id import ProductId


class ProductRepository(Protocol):
    @abstractmethod
    def find_product_by_id(self, product_id: ProductId) -> Optional[Product]:
        pass

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass


