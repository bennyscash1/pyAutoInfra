import json
import os
from enum import Enum
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class VarData(Enum):
    ApiEmail = ("API", "Email")
    ApiPassword = ("API", "Password")
    BaseApiUrl = ("API", "BaseApiUrl")
    WebUrl = ("WebUi", "WebUrl")
    WebUserName = ("WebUi", "WebUserName")
    WebPassword = ("WebUi", "WebPassword")
    ContactName = ("Mobile", "ContactName")
    ContactNumber = ("Mobile", "ContactNumber")
    AppPackage = ("Mobile", "appPackage")
    AppActivity = ("Mobile", "appActivity")
    Environment = ("Common", "Enviorment")


env = os.getenv("ENV", "dev")
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, f'jsonData.{env}.json')
with open(file_path, 'r') as file:
    data = json.load(file)

loaded_data = {key: data[key.value[0]][key.value[1]] for key in VarData}

# api init

def get_headers(include_token=False, bearer_token=None):
    headers = {
        'Content-Type': 'application/json'
    }
    if include_token and bearer_token:
        headers['Authorization'] = f'Bearer {bearer_token}'
    return headers
# Now you can use the URL value in your Python code
