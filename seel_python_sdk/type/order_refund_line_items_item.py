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


class RequiredOrderRefundLineItemsItem(TypedDict):
    pass

class OptionalOrderRefundLineItemsItem(TypedDict, total=False):
    line_item_id: str

    quantity: int

class OrderRefundLineItemsItem(RequiredOrderRefundLineItemsItem, OptionalOrderRefundLineItemsItem):
    pass
