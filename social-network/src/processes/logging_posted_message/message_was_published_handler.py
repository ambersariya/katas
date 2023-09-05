from src.core.events import Event, EventHandler


class MessageWasPublishedHandler(EventHandler):
    def __call__(self, event: Event) -> None:
        print(f"Event: {event}")
