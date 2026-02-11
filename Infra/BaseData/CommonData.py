from enum import Enum

import pytest


class EnumData(Enum):
    ApiEmail = "ApiEmail"
    ApiPassword = "ApiPassword"
    BaseApiUrl = "BaseApiUrl"
    WebUrl = "WebUrl"
    WebUserName = "WebUserName"
    WebPassword = "WebPassword"
    ContactName = "ContactName"
    ContactNumber = "ContactNumber"
    AppPackage = "appPackage"
    AppActivity = "appActivity"
    Environment = "Environment"


class TestLevel:
    level0 = pytest.mark.level0
    level1 = pytest.mark.level1