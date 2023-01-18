from dataclasses import dataclass, field
from datetime import datetime

from src.value_objects import AssetOwner, AssetName


@dataclass(init=True)
class Asset:
    name: AssetName
    number_of_shares: int
    first_operation: datetime = field(default=None)
    last_operation: datetime = field(default=None)
