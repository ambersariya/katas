from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class ShoppingBasketId:
    value: str
