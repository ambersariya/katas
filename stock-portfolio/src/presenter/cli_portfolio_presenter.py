from typing import List, Dict

from src.asset import Asset
from src.presenter.portfolio_presenter import PortfolioPresenter
from src.value_objects import StockName, StockPrice


class CliPortfolioPresenter(PortfolioPresenter):
    def present(self, assets: List[Asset], prices: Dict[StockName, StockPrice]):
        raise NotImplementedError()
