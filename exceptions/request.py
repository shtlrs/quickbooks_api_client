from typing import Any
from enums import HttpVerb
from .base import BaseExc


class RequestError(BaseExc):
    def __init__(
        self, text: str, status_code: int, http_verb: HttpVerb, extra_data: Any = None
    ):
        self.message = (
            f"Http verb {http_verb.value}\n"
            f"Response text: {text}\n"
            f"Status code: {status_code}\n"
            f"Data: {extra_data}"
        )
