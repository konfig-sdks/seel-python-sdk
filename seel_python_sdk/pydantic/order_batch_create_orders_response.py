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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from seel_python_sdk.pydantic.order import Order

class OrderBatchCreateOrdersResponse(BaseModel):
    # The list of orders.
    orders: typing.Optional[typing.List[Order]] = Field(None, alias='orders')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
