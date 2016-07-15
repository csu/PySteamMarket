import requests
from bs4 import BeautifulSoup

# constants
LISTING_ID_PREFIX = 'listing_'

class MarketItem:
    def __init__(self, item_id=None, listings=None):
        self.id = item_id

        if listings:
            self.listings = listings
        else:
            self.listings = []

class MarketListing:
    def __init__(self, listing_id, price):
        self.id = listing_id
        self.price = price

def parse_item(html):
    soup = BeautifulSoup(html, 'html.parser')
    market_item = MarketItem()

    for listing in soup.find_all('div', {'class': 'market_listing_row'}):
        text = listing.find('span', {'class': 'market_listing_price_with_fee'}).text.strip()
        if text.startswith('$'):
            market_item.listings.append(MarketListing(
                listing_id = listing.get('id').replace(LISTING_ID_PREFIX, ''),
                price = float(text[1:])
            ))

    return market_item

def get_item_from_url(url):
    r = requests.get(url)
    return parse_item(r.text)

def get_item(game_id, item):
    url = 'http://steamcommunity.com/market/listings/%(game_id)s/%(item)s'
    payload = {
        'game_id': game_id,
        'item': item
    }
    return get_item_from_url(url % payload)

def get_tf2_item(item):
    return get_item('440', item)

def encode_for_url(string):
    return string.replace(' ', '%20')
