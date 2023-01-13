from typing import List, Dict

from src.asset import Asset
from src.repository.asset_repository import AssetRepository


class InMemoryAssetRepository(AssetRepository):
    def __init__(self) -> None:
        self.__assets: Dict[str, List[Asset]] = {}

    def add_asset(self, asset: Asset) -> None:
        self.__assets[asset.owner] = [asset]

    def update_asset(self, asset: Asset) -> None:
        raise NotImplementedError()

    def fetch_assets(self, owner: str) -> List[Asset]:
        return self.__assets[owner]
