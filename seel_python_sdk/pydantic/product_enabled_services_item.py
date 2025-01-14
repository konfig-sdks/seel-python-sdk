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


class ProductEnabledServicesItem(BaseModel):
    # Service type (e.g., extended-warranty, buyback-guarantee).
    service_type: typing.Optional[str] = Field(None, alias='service_type')

    # Enable/disable selling of the service type on this product.
    is_enabled: typing.Optional[bool] = Field(None, alias='is_enabled')

    # Timestamp when the service was created.
    created_ts: typing.Optional[datetime] = Field(None, alias='created_ts')

    # Timestamp when the service was last updated.
    updated_ts: typing.Optional[datetime] = Field(None, alias='updated_ts')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
