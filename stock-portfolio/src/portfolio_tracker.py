from src.asset import Asset
from src.presenter.portfolio_presenter import Presenter
from src.repository.asset_repository import AssetRepository
from src.repository.stock_pricing_repository import StockPricingRepository


class PortfolioTracker:

    def __init__(self, asset_repository: AssetRepository,
                 stock_pricing_repository: StockPricingRepository,
                 portfolio_presenter: Presenter):
        self.portfolio_presenter = portfolio_presenter
        self.stock_pricing_repository = stock_pricing_repository
        self.asset_repository = asset_repository

    def add_purchase(self, number_of_shares, stock):
        asset = self.__to_asset(number_of_shares, stock)
        self.asset_repository.add_asset(asset)

    def add_sale(self, number_of_shares, stock):
        asset = self.__to_asset(number_of_shares, stock)
        self.asset_repository.update_asset(asset)

    def update_price(self, stock, price):
        self.stock_pricing_repository.set_stock_price(price=price, stock=stock)

    def print_portfolio(self):
        assets = self.asset_repository.fetch_assets()
        prices = self.stock_pricing_repository.fetch_prices()
        self.portfolio_presenter.present(assets=assets, prices=prices)

    @staticmethod
    def __to_asset(number_of_shares, stock) -> Asset:
        return Asset(number_of_shares=number_of_shares, stock=stock)
