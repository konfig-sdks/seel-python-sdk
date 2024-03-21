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


class InvoiceInvoiceItems(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of contracts associated with this invoice.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InvoiceInvoiceItemsItem']:
            return InvoiceInvoiceItemsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InvoiceInvoiceItemsItem'], typing.List['InvoiceInvoiceItemsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InvoiceInvoiceItems':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InvoiceInvoiceItemsItem':
        return super().__getitem__(i)

from seel_python_sdk.model.invoice_invoice_items_item import InvoiceInvoiceItemsItem
