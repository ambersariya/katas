import dataclasses
from abc import abstractmethod
from typing import Protocol


class CartPrinter(Protocol):
    @abstractmethod
    def print(self):
        pass


class APrinter(CartPrinter):
    def print(self):
        pass


@dataclasses.dataclass
class BasketItem:
    item_name: str
    price: float
    quantity: int


class ShoppingCart:
    def __init__(self, cart_printer: CartPrinter):
        self.__items = []
        self.cart_printer = cart_printer

    def add_item(self, product_name: str) -> None:
        raise NotImplementedError()

    def apply_discount(self, discount: float) -> None:
        raise NotImplementedError()

    def print_shopping_cart(self) -> None:
        raise NotImplementedError()
