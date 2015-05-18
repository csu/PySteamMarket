import steam_market

item = steam_market.get_tf2_item('Strange%20Killstreak%20Flame%20Thrower')
for listing in item.listings:
    print listing.price