from unittest import mock

import pytest

from constants import PAYMENT_DETAILS, PAYMENT_REFERENCE, UNPAID_ORDER, USER_ID
from shopping_basket.payment.infrastructure.errors import PaymentError


class TestPaymentGatewayShould:
    def test_raise_exception_for_unpaid_order(self, mocked_payment_provider, payment_gateway):
        mocked_payment_provider.pay.side_effect = PaymentError()

        with pytest.raises(PaymentError):
            payment_gateway.pay(
                order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
            )

    @mock.patch('shopping_basket.payment.infrastructure.payment_gateway.handle')
    def test_make_payment_successfully_for_unpaid_order(self, event_handler,
                                                        mocked_payment_provider,
                                                        payment_gateway,
                                                        mocked_order_repository):
        mocked_payment_provider.pay.return_value = PAYMENT_REFERENCE

        payment_gateway.pay(
            order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        mocked_payment_provider.pay.assert_called_once_with(
            order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        mocked_order_repository.add.assert_called_once_with(
            order=UNPAID_ORDER, payment_reference=PAYMENT_REFERENCE
        )
        event_handler.assert_called_once()
