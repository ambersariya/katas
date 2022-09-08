from unittest.mock import MagicMock

from _pytest.fixtures import fixture

from constants import DISCOUNT_STRATEGIES
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import (
    InMemoryShoppingBasketRepository,
)
from shopping_basket.basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.core.utilities import ItemLogger, IdGenerator
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.order.infrastructure.in_memory_order_repository import InMemoryOrderRepository
from shopping_basket.order.order_repository import OrderRepository
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider
from shopping_basket.payment.payment_service import PaymentService
from shopping_basket.product.product_repository import ProductRepository
from shopping_basket.product.product_service import ProductService
from shopping_basket.purchase.purchase_system import PurchaseSystem
from shopping_basket.stock.stock_management_service import StockManagementService
from shopping_basket.stock.stock_repository import StockRepository


@fixture()
def mocked_stock_repository():
    return MagicMock(StockRepository)


@fixture()
def stock_management_service(mocked_stock_repository):
    return StockManagementService(stock_repository=mocked_stock_repository)


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


@fixture()
def in_memory_shopping_basket_repo(date_provider):
    return InMemoryShoppingBasketRepository(date_provider=date_provider)


@fixture()
def mocked_shopping_basket_repository():
    return MagicMock(ShoppingBasketRepository)


@fixture()
def mocked_product_service():
    return MagicMock(ProductService)


@fixture()
def mocked_item_logger():
    return MagicMock(ItemLogger)


@fixture()
def mocked_discount_calculator():
    return MagicMock(DiscountCalculator)


@fixture()
def shopping_basket_service(
    mocked_discount_calculator,
    mocked_shopping_basket_repository,
    mocked_product_service,
    mocked_item_logger,
):
    return ShoppingBasketService(
        shopping_basket_repository=mocked_shopping_basket_repository,
        product_service=mocked_product_service,
        item_logger=mocked_item_logger,
        discount_calculator=mocked_discount_calculator,
    )


@fixture()
def discount_calculator_with_strategies(discount_calculator):
    return discount_calculator(DISCOUNT_STRATEGIES)


@fixture()
def mocked_id_generator():
    return MagicMock(IdGenerator)


@fixture()
def order_repository(mocked_id_generator):
    return InMemoryOrderRepository(id_generator=mocked_id_generator)


@fixture()
def mocked_product_repository():
    return MagicMock(ProductRepository)


@fixture()
def mocked_stock_management_service():
    return MagicMock(StockManagementService)


@fixture()
def product_service(mocked_product_repository, mocked_stock_management_service):
    _product_service = ProductService(
        product_repository=mocked_product_repository,
        stock_management_service=mocked_stock_management_service,
    )
    return _product_service


@fixture()
def mocked_purchase_system():
    return MagicMock(PurchaseSystem)


@fixture()
def payment_service(mocked_shopping_basket_service, mocked_payment_gateway):
    return PaymentService(
        shopping_basket_service=mocked_shopping_basket_service,
        payment_gateway=mocked_payment_gateway,
    )
