from typing import Optional, Dict

from shopping_basket.core.utilities import IdGenerator
from shopping_basket.order.order import UnpaidOrder, Order, PaidOrder
from shopping_basket.order.order_id import OrderId
from shopping_basket.order.order_repository import OrderRepository
from shopping_basket.payment.payment_reference import PaymentReference


class InMemoryOrderRepository(OrderRepository):
    def __init__(self, id_generator: IdGenerator):
        self._orders: Dict[OrderId, PaidOrder] = {}
        self.id_generator = id_generator

    def add(self, order: UnpaidOrder, payment_reference: PaymentReference) -> None:
        order_id = OrderId(self.id_generator.next())
        self._orders[order_id] = PaidOrder(
            order_id=order_id,
            user_id=order.user_id,
            shopping_basket=order.shopping_basket
        )

    def find_order_by_id(self, order_id: OrderId) -> Optional[Order]:
        return self._orders[order_id]

    def __len__(self) -> int:
        return len(self._orders)
