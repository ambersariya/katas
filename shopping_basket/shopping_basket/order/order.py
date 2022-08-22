from abc import ABC
from dataclasses import dataclass
from typing import Protocol

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.user import UserId
from shopping_basket.order.order_id import OrderId


class Order(Protocol):
    pass


@dataclass(init=True)
class UnpaidOrder:
    user_id: UserId
    shopping_basket: ShoppingBasket

    @staticmethod
    def from_shopping_basket(basket: ShoppingBasket) -> "UnpaidOrder":
        return UnpaidOrder(
            shopping_basket=basket,
            user_id=basket.user_id,
        )


@dataclass(init=True)
class PaidOrder(UnpaidOrder):
    order_id: OrderId
    user_id: UserId
    shopping_basket: ShoppingBasket

    @staticmethod
    def from_unpaid_order(order: UnpaidOrder, order_id: OrderId) -> "PaidOrder":
        return PaidOrder(
            order_id=order_id,
            shopping_basket=order.shopping_basket,
            user_id=order.user_id
        )
