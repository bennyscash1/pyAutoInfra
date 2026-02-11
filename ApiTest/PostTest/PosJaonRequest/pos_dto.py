from dataclasses import dataclass, asdict, fields
from typing import Any, Dict, Type, TypeVar

from ApiTest.HttpServices.base_api import BaseDTO


@dataclass
class PostPayloadDTO(BaseDTO):
    userId: str
    id: int
    myName: str


@dataclass
class PostResponseDTO(BaseDTO):
    userId: str
    id: int
    myName: str


