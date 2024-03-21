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

from seel_python_sdk.model.fulfillment_list_fulfillments_response import FulfillmentListFulfillmentsResponse as FulfillmentListFulfillmentsResponseSchema

from seel_python_sdk.type.fulfillment_list_fulfillments_response import FulfillmentListFulfillmentsResponse

from ...api_client import Dictionary
from seel_python_sdk.pydantic.fulfillment_list_fulfillments_response import FulfillmentListFulfillmentsResponse as FulfillmentListFulfillmentsResponsePydantic

# Query params
PageSchema = schemas.IntSchema
PageSizeSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
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
OrderIdSchema = schemas.StrSchema
PartnerSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'order_id': typing.Union[OrderIdSchema, str, ],
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


request_path_order_id = api_client.PathParameter(
    name="order_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrderIdSchema,
    required=True,
)
request_path_partner = api_client.PathParameter(
    name="partner",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PartnerSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = FulfillmentListFulfillmentsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FulfillmentListFulfillmentsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FulfillmentListFulfillmentsResponse


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

    def _list_fulfillments_mapped_args(
        self,
        order_id: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        if page is not None:
            _query_params["page"] = page
        if page_size is not None:
            _query_params["page_size"] = page_size
        if x_seel_api_key is not None:
            _header_params["X-Seel-API-Key"] = x_seel_api_key
        if x_seel_api_version is not None:
            _header_params["X-Seel-API-Version"] = x_seel_api_version
        if order_id is not None:
            _path_params["order_id"] = order_id
        if partner is not None:
            _path_params["partner"] = partner
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _alist_fulfillments_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List fulfillments
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_order_id,
            request_path_partner,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_page_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{partner}/orders/{order_id}/fulfillments',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_fulfillments_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List fulfillments
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_order_id,
            request_path_partner,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_page_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{partner}/orders/{order_id}/fulfillments',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListFulfillmentsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_fulfillments(
        self,
        order_id: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_fulfillments_mapped_args(
            order_id=order_id,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            page=page,
            page_size=page_size,
        )
        return await self._alist_fulfillments_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def list_fulfillments(
        self,
        order_id: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_fulfillments_mapped_args(
            order_id=order_id,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            page=page,
            page_size=page_size,
        )
        return self._list_fulfillments_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class ListFulfillments(BaseApi):

    async def alist_fulfillments(
        self,
        order_id: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> FulfillmentListFulfillmentsResponsePydantic:
        raw_response = await self.raw.alist_fulfillments(
            order_id=order_id,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            page=page,
            page_size=page_size,
            **kwargs,
        )
        if validate:
            return FulfillmentListFulfillmentsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FulfillmentListFulfillmentsResponsePydantic, raw_response.body)
    
    
    def list_fulfillments(
        self,
        order_id: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
    ) -> FulfillmentListFulfillmentsResponsePydantic:
        raw_response = self.raw.list_fulfillments(
            order_id=order_id,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            page=page,
            page_size=page_size,
        )
        if validate:
            return FulfillmentListFulfillmentsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FulfillmentListFulfillmentsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        order_id: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_fulfillments_mapped_args(
            order_id=order_id,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            page=page,
            page_size=page_size,
        )
        return await self._alist_fulfillments_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        order_id: str,
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_fulfillments_mapped_args(
            order_id=order_id,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            page=page,
            page_size=page_size,
        )
        return self._list_fulfillments_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

