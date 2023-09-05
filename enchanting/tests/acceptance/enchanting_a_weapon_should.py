import unittest

from enchanting.enchanting import Durance, MagicBook, Dagger


class EnchantingAWeaponShould(unittest.TestCase):
    def test_return_an_enchanted_weapon_with_updated_prefix_and_attribute(self):
        expected = """
Inferno Dagger of the Nooblet
5 - 10 attack damage
1.2 attack speed
+5 fire damage
"""
        magic_book = MagicBook()
        weapon = Dagger()
        durance = Durance(magic_book=magic_book, weapon=weapon)
        durance.enchant()

        result = durance.describe_weapon()
        self.assertEqual(expected, result)

    def test_return_a_non_enchanted_weapon_without_a_prefix_and_original_attribute(self):
        expected = """
Dagger of the Nooblet
5 - 10 attack damage
1.2 attack speed
"""
        magic_book = MagicBook()
        weapon = Dagger

        durance = Durance(magic_book=magic_book, weapon=weapon)
        durance.enchant()

        result = durance.describe_weapon()

        self.assertEqual(expected, result)
