from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.basket.user import UserId
from shopping_basket.core.messagebus import MessageBus
from shopping_basket.order.order import UnpaidOrder
from shopping_basket.payment.event import PaymentCompleted
from shopping_basket.payment.infrastructure.payment_gateway import PaymentGateway
from shopping_basket.payment.payment_details import PaymentDetails


class PaymentService:
    def __init__(
        self,
        shopping_basket_service: ShoppingBasketService,
        payment_gateway: PaymentGateway,
        message_bus: MessageBus,
    ):
        self.message_bus = message_bus
        self.payment_gateway = payment_gateway
        self.shopping_basket_service = shopping_basket_service

    def make_payment(self, user_id: UserId, payment_details: PaymentDetails) -> None:
        basket = self.shopping_basket_service.basket_for(user_id=user_id)
        self.payment_gateway.pay(
            order=UnpaidOrder.from_shopping_basket(basket=basket),
            user_id=user_id,
            payment_details=payment_details,
        )
        self.message_bus.handle(PaymentCompleted(items=basket.items))
