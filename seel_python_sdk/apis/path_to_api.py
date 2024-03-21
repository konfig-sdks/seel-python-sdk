import typing_extensions

from seel_python_sdk.paths import PathValues
from seel_python_sdk.apis.paths.partner_merchants import PartnerMerchants
from seel_python_sdk.apis.paths.partner_merchants_merchant_id import PartnerMerchantsMerchantId
from seel_python_sdk.apis.paths.partner_quotes import PartnerQuotes
from seel_python_sdk.apis.paths.partner_quotes_quote_id import PartnerQuotesQuoteId
from seel_python_sdk.apis.paths.partner_products import PartnerProducts
from seel_python_sdk.apis.paths.partner_products_batch import PartnerProductsBatch
from seel_python_sdk.apis.paths.partner_products_product_id import PartnerProductsProductId
from seel_python_sdk.apis.paths.partner_products_product_id_plans import PartnerProductsProductIdPlans
from seel_python_sdk.apis.paths.partner_orders import PartnerOrders
from seel_python_sdk.apis.paths.partner_orders_batch import PartnerOrdersBatch
from seel_python_sdk.apis.paths.partner_orders_order_id import PartnerOrdersOrderId
from seel_python_sdk.apis.paths.partner_orders_order_id_cancel import PartnerOrdersOrderIdCancel
from seel_python_sdk.apis.paths.partner_orders_order_id_fulfillments import PartnerOrdersOrderIdFulfillments
from seel_python_sdk.apis.paths.partner_orders_order_id_fulfillments_fulfillment_id import PartnerOrdersOrderIdFulfillmentsFulfillmentId
from seel_python_sdk.apis.paths.partner_orders_order_id_fulfillments_fulfillment_id_cancel import PartnerOrdersOrderIdFulfillmentsFulfillmentIdCancel
from seel_python_sdk.apis.paths.partner_contracts import PartnerContracts
from seel_python_sdk.apis.paths.partner_contracts_contract_id import PartnerContractsContractId
from seel_python_sdk.apis.paths.partner_claims import PartnerClaims
from seel_python_sdk.apis.paths.partner_claims_claim_id import PartnerClaimsClaimId
from seel_python_sdk.apis.paths.partner_invoices import PartnerInvoices
from seel_python_sdk.apis.paths.partner_invoices_invoice_id import PartnerInvoicesInvoiceId
from seel_python_sdk.apis.paths.partner_events import PartnerEvents

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PARTNER_MERCHANTS: PartnerMerchants,
        PathValues.PARTNER_MERCHANTS_MERCHANT_ID: PartnerMerchantsMerchantId,
        PathValues.PARTNER_QUOTES: PartnerQuotes,
        PathValues.PARTNER_QUOTES_QUOTE_ID: PartnerQuotesQuoteId,
        PathValues.PARTNER_PRODUCTS: PartnerProducts,
        PathValues.PARTNER_PRODUCTS_BATCH: PartnerProductsBatch,
        PathValues.PARTNER_PRODUCTS_PRODUCT_ID: PartnerProductsProductId,
        PathValues.PARTNER_PRODUCTS_PRODUCT_ID_PLANS: PartnerProductsProductIdPlans,
        PathValues.PARTNER_ORDERS: PartnerOrders,
        PathValues.PARTNER_ORDERS_BATCH: PartnerOrdersBatch,
        PathValues.PARTNER_ORDERS_ORDER_ID: PartnerOrdersOrderId,
        PathValues.PARTNER_ORDERS_ORDER_ID_CANCEL: PartnerOrdersOrderIdCancel,
        PathValues.PARTNER_ORDERS_ORDER_ID_FULFILLMENTS: PartnerOrdersOrderIdFulfillments,
        PathValues.PARTNER_ORDERS_ORDER_ID_FULFILLMENTS_FULFILLMENT_ID: PartnerOrdersOrderIdFulfillmentsFulfillmentId,
        PathValues.PARTNER_ORDERS_ORDER_ID_FULFILLMENTS_FULFILLMENT_ID_CANCEL: PartnerOrdersOrderIdFulfillmentsFulfillmentIdCancel,
        PathValues.PARTNER_CONTRACTS: PartnerContracts,
        PathValues.PARTNER_CONTRACTS_CONTRACT_ID: PartnerContractsContractId,
        PathValues.PARTNER_CLAIMS: PartnerClaims,
        PathValues.PARTNER_CLAIMS_CLAIM_ID: PartnerClaimsClaimId,
        PathValues.PARTNER_INVOICES: PartnerInvoices,
        PathValues.PARTNER_INVOICES_INVOICE_ID: PartnerInvoicesInvoiceId,
        PathValues.PARTNER_EVENTS: PartnerEvents,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PARTNER_MERCHANTS: PartnerMerchants,
        PathValues.PARTNER_MERCHANTS_MERCHANT_ID: PartnerMerchantsMerchantId,
        PathValues.PARTNER_QUOTES: PartnerQuotes,
        PathValues.PARTNER_QUOTES_QUOTE_ID: PartnerQuotesQuoteId,
        PathValues.PARTNER_PRODUCTS: PartnerProducts,
        PathValues.PARTNER_PRODUCTS_BATCH: PartnerProductsBatch,
        PathValues.PARTNER_PRODUCTS_PRODUCT_ID: PartnerProductsProductId,
        PathValues.PARTNER_PRODUCTS_PRODUCT_ID_PLANS: PartnerProductsProductIdPlans,
        PathValues.PARTNER_ORDERS: PartnerOrders,
        PathValues.PARTNER_ORDERS_BATCH: PartnerOrdersBatch,
        PathValues.PARTNER_ORDERS_ORDER_ID: PartnerOrdersOrderId,
        PathValues.PARTNER_ORDERS_ORDER_ID_CANCEL: PartnerOrdersOrderIdCancel,
        PathValues.PARTNER_ORDERS_ORDER_ID_FULFILLMENTS: PartnerOrdersOrderIdFulfillments,
        PathValues.PARTNER_ORDERS_ORDER_ID_FULFILLMENTS_FULFILLMENT_ID: PartnerOrdersOrderIdFulfillmentsFulfillmentId,
        PathValues.PARTNER_ORDERS_ORDER_ID_FULFILLMENTS_FULFILLMENT_ID_CANCEL: PartnerOrdersOrderIdFulfillmentsFulfillmentIdCancel,
        PathValues.PARTNER_CONTRACTS: PartnerContracts,
        PathValues.PARTNER_CONTRACTS_CONTRACT_ID: PartnerContractsContractId,
        PathValues.PARTNER_CLAIMS: PartnerClaims,
        PathValues.PARTNER_CLAIMS_CLAIM_ID: PartnerClaimsClaimId,
        PathValues.PARTNER_INVOICES: PartnerInvoices,
        PathValues.PARTNER_INVOICES_INVOICE_ID: PartnerInvoicesInvoiceId,
        PathValues.PARTNER_EVENTS: PartnerEvents,
    }
)
