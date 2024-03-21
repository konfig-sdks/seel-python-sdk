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


class RequiredProductUpdateProductDetailsRequestProductAttributes(TypedDict):
    pass

class OptionalProductUpdateProductDetailsRequestProductAttributes(TypedDict, total=False):
    # Color of the product.
    color: str

    # Size of the product.
    size: str

class ProductUpdateProductDetailsRequestProductAttributes(RequiredProductUpdateProductDetailsRequestProductAttributes, OptionalProductUpdateProductDetailsRequestProductAttributes):
    pass
