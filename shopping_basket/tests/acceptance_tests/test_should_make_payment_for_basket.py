from unittest import TestCase
from unittest.mock import MagicMock

from constants import USER_ID, STRATEGIES, UNPAID_ORDER
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import \
    InMemoryShoppingBasketRepository
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.basket.user import UserId
from shopping_basket.core.date_provider import DateProvider
from shopping_basket.core.utilities import ItemLogger
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider
from shopping_basket.payment.payment_details import PaymentDetails
from shopping_basket.payment.payment_service import PaymentService
from shopping_basket.product.infrastructure.in_memory_product_repository import \
    InMemoryProductRepository
from shopping_basket.product.product import Product
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_service import ProductService
from shopping_basket.stock.infrastructure.in_memory_stock_repository import InMemoryStockRepository
from shopping_basket.stock.stock import Stock
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
        self._fill_products()

    def _add_item(self, user_id: UserId, product_id: ProductId, quantity: int):
        self.shopping_basket_service.add_item(
            user_id=user_id, product_id=product_id, quantity=int(quantity)
        )

    def _fill_products(self):
        self.product_service.add_product(
            product=Product(
                id=ProductId("10001"),
                name="Lord of the Rings",
                price=10,
                category=ProductCategory.BOOK,
            ),
            stock=Stock(product_id=ProductId("10001"), available=5, reserved=0),
        )
        self.product_service.add_product(
            product=Product(
                id=ProductId("10002"),
                name="The Hobbit",
                price=5,
                category=ProductCategory.BOOK,
            ),
            stock=Stock(product_id=ProductId("10002"), available=5, reserved=0),
        )
        self.product_service.add_product(
            product=Product(
                id=ProductId("20001"),
                name="Game of Thrones",
                price=9,
                category=ProductCategory.VIDEO,
            ),
            stock=Stock(product_id=ProductId("20001"), available=5, reserved=0),
        )
        self.product_service.add_product(
            product=Product(
                id=ProductId("20110"),
                name="Breaking Bad",
                price=7,
                category=ProductCategory.VIDEO,
            ),
            stock=Stock(product_id=ProductId("20110"), available=5, reserved=0),
        )

    def test_be_successful(self):
        self._add_item(USER_ID, ProductId("10002"), 4)
        self._add_item(USER_ID, ProductId("20110"), 5)
        payment_details = PaymentDetails()

        self.payment_service.make_payment(
            user_id=USER_ID,
            payment_details=payment_details
        )

        self.payment_provider.pay.assert_called_once_with(UNPAID_ORDER)
