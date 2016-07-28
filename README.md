# PySteamMarket
(Under construction)

Python API for getting prices from the Steam market.

## Usage

```python
import steam_market as sm

item = sm.get_tf2_item('Strange Professional Killstreak Scattergun')
for listing in item.listings:
    print(listing.price)
```
