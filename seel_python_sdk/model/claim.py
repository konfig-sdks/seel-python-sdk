# coding: utf-8

"""
    Seel API

    Seel API

    The version of the OpenAPI document: 1.3.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from seel_python_sdk import schemas  # noqa: F401


class Claim(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            claim_id = schemas.StrSchema
            order_id = schemas.StrSchema
            contract_id = schemas.StrSchema
            payout_amount = schemas.Float64Schema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "pending": "PENDING",
                        "accepted": "ACCEPTED",
                        "rejected": "REJECTED",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
                
                @schemas.classproperty
                def ACCEPTED(cls):
                    return cls("accepted")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("rejected")
            
            
            class claim_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "return": "RETURN",
                        "loss": "LOSS",
                        "damage": "DAMAGE",
                        "delay": "DELAY",
                        "theft": "THEFT",
                    }
                
                @schemas.classproperty
                def RETURN(cls):
                    return cls("return")
                
                @schemas.classproperty
                def LOSS(cls):
                    return cls("loss")
                
                @schemas.classproperty
                def DAMAGE(cls):
                    return cls("damage")
                
                @schemas.classproperty
                def DELAY(cls):
                    return cls("delay")
                
                @schemas.classproperty
                def THEFT(cls):
                    return cls("theft")
            reject_reason = schemas.StrSchema
        
            @staticmethod
            def claim_details() -> typing.Type['ClaimClaimDetails']:
                return ClaimClaimDetails
            
            
            class updated_ts(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'updated_ts':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class created_ts(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'created_ts':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "claim_id": claim_id,
                "order_id": order_id,
                "contract_id": contract_id,
                "payout_amount": payout_amount,
                "status": status,
                "claim_type": claim_type,
                "reject_reason": reject_reason,
                "claim_details": claim_details,
                "updated_ts": updated_ts,
                "created_ts": created_ts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["claim_id"]) -> MetaOapg.properties.claim_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_id"]) -> MetaOapg.properties.order_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_id"]) -> MetaOapg.properties.contract_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payout_amount"]) -> MetaOapg.properties.payout_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["claim_type"]) -> MetaOapg.properties.claim_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reject_reason"]) -> MetaOapg.properties.reject_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["claim_details"]) -> 'ClaimClaimDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_ts"]) -> MetaOapg.properties.updated_ts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_ts"]) -> MetaOapg.properties.created_ts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["claim_id", "order_id", "contract_id", "payout_amount", "status", "claim_type", "reject_reason", "claim_details", "updated_ts", "created_ts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["claim_id"]) -> typing.Union[MetaOapg.properties.claim_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_id"]) -> typing.Union[MetaOapg.properties.order_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_id"]) -> typing.Union[MetaOapg.properties.contract_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payout_amount"]) -> typing.Union[MetaOapg.properties.payout_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["claim_type"]) -> typing.Union[MetaOapg.properties.claim_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reject_reason"]) -> typing.Union[MetaOapg.properties.reject_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["claim_details"]) -> typing.Union['ClaimClaimDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_ts"]) -> typing.Union[MetaOapg.properties.updated_ts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_ts"]) -> typing.Union[MetaOapg.properties.created_ts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["claim_id", "order_id", "contract_id", "payout_amount", "status", "claim_type", "reject_reason", "claim_details", "updated_ts", "created_ts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        claim_id: typing.Union[MetaOapg.properties.claim_id, str, schemas.Unset] = schemas.unset,
        order_id: typing.Union[MetaOapg.properties.order_id, str, schemas.Unset] = schemas.unset,
        contract_id: typing.Union[MetaOapg.properties.contract_id, str, schemas.Unset] = schemas.unset,
        payout_amount: typing.Union[MetaOapg.properties.payout_amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        claim_type: typing.Union[MetaOapg.properties.claim_type, str, schemas.Unset] = schemas.unset,
        reject_reason: typing.Union[MetaOapg.properties.reject_reason, str, schemas.Unset] = schemas.unset,
        claim_details: typing.Union['ClaimClaimDetails', schemas.Unset] = schemas.unset,
        updated_ts: typing.Union[MetaOapg.properties.updated_ts, None, str, datetime, schemas.Unset] = schemas.unset,
        created_ts: typing.Union[MetaOapg.properties.created_ts, None, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Claim':
        return super().__new__(
            cls,
            *args,
            claim_id=claim_id,
            order_id=order_id,
            contract_id=contract_id,
            payout_amount=payout_amount,
            status=status,
            claim_type=claim_type,
            reject_reason=reject_reason,
            claim_details=claim_details,
            updated_ts=updated_ts,
            created_ts=created_ts,
            _configuration=_configuration,
            **kwargs,
        )

from seel_python_sdk.model.claim_claim_details import ClaimClaimDetails
