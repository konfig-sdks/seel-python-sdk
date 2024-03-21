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


class RequiredProductUpdateProductDetailsRequestWeight(TypedDict):
    pass

class OptionalProductUpdateProductDetailsRequestWeight(TypedDict, total=False):
    # Weight of the product.
    value: typing.Union[int, float]

    # Unit of weight (e.g., g, oz, lb, kg).
    unit: str

class ProductUpdateProductDetailsRequestWeight(RequiredProductUpdateProductDetailsRequestWeight, OptionalProductUpdateProductDetailsRequestWeight):
    pass