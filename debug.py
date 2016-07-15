import steam_market as sm
from steam_market import encode_for_url

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
    market_item = sm.get_tf2_item(encode_for_url(item))
    print([i.price for i in market_item.listings])
