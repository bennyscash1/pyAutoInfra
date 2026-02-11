import pytest

from Infra.BaseData.CommonData import TestLevel
from Infra.BaseData.GetData import loaded_data, VarData
from ApiTest.HttpServices.http_requests import HttpService, HttpServiceOptions
from ApiTest.PostTest.PosJaonRequest.pos_dto import PostPayloadDTO, PostResponseDTO

@TestLevel.level0
def test_post_service():
    svc = HttpService(HttpServiceOptions(base_url=loaded_data[VarData.BaseApiUrl]))
    payload = PostPayloadDTO(userId="10", id=1, myName="John Doe")

    response = svc.post("posts", payload.to_dict(), token="thisisatoken")
    assert response.status_code in (200, 201)

    response_data = response.json()
    assert isinstance(response_data, dict)
    response_dto = PostResponseDTO.from_dict(response_data)

    assert response_dto.userId == "10"

