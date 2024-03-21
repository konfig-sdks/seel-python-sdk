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


class SeelServiceCoveredItemsItem(BaseModel):
    # The id of the item
    line_item_id: typing.Optional[str] = Field(None, alias='line_item_id')

    # The quantity of the item.
    quantity: typing.Optional[int] = Field(None, alias='quantity')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
