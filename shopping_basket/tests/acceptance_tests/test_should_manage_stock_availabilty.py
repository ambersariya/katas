import pytest

from constants import PRODUCT_ID_LORD_OF_THE_RINGS, USER_ID
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_error import InsufficientStockError


class TestManageStockAvailabilityShould:

    def test_raise_error_when_not_enough_product_in_stock(self,
                                                          shopping_basket_service_with_discounts):
        with pytest.raises(InsufficientStockError):
            shopping_basket_service_with_discounts.add_item(user_id=USER_ID,
                                                            product_id=PRODUCT_ID_LORD_OF_THE_RINGS,
                                                            quantity=10)

    def test_add_item_to_basket_when_stock_is_sufficient(self,
                                                         shopping_basket_service_with_discounts,
                                                         stock_repository):
        shopping_basket_service_with_discounts.add_item(user_id=USER_ID,
                                                        product_id=PRODUCT_ID_LORD_OF_THE_RINGS,
                                                        quantity=2)
        actual_stock = stock_repository.find_by_id(PRODUCT_ID_LORD_OF_THE_RINGS)
        expected_stock = Stock(
            product_id=PRODUCT_ID_LORD_OF_THE_RINGS, available=3, reserved=2, min_available=5
        )

        assert expected_stock == actual_stock
