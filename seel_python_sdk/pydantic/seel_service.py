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

from seel_python_sdk.pydantic.seel_service_covered_items import SeelServiceCoveredItems

class SeelService(BaseModel):
    # Cover ID
    contract_id: typing.Optional[str] = Field(None, alias='contract_id')

    # The identifier of the quote associated with the contract.
    quote_id: typing.Optional[str] = Field(None, alias='quote_id')

    # Service created timestamp in milliseconds
    created_ts: typing.Optional[datetime] = Field(None, alias='created_ts')

    # Cover type of the service
    type: typing.Optional[str] = Field(None, alias='type')

    # Price of the service
    price: typing.Optional[typing.Union[int, float]] = Field(None, alias='price')

    # The status of the service
    status: typing.Optional[Literal["active", "cancelled", "pending"]] = Field(None, alias='status')

    covered_items: typing.Optional[SeelServiceCoveredItems] = Field(None, alias='covered_items')

    # Additional information for the service
    extra_info: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='extra_info')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
