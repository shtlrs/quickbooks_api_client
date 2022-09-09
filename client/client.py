from urllib.parse import urljoin

import requests

from builder import Query
from enums import HttpVerb
from . import abstract
from enums.resource import Resource
from config import BASE_URL, MINOR_VERSION
from exceptions import RequestError


class QuickBooksApiClient(abstract.AbstractBaseClient):
    """
    An api client that interfaces with Quickbooks
    """

    access_token: str
    base_url: str = BASE_URL
    headers: dict
    __minor_version__ = MINOR_VERSION

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Host": "quickbooks.api.intuit.com",
        }

    def get(self, resource_id: str, resource: Resource) -> dict:
        """
        Returns the data of a particular resource
        """
        path = f"{resource.value}/{resource_id}"

        url = urljoin(self.base_url, path)

        query_parameters = {"minorversion": self.__minor_version__}

        response = requests.get(url=url, params=query_parameters, headers=self.headers)

        if response.status_code != 200:
            raise RequestError(
                resource_id=resource_id,
                resource=resource,
                http_verb=HttpVerb.GET,
                text=response.text,
                extra_data={"path": path},
                status_code=response.status_code,
            )

        return response.json().get(resource.value.capitalize())

    def delete(self, resource_id: str, sync_token: str, resource: Resource):
        """
        Deletes the provided resource
        """
        url = urljoin(self.base_url, resource.value)

        query_parameters = {"operation": "delete"}

        request_body = {"Id": resource_id, "SyncToken": sync_token}

        response = requests.post(
            url=url, params=query_parameters, json=request_body, headers=self.headers
        )

        return response

    def query(self, query: Query, bring_all=False):
        """
        A method that queries quickbooks for a particular resource based on the query param
        ...

        Attributes
        ----------
        query: Query
            the query that we'll be sending to QBO
        bring_all: bool
            a boolean that indicates whether we should be
            considering bringing all the resources or just the default page
        """

        entities = []

        url = urljoin(self.base_url, "query")

        if bring_all:
            query.MAX_RESULTS(1000).START_POSITION(1)

        params = {"minorversion": self.__minor_version__, "query": query.stringify()}

        response = requests.get(url=url, params=params, headers=self.headers)

        if response.status_code != 200:
            raise RequestError(
                text=response.text,
                status_code=response.status_code,
                http_verb=HttpVerb.GET,
                extra_data=query,
            )

        query_response = response.json().get("QueryResponse", {})

        entities.extend(query_response.get(query.target_table.capitalize(), []))

        if not bring_all:

            return entities

        while query_response.get("totalCount", 0) == query_response.get("maxResults", 0):

            total_count = query_response.get("totalCount", 0)
            new_start_position = query.start_position + total_count
            query.START_POSITION(new_start_position)
            params = {"minorversion": self.__minor_version__, "query": query.stringify()}

            response = requests.get(url=url, params=params, headers=self.headers)

            query_response = response.json().get("QueryResponse", {})

            entities.extend(query_response.get(query.target_table.capitalize(), []))

            max_results = query_response.get("maxResults", 0)

            if max_results < 1000:
                break

        return entities
