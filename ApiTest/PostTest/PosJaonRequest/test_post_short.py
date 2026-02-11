import pytest
import requests
import sys
import os

from ApiTest.CommonApiService.api_services import ApiServices
from Infra.BaseData.CommonData import TestLevel
from Infra.BaseData.GetData import loaded_data, VarData
from ApiTest.HttpServices.http_requests import HttpService, HttpServiceOptions
from ApiTest.PostTest.PosJaonRequest.pos_dto import PostPayloadDTO, PostResponseDTO
@TestLevel.level0
def test_post_service():
    api_services = ApiServices()
    userid= api_services.get_user_id(10)
    assert userid == '10'

    

