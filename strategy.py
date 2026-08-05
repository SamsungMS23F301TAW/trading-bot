"""Trading strategy base class."""

from abc import ABC, abstractmethod


class Strategy(ABC):
    """Base class all strategies should inherit from."""

    @abstractmethod
    def on_data(self, price: float) -> str:
        """Return one of: 'buy', 'sell', 'hold'."""
        raise NotImplementedError


class BuyAndHold(Strategy):
    def on_data(self, price: float) -> str:
        return "hold"
