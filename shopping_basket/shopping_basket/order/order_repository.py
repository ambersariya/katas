from typing import Protocol, Optional

from shopping_basket.order.order import UnpaidOrder, Order
from shopping_basket.order.order_id import OrderId
from shopping_basket.payment.payment_reference import PaymentReference


class OrderRepository(Protocol):
    def add(self, order: UnpaidOrder, payment_reference: PaymentReference) -> None:
        pass

    def find_order_by_id(self, order_id: OrderId) -> Optional[Order]:
        pass
