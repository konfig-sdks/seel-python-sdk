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


class RequiredCustomer(TypedDict):
    # The unique identifier for the customer
    customer_id: str

    # The email address of the customer
    email: str

class OptionalCustomer(TypedDict, total=False):
    # The first name of the customer
    first_name: str

    # The last name of the customer
    last_name: str

    # The phone number of the customer
    phone: str

    # Extra information about the product.
    extra_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class Customer(RequiredCustomer, OptionalCustomer):
    pass
