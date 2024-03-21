# coding: utf-8

"""
    Seel API

    Seel API

    The version of the OpenAPI document: 1.3.0
    Generated by: https://konfigthis.com
"""

from seel_python_sdk.paths.partner_contracts_contract_id.get import GetById
from seel_python_sdk.paths.partner_contracts.get import ListContracts
from seel_python_sdk.apis.tags.contract_api_raw import ContractApiRaw


class ContractApi(
    GetById,
    ListContracts,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ContractApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ContractApiRaw(api_client)
