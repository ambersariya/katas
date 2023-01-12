import pytest

from src.asset import Asset
from src.presenter.portfolio_presenter import Presenter
from src.repository.asset_repository import AssetRepository
from src.portfolio_tracker import PortfolioTracker
from src.repository.stock_pricing_repository import StockPricingRepository


@pytest.fixture
def mock_asset_repository(mocker):
    return mocker.MagicMock(AssetRepository)


@pytest.fixture
def mock_stock_pricing_repository(mocker):
    return mocker.MagicMock(StockPricingRepository)


@pytest.fixture
def mock_portfolio_presenter(mocker):
    return mocker.MagicMock(Presenter)


@pytest.fixture
def portfolio_tracker(mock_asset_repository, mock_stock_pricing_repository,
                      mock_portfolio_presenter):
    return PortfolioTracker(mock_asset_repository, mock_stock_pricing_repository,
                            mock_portfolio_presenter)


TSLA_ASSET = Asset(number_of_shares=10, stock="TSLA")


def test_asset_is_added_to_the_portfolio_tracker(mock_asset_repository, portfolio_tracker):
    portfolio_tracker.add_purchase(number_of_shares=10, stock="TSLA")

    mock_asset_repository.add_asset.assert_called_once_with(TSLA_ASSET)


def test_asset_has_been_sold_from_the_portfolio_tracker(mock_asset_repository, portfolio_tracker):
    portfolio_tracker.add_sale(number_of_shares=10, stock="TSLA")

    mock_asset_repository.update_asset.assert_called_once_with(TSLA_ASSET)


def test_asset_has_updated_value_of_the_stock_in_portfolio_tracker(mock_stock_pricing_repository,
                                                                   portfolio_tracker):
    portfolio_tracker.update_price(price=125, stock="TSLA")

    mock_stock_pricing_repository.set_stock_price.assert_called_once_with(price=125, stock="TSLA")


def test_should_print_asset_portfolio(mock_portfolio_presenter,
                                      mock_stock_pricing_repository, mock_asset_repository,
                                      portfolio_tracker
                                      ):
    user_assets = [Asset(100, 'AAPL'), Asset(80, 'MSFT')]
    stock_prices = {'AAPL': 100.0, 'MSFT': 80.0}

    mock_stock_pricing_repository.fetch_prices.return_value = stock_prices
    mock_asset_repository.fetch_assets.return_value = user_assets

    portfolio_tracker.print_portfolio()

    mock_portfolio_presenter.present.assert_called_once_with(assets=user_assets,
                                                             prices=stock_prices)
