import sys
from pathlib import Path

# Ensure project root is on path when running/debugging this file directly
ROOT = Path(__file__).resolve().parent.parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest
from ApiTest.CommonApiService.api_services import ApiServices
from Infra.BaseData.CommonData import RetryFauilureTest, TestLevel

@RetryFauilureTest()
@TestLevel.level0
def test_post_service():
    api_services = ApiServices()
    userid= api_services.get_user_id(10)
    assert userid == '10'

    

