import pytest

from constants import USER_ID, PAYMENT_REFERENCE, PAYMENT_DETAILS, PRODUCT_ID_HOBBIT, \
    PRODUCT_ID_BREAKING_BAD


class TestNotifyPurchaseSystemAboutLowStock:

    @pytest.mark.usefixtures('initialize_handlers')
    def test_be_successful(self, shopping_basket_service, payment_provider,
                           payment_service, unpaid_order, stock_repository, order_repository):
        shopping_basket_service.add_item(user_id=USER_ID,
                                         product_id=PRODUCT_ID_HOBBIT,
                                         quantity=4)
        shopping_basket_service.add_item(user_id=USER_ID,
                                         product_id=PRODUCT_ID_BREAKING_BAD,
                                         quantity=5)

        payment_provider.pay.return_value = PAYMENT_REFERENCE

        payment_service.make_payment(user_id=USER_ID, payment_details=PAYMENT_DETAILS)

        payment_provider.pay.assert_called_once_with(
            order=unpaid_order, user_id=USER_ID, payment_details=PAYMENT_DETAILS
        )
        stock = stock_repository.find_by_id(product_id=PRODUCT_ID_HOBBIT)
        assert len(order_repository) == 1
        assert stock.available == 5
        assert stock.reserved == 0
