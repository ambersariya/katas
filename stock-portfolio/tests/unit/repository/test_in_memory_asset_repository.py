import datetime
from unittest.mock import patch

from src.asset import Asset
from src.repository.in_memory_asset_repository import InMemoryAssetRepository
from src.value_objects import AssetOwner, AssetName

ASSET_OWNER = AssetOwner('alice')
ASSET_NAME_TSLA = AssetName('TSLA')
ASSET_NAME_MSFT = AssetName('MSFT')
ASSET_TSLA = Asset(
    last_operation=datetime.datetime.strptime('01/01/2000', '%d/%m/%Y'),
    name=ASSET_NAME_TSLA,
    number_of_shares=100
)
ASSET_SELL_TSLA = Asset(
    last_operation=datetime.datetime.strptime('01/02/2000', '%d/%m/%Y'),
    name=ASSET_NAME_TSLA,
    number_of_shares=-10
)
ASSET_MSFT = Asset(
    last_operation=datetime.datetime.strptime('01/01/2019', '%d/%m/%Y'),
    name=ASSET_NAME_MSFT,
    number_of_shares=50
)

EXPECTED_INCREASED_QUANTITY_ASSET = Asset(
    last_operation=datetime.datetime.strptime('01/01/2020', '%d/%m/%Y'),
    name=ASSET_NAME_TSLA,
    number_of_shares=100
)


def test_should_fetch_singular_asset(in_memory_asset_repository: InMemoryAssetRepository):
    in_memory_asset_repository.save_asset(ASSET_TSLA)
    fetched_assets = in_memory_asset_repository.fetch_assets()

    assert [ASSET_TSLA] == fetched_assets


def test_should_fetch_multiple_assets(in_memory_asset_repository: InMemoryAssetRepository):
    in_memory_asset_repository.save_asset(ASSET_TSLA)
    in_memory_asset_repository.save_asset(ASSET_MSFT)
    fetched_assets = in_memory_asset_repository.fetch_assets()

    assert fetched_assets == [ASSET_TSLA, ASSET_MSFT]


def test_should_increase_asset_quantity_when_the_asset_exists(in_memory_asset_repository,
                                                              mock_system_clock):
    mock_system_clock.return_value = datetime.datetime.strptime('01/01/2020', '%d/%m/%Y')
    in_memory_asset_repository.save_asset(ASSET_TSLA)
    fetched_assets = in_memory_asset_repository.fetch_assets()
    assert fetched_assets == [EXPECTED_INCREASED_QUANTITY_ASSET]


def test_should_decrease_asset_quantity_when_the_asset_is_sold(in_memory_asset_repository,
                                                               mock_system_clock):
    # mock_system_clock.return_value = datetime.datetime.strptime('01/02/2020', '%d/%m/%Y')
    # in_memory_asset_repository.update_asset()
    pass

def test_should_remove_asset_when_all_the_shares_are_sold(in_memory_asset_repository,
                                                          mock_system_clock):
    pass


def test_should_ensure_one_cannot_sell_more_shares_than_owned(in_memory_asset_repository,
                                                              mock_system_clock):
    pass
