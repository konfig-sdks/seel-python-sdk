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

from seel_python_sdk.model.event_create_new_event_request import EventCreateNewEventRequest as EventCreateNewEventRequestSchema
from seel_python_sdk.model.event import Event as EventSchema

from seel_python_sdk.type.event_create_new_event_request import EventCreateNewEventRequest
from seel_python_sdk.type.event import Event

from ...api_client import Dictionary
from seel_python_sdk.pydantic.event_create_new_event_request import EventCreateNewEventRequest as EventCreateNewEventRequestPydantic
from seel_python_sdk.pydantic.event import Event as EventPydantic

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
SchemaForRequestBodyApplicationJson = EventCreateNewEventRequestSchema


request_body_event_create_new_event_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = EventSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Event


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Event


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

    def _create_new_event_mapped_args(
        self,
        session_id: str,
        customer_id: str,
        event_source: str,
        event_type: str,
        event_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        event_ts: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_ip: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if session_id is not None:
            _body["session_id"] = session_id
        if event_ts is not None:
            _body["event_ts"] = event_ts
        if customer_id is not None:
            _body["customer_id"] = customer_id
        if device_id is not None:
            _body["device_id"] = device_id
        if client_ip is not None:
            _body["client_ip"] = client_ip
        if event_source is not None:
            _body["event_source"] = event_source
        if event_type is not None:
            _body["event_type"] = event_type
        if event_info is not None:
            _body["event_info"] = event_info
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

    async def _acreate_new_event_oapg(
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
        Create events
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
            path_template='/{partner}/events',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_event_create_new_event_request.serialize(body, content_type)
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


    def _create_new_event_oapg(
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
        Create events
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
            path_template='/{partner}/events',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_event_create_new_event_request.serialize(body, content_type)
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


class CreateNewEventRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_event(
        self,
        session_id: str,
        customer_id: str,
        event_source: str,
        event_type: str,
        event_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        event_ts: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_ip: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_event_mapped_args(
            session_id=session_id,
            customer_id=customer_id,
            event_source=event_source,
            event_type=event_type,
            event_info=event_info,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            event_ts=event_ts,
            device_id=device_id,
            client_ip=client_ip,
        )
        return await self._acreate_new_event_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_event(
        self,
        session_id: str,
        customer_id: str,
        event_source: str,
        event_type: str,
        event_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        event_ts: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_ip: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_event_mapped_args(
            session_id=session_id,
            customer_id=customer_id,
            event_source=event_source,
            event_type=event_type,
            event_info=event_info,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            event_ts=event_ts,
            device_id=device_id,
            client_ip=client_ip,
        )
        return self._create_new_event_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class CreateNewEvent(BaseApi):

    async def acreate_new_event(
        self,
        session_id: str,
        customer_id: str,
        event_source: str,
        event_type: str,
        event_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        event_ts: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_ip: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> EventPydantic:
        raw_response = await self.raw.acreate_new_event(
            session_id=session_id,
            customer_id=customer_id,
            event_source=event_source,
            event_type=event_type,
            event_info=event_info,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            event_ts=event_ts,
            device_id=device_id,
            client_ip=client_ip,
            **kwargs,
        )
        if validate:
            return EventPydantic(**raw_response.body)
        return api_client.construct_model_instance(EventPydantic, raw_response.body)
    
    
    def create_new_event(
        self,
        session_id: str,
        customer_id: str,
        event_source: str,
        event_type: str,
        event_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        event_ts: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_ip: typing.Optional[str] = None,
        validate: bool = False,
    ) -> EventPydantic:
        raw_response = self.raw.create_new_event(
            session_id=session_id,
            customer_id=customer_id,
            event_source=event_source,
            event_type=event_type,
            event_info=event_info,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            event_ts=event_ts,
            device_id=device_id,
            client_ip=client_ip,
        )
        if validate:
            return EventPydantic(**raw_response.body)
        return api_client.construct_model_instance(EventPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        session_id: str,
        customer_id: str,
        event_source: str,
        event_type: str,
        event_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        event_ts: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_ip: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_event_mapped_args(
            session_id=session_id,
            customer_id=customer_id,
            event_source=event_source,
            event_type=event_type,
            event_info=event_info,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            event_ts=event_ts,
            device_id=device_id,
            client_ip=client_ip,
        )
        return await self._acreate_new_event_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        session_id: str,
        customer_id: str,
        event_source: str,
        event_type: str,
        event_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        x_seel_api_key: str,
        x_seel_api_version: str,
        partner: str,
        event_ts: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_ip: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_event_mapped_args(
            session_id=session_id,
            customer_id=customer_id,
            event_source=event_source,
            event_type=event_type,
            event_info=event_info,
            x_seel_api_key=x_seel_api_key,
            x_seel_api_version=x_seel_api_version,
            partner=partner,
            event_ts=event_ts,
            device_id=device_id,
            client_ip=client_ip,
        )
        return self._create_new_event_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

