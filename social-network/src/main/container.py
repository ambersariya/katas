from typing import NewType

import pymessagebus
from lagom import Container, Singleton

from src.core.command import CommandBus
from src.core.events import EventBus
from src.core.query import QueryBus
from src.processes.logging_posted_message.message_was_published_handler import (
    MessageWasPublishedHandler,
)
from src.social_network.application.commands.publish_message_command import (
    PublishMessageCommand,
)
from src.social_network.application.commands.publish_message_command_handler import (
    PublishMessageCommandHandler,
)
from src.social_network.application.queries.fetch_timeline_query import (
    FetchTimelineQuery,
    FetchTimelineQueryHandler,
)
from src.social_network.domain.events import MessageWasPublished
from src.social_network.domain.timeline_repository import TimelineRepository
from src.social_network.infrastructure.queries.in_memory_fetch_timeline_query_handler import (
    InMemoryFetchTimelineQueryHandler,
)
from src.social_network.infrastructure.repositories.in_memory_timeline_repository import (
    InMemoryTimelineRepository,
)

CommandHandlers = NewType("CommandHandlers", dict)
QueryHandlers = NewType("QueryHandlers", dict)
EventHandlers = NewType("EventHandlers", dict)


class _PyCommandBus(pymessagebus.CommandBus):
    pass


class _PyEventBus(pymessagebus.MessageBus):
    pass


class _PyQueryBus(pymessagebus.MessageBus):
    pass


container = Container(log_undefined_deps=True)
# We need a specific url
container[CommandHandlers] = lambda c: {
    PublishMessageCommand: c[PublishMessageCommandHandler],
}
container[QueryHandlers] = lambda c: {
    FetchTimelineQuery: c[FetchTimelineQueryHandler],
}
container[EventHandlers] = lambda c: {
    MessageWasPublished: [c[MessageWasPublishedHandler]],
}

container[_PyCommandBus] = _PyCommandBus()
container[_PyEventBus] = _PyEventBus()
container[_PyQueryBus] = _PyQueryBus()

container[CommandBus] = Singleton(
    lambda c: CommandBus(
        handlers=c[CommandHandlers], message_command_bus=c[_PyCommandBus]
    )
)
container[QueryBus] = Singleton(
    lambda c: QueryBus(handlers=c[QueryHandlers], message_query_bus=c[_PyQueryBus])
)
container[EventBus] = Singleton(
    lambda c: EventBus(handlers=c[EventHandlers], message_event_bus=c[_PyEventBus])
)

container[TimelineRepository] = lambda c: InMemoryTimelineRepository(
    event_bus=c[EventBus]
)
container[PublishMessageCommandHandler] = lambda c: PublishMessageCommandHandler(
    timeline_repository=c[TimelineRepository]
)
container[FetchTimelineQueryHandler] = lambda c: InMemoryFetchTimelineQueryHandler(
    timeline_repository=c[TimelineRepository]
)
