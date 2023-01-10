from __future__ import annotations

from dataclasses import dataclass

from src.social_network.domain.value_objects import PublishingTime


@dataclass(init=True)
class Message:
    message: str
    created_at: PublishingTime

    @classmethod
    def from_dto(cls, message: str) -> Message:
        _message = cls(message=message.message)
        return _message
