import pytest
from ApiTest.CommonApiService.api_services import ApiServices

@pytest.mark.parametrize(
    "id_param, expected_result, description",
    [
        (10, True, "valid input"),
        (5, False, "invalid test param"),
    ]
)
def test_post_tdd(id_param, expected_result, description):
    api_services = ApiServices()
    user_id = api_services.get_user_id(id_param)

    actual_result = (user_id == str(id_param))

    assert actual_result == expected_result, \
        f"{description} | Expected {expected_result} but got {actual_result}"
