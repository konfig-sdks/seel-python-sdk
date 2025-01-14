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
from seel_python_sdk.type.item import Item
from seel_python_sdk.type.order_create_new_order_request_seel_services import OrderCreateNewOrderRequestSeelServices

class RequiredOrderCreateNewOrderRequest(TypedDict):
    # The unique identifier for the order in the system.
    order_id: str

    # The reference number that is visible to the merchant and shopper. Use the order ID value if there is no separate order number.
    order_number: str

    # Shopping session ID of the order
    session_id: str

    # Order created timestamp in milliseconds
    created_ts: str

    # The list of items included in the order.
    line_items: typing.List[Item]

    shipping_address: Address

    customer: Customer

class OptionalOrderCreateNewOrderRequest(TypedDict, total=False):
    # Cart ID of the order
    cart_id: str

    # Merchant ID of the order
    merchant_id: str

    # The ID of the client device.
    device_id: str

    # The IP address of the client.
    client_ip: str

    seel_services: OrderCreateNewOrderRequestSeelServices

    # Additional information for the order
    extra_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OrderCreateNewOrderRequest(RequiredOrderCreateNewOrderRequest, OptionalOrderCreateNewOrderRequest):
    pass
