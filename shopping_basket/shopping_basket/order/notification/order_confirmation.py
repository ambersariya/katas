from shopping_basket.core.value_objects import UserId
from shopping_basket.core.email_gateway import EmailGateway
from shopping_basket.order.order_id import OrderId
from shopping_basket.payment.payment_reference import PaymentReference


class OrderConfirmation:
    def __init__(self, email_gateway: EmailGateway):
        self._email_gateway = email_gateway
        print("order confirmation happened")

    def send(self, user_id: UserId, order_id: OrderId, payment_reference: PaymentReference) -> None:
        self._email_gateway.send()
