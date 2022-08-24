from unittest import TestCase
from unittest.mock import MagicMock

from constants import PAYMENT_DETAILS, PAYMENT_REFERENCE, UNPAID_ORDER, USER_ID
from shopping_basket.core.messagebus import MessageBus

from shopping_basket.order.order_repository import OrderRepository
from shopping_basket.payment.infrastructure.errors import PaymentError
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider


class PaymentGatewayShould(TestCase):
    def setUp(self) -> None:
        self.payment_provider = MagicMock(PaymentProvider)
        self.order_repository = MagicMock(OrderRepository)
        self.message_bus = MagicMock(MessageBus)
        self.payment_gateway = PaymentGateway(
            payment_provider=self.payment_provider,
            order_repository=self.order_repository,
            message_bus=self.message_bus
        )

    def test_raise_exception_for_unpaid_order(self):
        self.payment_provider.pay.side_effect = PaymentError()

        with self.assertRaises(PaymentError):
            self.payment_gateway.pay(
                order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
            )

    def test_make_payment_successfully_for_unpaid_order(self):
        self.payment_provider.pay.return_value = PAYMENT_REFERENCE
        self.payment_gateway.pay(
            order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        self.payment_provider.pay.assert_called_once_with(
            order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        self.order_repository.add.assert_called_once_with(
            order=UNPAID_ORDER, payment_reference=PAYMENT_REFERENCE
        )
        self.message_bus.handle.assert_called_once()
