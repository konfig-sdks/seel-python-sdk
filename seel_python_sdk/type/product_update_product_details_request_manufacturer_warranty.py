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


class RequiredProductUpdateProductDetailsRequestManufacturerWarranty(TypedDict):
    pass

class OptionalProductUpdateProductDetailsRequestManufacturerWarranty(TypedDict, total=False):
    # A URL linking to the full details of the manufacturer's warranty, probably on the manufacturer's website.
    url: str

    # The length of the manufacturer warranty coverage in months.
    term_length: typing.Union[int, float]

class ProductUpdateProductDetailsRequestManufacturerWarranty(RequiredProductUpdateProductDetailsRequestManufacturerWarranty, OptionalProductUpdateProductDetailsRequestManufacturerWarranty):
    pass