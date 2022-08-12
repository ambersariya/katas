from dataclasses import dataclass

from shopping_basket.errors import InsufficientStockError
from shopping_basket.product import ProductId


@dataclass(init=True, frozen=True)
class Stock:
    product_id: ProductId
    available: int
    reserved: int = 0

    def reserve(self, quantity: int) -> 'Stock':
        availability = self.available - quantity
        if availability < 0:
            raise InsufficientStockError()
        return Stock(product_id=self.product_id, available=self.available - quantity, reserved=quantity)
