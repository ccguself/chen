"""
Basic data structure used for general trading function in the trading platform.
"""

from dataclasses import dataclass, field
from datetime import datetime
from logging import INFO

from .constant import Direction, Status, OrderType

@dataclass
class OrderData:
    """
    Order data contains information for tracking lastest status
    of a specific order.
    """

    symbol: str
    orderid: str

    type: OrderType = OrderType.LIMIT
    direction: Direction = None
    price: float = 0
    volume: float = 0
    traded: float = 0
    status: Status = Status.SUBMITTING
    datetime: datetime = None
    reference: str = ""

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
        self.vt_orderid: str = f"{self.gateway_name}.{self.orderid}"

@dataclass
class OrderBook:
    """
    订单簿指，某一特定价格下的订单
    """
    direciton: Direction = None
    price: float = 0





class Snapshot:
    def __init__(self, symbol, datetime) -> None:
        self.symbol = symbol
        self.datetime = datetime

        pass






