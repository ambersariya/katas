from src.asset import Asset
from src.value_objects import StockName, StockPrice, AssetOwner, AssetName

ASSET_OWNER = AssetOwner('alice')
TSLA_ASSET = Asset(number_of_shares=10, name=AssetName("TSLA"), owner=ASSET_OWNER)


def test_asset_is_added_to_the_portfolio_tracker(mock_asset_repository, portfolio_tracker):
    portfolio_tracker.add_purchase(number_of_shares=10, asset_name="TSLA", asset_owner=ASSET_OWNER)

    mock_asset_repository.add_asset.assert_called_once_with(TSLA_ASSET)


def test_asset_has_been_sold_from_the_portfolio_tracker(mock_asset_repository, portfolio_tracker):
    portfolio_tracker.add_sale(number_of_shares=10, asset_name="TSLA", asset_owner=ASSET_OWNER)

    mock_asset_repository.update_asset.assert_called_once_with(TSLA_ASSET)


def test_asset_has_updated_value_of_the_stock_in_portfolio_tracker(mock_stock_pricing_repository,
                                                                   portfolio_tracker):
    portfolio_tracker.update_price(price=125, stock="TSLA")

    mock_stock_pricing_repository.set_stock_price.assert_called_once_with(price=125, stock="TSLA")


def test_should_print_asset_portfolio(mock_portfolio_presenter,
                                      mock_stock_pricing_repository,
                                      mock_asset_repository,
                                      portfolio_tracker
                                      ):
    user_assets = [
        Asset(number_of_shares=100, name=AssetName('AAPL'), owner=ASSET_OWNER),
        Asset(number_of_shares=80, name=AssetName('MSFT'), owner=ASSET_OWNER),
    ]
    stock_prices = {
        StockName('AAPL'): StockPrice(100.0), StockName('MSFT'): StockPrice(80.0)
    }

    mock_asset_repository.fetch_assets.return_value = user_assets
    mock_stock_pricing_repository.fetch_stock_price.side_effect = [
        StockPrice(100.0),
        StockPrice(80.0)
    ]

    portfolio_tracker.print_portfolio(owner=ASSET_OWNER)

    mock_portfolio_presenter.present.assert_called_once_with(
        assets=user_assets,
        prices=stock_prices
    )
