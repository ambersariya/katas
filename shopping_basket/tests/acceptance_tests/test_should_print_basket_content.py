from unittest.mock import MagicMock, patch

from acceptance_tests.base_test_case import BaseTestCase
from constants import USER_ID, PRODUCT_ID_HOBBIT, PRODUCT_ID_BREAKING_BAD


class PrintBasketContentShould(BaseTestCase):

    @patch("builtins.print")
    def test_return_contents_of_the_basket(self, mock_print: MagicMock):
        self._add_item(PRODUCT_ID_HOBBIT, 2)
        self._add_item(PRODUCT_ID_HOBBIT, 2)
        self._add_item(PRODUCT_ID_BREAKING_BAD, 5)

        basket = self.shopping_basket_service.basket_for(USER_ID)

        basket_printout = (
            "Creation date 15/06/2022\n"
            "4 x The Hobbit // Book // 4 x 5.00 = £20.00\n"
            "5 x Breaking Bad // Video // 5 x 7.00 = £35.00\n"
            "Total: £55.00"
        )

        assert str(basket) == basket_printout
        assert mock_print.call_count == 3

