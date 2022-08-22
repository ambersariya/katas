from typing import Protocol

from shopping_basket.order.order import UnpaidOrder
from shopping_basket.payment.payment_reference import PaymentReference


class OrderRepository(Protocol):
    def add(self, order: UnpaidOrder, payment_reference: PaymentReference) -> None:
        pass
