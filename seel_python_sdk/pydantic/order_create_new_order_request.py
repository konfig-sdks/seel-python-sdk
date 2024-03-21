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
from seel_python_sdk.pydantic.item import Item
from seel_python_sdk.pydantic.order_create_new_order_request_seel_services import OrderCreateNewOrderRequestSeelServices

class OrderCreateNewOrderRequest(BaseModel):
    # The unique identifier for the order in the system.
    order_id: str = Field(alias='order_id')

    # The reference number that is visible to the merchant and shopper. Use the order ID value if there is no separate order number.
    order_number: str = Field(alias='order_number')

    # Shopping session ID of the order
    session_id: str = Field(alias='session_id')

    # Order created timestamp in milliseconds
    created_ts: str = Field(alias='created_ts')

    # The list of items included in the order.
    line_items: typing.List[Item] = Field(alias='line_items')

    shipping_address: Address = Field(alias='shipping_address')

    customer: Customer = Field(alias='customer')

    # Cart ID of the order
    cart_id: typing.Optional[str] = Field(None, alias='cart_id')

    # Merchant ID of the order
    merchant_id: typing.Optional[str] = Field(None, alias='merchant_id')

    # The ID of the client device.
    device_id: typing.Optional[str] = Field(None, alias='device_id')

    # The IP address of the client.
    client_ip: typing.Optional[str] = Field(None, alias='client_ip')

    seel_services: typing.Optional[OrderCreateNewOrderRequestSeelServices] = Field(None, alias='seel_services')

    # Additional information for the order
    extra_info: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='extra_info')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
