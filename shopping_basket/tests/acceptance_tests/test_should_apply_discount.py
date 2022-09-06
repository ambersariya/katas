import pytest

from constants import USER_ID, PRODUCT_ID_HOBBIT, PRODUCT_ID_BREAKING_BAD


class TestApplyDiscountShould:

    @pytest.mark.usefixtures('initialize_handlers')
    def test_return_contents_of_the_basket(self, shopping_basket_service_with_discounts):
        shopping_basket_service_with_discounts.add_item(
            user_id=USER_ID, product_id=PRODUCT_ID_HOBBIT, quantity=4
        )
        shopping_basket_service_with_discounts.add_item(
            user_id=USER_ID, product_id=PRODUCT_ID_BREAKING_BAD, quantity=5
        )

        basket = shopping_basket_service_with_discounts.basket_for(USER_ID)

        basket_printout = (
            "Creation date 15/06/2022\n"
            "4 x The Hobbit // Book // 4 x 5.00 = £20.00\n"
            "5 x Breaking Bad // Video // 5 x 7.00 = £35.00\n"
            "Discount applied: 20%\n"
            "Total: £44.00"
        )

        assert str(basket) == basket_printout
