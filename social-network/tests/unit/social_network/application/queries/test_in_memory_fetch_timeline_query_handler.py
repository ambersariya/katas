from datetime import datetime

from src.core.value_objects import UserId
from src.social_network.application.queries.fetch_timeline_query import (
    FetchTimelineQuery,
)
from src.social_network.domain.model.message import Message
from src.social_network.domain.timeline import Timeline
from src.social_network.infrastructure.queries.in_memory_fetch_timeline_query_handler import (
    InMemoryFetchTimelineQueryHandler,
)

USER_ID = UserId("alice")
USER_ID_BOB = UserId("bob")
QUERY = FetchTimelineQuery(timeline_user=USER_ID)
PUBLISHING_TIME = datetime(2020, 12, 21, 12, 19)
MESSAGE = Message(
    message="functional programming is awesome", created_at=PUBLISHING_TIME
)
TIMELINE_ALICE = Timeline(user=USER_ID, messages=[MESSAGE])
EMPTY_TIMELINE_BOB = Timeline(user=USER_ID_BOB, messages=[])


def test_should_return_timeline_with_published_messages(mock_timeline_repository):
    mock_timeline_repository.fetch_timeline.return_value = TIMELINE_ALICE
    handler = InMemoryFetchTimelineQueryHandler(
        timeline_repository=mock_timeline_repository
    )

    timeline = handler(query=QUERY)

    mock_timeline_repository.fetch_timeline.assert_called_once()
    assert len(timeline) == len(TIMELINE_ALICE)
    assert timeline.messages() == TIMELINE_ALICE.messages()


def test_should_return_empty_timeline_when_user_timeline_has_no_messages(
    mock_timeline_repository,
):
    mock_timeline_repository.fetch_timeline.return_value = EMPTY_TIMELINE_BOB
    handler = InMemoryFetchTimelineQueryHandler(
        timeline_repository=mock_timeline_repository
    )

    timeline = handler(query=QUERY)
    assert len(timeline) == 0
    assert timeline.messages() == []
