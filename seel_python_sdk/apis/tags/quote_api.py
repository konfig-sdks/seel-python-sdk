# coding: utf-8

"""
    Seel API

    Seel API

    The version of the OpenAPI document: 1.3.0
    Generated by: https://konfigthis.com
"""

from seel_python_sdk.paths.partner_quotes.post import GenerateQuote
from seel_python_sdk.paths.partner_quotes_quote_id.get import GetById
from seel_python_sdk.apis.tags.quote_api_raw import QuoteApiRaw


class QuoteApi(
    GenerateQuote,
    GetById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: QuoteApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = QuoteApiRaw(api_client)
