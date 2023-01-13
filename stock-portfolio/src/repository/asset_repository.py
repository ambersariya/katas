from abc import abstractmethod
from typing import Protocol, List

from src.asset import Asset


class AssetRepository(Protocol):
    @abstractmethod
    def add_asset(self, asset: Asset):
        pass

    @abstractmethod
    def update_asset(self, asset: Asset):
        pass

    @abstractmethod
    def fetch_assets(self, owner: str) -> List[Asset]:
        pass
