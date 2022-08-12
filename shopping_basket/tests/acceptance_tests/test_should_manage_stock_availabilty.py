from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.date_provider import DateProvider
from shopping_basket.errors import InsufficientStockError
from shopping_basket.product import Product, ProductId
from shopping_basket.product_repository import InMemoryProductRepository
from shopping_basket.product_service import ProductService
from shopping_basket.shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_management_service import StockManagementService
from shopping_basket.stock.stock_repository import InMemoryStockRepository
from shopping_basket.user import UserId
from shopping_basket.utilities import ItemLogger


class ManageStockAvailabilityShould(TestCase):

    def setUp(self):
        date_provider = MagicMock(DateProvider)
        date_provider.current_date.return_value = "14/6/2022"
        self.shopping_basket_repository = InMemoryShoppingBasketRepository(date_provider=date_provider)
        self.product_repository = InMemoryProductRepository()
        self.stock_management_service = StockManagementService(InMemoryStockRepository())
        self.product_service = ProductService(self.product_repository, self.stock_management_service)
        self.item_logger = ItemLogger()
        self.shopping_basket_service = ShoppingBasketService(product_service=self.product_service,
                                                             shopping_basket_repository=self.shopping_basket_repository,
                                                             item_logger=self.item_logger)
        self.user_id = UserId('user-01')
        self._fill_products()
        self.stock_management_service.save_stock(stock=Stock(product_id=ProductId('10001'), available=0, reserved=4))

    def test_raise_error_when_not_enough_product_in_stock(self):
        with self.assertRaises(InsufficientStockError):
            self._add_item(user_id=self.user_id, product_id=ProductId('10001'), quantity=5)

    def _add_item(self, user_id, product_id, quantity):
        self.shopping_basket_service.add_item(user_id=user_id,
                                              product_id=product_id,
                                              quantity=int(quantity))

    def _fill_products(self):
        self.product_repository.add_product(
            Product(id=ProductId('10001'), name="Lord of the Rings", price=10))
