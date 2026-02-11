from dataclasses import dataclass
from ApiTest.HttpServices.base_api import BaseDTO


class PageOutputDTO:
    def __init__(self, page):
        self.result = {"userId": page}
    def to_json(self):
        return self.result


@dataclass
class GetResponseDTO(BaseDTO):
    userId: int
    id: int
