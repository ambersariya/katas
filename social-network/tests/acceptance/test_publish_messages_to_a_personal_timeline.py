from typing import List


def publish_message_usecase():
    pass


def fetch_timeline_usecase():
    pass


class Message:
    pass


class Timeline:
    def all(self) -> List[Message]:
        pass


def test_publish_messages_to_a_personal_timeline():
    message = 'functional programming is awesome'
    username = 'Alice'
    expected_messages = []

    publish_message_usecase.publish_message(message)
    timeline = fetch_timeline_usecase.fetch_timeline(username=username)

    assert isinstance(timeline, Timeline)
    assert timeline.all() == expected_messages
