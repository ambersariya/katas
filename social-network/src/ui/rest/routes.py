from fastapi import APIRouter
from lagom.integrations.fast_api import FastApiIntegration
from starlette.status import HTTP_201_CREATED

from src.core.command import CommandBus
from src.core.query import QueryBus
from src.core.value_objects import UserId
from src.main.container import container
from src.social_network.application.commands.publish_message_command import (
    PublishMessageCommand,
)
from src.social_network.application.queries.fetch_timeline_query import FetchTimelineQuery

timeline = APIRouter()
deps = FastApiIntegration(container)


@timeline.post("/timelines/{user_id}/messages", status_code=HTTP_201_CREATED)
def timeline_publish_message(
    user_id: UserId,
    publish_message_command: PublishMessageCommand,
    command_bus: CommandBus = deps.depends(CommandBus),
):
    command_bus.dispatch(publish_message_command)
    return {}


@timeline.get("/timelines/{user_id}/messages")
def fetch_timeline_for_user(user_id: UserId, query_bus=deps.depends(QueryBus)):
    fetch_timeline_query = FetchTimelineQuery(timeline_user=user_id)
    return query_bus.dispatch(fetch_timeline_query)
