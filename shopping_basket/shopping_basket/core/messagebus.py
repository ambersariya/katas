from typing import List, Dict

from shopping_basket.core.event import Event, EventListener


class MessageBus:
    def __init__(self) -> None:
        self._handlers: Dict[str, List[EventListener]] = {}

    def add_handler(self, event: Event, listener: EventListener) -> None:
        event_name = event.name()
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(listener)

    def handle(self, event: Event) -> None:
        event_name = event.name()
        for handler in self._handlers[event_name]:
            handler.handle(event)
