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


class Customer(BaseModel):
    # The unique identifier for the customer
    customer_id: str = Field(alias='customer_id')

    # The email address of the customer
    email: str = Field(alias='email')

    # The first name of the customer
    first_name: typing.Optional[str] = Field(None, alias='first_name')

    # The last name of the customer
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # The phone number of the customer
    phone: typing.Optional[str] = Field(None, alias='phone')

    # Extra information about the product.
    extra_info: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='extra_info')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
