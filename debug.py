import steam_market as sm
from steam_market import encode_for_url

item = sm.get_tf2_item(encode_for_url('Strange Killstreak Flame Thrower'))
for listing in item.listings:
    print listing.price