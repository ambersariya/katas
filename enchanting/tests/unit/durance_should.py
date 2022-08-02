import unittest
from unittest.mock import Mock

from enchanting.enchanting import Durance, MagicBook, Weapon, Enchantment, Dagger, AttackDamage


class DuranceShould(unittest.TestCase):
    def test_describe_weapon_with_enchantment(self):
        expected = """Inferno Dagger of the Nooblet
5 - 10 attack damage
1.2 attack speed
+5 fire damage
"""
        enchantment = Enchantment(prefix='Inferno', attribute="+5 fire damage")

        magic_book = Mock(MagicBook)
        magic_book.random_enchantment.return_value = enchantment
        weapon = self.weapon()

        durance = Durance(magic_book=magic_book, weapon=weapon)
        durance.enchant()

        self.assertEqual(durance.describe_weapon(), expected)

    def test_describe_weapon_without_any_enhanctments(self):
        expected = """Dagger of the Nooblet
5 - 10 attack damage
1.2 attack speed
"""
        enchantment = None

        magic_book = Mock(MagicBook)
        magic_book.random_enchantment.return_value = enchantment
        weapon = self.weapon()

        durance = Durance(magic_book=magic_book, weapon=weapon)
        durance.enchant()

        self.assertEqual(str(durance.describe_weapon()), expected)

    @staticmethod
    def weapon():
        return Dagger(
            name='Dagger of the Nooblet',
            attack_speed=1.2,
            attack_damage=AttackDamage(min=5, max=10)
        )
