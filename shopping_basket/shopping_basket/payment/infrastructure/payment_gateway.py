from shopping_basket.basket.user import UserId
from shopping_basket.order.order import Order
from shopping_basket.payment.infrastructure.payment_provider import PaymentProvider
from shopping_basket.payment.payment_details import PaymentDetails


class PaymentGateway:
    def __init__(self, payment_provider: PaymentProvider):
        self.payment_provider = payment_provider

    def pay(self, order: Order, user_id: UserId, payment_details: PaymentDetails) -> None:
        raise NotImplementedError()
