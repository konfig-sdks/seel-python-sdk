# coding: utf-8

"""
    Seel API

    Seel API

    The version of the OpenAPI document: 1.3.0
    Generated by: https://konfigthis.com
"""

from seel_python_sdk.paths.partner_invoices_invoice_id.get import GetInvoiceById
from seel_python_sdk.paths.partner_invoices.get import ListInvoices
from seel_python_sdk.apis.tags.invoice_api_raw import InvoiceApiRaw


class InvoiceApi(
    GetInvoiceById,
    ListInvoices,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: InvoiceApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = InvoiceApiRaw(api_client)
