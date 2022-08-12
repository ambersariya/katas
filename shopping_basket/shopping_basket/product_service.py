from typing import Optional

from shopping_basket.errors import ProductNotFoundError
from shopping_basket.product import Product, ProductId
from shopping_basket.product_repository import ProductRepository
from shopping_basket.stock.stock_management_service import StockManagementService


class ProductService:

    def __init__(self, product_repository: ProductRepository, stock_management_service: StockManagementService):
        self._stock_management_service = stock_management_service
        self._product_repository = product_repository

    def find_and_reserve(self, product_id: ProductId, quantity: int) -> Optional[Product]:
        product = self._product_repository.find_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError()
        self._stock_management_service.reserve(product_id=product_id, quantity=quantity)
        return product

    def add_product(self, product, stock):
        self._product_repository.add_product(product=product)
        self._stock_management_service.save_stock(stock=stock)
