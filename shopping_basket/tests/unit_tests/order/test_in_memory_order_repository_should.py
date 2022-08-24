from unittest import TestCase
from unittest.mock import MagicMock

from constants import ORDER_ID, PAID_ORDER, PAYMENT_REFERENCE, UNPAID_ORDER

from shopping_basket.core.utilities import IdGenerator
from shopping_basket.order.infrastructure.in_memory_order_repository import InMemoryOrderRepository


class InMemoryOrderRepositoryShould(TestCase):
    def setUp(self) -> None:
        self.id_generator = MagicMock(IdGenerator)
        self.repository = InMemoryOrderRepository(id_generator=self.id_generator)

    def test_find_order_by_given_id(self):
        self.id_generator.next.return_value = "order-01"
        self.repository.add(order=UNPAID_ORDER, payment_reference=PAYMENT_REFERENCE)
        result = self.repository.find_order_by_id(order_id=ORDER_ID)

        self.assertEqual(PAID_ORDER, result)
