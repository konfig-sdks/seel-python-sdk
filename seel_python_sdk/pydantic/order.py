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

from seel_python_sdk.pydantic.address import Address
from seel_python_sdk.pydantic.customer import Customer
from seel_python_sdk.pydantic.fulfillment import Fulfillment
from seel_python_sdk.pydantic.item import Item
from seel_python_sdk.pydantic.order_refund import OrderRefund
from seel_python_sdk.pydantic.seel_service import SeelService

class Order(BaseModel):
    # The unique identifier for the order in the system.
    order_id: typing.Optional[str] = Field(None, alias='order_id')

    # The reference number that is visible to the merchant and shopper. Use the order ID value if there is no separate order number.
    order_number: typing.Optional[str] = Field(None, alias='order_number')

    # The ID of a cart.
    cart_id: typing.Optional[str] = Field(None, alias='cart_id')

    # The unique identifier for the merchant within Seel's system.
    merchant_id: typing.Optional[str] = Field(None, alias='merchant_id')

    # The ID of the session.
    session_id: typing.Optional[str] = Field(None, alias='session_id')

    # The ID of the client device.
    device_id: typing.Optional[str] = Field(None, alias='device_id')

    # The IP address of the client.
    client_ip: typing.Optional[str] = Field(None, alias='client_ip')

    # Order created timestamp in milliseconds
    created_ts: typing.Optional[datetime] = Field(None, alias='created_ts')

    # Order cancelled timestamp in milliseconds
    cancelled_ts: typing.Optional[datetime] = Field(None, alias='cancelled_ts')

    # Order updated timestamp in milliseconds
    updated_ts: typing.Optional[datetime] = Field(None, alias='updated_ts')

    # The list of items included in the quote.
    line_items: typing.Optional[typing.List[Item]] = Field(None, alias='line_items')

    shipping_address: typing.Optional[Address] = Field(None, alias='shipping_address')

    # The list of fulfillments for the order.
    fulfillments: typing.Optional[typing.List[Fulfillment]] = Field(None, alias='fulfillments')

    # The list of Seel services of the order.
    seel_services: typing.Optional[typing.List[SeelService]] = Field(None, alias='seel_services')

    # The list of refunds for the order.
    refunds: typing.Optional[typing.List[OrderRefund]] = Field(None, alias='refunds')

    customer: typing.Optional[Customer] = Field(None, alias='customer')

    # Additional information for the order
    extra_info: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='extra_info')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
