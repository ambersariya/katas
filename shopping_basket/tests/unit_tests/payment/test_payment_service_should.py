from unittest import TestCase
from unittest.mock import MagicMock

from constants import SHOPPING_BASKET, USER_ID, UNPAID_ORDER, PAYMENT_DETAILS
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.core.messagebus import MessageBus
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.payment_service import PaymentService


class PaymentServiceShould(TestCase):
    def setUp(self) -> None:
        self.payment_gateway = MagicMock(PaymentGateway)
        self.message_bus = MagicMock(MessageBus)
        self.shopping_basket_service = MagicMock(ShoppingBasketService)
        self.payment_service = PaymentService(
            shopping_basket_service=self.shopping_basket_service,
            payment_gateway=self.payment_gateway,
            message_bus=self.message_bus
        )

    def test_make_payment_for_given_shopping_basket(self):
        self.shopping_basket_service.basket_for.return_value = SHOPPING_BASKET

        result = self.payment_service.make_payment(
            user_id=USER_ID,
            payment_details=PAYMENT_DETAILS,
        )

        self.assertIsNone(result)
        self.payment_gateway.pay.assert_called_once_with(
            order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        self.message_bus.handle.assert_called_once()
