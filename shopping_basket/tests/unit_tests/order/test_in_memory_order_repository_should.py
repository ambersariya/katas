from tests.constants import ORDER_ID, PAID_ORDER, PAYMENT_REFERENCE, UNPAID_ORDER


class TestInMemoryOrderRepositoryShould:
    def test_find_order_by_given_id(self, mocked_id_generator, order_repository):
        mocked_id_generator.next.return_value = "order-01"
        order_repository.add(order=UNPAID_ORDER, payment_reference=PAYMENT_REFERENCE)
        result = order_repository.find_order_by_id(order_id=ORDER_ID)

        assert PAID_ORDER == result
