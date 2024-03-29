from datetime import datetime
from unittest.mock import patch

from src.core.value_objects import UserId
from src.social_network.application.commands.publish_message_command import (
    PublishMessageCommand,
)
from src.social_network.application.queries.fetch_timeline_query import (
    FetchTimelineQuery,
)
from src.social_network.infrastructure.queries.in_memory_fetch_timeline_query_handler import \
    TimelineResponse, MessageResponse

MESSAGE = "functional programming is awesome"
USER_ID = UserId("alice")
PUBLISH_MESSAGE_COMMAND = PublishMessageCommand(
    message=MESSAGE, publisher=USER_ID, timeline_user=USER_ID
)
FETCH_TIMELINE_QUERY = FetchTimelineQuery(timeline_user=USER_ID)
PUBLISHING_TIME = datetime(2020, 12, 21, 12, 19)
TIMELINE_MESSAGE = MessageResponse(message=MESSAGE, created_at='2020-12-21T12:19:00')


@patch("src.social_network.domain.timeline.PublishingTime")
def test_should_publish_messages_to_personal_timeline(
    mocked_publishing_time, command_bus, query_bus
):
    mocked_publishing_time.return_value = PUBLISHING_TIME

    expected_messages = [TIMELINE_MESSAGE]
    command_bus.dispatch(PUBLISH_MESSAGE_COMMAND)
    timeline = query_bus.dispatch(FETCH_TIMELINE_QUERY)

    assert isinstance(timeline, TimelineResponse)
    assert timeline.messages == expected_messages
