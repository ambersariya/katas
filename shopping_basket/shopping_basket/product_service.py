from typing import Optional

from shopping_basket.product import Product, ProductId
from shopping_basket.product_repository import ProductRepository


class ProductService:

    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def find_product_by_id(self, product_id: ProductId) -> Optional[Product]:
        product = self._product_repository.find_product_by_id(product_id)
        if not product:
            raise self.ProductNotFoundError()
        return product

    class ProductNotFoundError(Exception):
        pass
