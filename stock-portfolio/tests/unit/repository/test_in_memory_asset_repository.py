import datetime

from src.asset import Asset
from src.repository.in_memory_asset_repository import InMemoryAssetRepository
from src.value_objects import AssetOwner, AssetName

ASSET_OWNER = AssetOwner('alice')
ASSET_NAME_TSLA = AssetName('TSLA')
ASSET_NAME_MSFT = AssetName('MSFT')
ASSET_TSLA = Asset(
    owner=ASSET_OWNER,
    last_operation=datetime.datetime.strptime('01/01/2000', '%d/%m/%Y'),
    name=ASSET_NAME_TSLA,
    number_of_shares=100
)
ASSET_MSFT = Asset(
    owner=ASSET_OWNER,
    last_operation=datetime.datetime.strptime('01/01/2019', '%d/%m/%Y'),
    name=ASSET_NAME_MSFT,
    number_of_shares=50
)

EXPECTED_INCREASED_QUANTITY_ASSET = Asset(
    owner=ASSET_OWNER,
    last_operation=datetime.datetime.strptime('01/01/2020', '%d/%m/%Y'),
    name=ASSET_NAME_TSLA,
    number_of_shares=200
)


def test_should_fetch_asset(in_memory_asset_repository: InMemoryAssetRepository):
    in_memory_asset_repository.add_asset(ASSET_TSLA)
    fetched_assets = in_memory_asset_repository.fetch_assets(owner=ASSET_OWNER)

    assert [ASSET_TSLA] == fetched_assets


def test_should_fetch_multiple_assets(in_memory_asset_repository: InMemoryAssetRepository):
    in_memory_asset_repository.add_asset(ASSET_TSLA)
    in_memory_asset_repository.add_asset(ASSET_MSFT)
    fetched_assets = in_memory_asset_repository.fetch_assets(owner=ASSET_OWNER)

    assert fetched_assets == [ASSET_TSLA, ASSET_MSFT]


def test_should_increase_asset_quantity_if_the_asset_exists(in_memory_asset_repository):
    in_memory_asset_repository.add_asset(ASSET_TSLA)
    in_memory_asset_repository.add_asset(ASSET_TSLA)
    fetched_assets = in_memory_asset_repository.fetch_assets(owner=ASSET_OWNER)

    assert fetched_assets == [EXPECTED_INCREASED_QUANTITY_ASSET]
