from abc import ABC, abstractmethod

from builder.query import Query
from enums.resource import Resource


class AbstractBaseClient(ABC):
    """
    A class to represent the interface that the api client should implement

    Attributes
    ----------
    base_url: str
        The base url to use in all HTTP requests
    base_headers: dict
        The base headers to use in all HTTP requests
        This is mostly used for auth purposes
    __minor_version__: int
        The API's minor version to use
    """

    base_url: str
    base_headers: dict
    __minor_version__: int

    @abstractmethod
    def get(self, resource_id: int, resource_type: Resource):
        """
        Sends out an HTTP GET request to fetch details of a particular resource

        Parameters
        ----------
            resource_id : int
                id of the resource
            resource_type : Resource
                type of the resource, e.g. an invoice, bill, etc.
        """

    @abstractmethod
    def delete(self, resource_id: str, sync_token: str, resource_type: Resource):
        """
        Sends out an HTTP DELETE request to delete a particular resource

        Parameters
        ----------
            resource_id : int
                id of the resource
            sync_token: str
                the resource's current sync token
            resource_type : Resource
                type of the resource, e.g. an invoice, bill, etc.
        """

    @abstractmethod
    def query(self, query: Query, bring_all=False):
        """
        Sends out an HTTP GET request to search for a particular resource
        depending on the provided query

        Parameters
        ----------
            query : Query
                The query object that will be used for the resource lookup
            bring_all : int
                A boolean that indicates whether to fetch all pages or just the default first page
        """
