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

from seel_python_sdk.type.product import Product

class RequiredProductBatchCreateProductsRequest(TypedDict):
    pass

class OptionalProductBatchCreateProductsRequest(TypedDict, total=False):
    # The list of products.
    products: typing.List[Product]

class ProductBatchCreateProductsRequest(RequiredProductBatchCreateProductsRequest, OptionalProductBatchCreateProductsRequest):
    pass
