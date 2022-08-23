from typing import Protocol


class Event(Protocol):
    @staticmethod
    def name() -> str:
        pass


class EventListener(Protocol):
    def handle(self, event: Event) -> None:
        pass
