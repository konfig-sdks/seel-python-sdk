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


class MerchantUpdateMerchantDetailsRequestSeelServicesItem(BaseModel):
    # The product type for the service, e.g. seel-ra, seel-gsp.
    type: typing.Optional[str] = Field(None, alias='type')

    # Boolean indicating if the service is currently enabled ('true') or disabled ('false') for the merchant.
    is_enabled: typing.Optional[bool] = Field(None, alias='is_enabled')

    # Default opt-in setting for the service widget. 'true' means opted in by default. 'false' means opted out by default.
    is_default_on: typing.Optional[str] = Field(None, alias='is_default_on')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
