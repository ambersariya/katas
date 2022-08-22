from typing import Protocol

from shopping_basket.basket.user import UserId
from shopping_basket.order.order import Order
from shopping_basket.payment.payment_details import PaymentDetails
from shopping_basket.payment.payment_reference import PaymentReference


class PaymentProvider(Protocol):
    def pay(
        self, order: Order, user_id: UserId, payment_details: PaymentDetails
    ) -> PaymentReference:
        pass
