from abc import abstractmethod
from typing import List, Protocol

from pymessagebus import MessageBus as PyMessageBus

from src.core.messagebus import Message, MessageBus, MessageHandler


class Event(Message):
    pass


class EventMixin:
    def __init__(self) -> None:
        self.__pending_domain_events: List[Event] = []

    def _record_event(self, event: Event) -> None:
        self.__pending_domain_events.append(event)

    @property
    def domain_events(self) -> List[Event]:
        return self.__pending_domain_events[:]

    def clear_events(self) -> None:
        self.__pending_domain_events.clear()


class EventHandlerNotFound(RuntimeError):
    pass


class EventBus(MessageBus):
    def __init__(self, handlers: dict, message_event_bus: PyMessageBus):
        self.__message_event_bus = message_event_bus
        self.__subscribe_handlers(handlers=handlers)

    def dispatch(self, event: Event) -> None:
        self.__message_event_bus.handle(event)

    def __subscribe_handlers(self, handlers: dict):
        for event_type, event_handlers in handlers.items():
            for event_handler in event_handlers:
                self.__message_event_bus.add_handler(event_type, event_handler)


class EventHandler(MessageHandler, Protocol):
    @abstractmethod
    def __call__(self, event: Event) -> None:
        raise NotImplementedError()
