from shopping_basket.basket.user import UserId
from shopping_basket.core.email_gateway import EmailGateway
from shopping_basket.order.order_id import OrderId
from shopping_basket.payment.payment_reference import PaymentReference


class OrderConfirmation:

    def __init__(self, email_gateway: EmailGateway):
        self.email_gateway = email_gateway

    def send(self, user_id: UserId, order_id: OrderId, payment_reference: PaymentReference):
        raise NotImplementedError()
