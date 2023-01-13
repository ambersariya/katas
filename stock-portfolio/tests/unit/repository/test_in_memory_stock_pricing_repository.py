import pytest as pytest

from src.repository.in_memory_stock_price_repository import InMemoryStockPriceRepository
from src.repository.stock_pricing_repository import StockName, StockPrice, StockUnknownError

STOCK_NAME = StockName('TSLA')
STOCK_PRICE = StockPrice(150.0)


def test_should_fetch_price_for_a_given_stock(
    in_memory_stock_price_repository: InMemoryStockPriceRepository
):
    in_memory_stock_price_repository.set_stock_price(stock=STOCK_NAME, price=STOCK_PRICE)
    stock_price = in_memory_stock_price_repository.fetch_stock_price(stock=STOCK_NAME)
    assert STOCK_PRICE == stock_price


def test_should_fetch_no_price_for_unknown_stock(
    in_memory_stock_price_repository: InMemoryStockPriceRepository
):
    with pytest.raises(StockUnknownError):
        in_memory_stock_price_repository.fetch_stock_price(stock=StockName('UNKWN'))
