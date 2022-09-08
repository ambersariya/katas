from typing import Protocol


class EmailGateway(Protocol):
    def send(self) -> None:
        pass
