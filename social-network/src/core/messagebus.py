import abc
from typing import Any, Protocol


class Message(Protocol):
    pass


class MessageBus(Protocol):
    @abc.abstractmethod
    def dispatch(self, message: Message) -> Any:
        pass


class MessageHandler(Protocol):
    @abc.abstractmethod
    def __call__(self, message: Message) -> Any:
        raise NotImplementedError()
