import datetime

from src.asset import Asset
from src.value_objects import AssetOwner, AssetName
from src.repository.in_memory_asset_repository import InMemoryAssetRepository

ASSET_OWNER = AssetOwner('alice')
ASSET_NAME = AssetName('TSLA')
ASSET_TSLA = Asset(
    owner=ASSET_OWNER,
    last_operation=datetime.datetime.strptime('01/01/2000', '%d/%m/%Y'),
    name=ASSET_NAME,
    number_of_shares=100
)


def test_should_fetch_asset(in_memory_asset_repository: InMemoryAssetRepository):
    in_memory_asset_repository.add_asset(ASSET_TSLA)
    fetched_assets = in_memory_asset_repository.fetch_assets(owner=ASSET_OWNER)

    assert [ASSET_TSLA] == fetched_assets
