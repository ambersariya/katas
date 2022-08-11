from unittest import TestCase
from unittest.mock import MagicMock, patch

from shopping_basket.date_provider import DateProvider
from shopping_basket.product import Product, ProductId
from shopping_basket.product_repository import InMemoryProductRepository
from shopping_basket.product_service import ProductService
from shopping_basket.shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.user import UserId


class PrintBasketContentShould(TestCase):

    def setUp(self):
        date_provider = MagicMock(DateProvider)
        date_provider.current_date.return_value = "14/6/2022"
        self.shopping_basket_repository = InMemoryShoppingBasketRepository(date_provider=date_provider)
        self.product_repository = InMemoryProductRepository()
        self.product_service = ProductService(self.product_repository)
        self.shopping_basket_service = ShoppingBasketService(product_service=self.product_service,
                                                             shopping_basket_repository=self.shopping_basket_repository)
        self.user_id = UserId('user-01')
        self._fill_products()

    @patch('builtins.print')
    def test_return_contents_of_the_basket(self, mock_print):
        self._add_item(self.user_id, ProductId("10002"), 2)
        self._add_item(self.user_id, ProductId("10002"), 2)
        self._add_item(self.user_id, ProductId("20110"), 5)

        basket = self.shopping_basket_service.basket_for(self.user_id)

        basket_printout = \
            "Creation date 14/6/2022\n" \
            "4 x The Hobbit // 4 x 5.00 = £20.00\n" \
            "5 x Breaking Bad // 5 x 7.00 = £35.00\n" \
            "Total: £55.00"

        assert str(basket) == basket_printout
        assert mock_print.call_count == 3

    def _add_item(self, user_id, product_id, quantity):
        self.shopping_basket_service.add_item(user_id=user_id,
                                              product_id=product_id,
                                              quantity=int(quantity))

    def _fill_products(self):
        self.product_repository.add_product(Product(id=ProductId('10001'), name="Lord of the Rings", price=10))
        self.product_repository.add_product(Product(id=ProductId('10002'), name="The Hobbit", price=5))
        self.product_repository.add_product(Product(id=ProductId('20001'), name="Game of Thrones", price=9))
        self.product_repository.add_product(Product(id=ProductId('20110'), name="Breaking Bad", price=7))
