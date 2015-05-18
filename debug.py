import steam_market
from steam_market import encode_for_url

item = steam_market.get_tf2_item(encode_for_url('Strange Killstreak Flame Thrower'))
for listing in item.listings:
    print listing.price