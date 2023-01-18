import pytest as pytest

from src.portfolio_tracker import PortfolioTracker
from src.presenter.portfolio_presenter import PortfolioPresenter
from src.repository.asset_repository import AssetRepository
from src.repository.in_memory_asset_repository import InMemoryAssetRepository
from src.repository.stock_pricing_repository import StockPricingRepository
from src.system_clock import SystemClock


@pytest.fixture
def mock_system_clock(mocker):
    return mocker.MagicMock(SystemClock)

@pytest.fixture
def in_memory_asset_repository(mock_system_clock):
    return InMemoryAssetRepository(mock_system_clock)

@pytest.fixture
def mock_asset_repository(mocker):
    return mocker.MagicMock(AssetRepository)


@pytest.fixture
def mock_stock_pricing_repository(mocker):
    return mocker.MagicMock(StockPricingRepository)


@pytest.fixture
def mock_portfolio_presenter(mocker):
    return mocker.MagicMock(PortfolioPresenter)


@pytest.fixture
def portfolio_tracker(
    mock_asset_repository,
    mock_stock_pricing_repository,
    mock_portfolio_presenter
):
    return PortfolioTracker(
        mock_asset_repository,
        mock_stock_pricing_repository,
        mock_portfolio_presenter
    )
