from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.core.date_provider import DateProvider
from shopping_basket.product.product import Product
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.infrastructure.in_memory_product_repository import InMemoryProductRepository
from shopping_basket.product.product_service import ProductService
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_management_service import StockManagementService
from shopping_basket.stock.infrastructure.in_memory_stock_repository import InMemoryStockRepository
from shopping_basket.basket.user import UserId
from shopping_basket.core.utilities import ItemLogger


class ApplyDiscountShould(TestCase):

    def setUp(self):
        date_provider = MagicMock(DateProvider)
        date_provider.current_date.return_value = "14/6/2022"
        self.shopping_basket_repository = InMemoryShoppingBasketRepository(date_provider=date_provider)
        self.stock_repository = InMemoryStockRepository()
        self.stock_management_service = StockManagementService(self.stock_repository)
        self.product_repository = InMemoryProductRepository()
        self.product_service = ProductService(product_repository=self.product_repository,
                                              stock_management_service=self.stock_management_service)
        self.item_logger = ItemLogger()
        self.shopping_basket_service = ShoppingBasketService(product_service=self.product_service,
                                                             shopping_basket_repository=self.shopping_basket_repository,
                                                             item_logger=self.item_logger)
        self.user_id = UserId('user-01')
        self._fill_products()

    def test_return_contents_of_the_basket(self):
        self._add_item(self.user_id, ProductId("10002"), 4)
        self._add_item(self.user_id, ProductId("20110"), 5)

        basket = self.shopping_basket_service.basket_for(self.user_id)

        basket_printout = \
            "Creation date 14/6/2022\n" \
            "4 x The Hobbit // Book // 4 x 5.00 = £20.00\n" \
            "5 x Breaking Bad // Video // 5 x 7.00 = £35.00\n" \
            "Discount applied: 20% \n" \
            "Total: £44.00"

        assert str(basket) == basket_printout

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
