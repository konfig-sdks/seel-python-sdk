# coding: utf-8

"""
    Seel API

    Seel API

    The version of the OpenAPI document: 1.3.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from seel_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from seel_python_sdk.api_response import AsyncGeneratorResponse
from seel_python_sdk import api_client, exceptions
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

from seel_python_sdk.model.product_add_new_product_request_dimensions import ProductAddNewProductRequestDimensions as ProductAddNewProductRequestDimensionsSchema
from seel_python_sdk.model.product_add_new_product_request_manufacturer_warranty import ProductAddNewProductRequestManufacturerWarranty as ProductAddNewProductRequestManufacturerWarrantySchema
from seel_python_sdk.model.product_add_new_product_request_product_attributes import ProductAddNewProductRequestProductAttributes as ProductAddNewProductRequestProductAttributesSchema
from seel_python_sdk.model.product import Product as ProductSchema
from seel_python_sdk.model.product_add_new_product_request import ProductAddNewProductRequest as ProductAddNewProductRequestSchema
from seel_python_sdk.model.product_add_new_product_request_identifiers import ProductAddNewProductRequestIdentifiers as ProductAddNewProductRequestIdentifiersSchema
from seel_python_sdk.model.product_add_new_product_request_weight import ProductAddNewProductRequestWeight as ProductAddNewProductRequestWeightSchema

from seel_python_sdk.type.product_add_new_product_request_product_attributes import ProductAddNewProductRequestProductAttributes
from seel_python_sdk.type.product_add_new_product_request_weight import ProductAddNewProductRequestWeight
from seel_python_sdk.type.product_add_new_product_request_identifiers import ProductAddNewProductRequestIdentifiers
from seel_python_sdk.type.product import Product
from seel_python_sdk.type.product_add_new_product_request_manufacturer_warranty import ProductAddNewProductRequestManufacturerWarranty
from seel_python_sdk.type.product_add_new_product_request_dimensions import ProductAddNewProductRequestDimensions
from seel_python_sdk.type.product_add_new_product_request import ProductAddNewProductRequest

from ...api_client import Dictionary
from seel_python_sdk.pydantic.product_add_new_product_request_manufacturer_warranty import ProductAddNewProductRequestManufacturerWarranty as ProductAddNewProductRequestManufacturerWarrantyPydantic
from seel_python_sdk.pydantic.product_add_new_product_request_product_attributes import ProductAddNewProductRequestProductAttributes as ProductAddNewProductRequestProductAttributesPydantic
from seel_python_sdk.pydantic.product_add_new_product_request_dimensions import ProductAddNewProductRequestDimensions as ProductAddNewProductRequestDimensionsPydantic
from seel_python_sdk.pydantic.product_add_new_product_request import ProductAddNewProductRequest as ProductAddNewProductRequestPydantic
from seel_python_sdk.pydantic.product_add_new_product_request_identifiers import ProductAddNewProductRequestIdentifiers as ProductAddNewProductRequestIdentifiersPydantic
from seel_python_sdk.pydantic.product_add_new_product_request_weight import ProductAddNewProductRequestWeight as ProductAddNewProductRequestWeightPydantic
from seel_python_sdk.pydantic.product import Product as ProductPydantic

# Header params
XSeelAPIKeySchema = schemas.StrSchema
XSeelAPIVersionSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'X-Seel-API-Key': typing.Union[XSeelAPIKeySchema, str, ],
        'X-Seel-API-Version': typing.Union[XSeelAPIVersionSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_seel_api_key = api_client.HeaderParameter(
    name="X-Seel-API-Key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XSeelAPIKeySchema,
    required=True,
)
request_header_x_seel_api_version = api_client.HeaderParameter(
    name="X-Seel-API-Version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XSeelAPIVersionSchema,
    required=True,
)
# Path params
PartnerSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'partner': typing.Union[PartnerSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_partner = api_client.PathParameter(
    name="partner",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PartnerSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ProductAddNewProductRequestSchema


request_body_product_add_new_product_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ProductSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Product


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Product


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_new_product_mapped_args(
        self,
        product_id: str,
        product_title: str,
        brand_name: str,
        price: typing.Union[int, float],
        currency: str,
        partner: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        merchant_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
        variant_title: typing.Optional[str] = None,
        manufacturer: typing.Optional[str] = None,
        category_1: typing.Optional[str] = None,
        category_2: typing.Optional[str] = None,
        category_3: typing.Optional[str] = None,
        category_4: typing.Optional[str] = None,
        product_description: typing.Optional[str] = None,
        image_url: typing.Optional[str] = None,
        requires_shipping: typing.Optional[bool] = None,
        model_number: typing.Optional[str] = None,
        condition: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        identifiers: typing.Optional[ProductAddNewProductRequestIdentifiers] = None,
        manufacturer_warranty: typing.Optional[ProductAddNewProductRequestManufacturerWarranty] = None,
        dimensions: typing.Optional[ProductAddNewProductRequestDimensions] = None,
        weight: typing.Optional[ProductAddNewProductRequestWeight] = None,
        product_attributes: typing.Optional[ProductAddNewProductRequestProductAttributes] = None,
        created_ts: typing.Optional[datetime] = None,
        updated_ts: typing.Optional[datetime] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if merchant_id is not None:
            _body["merchant_id"] = merchant_id
        if variant_id is not None:
            _body["variant_id"] = variant_id
        if product_id is not None:
            _body["product_id"] = product_id
        if product_title is not None:
            _body["product_title"] = product_title
        if variant_title is not None:
            _body["variant_title"] = variant_title
        if brand_name is not None:
            _body["brand_name"] = brand_name
        if manufacturer is not None:
            _body["manufacturer"] = manufacturer
        if category_1 is not None:
            _body["category_1"] = category_1
        if category_2 is not None:
            _body["category_2"] = category_2
        if category_3 is not None:
            _body["category_3"] = category_3
        if category_4 is not None:
            _body["category_4"] = category_4
        if product_description is not None:
            _body["product_description"] = product_description
        if image_url is not None:
            _body["image_url"] = image_url
        if price is not None:
            _body["price"] = price
        if currency is not None:
            _body["currency"] = currency
        if requires_shipping is not None:
            _body["requires_shipping"] = requires_shipping
        if model_number is not None:
            _body["model_number"] = model_number
        if condition is not None:
            _body["condition"] = condition
        if sku is not None:
            _body["sku"] = sku
        if identifiers is not None:
            _body["identifiers"] = identifiers
        if manufacturer_warranty is not None:
            _body["manufacturer_warranty"] = manufacturer_warranty
        if dimensions is not None:
            _body["dimensions"] = dimensions
        if weight is not None:
            _body["weight"] = weight
        if product_attributes is not None:
            _body["product_attributes"] = product_attributes
        if created_ts is not None:
            _body["created_ts"] = created_ts
        if updated_ts is not None:
            _body["updated_ts"] = updated_ts
        args.body = _body
        if x_seel_api_key is not None:
            _header_params["X-Seel-API-Key"] = x_seel_api_key
        if x_seel_api_version is not None:
            _header_params["X-Seel-API-Version"] = x_seel_api_version
        if partner is not None:
            _path_params["partner"] = partner
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aadd_new_product_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a product
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_partner,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_seel_api_key,
            request_header_x_seel_api_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{partner}/products',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_product_add_new_product_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _add_new_product_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a product
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_partner,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_seel_api_key,
            request_header_x_seel_api_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{partner}/products',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_product_add_new_product_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class AddNewProductRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_new_product(
        self,
        product_id: str,
        product_title: str,
        brand_name: str,
        price: typing.Union[int, float],
        currency: str,
        partner: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        merchant_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
        variant_title: typing.Optional[str] = None,
        manufacturer: typing.Optional[str] = None,
        category_1: typing.Optional[str] = None,
        category_2: typing.Optional[str] = None,
        category_3: typing.Optional[str] = None,
        category_4: typing.Optional[str] = None,
        product_description: typing.Optional[str] = None,
        image_url: typing.Optional[str] = None,
        requires_shipping: typing.Optional[bool] = None,
        model_number: typing.Optional[str] = None,
        condition: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        identifiers: typing.Optional[ProductAddNewProductRequestIdentifiers] = None,
        manufacturer_warranty: typing.Optional[ProductAddNewProductRequestManufacturerWarranty] = None,
        dimensions: typing.Optional[ProductAddNewProductRequestDimensions] = None,
        weight: typing.Optional[ProductAddNewProductRequestWeight] = None,
        product_attributes: typing.Optional[ProductAddNewProductRequestProductAttributes] = None,
        created_ts: typing.Optional[datetime] = None,
        updated_ts: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_new_product_mapped_args(
            product_id=product_id,
            product_title=product_title,
            brand_name=brand_name,
            price=price,
            currency=currency,
            partner=partner,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            merchant_id=merchant_id,
            variant_id=variant_id,
            variant_title=variant_title,
            manufacturer=manufacturer,
            category_1=category_1,
            category_2=category_2,
            category_3=category_3,
            category_4=category_4,
            product_description=product_description,
            image_url=image_url,
            requires_shipping=requires_shipping,
            model_number=model_number,
            condition=condition,
            sku=sku,
            identifiers=identifiers,
            manufacturer_warranty=manufacturer_warranty,
            dimensions=dimensions,
            weight=weight,
            product_attributes=product_attributes,
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
        return await self._aadd_new_product_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def add_new_product(
        self,
        product_id: str,
        product_title: str,
        brand_name: str,
        price: typing.Union[int, float],
        currency: str,
        partner: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        merchant_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
        variant_title: typing.Optional[str] = None,
        manufacturer: typing.Optional[str] = None,
        category_1: typing.Optional[str] = None,
        category_2: typing.Optional[str] = None,
        category_3: typing.Optional[str] = None,
        category_4: typing.Optional[str] = None,
        product_description: typing.Optional[str] = None,
        image_url: typing.Optional[str] = None,
        requires_shipping: typing.Optional[bool] = None,
        model_number: typing.Optional[str] = None,
        condition: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        identifiers: typing.Optional[ProductAddNewProductRequestIdentifiers] = None,
        manufacturer_warranty: typing.Optional[ProductAddNewProductRequestManufacturerWarranty] = None,
        dimensions: typing.Optional[ProductAddNewProductRequestDimensions] = None,
        weight: typing.Optional[ProductAddNewProductRequestWeight] = None,
        product_attributes: typing.Optional[ProductAddNewProductRequestProductAttributes] = None,
        created_ts: typing.Optional[datetime] = None,
        updated_ts: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_new_product_mapped_args(
            product_id=product_id,
            product_title=product_title,
            brand_name=brand_name,
            price=price,
            currency=currency,
            partner=partner,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            merchant_id=merchant_id,
            variant_id=variant_id,
            variant_title=variant_title,
            manufacturer=manufacturer,
            category_1=category_1,
            category_2=category_2,
            category_3=category_3,
            category_4=category_4,
            product_description=product_description,
            image_url=image_url,
            requires_shipping=requires_shipping,
            model_number=model_number,
            condition=condition,
            sku=sku,
            identifiers=identifiers,
            manufacturer_warranty=manufacturer_warranty,
            dimensions=dimensions,
            weight=weight,
            product_attributes=product_attributes,
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
        return self._add_new_product_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class AddNewProduct(BaseApi):

    async def aadd_new_product(
        self,
        product_id: str,
        product_title: str,
        brand_name: str,
        price: typing.Union[int, float],
        currency: str,
        partner: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        merchant_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
        variant_title: typing.Optional[str] = None,
        manufacturer: typing.Optional[str] = None,
        category_1: typing.Optional[str] = None,
        category_2: typing.Optional[str] = None,
        category_3: typing.Optional[str] = None,
        category_4: typing.Optional[str] = None,
        product_description: typing.Optional[str] = None,
        image_url: typing.Optional[str] = None,
        requires_shipping: typing.Optional[bool] = None,
        model_number: typing.Optional[str] = None,
        condition: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        identifiers: typing.Optional[ProductAddNewProductRequestIdentifiers] = None,
        manufacturer_warranty: typing.Optional[ProductAddNewProductRequestManufacturerWarranty] = None,
        dimensions: typing.Optional[ProductAddNewProductRequestDimensions] = None,
        weight: typing.Optional[ProductAddNewProductRequestWeight] = None,
        product_attributes: typing.Optional[ProductAddNewProductRequestProductAttributes] = None,
        created_ts: typing.Optional[datetime] = None,
        updated_ts: typing.Optional[datetime] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProductPydantic:
        raw_response = await self.raw.aadd_new_product(
            product_id=product_id,
            product_title=product_title,
            brand_name=brand_name,
            price=price,
            currency=currency,
            partner=partner,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            merchant_id=merchant_id,
            variant_id=variant_id,
            variant_title=variant_title,
            manufacturer=manufacturer,
            category_1=category_1,
            category_2=category_2,
            category_3=category_3,
            category_4=category_4,
            product_description=product_description,
            image_url=image_url,
            requires_shipping=requires_shipping,
            model_number=model_number,
            condition=condition,
            sku=sku,
            identifiers=identifiers,
            manufacturer_warranty=manufacturer_warranty,
            dimensions=dimensions,
            weight=weight,
            product_attributes=product_attributes,
            created_ts=created_ts,
            updated_ts=updated_ts,
            **kwargs,
        )
        if validate:
            return ProductPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProductPydantic, raw_response.body)
    
    
    def add_new_product(
        self,
        product_id: str,
        product_title: str,
        brand_name: str,
        price: typing.Union[int, float],
        currency: str,
        partner: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        merchant_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
        variant_title: typing.Optional[str] = None,
        manufacturer: typing.Optional[str] = None,
        category_1: typing.Optional[str] = None,
        category_2: typing.Optional[str] = None,
        category_3: typing.Optional[str] = None,
        category_4: typing.Optional[str] = None,
        product_description: typing.Optional[str] = None,
        image_url: typing.Optional[str] = None,
        requires_shipping: typing.Optional[bool] = None,
        model_number: typing.Optional[str] = None,
        condition: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        identifiers: typing.Optional[ProductAddNewProductRequestIdentifiers] = None,
        manufacturer_warranty: typing.Optional[ProductAddNewProductRequestManufacturerWarranty] = None,
        dimensions: typing.Optional[ProductAddNewProductRequestDimensions] = None,
        weight: typing.Optional[ProductAddNewProductRequestWeight] = None,
        product_attributes: typing.Optional[ProductAddNewProductRequestProductAttributes] = None,
        created_ts: typing.Optional[datetime] = None,
        updated_ts: typing.Optional[datetime] = None,
        validate: bool = False,
    ) -> ProductPydantic:
        raw_response = self.raw.add_new_product(
            product_id=product_id,
            product_title=product_title,
            brand_name=brand_name,
            price=price,
            currency=currency,
            partner=partner,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            merchant_id=merchant_id,
            variant_id=variant_id,
            variant_title=variant_title,
            manufacturer=manufacturer,
            category_1=category_1,
            category_2=category_2,
            category_3=category_3,
            category_4=category_4,
            product_description=product_description,
            image_url=image_url,
            requires_shipping=requires_shipping,
            model_number=model_number,
            condition=condition,
            sku=sku,
            identifiers=identifiers,
            manufacturer_warranty=manufacturer_warranty,
            dimensions=dimensions,
            weight=weight,
            product_attributes=product_attributes,
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
        if validate:
            return ProductPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProductPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        product_id: str,
        product_title: str,
        brand_name: str,
        price: typing.Union[int, float],
        currency: str,
        partner: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        merchant_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
        variant_title: typing.Optional[str] = None,
        manufacturer: typing.Optional[str] = None,
        category_1: typing.Optional[str] = None,
        category_2: typing.Optional[str] = None,
        category_3: typing.Optional[str] = None,
        category_4: typing.Optional[str] = None,
        product_description: typing.Optional[str] = None,
        image_url: typing.Optional[str] = None,
        requires_shipping: typing.Optional[bool] = None,
        model_number: typing.Optional[str] = None,
        condition: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        identifiers: typing.Optional[ProductAddNewProductRequestIdentifiers] = None,
        manufacturer_warranty: typing.Optional[ProductAddNewProductRequestManufacturerWarranty] = None,
        dimensions: typing.Optional[ProductAddNewProductRequestDimensions] = None,
        weight: typing.Optional[ProductAddNewProductRequestWeight] = None,
        product_attributes: typing.Optional[ProductAddNewProductRequestProductAttributes] = None,
        created_ts: typing.Optional[datetime] = None,
        updated_ts: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_new_product_mapped_args(
            product_id=product_id,
            product_title=product_title,
            brand_name=brand_name,
            price=price,
            currency=currency,
            partner=partner,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            merchant_id=merchant_id,
            variant_id=variant_id,
            variant_title=variant_title,
            manufacturer=manufacturer,
            category_1=category_1,
            category_2=category_2,
            category_3=category_3,
            category_4=category_4,
            product_description=product_description,
            image_url=image_url,
            requires_shipping=requires_shipping,
            model_number=model_number,
            condition=condition,
            sku=sku,
            identifiers=identifiers,
            manufacturer_warranty=manufacturer_warranty,
            dimensions=dimensions,
            weight=weight,
            product_attributes=product_attributes,
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
        return await self._aadd_new_product_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        product_id: str,
        product_title: str,
        brand_name: str,
        price: typing.Union[int, float],
        currency: str,
        partner: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        merchant_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
        variant_title: typing.Optional[str] = None,
        manufacturer: typing.Optional[str] = None,
        category_1: typing.Optional[str] = None,
        category_2: typing.Optional[str] = None,
        category_3: typing.Optional[str] = None,
        category_4: typing.Optional[str] = None,
        product_description: typing.Optional[str] = None,
        image_url: typing.Optional[str] = None,
        requires_shipping: typing.Optional[bool] = None,
        model_number: typing.Optional[str] = None,
        condition: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        identifiers: typing.Optional[ProductAddNewProductRequestIdentifiers] = None,
        manufacturer_warranty: typing.Optional[ProductAddNewProductRequestManufacturerWarranty] = None,
        dimensions: typing.Optional[ProductAddNewProductRequestDimensions] = None,
        weight: typing.Optional[ProductAddNewProductRequestWeight] = None,
        product_attributes: typing.Optional[ProductAddNewProductRequestProductAttributes] = None,
        created_ts: typing.Optional[datetime] = None,
        updated_ts: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_new_product_mapped_args(
            product_id=product_id,
            product_title=product_title,
            brand_name=brand_name,
            price=price,
            currency=currency,
            partner=partner,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            merchant_id=merchant_id,
            variant_id=variant_id,
            variant_title=variant_title,
            manufacturer=manufacturer,
            category_1=category_1,
            category_2=category_2,
            category_3=category_3,
            category_4=category_4,
            product_description=product_description,
            image_url=image_url,
            requires_shipping=requires_shipping,
            model_number=model_number,
            condition=condition,
            sku=sku,
            identifiers=identifiers,
            manufacturer_warranty=manufacturer_warranty,
            dimensions=dimensions,
            weight=weight,
            product_attributes=product_attributes,
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
        return self._add_new_product_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

