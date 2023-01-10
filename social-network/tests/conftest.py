import pytest
from pymessagebus import CommandBus as PyCommandBus, MessageBus
from pymessagebus import MessageBus as PyEventBus

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
)
from src.social_network.domain.events import MessageWasPublished
from src.social_network.infrastructure.queries.in_memory_fetch_timeline_query_handler import (
    InMemoryFetchTimelineQueryHandler,
)
from src.social_network.infrastructure.repositories.in_memory_timeline_repository import (
    InMemoryTimelineRepository,
)


@pytest.fixture()
def publish_message_handler(in_memory_timeline_repository):
    return PublishMessageCommandHandler(
        timeline_repository=in_memory_timeline_repository
    )


@pytest.fixture()
def in_memory_timeline_repository(event_bus):
    return InMemoryTimelineRepository(event_bus)


@pytest.fixture()
def command_handlers(publish_message_handler) -> dict:
    return {
        PublishMessageCommand: publish_message_handler,
    }


@pytest.fixture()
def query_handlers(fetch_timeline_handler) -> dict:
    return {
        FetchTimelineQuery: fetch_timeline_handler,
    }


@pytest.fixture()
def fetch_timeline_handler(in_memory_timeline_repository):
    return InMemoryFetchTimelineQueryHandler(
        timeline_repository=in_memory_timeline_repository
    )


@pytest.fixture()
def message_was_published_handler() -> MessageWasPublishedHandler:
    return MessageWasPublishedHandler()


@pytest.fixture()
def event_handlers(message_was_published_handler) -> dict:
    return {
        # event: [handlers]
        MessageWasPublished: [message_was_published_handler]
    }


@pytest.fixture()
def pycommandbus() -> PyCommandBus:
    return PyCommandBus()


@pytest.fixture()
def command_bus(command_handlers: dict, pycommandbus: PyCommandBus) -> CommandBus:
    return CommandBus(handlers=command_handlers, message_command_bus=pycommandbus)


@pytest.fixture()
def pyquerybus() -> MessageBus:
    return MessageBus()


@pytest.fixture()
def query_bus(query_handlers: dict, pyquerybus) -> QueryBus:
    return QueryBus(handlers=query_handlers, message_query_bus=pyquerybus)


@pytest.fixture()
def py_event_bus():
    return PyEventBus()


@pytest.fixture()
def event_bus(event_handlers, py_event_bus):
    return EventBus(handlers=event_handlers, message_event_bus=py_event_bus)
