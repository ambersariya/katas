from abc import abstractmethod
from typing import Protocol

from pymessagebus import CommandBus as PyCommandBus

from src.core.messagebus import Message, MessageBus, MessageHandler


class Command(Message):
    pass


class CommandHandler(MessageHandler, Protocol):
    @abstractmethod
    def __call__(self, command: Command) -> None:
        raise NotImplementedError()


class CommandHandlerNotFound(RuntimeError):
    pass


class CommandBus(MessageBus):
    def __init__(self, handlers: dict, message_command_bus: PyCommandBus):
        self.__pycommandbus = message_command_bus
        self.__subscribe_handlers(handlers=handlers)

    def dispatch(self, command: Command) -> None:
        self.__pycommandbus.handle(command)

    def __subscribe_handlers(self, handlers: dict):
        for message_type, handler in handlers.items():
            self.__pycommandbus.add_handler(message_type, handler)
