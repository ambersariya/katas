import datetime
import unittest

from fridgecraft.src.fridge import Fridge, FridgeState
from fridgecraft.src.item import ItemCondition


class TestFridge(unittest.TestCase):
    def setUp(self) -> None:
        self.fridge = Fridge()
        self.fridge.set_current_date('18/10/21')

    def test_not_be_able_to_add_items_when_door_is_closed(self):
        with self.assertRaises(self.fridge.DoorClosed):
            self.fridge.scan_added_item(name='thing', expiry='10/10/21', condition='opened')
        self.assertEqual(0, len(self.fridge._items))

    def test_not_be_able_to_remove_items_when_door_is_closed(self):
        with self.assertRaises(self.fridge.DoorClosed):
            self.fridge.scan_removed_item(name='thing')
        self.assertEqual(0, len(self.fridge._items))

    def test_be_able_to_add_items_when_door_is_opened(self):
        self.fridge.signal_fridge_door_opened()
        self.fridge.scan_added_item(name='thing', expiry='10/10/21', condition='opened')
        self.assertEqual(1, len(self.fridge._items))

    def test_should_set_the_current_time_to_given_string(self):
        self.assertIsInstance(self.fridge._current_time, datetime.datetime)
        self.assertEqual(self.fridge._current_time.strftime("%d/%m/%y"), '18/10/21')

    def test_should_simulate_day_over_to_next_date(self):
        self.fridge.simulate_day_over()

        self.assertIsInstance(self.fridge._current_time, datetime.datetime)
        self.assertEqual(self.fridge._current_time.strftime("%d/%m/%y"), '19/10/21')

    def test_should_signal_fridge_door_closed(self):
        self.fridge.signal_fridge_door_opened()

        self.fridge.signal_fridge_door_closed()

        self.assertEqual(self.fridge._state, FridgeState.DOOR_CLOSED)

    def test_should_not_remove_item_when_fridge_door_is_closed(self):
        with self.assertRaises(self.fridge.DoorClosed):
            self.fridge.scan_removed_item('jam')

    def test_should_not_remove_item_when_there_is_no_matching_item_with_name(self):
        self.fridge.signal_fridge_door_opened()
        self.fridge.scan_added_item(name='bread', expiry='2021', condition=str(ItemCondition.SEALED))

        with self.assertRaises(self.fridge.CannotRemoveItem):
            self.fridge.scan_removed_item('jam')
