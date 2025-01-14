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

from seel_python_sdk.pydantic.claim_claim_details import ClaimClaimDetails

class Claim(BaseModel):
    # The unique identifier of the claim.
    claim_id: typing.Optional[str] = Field(None, alias='claim_id')

    # The identifier of the order associated with the claim.
    order_id: typing.Optional[str] = Field(None, alias='order_id')

    # The identifier of the contract associated with the claim.
    contract_id: typing.Optional[str] = Field(None, alias='contract_id')

    # The settled amount of the claim.
    payout_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='payout_amount')

    # The status of the claim.
    status: typing.Optional[Literal["pending", "accepted", "rejected"]] = Field(None, alias='status')

    # The status of the claim.
    claim_type: typing.Optional[Literal["return", "loss", "damage", "delay", "theft"]] = Field(None, alias='claim_type')

    # The reject reason of the claim.
    reject_reason: typing.Optional[str] = Field(None, alias='reject_reason')

    claim_details: typing.Optional[ClaimClaimDetails] = Field(None, alias='claim_details')

    # The timestamp in milliseconds when the contract was cancelled (if applicable).
    updated_ts: typing.Optional[typing.Optional[datetime]] = Field(None, alias='updated_ts')

    # The timestamp in milliseconds when the contract was created.
    created_ts: typing.Optional[typing.Optional[datetime]] = Field(None, alias='created_ts')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
