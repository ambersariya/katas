import dataclasses


@dataclasses.dataclass(frozen=True)
class ProductID:
    id: str
