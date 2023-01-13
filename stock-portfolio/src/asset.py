from dataclasses import dataclass, field
from datetime import datetime

from src.value_objects import AssetOwner, AssetName


@dataclass(init=True, frozen=True)
class Asset:
    owner: AssetOwner
    name: AssetName
    number_of_shares: int
    last_operation: datetime = field(default=None)
