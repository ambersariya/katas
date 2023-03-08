from dataclasses import dataclass
from typing import NewType

UserId = NewType('UserId', str)

@dataclass(init=True, frozen=True)
class User:
    id: UserId


