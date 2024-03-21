# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from seel_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    PARTNER_MERCHANTS = "/{partner}/merchants"
    PARTNER_MERCHANTS_MERCHANT_ID = "/{partner}/merchants/{merchant_id}"
    PARTNER_QUOTES = "/{partner}/quotes"
    PARTNER_QUOTES_QUOTE_ID = "/{partner}/quotes/{quote_id}"
    PARTNER_PRODUCTS = "/{partner}/products"
    PARTNER_PRODUCTS_BATCH = "/{partner}/products/batch"
    PARTNER_PRODUCTS_PRODUCT_ID = "/{partner}/products/{product_id}"
    PARTNER_PRODUCTS_PRODUCT_ID_PLANS = "/{partner}/products/{product_id}/plans"
    PARTNER_ORDERS = "/{partner}/orders"
    PARTNER_ORDERS_BATCH = "/{partner}/orders/batch"
    PARTNER_ORDERS_ORDER_ID = "/{partner}/orders/{order_id}"
    PARTNER_ORDERS_ORDER_ID_CANCEL = "/{partner}/orders/{order_id}/cancel"
    PARTNER_ORDERS_ORDER_ID_FULFILLMENTS = "/{partner}/orders/{order_id}/fulfillments"
    PARTNER_ORDERS_ORDER_ID_FULFILLMENTS_FULFILLMENT_ID = "/{partner}/orders/{order_id}/fulfillments/{fulfillment_id}"
    PARTNER_ORDERS_ORDER_ID_FULFILLMENTS_FULFILLMENT_ID_CANCEL = "/{partner}/orders/{order_id}/fulfillments/{fulfillment_id}/cancel"
    PARTNER_CONTRACTS = "/{partner}/contracts"
    PARTNER_CONTRACTS_CONTRACT_ID = "/{partner}/contracts/{contract_id}"
    PARTNER_CLAIMS = "/{partner}/claims"
    PARTNER_CLAIMS_CLAIM_ID = "/{partner}/claims/{claim_id}"
    PARTNER_INVOICES = "/{partner}/invoices"
    PARTNER_INVOICES_INVOICE_ID = "/{partner}/invoices/{invoice_id}"
    PARTNER_EVENTS = "/{partner}/events"
