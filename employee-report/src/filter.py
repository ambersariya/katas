from dataclasses import dataclass
from enum import Enum
from typing import Any


class FilterOperation(Enum):
    GTE = 'gte'


@dataclass(init=True, frozen=True, eq=True)
class FilterCriteria:
    field: str
    operation: FilterOperation
    value: Any
