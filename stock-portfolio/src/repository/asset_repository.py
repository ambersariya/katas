from abc import abstractmethod
from typing import Protocol, List

from src.asset import Asset
from src.value_objects import AssetName


class AssetRepository(Protocol):
    @abstractmethod
    def save_asset(self, asset: Asset) -> None:
        pass

    @abstractmethod
    def fetch_assets(self) -> List[Asset]:
        pass

    @abstractmethod
    def fetch_asset_by_name(self, asset_name: AssetName) -> Asset:
        pass


