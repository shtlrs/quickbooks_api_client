from abc import ABC, abstractmethod
from typing import Iterable, Union


class AbstractCondition(ABC):
    """
    A base abstract class for all conditions
    """

    attribute: str
    target: Union[Iterable, str, int]

    def __init__(self, attribute: str):
        self.attribute = attribute

    @abstractmethod
    def stringify(self) -> str:
        """
        Turns the condition into a string
        """
