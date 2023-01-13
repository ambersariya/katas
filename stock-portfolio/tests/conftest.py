import pytest as pytest

from src.portfolio_tracker import PortfolioTracker
from src.repository.in_memory_asset_repository import InMemoryAssetRepository
from src.repository.in_memory_stock_price_repository import InMemoryStockPriceRepository


@pytest.fixture
def in_memory_asset_repository():
    return InMemoryAssetRepository()


@pytest.fixture
def in_memory_stock_price_repository():
    return InMemoryStockPriceRepository()


@pytest.fixture
def portfolio_presenter():
    raise NotImplementedError()


@pytest.fixture
def portfolio_tracker(
    in_memory_asset_repository,
    in_memory_stock_price_repository,
    portfolio_presenter
):
    return PortfolioTracker(
        in_memory_asset_repository,
        in_memory_stock_price_repository,
        portfolio_presenter
    )
