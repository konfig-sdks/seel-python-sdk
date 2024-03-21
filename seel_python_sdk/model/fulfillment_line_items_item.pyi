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


class FulfillmentLineItemsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "line_item_id",
            "quantity",
        }
        
        class properties:
            line_item_id = schemas.StrSchema
            quantity = schemas.IntSchema
            __annotations__ = {
                "line_item_id": line_item_id,
                "quantity": quantity,
            }
    
    line_item_id: MetaOapg.properties.line_item_id
    quantity: MetaOapg.properties.quantity
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line_item_id"]) -> MetaOapg.properties.line_item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["line_item_id", "quantity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line_item_id"]) -> MetaOapg.properties.line_item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["line_item_id", "quantity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        line_item_id: typing.Union[MetaOapg.properties.line_item_id, str, ],
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FulfillmentLineItemsItem':
        return super().__new__(
            cls,
            *args,
            line_item_id=line_item_id,
            quantity=quantity,
            _configuration=_configuration,
            **kwargs,
        )
