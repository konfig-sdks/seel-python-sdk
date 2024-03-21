# coding: utf-8

"""
    Seel API

    Seel API

    The version of the OpenAPI document: 1.3.0
    Generated by: https://konfigthis.com
"""

from seel_python_sdk.paths.partner_events.post import CreateNewEvent
from seel_python_sdk.apis.tags.event_api_raw import EventApiRaw


class EventApi(
    CreateNewEvent,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EventApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EventApiRaw(api_client)