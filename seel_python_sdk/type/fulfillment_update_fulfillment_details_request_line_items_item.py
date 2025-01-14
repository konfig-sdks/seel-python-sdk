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


class RequiredFulfillmentUpdateFulfillmentDetailsRequestLineItemsItem(TypedDict):
    # The id of the line item.
    line_item_id: str

    # The quantity of the line item.
    quantity: int

class OptionalFulfillmentUpdateFulfillmentDetailsRequestLineItemsItem(TypedDict, total=False):
    pass

class FulfillmentUpdateFulfillmentDetailsRequestLineItemsItem(RequiredFulfillmentUpdateFulfillmentDetailsRequestLineItemsItem, OptionalFulfillmentUpdateFulfillmentDetailsRequestLineItemsItem):
    pass
