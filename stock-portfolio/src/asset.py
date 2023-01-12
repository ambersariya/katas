from dataclasses import dataclass, field
from datetime import datetime


@dataclass(init=True, frozen=True)
class Asset:
    number_of_shares: int
    stock: str
    last_operation: datetime = field(default=None)
