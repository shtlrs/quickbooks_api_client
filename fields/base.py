from abc import ABC
from typing import Any, Optional


class BaseField(ABC):

    val: Optional[Any] = None
    query_param_name: str

    def __init__(self, query_param_name: str,):
        self.query_param_name = query_param_name

    def __set_name__(self, owner, name):
        self.attr = "_" + name

    def __set__(self, obj, value):
        setattr(obj, self.attr, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self.query_param_name
        return getattr(instance, self.attr)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.attr})"
