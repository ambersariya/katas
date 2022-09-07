from unittest.mock import MagicMock

from _pytest.fixtures import fixture

from shopping_basket.order.order_repository import OrderRepository
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider
from shopping_basket.stock.stock_management_service import StockManagementService
from shopping_basket.stock.stock_repository import StockRepository


@fixture()
def mocked_stock_repository():
    return MagicMock(StockRepository)


@fixture()
def stock_management_service(mocked_stock_repository):
    return StockManagementService(
        stock_repository=mocked_stock_repository
    )


@fixture()
def mock_stock_management_service():
    return MagicMock(StockManagementService)


@fixture()
def mocked_payment_provider():
    return MagicMock(PaymentProvider)


@fixture()
def mocked_order_repository():
    return MagicMock(OrderRepository)


@fixture()
def payment_gateway(mocked_payment_provider, mocked_order_repository):
    return PaymentGateway(
        payment_provider=mocked_payment_provider,
        order_repository=mocked_order_repository,
    )
