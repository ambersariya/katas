import pytest
from pydantic import PaymentCardNumber
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import \
    InMemoryShoppingBasketRepository
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.core.messagebus import MessageBus
from shopping_basket.core.utilities import ItemLogger, IdGenerator
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.order.infrastructure.in_memory_order_repository import InMemoryOrderRepository
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider
from shopping_basket.payment.payment_service import PaymentService
from shopping_basket.product.infrastructure.in_memory_product_repository import \
    InMemoryProductRepository
from shopping_basket.product.product_service import ProductService
from shopping_basket.purchase.handler import OrderMoreHandler
from shopping_basket.purchase.purchase_system import PurchaseSystem
from shopping_basket.stock.handler import StockUpdateHandler, StockPurchasedHandler
from shopping_basket.stock.infrastructure.in_memory_stock_repository import InMemoryStockRepository
from shopping_basket.stock.stock_management_service import StockManagementService


@pytest.fixture()
def date_provider():
    date_provider = MagicMock(DateProvider)
    date_provider.current_date.return_value = "15/06/2022"
    return date_provider


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
    return DiscountCalculator(strategies=[])


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
def stock_purchased_handler(stock_management_service):
    return StockPurchasedHandler(stock_management_service=stock_management_service)


@pytest.fixture()
def message_bus(stock_handler, order_more_handler, stock_purchased_handler):
    _message_bus = MessageBus()
    _message_bus.add_handler(event_class=OrderConfirmed.name(), handler=stock_handler)
    _message_bus.add_handler(event_class=StockIsLow.name(), handler=order_more_handler)
    _message_bus.add_handler(event_class=StockPurchased.name(), handler=stock_purchased_handler)
    return _message_bus


@pytest.fixture()
def purchase_system(message_bus):
    return PurchaseSystem(message_bus=message_bus)


@pytest.fixture()
def payment_gateway(payment_provider, order_repository, message_bus):
    return PaymentGateway(
        payment_provider=payment_provider,
        order_repository=order_repository,
        message_bus=message_bus,
    )


@pytest.fixture()
def payment_service(shopping_basket_service, payment_gateway):
    return PaymentService(shopping_basket_service=shopping_basket_service,
                          payment_gateway=payment_gateway)


@pytest.fixture()
def shopping_basket_service(product_service, shopping_basket_repository, item_logger,
                            discount_calculator):
    return ShoppingBasketService(product_service=product_service,
                                 shopping_basket_repository=shopping_basket_repository,
                                 item_logger=item_logger,
                                 discount_calculator=discount_calculator)


@pytest.fixture()
def stock_management_service(stock_repository, message_bus):
    return StockManagementService(stock_repository=stock_repository, message_bus=message_bus)


@pytest.fixture()
def product_service(product_repository, stock_management_service):
    _product_service =  ProductService(product_repository=product_repository,
                          stock_management_service=stock_management_service)
    _fill_products()
    return _product_service

def _fill_products(self):
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
