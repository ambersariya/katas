from typing import List, Dict

from src.asset import Asset
from src.repository.asset_repository import AssetRepository
from src.value_objects import AssetOwner, AssetName


class InMemoryAssetRepository(AssetRepository):
    def __init__(self) -> None:
        self.__assets: Dict[AssetOwner, Dict[AssetName, Asset]] = {}

    def add_asset(self, asset: Asset) -> None:
        if asset.owner not in self.__assets:
            self.__assets[asset.owner] = []
        return self.update_asset(asset=asset)

        # assets = self.__assets[asset.owner]  # [asset1, asset2]
        # for existing_asset in assets:
        #     if asset.name == existing_asset.name:
        #         self.update_asset(asset=asset)
        #         return

        self.__assets[asset.owner] = assets

    def update_asset(self, asset: Asset) -> None:
        assets = self.__assets[asset.owner]  # [asset1, asset2]
        for existing_asset in assets:
            if asset.name == existing_asset.name:
                existing_asset.number_of_shares += asset.number_of_shares
                existing_asset.last_operation = asset.last_operation

    def fetch_assets(self, owner: str) -> List[Asset]:
        return self.__assets[AssetOwner(owner)]

    def __find_matching_asset(self, asset_name: AssetName):
        pass
