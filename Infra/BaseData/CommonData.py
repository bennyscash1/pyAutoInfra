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

class RetryFauilureTest:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries
    
    def __call__(self, func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(self.max_retries):
                print(f"Attempt tesst failure {attempt + 1}/{self.max_retries}")
                try:
                    return func(*args, **kwargs)
                except AssertionError:
                    if attempt == self.max_retries - 1:
                      #  print(f"Test failed after {self.max_retries} attempts")
                        raise
        return wrapper