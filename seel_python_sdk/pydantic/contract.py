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

from seel_python_sdk.pydantic.contract_covered_items import ContractCoveredItems
from seel_python_sdk.pydantic.customer import Customer

class Contract(BaseModel):
    # The unique identifier of the contract.
    contract_id: typing.Optional[str] = Field(None, alias='contract_id')

    # The identifier of the order associated with the contract.
    order_id: typing.Optional[str] = Field(None, alias='order_id')

    # The identifier of the quote associated with the contract.
    quote_id: typing.Optional[str] = Field(None, alias='quote_id')

    customer: typing.Optional[Customer] = Field(None, alias='customer')

    # The premium (i.e., cost) of the contract.
    premium: typing.Optional[typing.Union[int, float]] = Field(None, alias='premium')

    # The tax applied to the contract premium.
    premium_tax: typing.Optional[typing.Union[int, float]] = Field(None, alias='premium_tax')

    # The currency of the contract.
    currency: typing.Optional[str] = Field(None, alias='currency')

    # The current status of the contract (e.g., \"active\", \"cancelled\").
    status: typing.Optional[Literal["active", "cancelled", "pending"]] = Field(None, alias='status')

    # The timestamp in millisecond when the contract was cancelled (if applicable).
    cancelled_ts: typing.Optional[typing.Optional[datetime]] = Field(None, alias='cancelled_ts')

    # The timestamp in millisecond when the contract was created.
    created_ts: typing.Optional[typing.Optional[datetime]] = Field(None, alias='created_ts')

    # The timestamp in millisecond when the contract was updated.
    updated_ts: typing.Optional[typing.Optional[datetime]] = Field(None, alias='updated_ts')

    covered_items: typing.Optional[ContractCoveredItems] = Field(None, alias='covered_items')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
