# coding: utf-8
"""
    Seel API

    Seel API

    The version of the OpenAPI document: 1.3.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from seel_python_sdk.client_custom import ClientCustom
from seel_python_sdk.configuration import Configuration
from seel_python_sdk.api_client import ApiClient
from seel_python_sdk.type_util import copy_signature
from seel_python_sdk.apis.tags.claim_api import ClaimApi
from seel_python_sdk.apis.tags.contract_api import ContractApi
from seel_python_sdk.apis.tags.event_api import EventApi
from seel_python_sdk.apis.tags.fulfillment_api import FulfillmentApi
from seel_python_sdk.apis.tags.invoice_api import InvoiceApi
from seel_python_sdk.apis.tags.merchant_api import MerchantApi
from seel_python_sdk.apis.tags.order_api import OrderApi
from seel_python_sdk.apis.tags.product_api import ProductApi
from seel_python_sdk.apis.tags.quote_api import QuoteApi



class Seel(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.claim: ClaimApi = ClaimApi(api_client)
        self.contract: ContractApi = ContractApi(api_client)
        self.event: EventApi = EventApi(api_client)
        self.fulfillment: FulfillmentApi = FulfillmentApi(api_client)
        self.invoice: InvoiceApi = InvoiceApi(api_client)
        self.merchant: MerchantApi = MerchantApi(api_client)
        self.order: OrderApi = OrderApi(api_client)
        self.product: ProductApi = ProductApi(api_client)
        self.quote: QuoteApi = QuoteApi(api_client)
