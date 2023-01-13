from abc import abstractmethod
from typing import Protocol, NewType

StockName = NewType('StockName', str)
StockPrice = NewType('StockPrice', float)


class StockUnknownError(Exception):
    pass


class StockPricingRepository(Protocol):
    @abstractmethod
    def set_stock_price(self, stock: StockName, price: StockPrice) -> None:
        pass

    @abstractmethod
    def fetch_stock_price(self, stock: StockName) -> StockPrice:
        """
        :param stock:
        :return:
        :raise: StockUnknownError
        """
        pass
