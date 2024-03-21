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


class RequiredEventCreateNewEventRequest(TypedDict):
    # Session ID
    session_id: str

    # Customer ID
    customer_id: str

    # Event source
    event_source: str

    # Event type
    event_type: str

    # Each event_type has its own unique schema. For specific details, please refer to the custom pixel guide.
    event_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalEventCreateNewEventRequest(TypedDict, total=False):
    # Event created timestamp in milliseconds
    event_ts: str

    # Device ID
    device_id: str

    # Browser IP address
    client_ip: str

class EventCreateNewEventRequest(RequiredEventCreateNewEventRequest, OptionalEventCreateNewEventRequest):
    pass