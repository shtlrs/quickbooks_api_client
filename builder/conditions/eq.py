from typing import Union
from builder.utils import escape_characters
from builder.conditions.abstract import AbstractCondition


class Equals(AbstractCondition):
    def __init__(self, attribute: str, target: Union[str, int]):
        super(Equals, self).__init__(attribute)
        self.target = target

    def stringify(self):
        return f"{self.attribute} = '{escape_characters(self.target)}'"
