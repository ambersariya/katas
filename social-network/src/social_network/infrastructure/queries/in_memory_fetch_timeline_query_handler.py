from src.social_network.application.queries.fetch_timeline_query import (
    FetchTimelineQuery,
    FetchTimelineQueryHandler,
)
from src.social_network.domain.timeline import Timeline
from src.social_network.domain.timeline_repository import TimelineRepository


class InMemoryFetchTimelineQueryHandler(FetchTimelineQueryHandler):
    def __init__(self, timeline_repository: TimelineRepository) -> None:
        self.__timeline_repository = timeline_repository

    def __call__(self, query: FetchTimelineQuery) -> Timeline:
        print(query)
        return self.__timeline_repository.fetch_timeline(user=query.timeline_user)
