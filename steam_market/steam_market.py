import requests
from bs4 import BeautifulSoup

class MarketItem:
    def __init__(self, item_id, listings=None):
        self.id = item_id
        self.listings = []

def parse_item(html):
    

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