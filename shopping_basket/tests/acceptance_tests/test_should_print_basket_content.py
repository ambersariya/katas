from unittest import TestCase, skip
from unittest.mock import MagicMock

from shopping_basket.date_provider import DateProvider
from shopping_basket.product_service import ProductService
from shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.user import UserId


@skip(reason="Have to implement unit tests first")
class PrintBasketContentShould(TestCase):

    def setUp(self):
        self.shopping_basket_service = ShoppingBasketService()
        self.product_service = ProductService()
        self.user_id = UserId()

    def test_return_contents_of_the_basket(self):
        date_provider = MagicMock(DateProvider)
        date_provider.current_date.return_value = "14/6/2022"
        self._add_item(self.user_id, "The Hobbit", 2)
        self._add_item(self.user_id, "Breaking Bad", 5)

        basket = self.shopping_basket_service.basket_for(self.user_id)

        basket_printout = \
            """
            Creation date 14/6/2022\
            2 x The Hobbit // 2 x 5.00 = £10.00\
            5 x Breaking Bad // 5 x 7.00 = £35.00\
            Total: £45.00
            """

        assert str(basket) == basket_printout

    def _add_item(self, user_id, item_name, quantity):
        item = self.product_service.find_product_by_name(item_name)

        self.shopping_basket_service.add_item(user_id=self.user_id,
                                              product_id=item.id,
                                              quantity=int(quantity))
