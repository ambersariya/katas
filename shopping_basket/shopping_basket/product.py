from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class ProductId:
    value: str


@dataclass(init=True, frozen=True)
class Product:
    id: ProductId
    name: str
    price: int
