import pytest

from tests.constants import USER_ID, PRODUCT_ID_HOBBIT, PRODUCT_ID_BREAKING_BAD


class TestPrintBasketContentShould:
    @pytest.mark.usefixtures("initialize_handlers")
    def test_return_contents_of_the_basket(self, shopping_basket_service):
        shopping_basket_service.add_item(user_id=USER_ID, product_id=PRODUCT_ID_HOBBIT, quantity=2)
        shopping_basket_service.add_item(user_id=USER_ID, product_id=PRODUCT_ID_HOBBIT, quantity=2)
        shopping_basket_service.add_item(
            user_id=USER_ID, product_id=PRODUCT_ID_BREAKING_BAD, quantity=5
        )

        basket = shopping_basket_service.basket_for(USER_ID)

        basket_printout = (
            "Creation date 15/06/2022\n"
            "4 x The Hobbit // Book // 4 x 5.00 = £20.00\n"
            "5 x Breaking Bad // Video // 5 x 7.00 = £35.00\n"
            "Total: £55.00"
        )

        assert str(basket) == basket_printout
