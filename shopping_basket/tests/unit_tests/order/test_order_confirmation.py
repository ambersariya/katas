from tests.constants import USER_ID, ORDER_ID, PAYMENT_REFERENCE


class TestOrderConfirmationShould:
    def test_send_email(self, order_confirmation, email_gateway):
        order_confirmation.send(
            user_id=USER_ID, order_id=ORDER_ID, payment_reference=PAYMENT_REFERENCE
        )

        email_gateway.send.assert_called_once()
