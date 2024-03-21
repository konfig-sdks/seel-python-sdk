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

from seel_python_sdk.type.item_shipping_origin import ItemShippingOrigin
from seel_python_sdk.type.product_attributes import ProductAttributes

class RequiredItem(TypedDict):
    # The ID of the item.
    line_item_id: str

    # The ID of the product.
    product_id: str

    # The title of the product.
    product_title: str

    # The quantity of the product.
    quantity: int

    # The price of the product.
    price: typing.Union[int, float]

    # The allocated discounts of the product.
    allocated_discounts: typing.Union[int, float]

    # The sales tax of the product.
    sales_tax: typing.Union[int, float]

    # The final price of the product.
    final_price: typing.Union[int, float]

    # The currency of the price.
    currency: str

    # Whether the item requires shipping or not.
    requires_shipping: bool

    # The main category of the product.
    category_1: str

    # The sub category of the product.
    category_2: str

    # Whether the item is final sale or not.
    is_final_sale: bool

    # The physical condition of the item (e.g. new, used, refurbished)
    condition: str

class OptionalItem(TypedDict, total=False):
    # The description of the product.
    product_description: str

    # The ID of the product variant.
    variant_id: str

    # The title of the product variant.
    variant_title: str

    # The sku of the product variant.
    sku: str

    # The ID of the seller.
    seller_id: str

    # The name of the seller.
    seller_name: str

    # The brand name of the product.
    brand_name: str

    # The retail price of the product.
    retail_price: typing.Union[int, float]

    # The URL of the product.
    product_url: str

    # The URL of the product image.
    image_url: str

    # The sub category of the product.
    category_3: str

    # The sub category of the product.
    category_4: str

    product_attributes: ProductAttributes

    shipping_origin: ItemShippingOrigin

    # Extra information about the product.
    extra_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class Item(RequiredItem, OptionalItem):
    pass
