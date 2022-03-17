from unittest import TestCase

from fridgecraft.src.fridge import Fridge


class FridgeTestShould(TestCase):
    @staticmethod
    def fridge_with_items() -> Fridge:
        fridge = Fridge()
        fridge.set_current_date('18/10/21')
        fridge.signal_fridge_door_opened()
        fridge.scan_added_item(name='Milk', condition='sealed', expiry='17/10/21')
        fridge.scan_added_item(name='Lettuce', condition='sealed', expiry='18/10/21')
        fridge.scan_added_item(name='Peppers', condition='sealed', expiry='21/10/21')
        fridge.scan_added_item(name='Cheese', condition='sealed', expiry='21/11/21')
        fridge.signal_fridge_door_closed()

        return fridge

    def test_display_current_state_of_items_in_chronological_order_of_expiry(self):
        expected = """
        EXPIRED: Milk
        Lettuce: 0 days remaining
        Peppers: 1 day remaining
        Cheese: 31 days remaining
        """
        fridge = self.fridge_with_items()
        actual = fridge.show_display()
        self.assertEqual(expected, actual)
