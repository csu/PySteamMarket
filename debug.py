import steam_market

item = steam_market.get_tf2_item(steam_market.encode_for_url('Strange Killstreak Flame Thrower'))
for listing in item.listings:
    print listing.price