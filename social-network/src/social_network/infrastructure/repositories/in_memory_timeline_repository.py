from src.core.events import EventBus
from src.core.value_objects import UserId
from src.social_network.domain.timeline import Timeline
from src.social_network.domain.timeline_repository import TimelineRepository


class InMemoryTimelineRepository(TimelineRepository):
    def __init__(self, event_bus: EventBus):
        self.__event_bus = event_bus
        self.__timelines: dict[str, Timeline] = {}

    def fetch_timeline(self, user: UserId) -> Timeline:
        if user in self.__timelines:
            return self.__timelines[user]
        return Timeline(user=user, messages=[])

    def add(self, timeline: Timeline) -> None:
        self.__timelines[timeline.user] = timeline
        self.__emit_events(timeline.domain_events)
        timeline.clear_events()

    def __emit_events(self, events: list) -> None:
        for event in events:
            self.__event_bus.dispatch(event=event)
