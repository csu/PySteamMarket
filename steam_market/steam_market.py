import requests, urllib

'''
TODO:
  * add all currencies supported by the Steam Marketplace to `curAbbrev`
  * create docstrings for all functions
  * listings parser; get total number of listings (`total_count` in JSON)
  * get price overview via http://steamcommunity.com/market/priceoverview/
'''

class MarketListing:
    def __init__(self, listing_id, price):
        self._id = listing_id
        self.price = price

class MarketItem:
    def __init__(self, item_id=None, listings=None):
        self._id = item_id
        if listings:
            self.listings = listings
        else:
            self.listings = []

    def add_listing(self, l_id, price):
        self.listings.append(MarketListing(l_id, price))

# Currency abbreviations
curAbbrev = {
    'USD' : 1,
    'GBP' : 2,
    'EUR' : 3,
    'CHF' : 4,
    'RUB' : 5,
    'KRW' : 16,
    'CAD' : 20,
}

"""
Gets item listings from the Steam Marketplace.

@param game_id: ID of game item belongs to.
@param item: Name of item to lookup.
@param start: Listing index to start from. 0 is the most recent listing.
@param start: number >= 0
@param count: Number of listings to grab, start and beyond.
@param count: number >= 1
@param currency: Abbreviation of currency to return listing prices in.
@type currency:
    Accepted currencies:

      - USD
      - GBP
      - EUR
      - CHF
      - RUB
      - KRW
      - CAD

    Please lookup the proper abbreviation for your currency of choice.
@return A list of prices. Depending on your chosen currency, you may need to
    move the decimal place. For instance, in USD, $25.98 would be returned
    as 2598
"""
def get_item(game_id, item, start=0, count=10, currency='USD'):
    url = 'http://steamcommunity.com/market/listings/{}/{}/render'.format(
        game_id,
        urllib.parse.quote(item)
    )
    payload = {
        'start' : start,
        'count' : count,
        'currency' : curAbbrev[currency]
    }
    resp = requests.get(url, params=payload)
    listings = resp.json()['listinginfo']
    market_item = MarketItem()
    for l_id, v in listings.items():
        price = v['converted_price_per_unit'] + v['converted_fee_per_unit']
        market_item.add_listing(l_id, price)
    return market_item

def get_tf2_item(item, start=0, count=10, currency='USD'):
    return get_item('440', item, start, count)

def get_csgo_item(item, start=0, count=10, currency='USD'):
    return get_item('730', item, start, count)
