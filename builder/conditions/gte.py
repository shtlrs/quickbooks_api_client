from typing import Union
from builder.conditions.abstract import AbstractCondition


class GreaterThanOrEqual(AbstractCondition):

    def __init__(self, attribute: str, target: Union[str, int]):
        super(GreaterThanOrEqual, self).__init__(attribute)
        self.target = target

    def stringify(self):
        return f"{self.attribute} >= '{self.target}'"
