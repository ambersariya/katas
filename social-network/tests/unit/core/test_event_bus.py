from src.core.events import Event


def test_should_dispatch_event_to_handlers(event_bus, mocked_event_bus):
    event = Event()
    event_bus.dispatch(event=event)
    mocked_event_bus.handle.assert_called_once_with(event)
