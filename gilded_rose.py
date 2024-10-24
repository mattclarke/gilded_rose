# -*- coding: utf-8 -*-
from pkgutil import iter_modules

from third_party import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                # this is normal items
                item.quality -= 1
                item.quality = max(0, item.quality)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                # backstage passes
                if item.sell_in < 6:
                    item.quality += 3
                    item.quality -= 2
                elif item.sell_in < 11:
                    item.quality += 2
                    item.quality -= 1
                else:
                    item.quality += 1

                item.quality = min(50, item.quality)
            else:
                # brie
                item.quality += 1
                item.quality = min(50, item.quality)

            item.sell_in -= 1

            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    # Brie
                    item.quality += 1
                    item.quality = min(50, item.quality)

                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0

                else:
                    # Normal
                    item.quality -= 1
                    item.quality = max(0, item.quality)

