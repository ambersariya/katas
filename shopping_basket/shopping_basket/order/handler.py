from shopping_basket.order.notification.order_confirmation import OrderConfirmation
from shopping_basket.payment.event import OrderConfirmed


class OrderConfirmedHandler:
    def __init__(self, order_confirmation: OrderConfirmation):
        self.order_confirmation = order_confirmation

    def __call__(self, event: OrderConfirmed) -> None:
        self.order_confirmation.send(
            user_id=event.shopping_basket.user_id,
            order_id=event.order_id,
            payment_reference=event.payment_reference,
        )
