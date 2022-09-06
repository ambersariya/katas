from typing import Dict, List

from shopping_basket.core.event import Event, EventHandler
from shopping_basket.payment.event import OrderConfirmed
from shopping_basket.stock.handler import StockPurchasedHandler


# class MessageBus:
#     def __init__(self) -> None:
#         self._handlers: Dict[str, List[EventHandler]] = {}
#
#     def add_handler(self, event_class: str, handler: EventHandler) -> None:
#         event_name = event_class
#         if event_name not in self._handlers:
#             self._handlers[event_name] = []
#         self._handlers[event_name].append(handler)
#
#     def handle(self, event: Event) -> None:
#         event_name = event.name()
#         for handler in self._handlers[event_name]:
#             handler.handle(event)


class NoEventHandlersError(Exception):
    pass


def handle(event: Event):
    if len(HANDLERS) == 0:
        raise NoEventHandlersError()
    for handler in HANDLERS[type(event)]:
        handler(event)


HANDLERS = {

}

# type: Dict[Type[events.Event], List[Callable]]
