from dataclasses import dataclass

from shopping_basket.product.product_id import ProductId
from shopping_basket.stock.stock_error import InsufficientStockError


@dataclass(init=True, frozen=True)
class Stock:
    product_id: ProductId
    available: int
    min_available: int
    reserved: int = 0

    def reserve(self, quantity: int) -> "Stock":
        availability = self.available - quantity
        if availability < 0:
            raise InsufficientStockError()
        return Stock(
            product_id=self.product_id,
            available=self.available - quantity,
            min_available=self.min_available,
            reserved=quantity,
        )

    def reduce_reserved(self, quantity: int) -> "Stock":
        return Stock(
            product_id=self.product_id,
            available=self.available,
            min_available=self.min_available,
            reserved=self.reserved - quantity,
        )

    def order_quantity(self) -> int:
        return self.min_available - self.total_stock()

    def total_stock(self) -> int:
        return self.available + self.reserved

    def is_enough_available(self) -> bool:
        return self.total_stock() >= self.min_available
