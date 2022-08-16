from typing import Dict, Optional

from shopping_basket.product.product import Product
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_repository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    _products: Dict[ProductId, Product]

    def __init__(self):
        self._products = {}

    def find_product_by_id(self, product_id: ProductId) -> Optional[Product]:
        if product_id in self._products:
            return self._products[product_id]

    def add_product(self, product: Product):
        self._products[product.id] = product
