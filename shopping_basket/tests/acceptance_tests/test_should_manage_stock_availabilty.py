from acceptance_tests.base_test_case import BaseTestCase
from constants import PRODUCT_ID_LORD_OF_THE_RINGS
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_error import InsufficientStockError


class ManageStockAvailabilityShould(BaseTestCase):

    def test_raise_error_when_not_enough_product_in_stock(self):
        with self.assertRaises(InsufficientStockError):
            self._add_item(product_id=PRODUCT_ID_LORD_OF_THE_RINGS, quantity=10)

    def test_add_item_to_basket_when_stock_is_sufficient(self):
        self._add_item(product_id=PRODUCT_ID_LORD_OF_THE_RINGS, quantity=2)
        actual_stock = self.stock_repository.find_by_id(PRODUCT_ID_LORD_OF_THE_RINGS)
        expected_stock = Stock(product_id=PRODUCT_ID_LORD_OF_THE_RINGS, available=3, reserved=2, min_available=5)

        self.assertEqual(expected_stock, actual_stock)

