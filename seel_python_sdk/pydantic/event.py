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


class Event(BaseModel):
    # Event ID
    event_id: typing.Optional[str] = Field(None, alias='event_id')

    # Session ID
    session_id: typing.Optional[str] = Field(None, alias='session_id')

    # Event created timestamp
    event_ts: typing.Optional[str] = Field(None, alias='event_ts')

    # Customer ID
    customer_id: typing.Optional[str] = Field(None, alias='customer_id')

    # Device ID
    device_id: typing.Optional[str] = Field(None, alias='device_id')

    # Browser IP address
    browser_ip: typing.Optional[str] = Field(None, alias='browser_ip')

    # Event source
    event_source: typing.Optional[str] = Field(None, alias='event_source')

    # Event type
    event_type: typing.Optional[Literal["product_page_enter", "product_page_exit", "product_share", "favorite_add", "favorite_remove", "cart_add", "cart_remove", "ra_checked", "ra_unchecked", "checkout_begin", "checkout_complete"]] = Field(None, alias='event_type')

    event_info: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='event_info')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
