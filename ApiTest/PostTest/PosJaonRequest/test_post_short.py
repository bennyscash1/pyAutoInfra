import pytest

from ApiTest.CommonApiService.api_services import ApiServices
from Infra.BaseData.CommonData import RetryFauilureTest, TestLevel

@RetryFauilureTest()
@TestLevel.level0
def test_post_service():
    api_services = ApiServices()
    userid= api_services.get_user_id(10)
    assert userid == '10'

    

