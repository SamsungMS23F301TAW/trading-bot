"""Market data feed helpers."""

import requests


def fetch_price(symbol: str, base_url: str = "https://api.example.com") -> float:
    """Fetch the latest price for a symbol.

    Placeholder implementation — swap in a real endpoint later.
    """
    resp = requests.get(f"{base_url}/price", params={"symbol": symbol}, timeout=10)
    resp.raise_for_status()
    return float(resp.json()["price"])
