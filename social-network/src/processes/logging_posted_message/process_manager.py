from src.core.events import Event


class ProcessManager:
    def __init__(self) -> None:
        pass

    def handle_message_was_published(self, event: Event):
        print(f"Event: {event}")
