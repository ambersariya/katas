from abc import abstractmethod
from typing import Protocol

from src.asset import Asset
from src.presenter.portfolio_presenter import PortfolioPresenter
from src.repository.asset_repository import AssetRepository
from src.repository.stock_pricing_repository import StockPricingRepository
from src.value_objects import StockName, AssetName


class Portfolio(Protocol):
    @abstractmethod
    def buy(self, number_of_shares, asset_name):
        pass


    @abstractmethod
    def sell(self, number_of_shares, asset_name):
        pass

    @abstractmethod
    def print_portfolio(self):
        pass


class InsufficientAssetsException(Exception):
    DEFAULT_MESSAGE = "Sorry, you don't have enough assets to complete this transaction"

    def __init__(self, message: str = None):
        self.message = message or self.DEFAULT_MESSAGE

    def __str__(self):
        return self.message

class PortfolioTracker(Portfolio):

    def __init__(
        self,
        asset_repository: AssetRepository,
        stock_pricing_repository: StockPricingRepository,
        portfolio_presenter: PortfolioPresenter
    ):
        self.__portfolio_presenter = portfolio_presenter
        self.__stock_pricing_repository = stock_pricing_repository
        self.__asset_repository = asset_repository


    def buy(self, number_of_shares: int, asset_name: AssetName):
        asset: Asset = self.__to_asset(number_of_shares, asset_name=asset_name)
        self.__asset_repository.save_asset(asset)

    def sell(self, number_of_shares, asset_name):
        asset: Asset = self.__asset_repository.fetch_asset_by_name(asset_name=asset_name)
        if asset.number_of_shares < number_of_shares:
            raise InsufficientAssetsException()
        asset.number_of_shares = asset.number_of_shares - number_of_shares
        self.__asset_repository.save_asset(asset)

    def add_sale(self, number_of_shares: int, asset_name, asset_owner):
        asset = self.__to_asset(number_of_shares, asset_name=asset_name, asset_owner=asset_owner)
        self.__asset_repository.save_asset(asset)

    def update_price(self, stock, price):
        self.__stock_pricing_repository.set_stock_price(price=price, stock=stock)

    def print_portfolio(self):
        assets = self.__asset_repository.fetch_assets()
        prices = {
            StockName(asset.name): self.__stock_pricing_repository.fetch_stock_price(
                stock=StockName(asset.name))
            for asset in assets
        }
        self.__portfolio_presenter.present(assets=assets, prices=prices)

    @staticmethod
    def __to_asset(number_of_shares, asset_name) -> Asset:
        return Asset(number_of_shares=number_of_shares, name=asset_name)
