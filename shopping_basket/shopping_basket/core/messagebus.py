from typing import Dict, List

from shopping_basket.core.event import Event


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
