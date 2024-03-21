operation_parameter_map = {
    '/{partner}/claims-GET': {
        'parameters': [
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'order_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/{partner}/claims/{claim_id}-GET': {
        'parameters': [
            {
                'name': 'claim_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/contracts/{contract_id}-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/contracts-GET': {
        'parameters': [
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'order_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/{partner}/events-POST': {
        'parameters': [
            {
                'name': 'session_id'
            },
            {
                'name': 'customer_id'
            },
            {
                'name': 'event_source'
            },
            {
                'name': 'event_type'
            },
            {
                'name': 'event_info'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'event_ts'
            },
            {
                'name': 'device_id'
            },
            {
                'name': 'client_ip'
            },
        ]
    },
    '/{partner}/orders/{order_id}/fulfillments/{fulfillment_id}/cancel-POST': {
        'parameters': [
            {
                'name': 'order_id'
            },
            {
                'name': 'fulfillment_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/orders/{order_id}/fulfillments-POST': {
        'parameters': [
            {
                'name': 'fulfillment_id'
            },
            {
                'name': 'created_ts'
            },
            {
                'name': 'updated_ts'
            },
            {
                'name': 'tracking_number'
            },
            {
                'name': 'carrier'
            },
            {
                'name': 'shipment_status'
            },
            {
                'name': 'line_items'
            },
            {
                'name': 'order_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'tracking_url'
            },
        ]
    },
    '/{partner}/orders/{order_id}/fulfillments/{fulfillment_id}-GET': {
        'parameters': [
            {
                'name': 'order_id'
            },
            {
                'name': 'fulfillment_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/orders/{order_id}/fulfillments-GET': {
        'parameters': [
            {
                'name': 'order_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/{partner}/orders/{order_id}/fulfillments/{fulfillment_id}-POST': {
        'parameters': [
            {
                'name': 'updated_ts'
            },
            {
                'name': 'tracking_number'
            },
            {
                'name': 'carrier'
            },
            {
                'name': 'shipment_status'
            },
            {
                'name': 'line_items'
            },
            {
                'name': 'order_id'
            },
            {
                'name': 'fulfillment_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'tracking_url'
            },
        ]
    },
    '/{partner}/invoices/{invoice_id}-GET': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/invoices-GET': {
        'parameters': [
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/{partner}/merchants-POST': {
        'parameters': [
            {
                'name': 'shop_id'
            },
            {
                'name': 'admin_domain'
            },
            {
                'name': 'shop_domain'
            },
            {
                'name': 'shop_platform'
            },
            {
                'name': 'shop_currency'
            },
            {
                'name': 'shop_name'
            },
            {
                'name': 'contact_name'
            },
            {
                'name': 'contact_email'
            },
            {
                'name': 'seel_services'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'contact_phone_number'
            },
        ]
    },
    '/{partner}/merchants/{merchant_id}-GET': {
        'parameters': [
            {
                'name': 'merchant_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/merchants-GET': {
        'parameters': [
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/{partner}/merchants/{merchant_id}-POST': {
        'parameters': [
            {
                'name': 'merchant_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'shop_id'
            },
            {
                'name': 'admin_domain'
            },
            {
                'name': 'shop_domain'
            },
            {
                'name': 'shop_platform'
            },
            {
                'name': 'shop_currency'
            },
            {
                'name': 'shop_name'
            },
            {
                'name': 'contact_name'
            },
            {
                'name': 'contact_email'
            },
            {
                'name': 'contact_phone_number'
            },
            {
                'name': 'seel_services'
            },
        ]
    },
    '/{partner}/orders/batch-POST': {
        'parameters': [
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'orders'
            },
        ]
    },
    '/{partner}/orders/{order_id}/cancel-POST': {
        'parameters': [
            {
                'name': 'order_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/orders-POST': {
        'parameters': [
            {
                'name': 'order_id'
            },
            {
                'name': 'order_number'
            },
            {
                'name': 'session_id'
            },
            {
                'name': 'created_ts'
            },
            {
                'name': 'line_items'
            },
            {
                'name': 'shipping_address'
            },
            {
                'name': 'customer'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'cart_id'
            },
            {
                'name': 'merchant_id'
            },
            {
                'name': 'device_id'
            },
            {
                'name': 'client_ip'
            },
            {
                'name': 'seel_services'
            },
            {
                'name': 'extra_info'
            },
        ]
    },
    '/{partner}/orders/{order_id}-GET': {
        'parameters': [
            {
                'name': 'order_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/orders/{order_id}-POST': {
        'parameters': [
            {
                'name': 'updated_ts'
            },
            {
                'name': 'order_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'line_items'
            },
            {
                'name': 'shipping_address'
            },
            {
                'name': 'customer'
            },
            {
                'name': 'extra_info'
            },
        ]
    },
    '/{partner}/products-POST': {
        'parameters': [
            {
                'name': 'product_id'
            },
            {
                'name': 'product_title'
            },
            {
                'name': 'brand_name'
            },
            {
                'name': 'price'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'merchant_id'
            },
            {
                'name': 'variant_id'
            },
            {
                'name': 'variant_title'
            },
            {
                'name': 'manufacturer'
            },
            {
                'name': 'category_1'
            },
            {
                'name': 'category_2'
            },
            {
                'name': 'category_3'
            },
            {
                'name': 'category_4'
            },
            {
                'name': 'product_description'
            },
            {
                'name': 'image_url'
            },
            {
                'name': 'requires_shipping'
            },
            {
                'name': 'model_number'
            },
            {
                'name': 'condition'
            },
            {
                'name': 'sku'
            },
            {
                'name': 'identifiers'
            },
            {
                'name': 'manufacturer_warranty'
            },
            {
                'name': 'dimensions'
            },
            {
                'name': 'weight'
            },
            {
                'name': 'product_attributes'
            },
            {
                'name': 'created_ts'
            },
            {
                'name': 'updated_ts'
            },
        ]
    },
    '/{partner}/products/batch-POST': {
        'parameters': [
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'products'
            },
        ]
    },
    '/{partner}/products/{product_id}-GET': {
        'parameters': [
            {
                'name': 'product_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/products/{product_id}/plans-GET': {
        'parameters': [
            {
                'name': 'product_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/products/{product_id}-DELETE': {
        'parameters': [
            {
                'name': 'product_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
    '/{partner}/products/{product_id}-POST': {
        'parameters': [
            {
                'name': 'product_id'
            },
            {
                'name': 'product_title'
            },
            {
                'name': 'brand_name'
            },
            {
                'name': 'price'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'product_id'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'merchant_id'
            },
            {
                'name': 'variant_id'
            },
            {
                'name': 'variant_title'
            },
            {
                'name': 'manufacturer'
            },
            {
                'name': 'category_1'
            },
            {
                'name': 'category_2'
            },
            {
                'name': 'category_3'
            },
            {
                'name': 'category_4'
            },
            {
                'name': 'product_description'
            },
            {
                'name': 'image_url'
            },
            {
                'name': 'requires_shipping'
            },
            {
                'name': 'model_number'
            },
            {
                'name': 'condition'
            },
            {
                'name': 'sku'
            },
            {
                'name': 'identifiers'
            },
            {
                'name': 'manufacturer_warranty'
            },
            {
                'name': 'dimensions'
            },
            {
                'name': 'weight'
            },
            {
                'name': 'product_attributes'
            },
            {
                'name': 'created_ts'
            },
            {
                'name': 'updated_ts'
            },
        ]
    },
    '/{partner}/quotes-POST': {
        'parameters': [
            {
                'name': 'session_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'line_items'
            },
            {
                'name': 'shipping_address'
            },
            {
                'name': 'customer'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'cart_id'
            },
            {
                'name': 'merchant_id'
            },
            {
                'name': 'device_id'
            },
            {
                'name': 'client_ip'
            },
            {
                'name': 'extra_info'
            },
        ]
    },
    '/{partner}/quotes/{quote_id}-GET': {
        'parameters': [
            {
                'name': 'quote_id'
            },
            {
                'name': 'X-Seel-API-Key'
            },
            {
                'name': 'X-Seel-API-Version'
            },
            {
                'name': 'partner'
            },
        ]
    },
};