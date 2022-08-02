import unittest

from enchanting.enchanting import MagicBook


class MagicBookShould(unittest.TestCase):
    def test_return_enchantment_selection_from_spells(self):
        magic_book = MagicBook()
        self.assertEqual(magic_book.random_enchantment(), 'Icy')
