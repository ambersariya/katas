from typing import Callable, Dict, List, Type

from shopping_basket.core.event import Event


class NoEventHandlersError(Exception):
    pass


def handle(event: Event):
    if len(HANDLERS) == 0:
        raise NoEventHandlersError()
    for handler in HANDLERS[type(event)]:
        handler(event)


HANDLERS: Dict[Type[Event], List[Callable]] = {}
