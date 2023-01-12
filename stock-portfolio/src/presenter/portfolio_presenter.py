from abc import abstractmethod
from typing import Protocol, Dict, List

from src.asset import Asset


class Presenter(Protocol):
    @abstractmethod
    def present(self, assets: List[Asset], prices: Dict[str, float]):
        pass
