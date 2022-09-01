from unittest import TestCase
from unittest.mock import MagicMock

from constants import USER_ID, ORDER_ID, PAYMENT_REFERENCE
from shopping_basket.core.email_gateway import EmailGateway
from shopping_basket.order.notification.order_confirmation import OrderConfirmation


class OrderConfirmationShould(TestCase):
    def test_send_email(self):
        self.email_gateway = MagicMock(EmailGateway)
        self.order_confirmation = OrderConfirmation(self.email_gateway)

        self.order_confirmation.send(
            user_id=USER_ID, order_id=ORDER_ID, payment_reference=PAYMENT_REFERENCE
        )

        self.email_gateway.send.assert_called_once()
