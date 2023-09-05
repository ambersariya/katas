from unittest.mock import MagicMock

import pytest
from pymessagebus import MessageBus, CommandBus

from src.core.command import Command, CommandHandler
from src.core.events import EventBus, EventHandler, Event
from src.core.query import Query, QueryHandler
from src.social_network.application.commands.publish_message_command_handler import (
    PublishMessageCommandHandler,
)
from src.social_network.application.queries.fetch_timeline_query import (
    FetchTimelineQueryHandler,
)
from src.social_network.domain.timeline_repository import TimelineRepository
from src.social_network.infrastructure.repositories.in_memory_timeline_repository import (
    InMemoryTimelineRepository,
)


class FakeCommand(Command):
    pass


class FakeQuery(Query):
    pass


@pytest.fixture()
def publish_message_handler(mock_timeline_repository):
    return PublishMessageCommandHandler(mock_timeline_repository)


@pytest.fixture()
def mock_timeline_repository():
    return MagicMock(TimelineRepository)


@pytest.fixture()
def fake_command():
    return FakeCommand()


@pytest.fixture()
def fake_command_handler(mocker):
    return mocker.MagicMock(spec_set=CommandHandler)


@pytest.fixture()
def fake_wrong_command(mocker):
    return mocker.MagicMock(spec_set=FakeCommand)


@pytest.fixture()
def fake_wrong_command_handler(mocker):
    return mocker.MagicMock(spec_set=CommandHandler)


@pytest.fixture()
def command_handlers(
    fake_command, fake_command_handler, fake_wrong_command, fake_wrong_command_handler
):
    return {
        type(fake_command): fake_command_handler,
        type(fake_wrong_command): fake_wrong_command_handler,
    }


@pytest.fixture()
def event_handler_1(mocker):
    return mocker.MagicMock(EventHandler)


@pytest.fixture()
def event_handler_2(mocker):
    return mocker.MagicMock(EventHandler)


@pytest.fixture()
def wrong_event_handler(mocker):
    return mocker.MagicMock(EventHandler)


@pytest.fixture()
def event_handlers(event_handler_1, event_handler_2) -> dict:
    return {
        Event: [event_handler_1, event_handler_2],
    }


@pytest.fixture()
def fake_query():
    return FakeQuery()


@pytest.fixture()
def fake_query_handler(mocker):
    return mocker.MagicMock(spec_set=QueryHandler)


@pytest.fixture()
def fake_wrong_query_handler(mocker):
    return mocker.MagicMock(spec_set=QueryHandler)


@pytest.fixture()
def query_handlers(fake_query_handler, fake_wrong_query_handler) -> dict:
    return {FakeQuery: fake_query_handler, Query: fake_wrong_query_handler}


@pytest.fixture()
def fetch_timeline_handler(mocker):
    return mocker.MagicMock(FetchTimelineQueryHandler)


@pytest.fixture()
def mocked_event_bus(mocker):
    return mocker.Mock(spec_set=MessageBus)


@pytest.fixture()
def event_bus(mocked_event_bus, event_handlers):
    return EventBus(handlers=event_handlers, message_event_bus=mocked_event_bus)


@pytest.fixture()
def fake_event_bus(mocker):
    return mocker.Mock(spec_set=EventBus)


@pytest.fixture()
def pyquerybus(mocker) -> MessageBus:
    return mocker.Mock(spec_set=MessageBus)


@pytest.fixture()
def pycommandbus(mocker) -> CommandBus:
    return mocker.Mock(spec_set=CommandBus)


@pytest.fixture()
def in_memory_timeline_repository(fake_event_bus):
    return InMemoryTimelineRepository(fake_event_bus)
