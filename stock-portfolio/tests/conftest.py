import pytest as pytest

from src.portfolio_tracker import PortfolioTracker
from src.presenter.cli_portfolio_presenter import CliPortfolioPresenter
from src.repository.in_memory_asset_repository import InMemoryAssetRepository
from src.repository.in_memory_stock_price_repository import InMemoryStockPriceRepository
from src.system_clock import SystemClock


@pytest.fixture
def system_clock():
    return SystemClock()


@pytest.fixture
def in_memory_asset_repository(system_clock):
    return InMemoryAssetRepository(system_clock)


@pytest.fixture
def in_memory_stock_price_repository():
    return InMemoryStockPriceRepository()


@pytest.fixture
def portfolio_presenter():
    return CliPortfolioPresenter()


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
