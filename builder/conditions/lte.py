from typing import Union
from . import abstract


class LessThanOrEqual(abstract.AbstractCondition):

    def __init__(self, attribute: str, target: Union[str, int]):
        super(LessThanOrEqual, self).__init__(attribute)
        self.target = target

    def stringify(self):
        return f"{self.attribute} <= '{self.target}'"
