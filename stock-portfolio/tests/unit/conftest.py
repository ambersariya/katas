import pytest as pytest

from src.portfolio_tracker import PortfolioTracker
from src.presenter.portfolio_presenter import PortfolioPresenter
from src.repository.asset_repository import AssetRepository
from src.repository.stock_pricing_repository import StockPricingRepository


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
