# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



# Test Cases for Conjured Items

def test_conjured_item_quality():
    conjured_item = Item(name="Conjured Mana Cake", sell_in=5, quality=10)
    gilded_rose = GildedRose([conjured_item])
    
    # Update quality once before sell-in
    gilded_rose.update_quality()
    assert conjured_item.quality == 8, f"Expected 8, but got {conjured_item.quality}"
    
    # Test after sell-by date
    conjured_item.sell_in = -1
    gilded_rose.update_quality()
    assert conjured_item.quality == 4, f"Expected 4, but got {conjured_item.quality}"
    
    # Test for minimum quality (should not go negative)
    conjured_item.quality = 1
    gilded_rose.update_quality()
    assert conjured_item.quality == 0, f"Expected 0, but got {conjured_item.quality}"

def test_normal_item_quality():
    normal_item = Item(name="Normal Item", sell_in=5, quality=10)
    gilded_rose = GildedRose([normal_item])
    
    # Update quality once before sell-in
    gilded_rose.update_quality()
    assert normal_item.quality == 9, f"Expected 9, but got {normal_item.quality}"
    
    # Test after sell-by date
    normal_item.sell_in = -1
    gilded_rose.update_quality()
    assert normal_item.quality == 8, f"Expected 8, but got {normal_item.quality}"

def test_aged_brie_quality():
    aged_brie = Item(name="Aged Brie", sell_in=5, quality=10)
    gilded_rose = GildedRose([aged_brie])
    
    # Aged Brie increases in quality
    gilded_rose.update_quality()
    assert aged_brie.quality == 11, f"Expected 11, but got {aged_brie.quality}"

def test_backstage_pass_quality():
    backstage_pass = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10)
    gilded_rose = GildedRose([backstage_pass])
    
    # Backstage passes increase in quality before sell-in
    gilded_rose.update_quality()
    assert backstage_pass.quality == 12, f"Expected 12, but got {backstage_pass.quality}"
    
    # Test after sell-by date
    backstage_pass.sell_in = 0
    gilded_rose.update_quality()
    assert backstage_pass.quality == 0, f"Expected 0, but got {backstage_pass.quality}"

# Run Tests
test_conjured_item_quality()
test_normal_item_quality()
test_aged_brie_quality()
test_backstage_pass_quality()

print("All tests passed!")
