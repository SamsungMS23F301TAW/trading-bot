"""Configuration loading for the trading bot."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    api_key: str = os.getenv("API_KEY", "")
    api_secret: str = os.getenv("API_SECRET", "")
    paper_trading: bool = os.getenv("PAPER_TRADING", "true").lower() == "true"
    base_currency: str = os.getenv("BASE_CURRENCY", "USD")


def load_config() -> Config:
    return Config()
