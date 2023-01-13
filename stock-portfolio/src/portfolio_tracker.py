from src.asset import Asset
from src.presenter.portfolio_presenter import Presenter
from src.repository.asset_repository import AssetRepository
from src.repository.stock_pricing_repository import StockPricingRepository
from src.value_objects import StockName


class PortfolioTracker:
    def __init__(
        self,
        asset_repository: AssetRepository,
        stock_pricing_repository: StockPricingRepository,
        portfolio_presenter: Presenter
    ):
        self.portfolio_presenter = portfolio_presenter
        self.stock_pricing_repository = stock_pricing_repository
        self.asset_repository = asset_repository

    def add_purchase(self, number_of_shares, asset_name, asset_owner):
        asset = self.__to_asset(number_of_shares, asset_name=asset_name, asset_owner=asset_owner)
        self.asset_repository.add_asset(asset)

    def add_sale(self, number_of_shares: int, asset_name, asset_owner):
        asset = self.__to_asset(number_of_shares, asset_name=asset_name, asset_owner=asset_owner)
        self.asset_repository.update_asset(asset)

    def update_price(self, stock, price):
        self.stock_pricing_repository.set_stock_price(price=price, stock=stock)

    def print_portfolio(self, owner):
        assets = self.asset_repository.fetch_assets(owner=owner)
        prices = {
            StockName(asset.name): self.stock_pricing_repository.fetch_stock_price(
                stock=StockName(asset.name))
            for asset in assets
        }
        self.portfolio_presenter.present(assets=assets, prices=prices)

    @staticmethod
    def __to_asset(number_of_shares, asset_name, asset_owner) -> Asset:
        return Asset(number_of_shares=number_of_shares, name=asset_name, owner=asset_owner)
