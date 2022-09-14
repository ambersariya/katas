from typing import Protocol


class EmailGateway(Protocol):
    def send(self) -> None:
        pass


class FakeEmailGateway(EmailGateway):
    def send(self) -> None:
        pass
