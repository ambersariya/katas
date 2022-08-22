from unittest import TestCase
from unittest.mock import MagicMock

from constants import USER_ID, STRATEGIES
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import \
    InMemoryShoppingBasketRepository
from shopping_basket.basket.shopping_basket_id import ShoppingBasketId
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.core.date_provider import DateProvider
from shopping_basket.core.utilities import ItemLogger
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider
from shopping_basket.payment.payment_details import PaymentDetails
from shopping_basket.payment.payment_service import PaymentService
from shopping_basket.product.infrastructure.in_memory_product_repository import \
    InMemoryProductRepository
from shopping_basket.product.product_service import ProductService
from shopping_basket.stock.infrastructure.in_memory_stock_repository import InMemoryStockRepository
from shopping_basket.stock.stock_management_service import StockManagementService


class MakePaymentForBasketShould(TestCase):
    def setUp(self) -> None:
        date_provider = MagicMock(DateProvider)
        date_provider.current_date.return_value = "14/6/2022"
        self.shopping_basket_repository = InMemoryShoppingBasketRepository(
            date_provider=date_provider
        )
        self.stock_repository = InMemoryStockRepository()
        self.stock_management_service = StockManagementService(self.stock_repository)
        self.product_repository = InMemoryProductRepository()
        self.discount_calculator = DiscountCalculator(STRATEGIES)
        self.product_service = ProductService(
            product_repository=self.product_repository,
            stock_management_service=self.stock_management_service,
        )
        self.item_logger = ItemLogger()
        self.shopping_basket_service = ShoppingBasketService(
            product_service=self.product_service,
            shopping_basket_repository=self.shopping_basket_repository,
            item_logger=self.item_logger,
            discount_calculator=self.discount_calculator
        )
        self.payment_provider = MagicMock(PaymentProvider)
        self.payment_gateway = PaymentGateway(
            payment_provider=self.payment_provider
        )
        self.payment_service = PaymentService(
            shopping_basket_service=self.shopping_basket_service,
            payment_gateway=self.payment_gateway,
        )

    def test_be_successful(self):
        shopping_basket_id = ShoppingBasketId('sdsdsds')
        payment_details = PaymentDetails()

        self.payment_service.make_payment(
            user_id=USER_ID,
            shopping_basket_id=shopping_basket_id,
            payment_details=payment_details
        )

        self.payment_provider.pay.assert_called_once_with(UNPAID_ORDER)
