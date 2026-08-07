"""Basic risk management rules."""

from dataclasses import dataclass


@dataclass
class RiskLimits:
    max_position_size: float = 1000.0
    max_daily_loss: float = 100.0


def position_allowed(current_exposure: float, order_size: float, limits: RiskLimits) -> bool:
    """Return True if adding order_size keeps us within the position limit."""
    return current_exposure + order_size <= limits.max_position_size
