from __future__ import annotations
from abc import ABC, abstractmethod


class BaseModel(ABC):

    ALL = "*"
    table_name: str

    @abstractmethod
    def from_dict(self, json: dict) -> BaseModel:
        ...
