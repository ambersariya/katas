import pytest

from constants import USER_ID, PAYMENT_REFERENCE, PAYMENT_DETAILS, PRODUCT_ID_HOBBIT, \
    PRODUCT_ID_BREAKING_BAD
from shopping_basket.payment.infrastructure.errors import PaymentError


class TestMakePaymentForBasketShould:
    def test_raise_exception_when_making_payment(self,
                                                 shopping_basket_service,
                                                 payment_provider,
                                                 payment_service):
        payment_provider.pay.side_effect = PaymentError()

        shopping_basket_service.add_item(user_id=USER_ID, product_id=PRODUCT_ID_HOBBIT, quantity=4)
        shopping_basket_service.add_item(
            user_id=USER_ID, product_id=PRODUCT_ID_BREAKING_BAD, quantity=5)

        with pytest.raises(PaymentError):
            payment_service.make_payment(user_id=USER_ID, payment_details=PAYMENT_DETAILS)

    @pytest.mark.usefixtures('initialize_handlers')
    def test_notify_user_that_order_is_confirmed(self,
                                                 shopping_basket_service,
                                                 payment_provider,
                                                 payment_service,
                                                 unpaid_order,
                                                 email_gateway
                                                 ) -> None:
        shopping_basket_service.add_item(user_id=USER_ID, product_id=PRODUCT_ID_HOBBIT, quantity=4)
        shopping_basket_service.add_item(
            user_id=USER_ID, product_id=PRODUCT_ID_BREAKING_BAD, quantity=5)

        payment_provider.pay.return_value = PAYMENT_REFERENCE

        payment_service.make_payment(user_id=USER_ID, payment_details=PAYMENT_DETAILS)

        payment_provider.pay.assert_called_once_with(
            order=unpaid_order, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        email_gateway.send.assert_called_once()
