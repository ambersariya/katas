from unittest import TestCase

from constants import USER_ID
from shopping_basket.basket.shopping_basket_id import ShoppingBasketId
from shopping_basket.payment.payment_details import PaymentDetails
from shopping_basket.payment.payment_service import PaymentService


class MakePaymentForBasketShould(TestCase):
    def setUp(self) -> None:
        self.payment_service = PaymentService()

    def test_be_successful(self):
        shopping_basket_id = ShoppingBasketId('sdsdsds')
        payment_details = PaymentDetails()

        self.payment_service.make_payment(
            user_id=USER_ID,
            shopping_basket_id=shopping_basket_id,
            payment_details=payment_details
        )
