# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 4
    output = []
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        output.append("-------- day %s --------" % day )
        output.append("name, sellIn, quality")
        # print("-------- day %s --------" % day)
        # print("name, sellIn, quality")
        for item in items:
            output.append(item.__repr__())
            # print(item)
        output.append("")
        GildedRose(items).update_quality()

    with open("golden.txt") as f:
        golden = f.readlines()
        for i, line in enumerate(output):
            if line != golden[i].strip():
                print(line)
                print(golden[i])
