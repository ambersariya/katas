from abc import ABC
from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class IntergalacticSymbol(ABC):
    name: str
    value: int
