# -*- coding: utf-8 -*-
import unittest

from parameterized import parameterized  # type: ignore

from gilded_rose import GildedRose
from items import create_item


class GildedRoseTest(unittest.TestCase):
    @parameterized.expand([
        ('Foo', 0, 0, -1, 0),
        ('Foo', 0, 51, -1, 50),
        ('Foo', 0, 1, -1, 0),
        ('Foo', -1, 1, -2, 0),
        ('Foo', -1, 0, -2, 0),
        ('Aged Brie', 1, 1, 0, 2),
        ('Aged Brie', 10, 50, 9, 50),
        ('Aged Brie', 10, 49, 9, 50),
        ('Aged Brie', -1, 60, -2, 60),
        ('Sulfuras, Hand of Ragnaros', 10, 80, 10, 80),
        ('Sulfuras, Hand of Ragnaros', -1, 80, -1, 80),
        ('+5 Dexterity Vest', 10, 20, 9, 19),
        ('+5 Dexterity Vest', -1, 20, -2, 19),
        ('Backstage passes to a TAFKAL80ETC concert', 15, 10, 14, 11),
        ('Backstage passes to a TAFKAL80ETC concert', 15, 20, 14, 21),
        ('Backstage passes to a TAFKAL80ETC concert', 10, 49, 9, 50),
        ('Backstage passes to a TAFKAL80ETC concert', 9, 50, 8, 50),
        ('Backstage passes to a TAFKAL80ETC concert', 10, 10, 9, 12),
        ('Backstage passes to a TAFKAL80ETC concert', 5, 10, 4, 13),
        ('Backstage passes to a TAFKAL80ETC concert', -1, 10, -2, 0),
        ('Backstage passes to a TAFKAL80ETC concert', -2, 10, -3, 0),
        ('Conjured Mana Cake', 0, 0, -1, 0),
        ('Conjured Mana Cake', 0, 51, -1, 50),
        ('Conjured Mana Cake', 0, 1, -1, 0),
        ('Conjured Mana Cake', -1, 1, -2, 0),
        ('Conjured Mana Cake', -1, 0, -2, 0),
    ])
    def test_item(self, item_name, sell_in, quality, expected_sell_in, expected_quality):
        items = [create_item(name=item_name, sell_in=sell_in, quality=quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(item_name, items[0].name)
        self.assertEquals(expected_quality, items[0].quality)
        self.assertEquals(expected_sell_in, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
