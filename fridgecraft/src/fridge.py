import datetime
from enum import Enum

from fridgecraft.src.item import Item


class FridgeState(Enum):
    OPENED = 'door_opened'
    CLOSED = 'door_closed'


class Fridge:
    def __init__(self):
        self._items = []
        self._state = FridgeState.CLOSED
        self._current_time = None

    def signal_fridge_door_opened(self):
        self._state = FridgeState.OPENED

    def show_display(self):
        pass

    def scan_added_item(self, name: str, expiry: str, condition: str):
        self._ensure_fridge_opened()
        self._items.append(Item(name=name, expiry=expiry, condition=condition))

    def scan_removed_item(self, name: str):
        self._ensure_fridge_opened()

    def _ensure_fridge_opened(self):
        if self._state != FridgeState.OPENED:
            raise self.CannotAddItem()

    def signal_fridge_door_closed(self):
        pass

    def set_current_date(self, date: str):
        self._current_time = datetime.datetime.strptime(date, '%d/%m/%y')

    def simulate_day_over(self):
        self._current_time = self._current_time + datetime.timedelta(days=1)

    class CannotAddItem(Exception):
        pass
