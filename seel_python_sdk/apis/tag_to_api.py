import typing_extensions

from seel_python_sdk.apis.tags import TagValues
from seel_python_sdk.apis.tags.product_api import ProductApi
from seel_python_sdk.apis.tags.order_api import OrderApi
from seel_python_sdk.apis.tags.fulfillment_api import FulfillmentApi
from seel_python_sdk.apis.tags.merchant_api import MerchantApi
from seel_python_sdk.apis.tags.quote_api import QuoteApi
from seel_python_sdk.apis.tags.contract_api import ContractApi
from seel_python_sdk.apis.tags.claim_api import ClaimApi
from seel_python_sdk.apis.tags.invoice_api import InvoiceApi
from seel_python_sdk.apis.tags.event_api import EventApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PRODUCT: ProductApi,
        TagValues.ORDER: OrderApi,
        TagValues.FULFILLMENT: FulfillmentApi,
        TagValues.MERCHANT: MerchantApi,
        TagValues.QUOTE: QuoteApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.CLAIM: ClaimApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.EVENT: EventApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PRODUCT: ProductApi,
        TagValues.ORDER: OrderApi,
        TagValues.FULFILLMENT: FulfillmentApi,
        TagValues.MERCHANT: MerchantApi,
        TagValues.QUOTE: QuoteApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.CLAIM: ClaimApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.EVENT: EventApi,
    }
)
