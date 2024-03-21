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


class OrderCreateNewOrderRequestSeelServices(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The list of Seel services of the order.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OrderCreateNewOrderRequestSeelServicesItem']:
            return OrderCreateNewOrderRequestSeelServicesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OrderCreateNewOrderRequestSeelServicesItem'], typing.List['OrderCreateNewOrderRequestSeelServicesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OrderCreateNewOrderRequestSeelServices':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OrderCreateNewOrderRequestSeelServicesItem':
        return super().__getitem__(i)

from seel_python_sdk.model.order_create_new_order_request_seel_services_item import OrderCreateNewOrderRequestSeelServicesItem