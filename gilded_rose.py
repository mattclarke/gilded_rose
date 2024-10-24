# -*- coding: utf-8 -*-
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
                if item.quality > 0:
                    item.quality -= 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                # backstage passes
                item.quality += 1
                if item.sell_in < 11:
                    item.quality += 1
                if item.sell_in < 6:
                    item.quality += 1
                item.quality = min(50, item.quality)
            else:
                # brie
                if item.quality < 50:
                    item.quality += 1

            item.sell_in -= 1

            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    # Brie
                    if item.quality < 50:
                        item.quality += 1

                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0

                elif item.name != "Aged Brie":
                    # Normal, backstage
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        # Normal
                        if item.quality > 0:
                            item.quality -= 1
                    else:
                        # backstage
                        item.quality = 0

