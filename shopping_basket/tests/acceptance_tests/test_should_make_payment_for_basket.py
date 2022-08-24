from acceptance_tests.base_test_case import BaseTestCase
from constants import USER_ID, PAYMENT_REFERENCE, PAYMENT_DETAILS
from shopping_basket.payment.infrastructure.errors import PaymentError
from shopping_basket.product.product_id import ProductId


class MakePaymentForBasketShould(BaseTestCase):

    def test_be_successful(self):
        self._add_item(ProductId("10002"), 4)
        self._add_item(ProductId("20110"), 5)
        self.payment_provider.pay.return_value = PAYMENT_REFERENCE

        self.payment_service.make_payment(user_id=USER_ID, payment_details=PAYMENT_DETAILS)

        self.payment_provider.pay.assert_called_once_with(
            order=self._unpaid_order(), user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        self.assertEqual(1, len(self.order_repository))

    def test_raise_exception_when_making_payment(self):
        self.payment_provider.pay.side_effect = PaymentError()
        self._add_item(ProductId("10002"), 4)
        self._add_item(ProductId("20110"), 5)

        with self.assertRaises(PaymentError):
            self.payment_service.make_payment(user_id=USER_ID, payment_details=PAYMENT_DETAILS)


