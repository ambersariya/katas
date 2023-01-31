import dataclasses
from enum import Enum


class SortOrder(Enum):
    ASC = 'asc'
    DESC = 'desc'
    NATURAL = None


@dataclasses.dataclass(init=True, frozen=True)
class SortCriteria:
    field: str
    order: SortOrder = dataclasses.field(default=SortOrder.NATURAL)
