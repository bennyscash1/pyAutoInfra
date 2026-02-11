from dataclasses import dataclass

from ApiTest.HttpServices.base_api import BaseDTO


@dataclass
class FormUploadDTO(BaseDTO):
    # Form-data fields for upload
    username: str
    role: str
    file_path: str

