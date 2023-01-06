from abc import abstractmethod
from typing import Protocol

from src.core.value_objects import UserId
from src.social_network.domain.timeline import Timeline


class TimelineRepository(Protocol):
    @abstractmethod
    def add(self, timeline: Timeline) -> None:
        pass

    @abstractmethod
    def fetch_timeline(self, user: UserId) -> Timeline:
        pass
