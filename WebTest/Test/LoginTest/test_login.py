import pytest

# from ApiTest.CommonApiService.api_services import ApiServices
from Infra.BaseData.GetData import loaded_data, VarData
from WebTest.Flows.login_flow import LoginFlow
from WebTest.WebInfra.web_driver_factory import WebDriverFactory


@pytest.mark.webtest
class TestLoginWeb:
    def setup_method(self):
        self.driver = WebDriverFactory(headless=False)
        self.page = self.driver.get_page()
        self.base_url = loaded_data[VarData.WebUrl]
        self.username = loaded_data[VarData.WebUserName]
        self.password = loaded_data[VarData.WebPassword]


    def test_login(self):
        flow = LoginFlow(self.page)
        flow.open_page(True, url=self.base_url)

        #region API Services
        # api = ApiServices()
        # user_id = api.get_user_id(1, "Benny shor")
        #endregion
        flow.do_valid_login(self.username, self.password)
        assert flow.is_home_page_open(), "Home page not opened"
