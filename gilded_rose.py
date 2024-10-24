from pkgutil import iter_modules


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            
            if item.name == "Aged Brie":
                item.quality += 1
                item.quality = min(50, item.quality)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 6:
                    item.quality += 3
                elif item.sell_in < 11:
                    item.quality += 2
                else:
                    item.quality += 1
                item.quality = min(50, item.quality)
            else:
                # this is normal items
                item.quality -= 1
                item.quality = max(0, item.quality)

            item.sell_in -= 1

            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    item.quality += 1
                    item.quality = min(50, item.quality)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                else:
                    # Normal
                    item.quality -= 1
                    item.quality = max(0, item.quality)
