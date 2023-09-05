from src.core.command import CommandHandler
from src.social_network.application.commands.publish_message_command import (
    PublishMessageCommand,
)
from src.social_network.domain.timeline_repository import TimelineRepository


class PublishMessageCommandHandler(CommandHandler):
    def __init__(self, timeline_repository: TimelineRepository):
        self.__timeline_repository = timeline_repository

    def __call__(self, command: PublishMessageCommand):
        timeline = self.__timeline_repository.fetch_timeline(user=command.timeline_user)
        timeline.publish_message(
            message=command.message, published_by=command.publisher
        )
        self.__timeline_repository.add(timeline)
