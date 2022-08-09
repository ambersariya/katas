from abc import abstractmethod
from typing import Protocol

from shopping_basket.product import ProductId, Product


class ProductRepository(Protocol):
    @abstractmethod
    def find_product_by_id(self, product_id: ProductId) -> Product:
        pass
