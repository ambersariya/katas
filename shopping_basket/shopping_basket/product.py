from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class ProductId:
    value: str

    def __str__(self):
        return self.value


@dataclass(init=True, frozen=True)
class Product:
    id: ProductId
    name: str
    price: int
