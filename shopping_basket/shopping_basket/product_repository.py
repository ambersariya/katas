from abc import abstractmethod
from typing import Protocol, Optional

from shopping_basket.product import ProductId, Product


class ProductRepository(Protocol):
    @abstractmethod
    def find_product_by_id(self, product_id: ProductId) -> Product:
        pass

    @abstractmethod
    def add_product(self, product: Product):
        pass


class InMemoryProductRepository(ProductRepository):
    _products: dict

    def __init__(self):
        self._products = {}

    def find_product_by_id(self, product_id: ProductId) -> Optional[Product]:
        if product_id in self._products:
            return self._products[product_id]

    def add_product(self, product: Product):
        self._products[product.id] = product
