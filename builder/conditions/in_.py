from typing import Iterable, Tuple
from builder import utils
from . import abstract


class In(abstract.AbstractCondition):
    """
    Implementation of the "IN" condition
    """

    target: Tuple

    def __init__(self, attribute: str, target: Iterable):
        super(In, self).__init__(attribute)
        aux_target = []
        for element in target:
            aux_target.append(utils.escape_characters(element))

        self.target = tuple(aux_target)

    def stringify(self):
        return f"{self.attribute} in {self.target}".lower()
