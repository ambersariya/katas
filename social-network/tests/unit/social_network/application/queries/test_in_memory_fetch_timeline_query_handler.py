from datetime import datetime

from src.core.value_objects import UserId
from src.social_network.application.queries.fetch_timeline_query import (
    FetchTimelineQuery,
)
from src.social_network.domain.model.message import Message
from src.social_network.domain.timeline import Timeline
from src.social_network.infrastructure.queries.in_memory_fetch_timeline_query_handler import (
    InMemoryFetchTimelineQueryHandler, TimelineResponse, MessageResponse, )

USER_ID = UserId("alice")
USER_ID_BOB = UserId("bob")
QUERY = FetchTimelineQuery(timeline_user=USER_ID)
PUBLISHING_TIME = datetime(2020, 12, 21, 12, 19, 00)
PUBLISHING_TIME_RESPONSE_STR = '2020-12-21T12:19:00'
MESSAGE = Message(
    message="functional programming is awesome", created_at=PUBLISHING_TIME
)
MESSAGE_RESPONSE = MessageResponse(
    message="functional programming is awesome", created_at=PUBLISHING_TIME_RESPONSE_STR
)
TIMELINE_ALICE = Timeline(user=USER_ID, messages=[MESSAGE])
TIMELINE_ALICE_RESPONSE = TimelineResponse(user=USER_ID, messages=[MESSAGE_RESPONSE])

EMPTY_TIMELINE_BOB = Timeline(user=USER_ID_BOB, messages=[])
EMPTY_TIMELINE_BOB_RESPONSE = TimelineResponse(user=USER_ID_BOB, messages=[])


def test_should_return_timeline_with_published_messages(mock_timeline_repository):
    mock_timeline_repository.fetch_timeline.return_value = TIMELINE_ALICE
    handler = InMemoryFetchTimelineQueryHandler(
        timeline_repository=mock_timeline_repository
    )

    timeline_response = handler(query=QUERY)

    mock_timeline_repository.fetch_timeline.assert_called_once()
    assert type(timeline_response) == TimelineResponse
    assert len(timeline_response.messages) == len(TIMELINE_ALICE_RESPONSE.messages)
    assert type(timeline_response.messages[0]) == MessageResponse
    assert timeline_response.messages == TIMELINE_ALICE_RESPONSE.messages


def test_should_return_empty_timeline_when_user_timeline_has_no_messages(
    mock_timeline_repository,
):
    mock_timeline_repository.fetch_timeline.return_value = EMPTY_TIMELINE_BOB
    handler = InMemoryFetchTimelineQueryHandler(
        timeline_repository=mock_timeline_repository
    )

    timeline_response = handler(query=QUERY)
    assert type(timeline_response) == TimelineResponse
    assert len(timeline_response.messages) == 0
    assert timeline_response.messages == []
