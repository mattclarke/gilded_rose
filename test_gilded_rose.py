# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_standard_item_before_expiry(self):
        items = [Item("Standard item", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_standard_item_day_one(self):
        # Potential edge case: it should only decrease by one.
        items = [Item("Standard item", 1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_standard_item_day_zero(self):
        # Potential edge case: it should decrease by two.
        items = [Item("Standard item", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_standard_item_after_expiry_decreases_twice_as_fast(self):
        items = [Item("Standard item", -2, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_standard_item_quality_cannot_be_negative(self):
        items = [Item("Standard item", 1, 0), Item("Standard item", -1, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality)
        self.assertEqual(0, items[1].quality)

    def test_sulfuras_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 100)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(100, items[0].quality)

    def test_aged_brie_before_expiry_quality_increases(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_aged_brie_after_expiry_quality_increases_twice_as_fast(self):
        items = [Item("Aged Brie", -5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-6, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_aged_brie_day_one(self):
        # Potential edge case: it should only increase by one.
        items = [Item("Aged Brie", 1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_aged_brie_day_zero(self):
        # Potential edge case: it should increase by two.
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_aged_brie_quality_cannot_exceed_50(self):
        items = [Item("Aged Brie", 5, 50), Item("Aged Brie", -5, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(50, items[0].quality)
        self.assertEqual(50, items[1].quality)

    def test_backstage_pass_more_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_pass_on_11_days(self):
        # Potential edge case: it should only increase by one.
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_pass_on_10_days(self):
        # Potential edge case: it should increase by two.
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_on_6_days(self):
        # Potential edge case: it should only increase by two.
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_on_5_days(self):
        # Potential edge case: it should increase by three.
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_pass_on_1_days(self):
        # Potential edge case: it should increase by three.
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_pass_on_0_days(self):
        # Potential edge case: it should jump to 0
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_on_after_expiry_goes_to_zero(self):
        # This test case shouldn't happen but check it does the right thing anyway.
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-6, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_quality_cannot_exceed_50(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 50),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 4, 48),
        ]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(50, items[0].quality)
        self.assertEqual(50, items[1].quality)
        self.assertEqual(50, items[2].quality)

    def test_conjured_item_before_expiry_degrades_twice_as_fast(self):
        items = [Item("Conjured item", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_conjured_item_on_1_days(self):
        # Potential edge case: it should only decrease by 2.
        items = [Item("Conjured item", 1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_conjured_item_on_0_days(self):
        # Potential edge case: it should decrease by 4.
        items = [Item("Conjured item", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_conjured_item_after_expiry_decreases_twice_as_fast(self):
        items = [Item("Conjured item", -1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_conjured_item_quality_cannot_be_negative(self):
        items = [Item("Conjured item", 1, 0), Item("Conjured item", -1, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality)
        self.assertEqual(0, items[1].quality)


if __name__ == "__main__":
    unittest.main()
 
