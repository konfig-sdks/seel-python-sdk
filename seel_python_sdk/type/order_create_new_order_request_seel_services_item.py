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


class RequiredOrderCreateNewOrderRequestSeelServicesItem(TypedDict):
    pass

class OptionalOrderCreateNewOrderRequestSeelServicesItem(TypedDict, total=False):
    # Cover type of the service
    type: str

    # Price of the service
    price: typing.Union[int, float]

    # Quote ID of the service
    quote_id: str

    # Additional information for the service
    extra_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OrderCreateNewOrderRequestSeelServicesItem(RequiredOrderCreateNewOrderRequestSeelServicesItem, OptionalOrderCreateNewOrderRequestSeelServicesItem):
    pass
