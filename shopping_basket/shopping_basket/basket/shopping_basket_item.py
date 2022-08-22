from dataclasses import dataclass

from shopping_basket.product.product import Product
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_id import ProductId


@dataclass(init=True, frozen=True, repr=True)
class ShoppingBasketItem:
    id: ProductId
    name: str
    price: int
    quantity: int
    category: ProductCategory

    @staticmethod
    def for_product(product: Product, quantity: int) -> "ShoppingBasketItem":
        return ShoppingBasketItem(
            id=product.id,
            name=product.name,
            price=product.price,
            quantity=quantity,
            category=product.category,
        )

    def total(self) -> int:
        return self.price * self.quantity

    def __str__(self) -> str:
        price = "{:.2f}".format(self.price)
        total = "{:.2f}".format(self.total())
        return f"{self.quantity} x {self.name} // {self.category} // {self.quantity} x {price} = £{total}"

    def update_quantity(self, quantity) -> "ShoppingBasketItem":  # type: ignore
        return ShoppingBasketItem(
            id=self.id,
            price=self.price,
            name=self.name,
            quantity=quantity + self.quantity,
            category=self.category,
        )
