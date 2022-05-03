import datetime
from enum import Enum
from typing import Optional

from fridgecraft.src.item import Item


class FridgeState(Enum):
    DOOR_OPENED = 'door_opened'
    DOOR_CLOSED = 'door_closed'


class Fridge:
    def __init__(self):
        self._items = []
        self._state = FridgeState.DOOR_CLOSED
        self._current_time = None

    def signal_fridge_door_opened(self):
        self._state = FridgeState.DOOR_OPENED

    def show_display(self) -> Optional[str]:
        if len(self._items) == 0:
            return None
        item_status_lines = []
        for item in self._items:
            date_time_obj = datetime.datetime.strptime(item.expiry, '%d/%m/%y')
            days_remaining_detla = date_time_obj - self._current_time
            days_remaining = days_remaining_detla.days
            if days_remaining < 0:
                item_status_lines.append(f"EXPIRED: {item.name}")
            else:
                item_status_lines.append(f"{item.name}: {self.pluralise_day_statement(days_remaining)} remaining")
        return "\n".join(item_status_lines)

    def scan_added_item(self, name: str, expiry: str, condition: str):
        self._ensure_fridge_opened()
        self._items.append(Item(name=name, expiry=expiry, condition=condition))

    def scan_removed_item(self, name: str):
        self._ensure_fridge_opened()
        for item in self._items:
            if item.name == name:
                return self._items.remove(item)
        raise self.CannotRemoveItem

    def _ensure_fridge_opened(self):
        if self._state != FridgeState.DOOR_OPENED:
            raise self.DoorClosed()

    def signal_fridge_door_closed(self):
        self._state = FridgeState.DOOR_CLOSED

    def set_current_date(self, date: str):
        self._current_time = datetime.datetime.strptime(date, '%d/%m/%y')

    def simulate_day_over(self):
        self._current_time = self._current_time + datetime.timedelta(days=1)

    class CannotAddItem(Exception):
        pass

    class DoorClosed(Exception):
        pass

    class CannotRemoveItem(Exception):
        pass

    @staticmethod
    def pluralise_day_statement(remaining_days: int):
        return f"{remaining_days} day{'s' if remaining_days >= 0 and remaining_days != 1 else ''}"
