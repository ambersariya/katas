import dataclasses
from typing import Protocol

from src.core.query import Query, QueryHandler
from src.core.value_objects import UserId


@dataclasses.dataclass(init=True, frozen=True)
class FetchTimelineQuery(Query):
    timeline_user: UserId


class FetchTimelineQueryHandler(QueryHandler, Protocol):
    pass
