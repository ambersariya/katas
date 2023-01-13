from dataclasses import dataclass, field
from datetime import datetime
from typing import NewType

AssetOwner = NewType('AssetOwner', str)
AssetName = NewType('AssetName', str)


@dataclass(init=True, frozen=True)
class Asset:
    owner: AssetOwner
    name: AssetName
    number_of_shares: int
    last_operation: datetime = field(default=None)
