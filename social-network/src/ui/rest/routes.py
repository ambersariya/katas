from fastapi import APIRouter
from lagom.integrations.fast_api import FastApiIntegration
from starlette.status import HTTP_201_CREATED

from src.core.command import CommandBus
from src.core.value_objects import UserId
from src.main.container import container
from src.social_network.application.commands.publish_message_command import (
    PublishMessageCommand,
)

timeline = APIRouter()
deps = FastApiIntegration(container)


@timeline.post("/timelines/{user_id}/messages", status_code=HTTP_201_CREATED)
def timeline_publish_message(
    user_id: UserId,
    publish_message_command: PublishMessageCommand,
    command_bus=deps.depends(CommandBus),
):
    command_bus.dispatch(publish_message_command)
    return {}
