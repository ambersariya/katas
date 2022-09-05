from unittest import TestCase
from unittest.mock import MagicMock

from constants import PAYMENT_DETAILS, SHOPPING_BASKET_WITH_ONE_ITEM, UNPAID_ORDER, USER_ID

from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.core.messagebus import MessageBus
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.payment_service import PaymentService


class PaymentServiceShould(TestCase):
    def setUp(self) -> None:
        self.payment_gateway = MagicMock(PaymentGateway)
        self.shopping_basket_service = MagicMock(ShoppingBasketService)
        self.payment_service = PaymentService(
            shopping_basket_service=self.shopping_basket_service,
            payment_gateway=self.payment_gateway,
        )

    def test_make_payment_for_given_shopping_basket(self):
        self.shopping_basket_service.basket_for.return_value = SHOPPING_BASKET_WITH_ONE_ITEM

        self.payment_service.make_payment(
            user_id=USER_ID,
            payment_details=PAYMENT_DETAILS,
        )

        self.payment_gateway.pay.assert_called_once_with(
            order=UNPAID_ORDER, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )