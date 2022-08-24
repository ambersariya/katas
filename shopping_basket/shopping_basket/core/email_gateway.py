from typing import Protocol


class EmailGateway(Protocol):
    def send(self):
        pass
