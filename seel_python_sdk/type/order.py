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

from seel_python_sdk.type.address import Address
from seel_python_sdk.type.customer import Customer
from seel_python_sdk.type.fulfillment import Fulfillment
from seel_python_sdk.type.item import Item
from seel_python_sdk.type.order_refund import OrderRefund
from seel_python_sdk.type.seel_service import SeelService

class RequiredOrder(TypedDict):
    pass

class OptionalOrder(TypedDict, total=False):
    # The unique identifier for the order in the system.
    order_id: str

    # The reference number that is visible to the merchant and shopper. Use the order ID value if there is no separate order number.
    order_number: str

    # The ID of a cart.
    cart_id: str

    # The unique identifier for the merchant within Seel's system.
    merchant_id: str

    # The ID of the session.
    session_id: str

    # The ID of the client device.
    device_id: str

    # The IP address of the client.
    client_ip: str

    # Order created timestamp in milliseconds
    created_ts: datetime

    # Order cancelled timestamp in milliseconds
    cancelled_ts: datetime

    # Order updated timestamp in milliseconds
    updated_ts: datetime

    # The list of items included in the quote.
    line_items: typing.List[Item]

    shipping_address: Address

    # The list of fulfillments for the order.
    fulfillments: typing.List[Fulfillment]

    # The list of Seel services of the order.
    seel_services: typing.List[SeelService]

    # The list of refunds for the order.
    refunds: typing.List[OrderRefund]

    customer: Customer

    # Additional information for the order
    extra_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class Order(RequiredOrder, OptionalOrder):
    pass
