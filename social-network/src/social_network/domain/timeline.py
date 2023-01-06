from src.core.events import EventMixin
from src.core.value_objects import UserId
from src.social_network.domain.events import MessageWasPublished
from src.social_network.domain.model.message import Message
from src.social_network.domain.value_objects import PublishingTime


class Timeline(EventMixin):
    def __init__(self, user: UserId, messages: list[Message] = None):
        super().__init__()
        self.__user = user
        self.__messages = [] if messages is None else messages

    def messages(self) -> list[Message]:
        return self.__messages

    @property
    def user(self) -> UserId:
        return self.__user

    def __len__(self) -> int:
        return len(self.__messages)

    def publish_message(self, message: str, published_by: UserId):
        publishing_time = PublishingTime()
        self.__messages.append(Message(message=message, created_at=publishing_time))
        self._record_event(
            MessageWasPublished(
                message=message, publisher=published_by, created_at=publishing_time
            )
        )
