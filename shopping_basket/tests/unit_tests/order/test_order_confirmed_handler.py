from unittest import TestCase, mock
from unittest.mock import MagicMock

from tests.constants import ORDER_ID, SHOPPING_BASKET_WITH_ONE_ITEM, PAYMENT_REFERENCE
from shopping_basket.order.handler import OrderConfirmedHandler
from shopping_basket.order.notification.order_confirmation import OrderConfirmation
from shopping_basket.payment.event import OrderConfirmed


class TestOrderConfirmedHandlerShould:
    def test_send_email_when_order_is_confirmed(self, mocked_order_confirmation) -> None:
        self.order_confirmed_handler = OrderConfirmedHandler(mocked_order_confirmation)
        self.order_confirmed_handler(
            event=OrderConfirmed(
                order_id=ORDER_ID,
                shopping_basket=SHOPPING_BASKET_WITH_ONE_ITEM,
                payment_reference=PAYMENT_REFERENCE,
            )
        )

        mocked_order_confirmation.send.assert_called_once()
