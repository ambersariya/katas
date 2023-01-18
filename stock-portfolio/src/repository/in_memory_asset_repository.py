from typing import List, Dict

from src.asset import Asset
from src.repository.asset_repository import AssetRepository
from src.system_clock import SystemClock
from src.value_objects import AssetOwner, AssetName


class InMemoryAssetRepository(AssetRepository):
    def __init__(self, system_clock: SystemClock) -> None:
        self.__current_time = system_clock
        self.__assets: Dict[AssetName, Asset] = {}

    def save_asset(self, asset: Asset) -> None:
        updated_asset = self.__update_asset_details(asset)
        self.__assets[asset.name] = updated_asset

    def fetch_assets(self) -> List[Asset]:
        return list(self.__assets.values())

    def fetch_asset_by_name(self, asset_name: AssetName) -> Asset:
        pass

    def __find_matching_asset(self, asset_name: AssetName):
        pass

    def __update_asset_details(self, asset: Asset) -> Asset:
        if asset.name in self.__assets:
            existing_asset = self.__assets[asset.name]
            existing_asset.last_operation = asset.last_operation
            asset = existing_asset
        return asset
