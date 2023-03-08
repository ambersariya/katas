from unittest.mock import MagicMock

import pytest

from tests.constants import (
    PRODUCT_BOOK_LORD_OF_THE_RINGS,
    STOCK_BOOK_LORD_OF_THE_RINGS,
    USER_ID,
    DISCOUNT_STRATEGIES,
)
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import (
    InMemoryShoppingBasketRepository,
)
from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.core.date_provider import DateProvider
from shopping_basket.core.email_gateway import EmailGateway
from shopping_basket.core.messagebus import HANDLERS
from shopping_basket.core.utilities import IdGenerator
from basket.shopping_basket_item_logger import ItemLogger
from shopping_basket.basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.order.handler import OrderConfirmedHandler
from shopping_basket.order.infrastructure.in_memory_order_repository import InMemoryOrderRepository
from shopping_basket.order.notification.order_confirmation import OrderConfirmation
from shopping_basket.order.order import UnpaidOrder
from shopping_basket.payment.event import OrderConfirmed
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider
from shopping_basket.payment.payment_service import PaymentService
from shopping_basket.product.infrastructure.in_memory_product_repository import (
    InMemoryProductRepository,
)
from shopping_basket.product.product import Product
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_service import ProductService
from shopping_basket.purchase.event import StockPurchased
from shopping_basket.purchase.handler import OrderMoreHandler
from shopping_basket.purchase.purchase_system import PurchaseSystem
from shopping_basket.stock.event import StockIsLow
from shopping_basket.stock.handler import StockUpdateHandler, StockPurchasedHandler
from shopping_basket.stock.infrastructure.in_memory_stock_repository import InMemoryStockRepository
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_management_service import StockManagementService


@pytest.fixture()
def email_gateway():
    return MagicMock(EmailGateway)


@pytest.fixture()
def order_confirmation(email_gateway):
    return OrderConfirmation(email_gateway=email_gateway)


@pytest.fixture()
def mocked_order_confirmation():
    return MagicMock(OrderConfirmation)


@pytest.fixture()
def date_provider():
    _date_provider = MagicMock(DateProvider)
    _date_provider.current_date.return_value = "15/06/2022"
    return _date_provider


@pytest.fixture()
def shopping_basket_repository(date_provider):
    return InMemoryShoppingBasketRepository(date_provider=date_provider)


@pytest.fixture()
def stock_repository():
    return InMemoryStockRepository()


@pytest.fixture()
def product_repository():
    return InMemoryProductRepository()


@pytest.fixture()
def discount_calculator():
    def initialize_strategies(strategies=None):
        if strategies is None:
            strategies = []
        return DiscountCalculator(strategies=strategies)

    return initialize_strategies


@pytest.fixture()
def discount_strategies():
    return DISCOUNT_STRATEGIES


@pytest.fixture()
def item_logger():
    return ItemLogger()


@pytest.fixture()
def id_generator():
    return IdGenerator()


@pytest.fixture()
def payment_provider():
    return MagicMock(PaymentProvider)


@pytest.fixture()
def order_repository(id_generator):
    return InMemoryOrderRepository(id_generator=id_generator)


@pytest.fixture()
def stock_handler(stock_management_service):
    return StockUpdateHandler(stock_management_service=stock_management_service)


@pytest.fixture()
def order_more_handler(purchase_system):
    return OrderMoreHandler(purchase_system=purchase_system)


@pytest.fixture()
def order_confirmed_handler(order_confirmation):
    return OrderConfirmedHandler(order_confirmation=order_confirmation)


@pytest.fixture()
def stock_purchased_handler(stock_management_service):
    return StockPurchasedHandler(stock_management_service=stock_management_service)


@pytest.fixture()
def initialize_handlers(
    stock_handler, order_more_handler, stock_purchased_handler, order_confirmed_handler
):
    HANDLERS[OrderConfirmed] = [order_confirmed_handler, stock_handler]
    HANDLERS[StockIsLow] = [order_more_handler]
    HANDLERS[StockPurchased] = [stock_purchased_handler]


@pytest.fixture()
def purchase_system():
    return PurchaseSystem()


@pytest.fixture()
def payment_gateway(payment_provider, order_repository):
    return PaymentGateway(
        payment_provider=payment_provider,
        order_repository=order_repository,
    )


@pytest.fixture()
def mocked_payment_gateway():
    return MagicMock(PaymentGateway)


@pytest.fixture()
def payment_service(shopping_basket_service, payment_gateway):
    return PaymentService(
        shopping_basket_service=shopping_basket_service, payment_gateway=payment_gateway
    )


@pytest.fixture()
def shopping_basket_service(
    product_service, shopping_basket_repository, item_logger, discount_calculator
):
    return ShoppingBasketService(
        product_service=product_service,
        shopping_basket_repository=shopping_basket_repository,
        item_logger=item_logger,
        discount_calculator=discount_calculator(),
    )


@pytest.fixture()
def mocked_shopping_basket_service():
    return MagicMock(ShoppingBasketService)


@pytest.fixture()
def shopping_basket_service_with_discounts(
    product_service, shopping_basket_repository, item_logger, discount_calculator
):
    return ShoppingBasketService(
        product_service=product_service,
        shopping_basket_repository=shopping_basket_repository,
        item_logger=item_logger,
        discount_calculator=discount_calculator(strategies=DISCOUNT_STRATEGIES),
    )


@pytest.fixture()
def stock_management_service(stock_repository):
    return StockManagementService(stock_repository=stock_repository)


@pytest.fixture()
def product_service(product_repository, stock_management_service):
    _product_service = ProductService(
        product_repository=product_repository, stock_management_service=stock_management_service
    )
    _fill_products(_product_service)
    return _product_service


def _fill_products(product_service):
    product_service.add_product(
        product=PRODUCT_BOOK_LORD_OF_THE_RINGS,
        stock=STOCK_BOOK_LORD_OF_THE_RINGS,
    )
    product_service.add_product(
        product=Product(
            id=ProductId("10002"),
            name="The Hobbit",
            price=5,
            category=ProductCategory.BOOK,
        ),
        stock=Stock(product_id=ProductId("10002"), available=5, reserved=0, min_available=5),
    )
    product_service.add_product(
        product=Product(
            id=ProductId("20001"),
            name="Game of Thrones",
            price=9,
            category=ProductCategory.VIDEO,
        ),
        stock=Stock(product_id=ProductId("20001"), available=5, reserved=0, min_available=5),
    )
    product_service.add_product(
        product=Product(
            id=ProductId("20110"),
            name="Breaking Bad",
            price=7,
            category=ProductCategory.VIDEO,
        ),
        stock=Stock(product_id=ProductId("20110"), available=5, reserved=0, min_available=5),
    )


@pytest.fixture()
def unpaid_order():
    items = ShoppingBasketItems(
        [
            ShoppingBasketItem(
                id=ProductId("10002"),
                name="The Hobbit",
                quantity=4,
                price=5,
                category=ProductCategory.BOOK,
            ),
            ShoppingBasketItem(
                id=ProductId("20110"),
                name="Breaking Bad",
                quantity=5,
                price=7,
                category=ProductCategory.VIDEO,
            ),
        ]
    )
    basket = ShoppingBasket(user_id=USER_ID, created_at="15/06/2022", items=items)
    return UnpaidOrder(user_id=USER_ID, shopping_basket=basket)
