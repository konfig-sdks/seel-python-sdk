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


class FulfillmentLineItemsItem(BaseModel):
    # The id of the line item.
    line_item_id: str = Field(alias='line_item_id')

    # The quantity of the line item.
    quantity: int = Field(alias='quantity')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
