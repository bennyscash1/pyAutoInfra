import requests
import sys
import os

from ApiTest.GetTests.get_dto import GetResponseDTO
from Infra.BaseData.GetData import VarData, loaded_data
from ApiTest.HttpServices.http_requests import (
    HttpService,
    HttpServiceOptions,
    HttpCallOptionsSimple
)

def test_get_service():
    svc = HttpService(HttpServiceOptions(base_url=loaded_data[VarData.BaseApiUrl]))

    data = svc.call_without_body(HttpCallOptionsSimple(
        path="posts/5", token="thisisatoken"))

    response_dto = GetResponseDTO.from_dict(data)
    assert response_dto.userId == 1
    assert response_dto.id == 5




