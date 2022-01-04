import datetime
import unittest

from fridgecraft.src.fridge import Fridge


class TestFridge(unittest.TestCase):
    def setUp(self) -> None:
        self.fridge = Fridge()

    def test_not_be_able_to_add_items_when_door_is_closed(self):
        with self.assertRaises(self.fridge.CannotAddItem):
            self.fridge.scan_added_item(name='thing', expiry='10/10/21', condition='opened')
        self.assertEqual(0, len(self.fridge._items))

    def test_not_be_able_to_remove_items_when_door_is_closed(self):
        with self.assertRaises(self.fridge.CannotAddItem):
            self.fridge.scan_removed_item(name='thing')
        self.assertEqual(0, len(self.fridge._items))

    def test_be_able_to_add_items_when_door_is_opened(self):
        self.fridge.signal_fridge_door_opened()
        self.fridge.scan_added_item(name='thing', expiry='10/10/21', condition='opened')
        self.assertEqual(1, len(self.fridge._items))

    def test_should_set_the_current_time_to_given_string(self):
        fridge = Fridge()
        fridge.set_current_date('18/10/21')
        self.assertIsInstance(fridge._current_time, datetime.datetime)
