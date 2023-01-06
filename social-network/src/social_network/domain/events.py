from dataclasses import dataclass

from src.core.events import Event
from src.core.value_objects import UserId
from src.social_network.domain.value_objects import PublishingTime


@dataclass(init=True)
class MessageWasPublished(Event):
    message: str
    publisher: UserId
    created_at: PublishingTime
