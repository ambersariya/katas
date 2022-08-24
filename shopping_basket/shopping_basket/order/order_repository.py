from typing import Optional, Protocol

from shopping_basket.order.order import Order, UnpaidOrder
from shopping_basket.order.order_id import OrderId
from shopping_basket.payment.payment_reference import PaymentReference


class OrderRepository(Protocol):
    def add(self, order: UnpaidOrder, payment_reference: PaymentReference) -> OrderId:
        pass

    def find_order_by_id(self, order_id: OrderId) -> Optional[Order]:
        pass
