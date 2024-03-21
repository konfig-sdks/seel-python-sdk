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

from seel_python_sdk.type.order import Order

class RequiredOrderBatchCreateOrdersResponse(TypedDict):
    pass

class OptionalOrderBatchCreateOrdersResponse(TypedDict, total=False):
    # The list of orders.
    orders: typing.List[Order]

class OrderBatchCreateOrdersResponse(RequiredOrderBatchCreateOrdersResponse, OptionalOrderBatchCreateOrdersResponse):
    pass
