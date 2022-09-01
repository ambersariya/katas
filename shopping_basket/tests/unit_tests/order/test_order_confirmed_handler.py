from unittest import TestCase
from unittest.mock import MagicMock

from constants import ORDER_ID, SHOPPING_BASKET_WITH_ONE_ITEM, PAYMENT_REFERENCE
from shopping_basket.order.handler import OrderConfirmedHandler
from shopping_basket.order.notification.order_confirmation import OrderConfirmation
from shopping_basket.payment.event import OrderConfirmed


class OrderConfirmedHandlerShould(TestCase):
    def test_send_email_when_order_is_confirmed(self):
        self.order_confirmation = MagicMock(OrderConfirmation)
        self.order_confirmed_handler = OrderConfirmedHandler(self.order_confirmation)
        self.order_confirmed_handler.handle(
            event=OrderConfirmed(
                order_id=ORDER_ID,
                shopping_basket=SHOPPING_BASKET_WITH_ONE_ITEM,
                payment_reference=PAYMENT_REFERENCE,
            )
        )

        self.order_confirmation.send.assert_called_once()
