from acceptance_tests.base_test_case import BaseTestCase
from constants import USER_ID, PAYMENT_REFERENCE, PAYMENT_DETAILS
from shopping_basket.product.product_id import ProductId


class NotifyPurchaseSystemAboutLowStock(BaseTestCase):

    def test_be_successful(self):
        self._add_item(ProductId("10002"), 4)
        self._add_item(ProductId("20110"), 5)
        self.payment_provider.pay.return_value = PAYMENT_REFERENCE

        self.payment_service.make_payment(user_id=USER_ID, payment_details=PAYMENT_DETAILS)

        self.payment_provider.pay.assert_called_once_with(
            order=self._unpaid_order(), user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        stock = self.stock_repository.find_by_id(product_id=ProductId("10002"))
        self.assertEqual(1, len(self.order_repository))
        self.assertEqual(5, stock.available)
        self.assertEqual(0, stock.reserved)
