import dataclasses
from abc import abstractmethod
from typing import Protocol


@dataclasses.dataclass
class Product:
    name: str
    cost: float
    revenue_pct: float
    price_per_unit: float
    tax_pct: float
    final_price: float


class CartItems:
    pass


@dataclasses.dataclass
class ShoppingCartItem:
    item_name: str
    price: float
    quantity: int


class ShoppingCartList:
    def __init__(self, items: list[ShoppingCartItem]):
        self.__items = items

    def add_product(self, product):
        raise NotImplementedError()


class ShoppingCartRepository(Protocol):
    @abstractmethod
    def save_items(self, items: ShoppingCartList):
        pass

    @abstractmethod
    def get_cart_items(self) -> ShoppingCartList:
        pass


class ProductRepository(Protocol):
    @abstractmethod
    def find_product_by_name(self, name):
        pass


class ShoppingCart:
    def __init__(self, shopping_cart_repository: ShoppingCartRepository, product_repository: ProductRepository):
        self.__product_repository = product_repository
        self.__shopping_cart_repository = shopping_cart_repository
        self.__items = []

    def add_item(self, product_name: str) -> None:
        product = self.__product_repository.find_product_by_name(name=product_name)
        items = self.__shopping_cart_repository.get_cart_items()
        items.add_product(product)
        self.__shopping_cart_repository.save_items(items=items)

    def apply_discount(self, discount: float) -> None:
        raise NotImplementedError()

    def print_shopping_cart(self) -> ShoppingCartList:
        raise NotImplementedError()
