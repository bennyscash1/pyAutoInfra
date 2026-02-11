
from ApiTest.HttpServices.http_requests import HttpService, HttpServiceOptions
from ApiTest.PostTest.PosJaonRequest.pos_dto import PostPayloadDTO, PostResponseDTO
from Infra.BaseData.GetData import VarData, loaded_data
from Infra.CommonHelpers import HelperDataGenerator

class ApiServices:
    def __init__(self):
        self.svc = HttpService(HttpServiceOptions(base_url=loaded_data[VarData.BaseApiUrl]))
    
    def get_user_id(self, this_id: int, user_name: str = HelperDataGenerator.generate_full_name()):
        payload = PostPayloadDTO(userId="10", id=this_id, myName=user_name)
        response = self.svc.post("posts", payload.to_dict(), token="thisisatoken")
        assert response.status_code in (200, 201)
        response_dto = PostResponseDTO.from_dict(response.json())
        user_id = response_dto.userId
        return user_id
