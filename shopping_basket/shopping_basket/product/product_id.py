from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class ProductId:
    value: str

    def __str__(self) -> str:
        return self.value
