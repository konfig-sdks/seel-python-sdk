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


class RequiredProductUpdateProductDetailsRequestDimensions(TypedDict):
    pass

class OptionalProductUpdateProductDetailsRequestDimensions(TypedDict, total=False):
    # Length of the product in centimeters.
    length: typing.Union[int, float]

    # Width of the product in centimeters.
    width: typing.Union[int, float]

    # Height of the product in centimeters.
    height: typing.Union[int, float]

    # Unit of measurement (e.g., cm, in, ft, m).
    unit: str

class ProductUpdateProductDetailsRequestDimensions(RequiredProductUpdateProductDetailsRequestDimensions, OptionalProductUpdateProductDetailsRequestDimensions):
    pass
