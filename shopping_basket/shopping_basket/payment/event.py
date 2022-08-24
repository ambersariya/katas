from dataclasses import dataclass

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.core.event import Event
from shopping_basket.order.order_id import OrderId
from shopping_basket.payment.payment_reference import PaymentReference


@dataclass(init=True, frozen=True)
class OrderConfirmed(Event):
    order_id: OrderId
    shopping_basket: ShoppingBasket
    payment_reference: PaymentReference

    @staticmethod
    def name() -> str:
        return "OrderConfirmed"
