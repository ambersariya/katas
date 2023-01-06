from datetime import datetime
from unittest.mock import patch

from src.core.value_objects import UserId
from src.social_network.domain.timeline import Timeline

USER_ID = UserId("alice")
PUBLISHING_TIME = datetime(2020, 12, 21, 12, 19)
PUSHED_TIMELINE = Timeline(user=USER_ID)
PUSHED_TIMELINE.publish_message(message="some message", published_by=USER_ID)


def test_should_fetch_empty_timeline_for_user_when_no_messages_exist(
    in_memory_timeline_repository,
):
    user_dto = UserId("alice")
    timeline = in_memory_timeline_repository.fetch_timeline(user=user_dto)
    assert len(timeline) == 0


@patch("src.social_network.domain.timeline.PublishingTime")
def test_should_add_message_to_timeline(
    mocked_publishing_time, in_memory_timeline_repository, fake_event_bus
):
    mocked_publishing_time.return_value = PUBLISHING_TIME

    in_memory_timeline_repository.add(PUSHED_TIMELINE)
    timeline = in_memory_timeline_repository.fetch_timeline(user=USER_ID)

    assert len(timeline) == 1
    assert len(timeline.domain_events) == 1
    assert USER_ID == timeline.user
    fake_event_bus.dispatch.assert_called_once()
