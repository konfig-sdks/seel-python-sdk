# coding: utf-8

"""
    Seel API

    Seel API

    The version of the OpenAPI document: 1.3.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from seel_python_sdk.type.order_refund_line_items import OrderRefundLineItems

class RequiredOrderRefund(TypedDict):
    pass

class OptionalOrderRefund(TypedDict, total=False):
    # The unique identifier of the claim.
    refund_id: str

    # The timestamp in milliseconds when the contract was created.
    created_ts: typing.Optional[datetime]

    # The refund amount.
    refund_amount: typing.Union[int, float]

    # The refund reason.
    refund_reason: str

    line_items: OrderRefundLineItems

class OrderRefund(RequiredOrderRefund, OptionalOrderRefund):
    pass
