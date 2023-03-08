from core.value_objects import UserId
from shopping_basket.core.messagebus import handle
from shopping_basket.order.order import Order
from shopping_basket.order.order_repository import OrderRepository
from shopping_basket.payment.event import OrderConfirmed
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider
from shopping_basket.payment.payment_details import PaymentDetails


class PaymentGateway:
    def __init__(self, payment_provider: PaymentProvider, order_repository: OrderRepository):
        self.order_repository = order_repository
        self.payment_provider = payment_provider

    def pay(self, order: Order, user_id: UserId, payment_details: PaymentDetails) -> None:
        reference = self.payment_provider.pay(
            order=order, user_id=user_id, payment_details=payment_details
        )

        order_id = self.order_repository.add(order=order, payment_reference=reference)
        handle(
            OrderConfirmed(
                order_id=order_id,
                shopping_basket=order.shopping_basket,
                payment_reference=reference,
            )
        )
