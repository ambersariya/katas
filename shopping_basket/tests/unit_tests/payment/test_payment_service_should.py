from constants import PAYMENT_DETAILS, SHOPPING_BASKET_WITH_ONE_ITEM, UNPAID_ORDER, USER_ID


class TestPaymentServiceShould:
    def test_make_payment_for_given_shopping_basket(self,
                                                    mocked_shopping_basket_service,
                                                    mocked_payment_gateway,
                                                    payment_service):
        mocked_shopping_basket_service.basket_for.return_value = SHOPPING_BASKET_WITH_ONE_ITEM

        payment_service.make_payment(
            user_id=USER_ID,
            payment_details=PAYMENT_DETAILS,
        )

        mocked_payment_gateway.pay.assert_called_once_with(
            order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
