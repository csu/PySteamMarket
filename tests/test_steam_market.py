#!/usr/bin/env python3

import unittest
import steam_market as sm

class TestTF2Items(unittest.TestCase):
    def runTest(self):
        items = [
            'Strange Professional Killstreak Minigun',
            'Strange Professional Killstreak Mantreads',
            'Strange Professional Killstreak Overdose',
            'Strange Professional Killstreak Winger',
            'Strange Professional Killstreak Degreaser',
            'Strange Professional Killstreak Scattergun',
            'Strange Professional Killstreak Wrench',
            'Strange Professional Killstreak Knife',
            'Strange Professional Killstreak Rainblower',
            'Strange Professional Killstreak Huntsman'
        ]

        for item in items:
            print(item)
            market_item = sm.get_tf2_item(item)
            print([i.price for i in market_item.listings])
