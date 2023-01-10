from typing import List

from pydantic import BaseModel

from src.social_network.application.queries.fetch_timeline_query import (
    FetchTimelineQuery,
    FetchTimelineQueryHandler,
)
from src.social_network.domain.timeline_repository import TimelineRepository


class MessageResponse(BaseModel):
    message: str
    created_at: str


class TimelineResponse(BaseModel):
    user: str
    messages: List[MessageResponse]


class InMemoryFetchTimelineQueryHandler(FetchTimelineQueryHandler):
    def __init__(self, timeline_repository: TimelineRepository) -> None:
        self.__timeline_repository = timeline_repository

    def __call__(self, query: FetchTimelineQuery) -> TimelineResponse:
        print(query)
        timeline_for_user = self.__timeline_repository.fetch_timeline(user=query.timeline_user)
        messages = [
            MessageResponse(
                message=message.message, created_at=message.created_at.isoformat())
            for message in timeline_for_user.messages()
        ]
        return TimelineResponse(user=timeline_for_user.user, messages=messages)
