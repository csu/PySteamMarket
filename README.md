# PySteamMarket
(Under construction)

Python API for getting prices from the Steam market.

## Usage

```python
import steam_market as sm
from steam_market import encode_for_url

item = sm.get_tf2_item(encode_for_url('Strange Professional Killstreak Scattergun'))
for listing in item.listings:
    print listing.price
```