import uuid
from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class OrderId:
    value: str

    @classmethod
    def next(cls) -> "OrderId":
        return OrderId(str(uuid.uuid4()))
