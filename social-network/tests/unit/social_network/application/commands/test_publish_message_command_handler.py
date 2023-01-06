from src.core.value_objects import UserId
from src.social_network.application.commands.publish_message_command import (
    PublishMessageCommand,
)
from src.social_network.application.commands.publish_message_command_handler import (
    PublishMessageCommandHandler,
)
from src.social_network.domain.timeline import Timeline


MESSAGE = "functional programming is awesome"
USER = UserId("alice")
PUBLISH_MESSAGE_COMMAND = PublishMessageCommand(
    message=MESSAGE, publisher=USER, timeline_user=USER
)
ALICE_TIMELINE = Timeline(user=USER)


def test_should_successfully_publish_message_to_timeline(
    mock_timeline_repository, publish_message_handler: PublishMessageCommandHandler
):
    # Arrange
    mock_timeline_repository.fetch_timeline.return_value = ALICE_TIMELINE

    # Act
    publish_message_handler(command=PUBLISH_MESSAGE_COMMAND)

    # Assert
    assert len(ALICE_TIMELINE.domain_events) == 1
    mock_timeline_repository.add.assert_called_with(ALICE_TIMELINE)
