from abc import abstractmethod
from typing import Any, Protocol

from pymessagebus import MessageBus as PyMessageBus

from src.core.messagebus import Message, MessageBus, MessageHandler


class Query(Message):
    pass


class QueryBus(MessageBus):
    def __init__(self, handlers: dict, message_query_bus: PyMessageBus):
        self.__message_query_bus = message_query_bus
        self.__subscribe_handlers(handlers=handlers)

    def dispatch(self, query: Query) -> Any:
        if not self.__message_query_bus.has_handler_for(type(query)):
            raise QueryHandlerNotFound()
        results = self.__message_query_bus.handle(query)
        return results.pop()

    def __subscribe_handlers(self, handlers: dict):
        for message_type, handler in handlers.items():
            self.__message_query_bus.add_handler(message_type, handler)


class QueryHandlerNotFound(RuntimeError):
    pass


class QueryHandler(MessageHandler, Protocol):
    @abstractmethod
    def __call__(self, query: Query) -> Any:
        raise NotImplementedError()
