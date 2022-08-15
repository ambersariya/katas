from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.core.date_provider import DateProvider
from shopping_basket.product.product import Product
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.stock.stock_error import InsufficientStockError
from shopping_basket.product.infrastructure.in_memory_product_repository import InMemoryProductRepository
from shopping_basket.product.product_service import ProductService
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_management_service import StockManagementService
from shopping_basket.stock.infrastructure.in_memory_stock_repository import InMemoryStockRepository
from shopping_basket.basket.user import UserId
from shopping_basket.core.utilities import ItemLogger

PRODUCT_ID = ProductId('10001')


class ManageStockAvailabilityShould(TestCase):

    def setUp(self):
        date_provider = MagicMock(DateProvider)
        date_provider.current_date.return_value = "14/6/2022"
        self.shopping_basket_repository = InMemoryShoppingBasketRepository(date_provider=date_provider)
        self.product_repository = InMemoryProductRepository()
        self.stock_repository = InMemoryStockRepository()
        self.stock_management_service = StockManagementService(self.stock_repository)
        self.product_service = ProductService(self.product_repository, self.stock_management_service)
        self.item_logger = ItemLogger()
        self.shopping_basket_service = ShoppingBasketService(product_service=self.product_service,
                                                             shopping_basket_repository=self.shopping_basket_repository,
                                                             item_logger=self.item_logger)
        self.user_id = UserId('user-01')
        self._fill_products()
        self.stock_management_service.save_stock(stock=Stock(product_id=PRODUCT_ID, available=3, reserved=0))

    def test_raise_error_when_not_enough_product_in_stock(self):
        with self.assertRaises(InsufficientStockError):
            self._add_item(user_id=self.user_id, product_id=PRODUCT_ID, quantity=5)

    def test_add_item_to_basket_when_stock_is_sufficient(self):
        self._add_item(user_id=self.user_id, product_id=PRODUCT_ID, quantity=2)
        actual_stock = self.stock_repository.find_by_id(PRODUCT_ID)
        expected_stock = Stock(product_id=PRODUCT_ID, available=1, reserved=2)

        self.assertEqual(expected_stock, actual_stock)

    def _add_item(self, user_id: UserId, product_id: ProductId, quantity: int):
        self.shopping_basket_service.add_item(user_id=user_id,
                                              product_id=product_id,
                                              quantity=int(quantity))

    def _fill_products(self):
        self.product_service.add_product(
            product=Product(id=ProductId('10001'), name="Lord of the Rings", price=10, category=ProductCategory.BOOK),
            stock=Stock(product_id=ProductId('10001'), available=5, reserved=0))
        self.product_service.add_product(
            product=Product(id=ProductId('10002'), name="The Hobbit", price=5, category=ProductCategory.BOOK),
            stock=Stock(product_id=ProductId('10002'), available=5, reserved=0))
        self.product_service.add_product(
            product=Product(id=ProductId('20001'), name="Game of Thrones", price=9, category=ProductCategory.VIDEO),
            stock=Stock(product_id=ProductId('20001'), available=5, reserved=0))
        self.product_service.add_product(
            product=Product(id=ProductId('20110'), name="Breaking Bad", price=7, category=ProductCategory.VIDEO),
            stock=Stock(product_id=ProductId('20110'), available=5, reserved=0))
