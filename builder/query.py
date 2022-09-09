from __future__ import annotations
from typing import List
from builder.conditions.abstract import AbstractCondition
from builder.utils import clean_up


class Query:
    """
    The query object that will be used upon requesting resources from Quickbooks' API.
    """
    fields_to_select: str
    target_table: str
    conditions: List[AbstractCondition]
    query: str
    order_by: str
    ordering_type: str
    max_results: int
    start_position: int

    def __init__(self):
        self.conditions = []
        self.ordering_type = ''
        self.order_by = ''
        self.max_results = -1
        self.start_position = -1

    def SELECT(self, *fields):
        self.fields_to_select = ",".join(fields)
        return self

    def FROM(self, target_table: str):
        self.target_table = target_table
        return self

    def WHERE(self, condition: AbstractCondition):
        self.conditions.append(condition)
        return self

    def AND(self, condition: AbstractCondition):
        self.conditions.append(condition)
        return self

    def ORDERBY(self, column):
        self.order_by = column
        return self

    def ASC(self):
        self.ordering_type = "ASC "
        return self

    def DESC(self):
        self.ordering_type = "DESC "
        return self

    def MAX_RESULTS(self, max_results: int):
        self.max_results = max_results
        return self

    def START_POSITION(self, start_position: int):
        self.start_position = start_position
        return self

    def stringify(self):
        self.query = f"SELECT {self.fields_to_select} " \
                f"FROM {self.target_table} " \
                f"{self.compose_conditions()} "

        if self.order_by:
            self.query += f"ORDERBY {self.order_by} "

        if self.ordering_type:
            self.query += self.ordering_type

        if self.max_results > -1:
            self.query = self.query + f"MAXRESULTS {self.max_results} "

        if self.start_position > -1:
            self.query = self.query + f"STARTPOSITION {self.start_position}"

        self.query = clean_up(self.query)
        return self.query

    def compose_conditions(self):
        query = f""

        if not self.conditions:
            return ""

        query += f"WHERE {self.conditions[0].stringify()} "

        for condition in self.conditions[1:]:
            query += f"AND {condition.stringify()} "

        return query
