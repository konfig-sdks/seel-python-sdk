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

from seel_python_sdk.pydantic.merchant_seel_services import MerchantSeelServices

class Merchant(BaseModel):
    # The unique identifier for the merchant within Seel's system.
    merchant_id: typing.Optional[str] = Field(None, alias='merchant_id')

    # The identifier for the shop or store within the partner's platform.
    shop_id: typing.Optional[str] = Field(None, alias='shop_id')

    # The original subdomain domain for the shop provided by the ecommerce platform, e.g. subdomain.myshopify.com
    admin_domain: typing.Optional[str] = Field(None, alias='admin_domain')

    # The custom domain name assigned to the shop, e.g. www.myshop.com.
    shop_domain: typing.Optional[str] = Field(None, alias='shop_domain')

    # The source ecommerce platform for the shop, e.g. Shopify, BigCommerce.
    shop_platform: typing.Optional[str] = Field(None, alias='shop_platform')

    # 3-letter ISO 4217 currency code for the primary currency used in the shop, e.g. USD, EUR.
    shop_currency: typing.Optional[str] = Field(None, alias='shop_currency')

    # The registered business name for the shop.
    shop_name: typing.Optional[str] = Field(None, alias='shop_name')

    # The registered business name for the merchant.
    contact_name: typing.Optional[str] = Field(None, alias='contact_name')

    # The contact email address on file for the merchant.
    contact_email: typing.Optional[str] = Field(None, alias='contact_email')

    # The phone number on file for the merchant.
    contact_phone_number: typing.Optional[str] = Field(None, alias='contact_phone_number')

    seel_services: typing.Optional[MerchantSeelServices] = Field(None, alias='seel_services')

    # The timestamp when the merchant was created.
    created_ts: typing.Optional[datetime] = Field(None, alias='created_ts')

    # The timestamp when the merchant was last updated.
    updated_ts: typing.Optional[datetime] = Field(None, alias='updated_ts')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
