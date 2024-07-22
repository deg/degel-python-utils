"""
USPTO patent API
"""

import requests


from ..sys_utils.errors import ExternalApiError
from ..sys_utils.log_tools import setup_logger

logger = setup_logger(__name__)


def fetch_us_patent_application_from_uspto_api(
    application_number: str, kind_code: str = "A1"
) -> dict[str, str]:
    """
    Fetches a US patent application from the USPTO API.

    :param application_number: The patent number to fetch.
    :param kind_code: The kind code of the patent, default is "A1".
    :return: A dictionary containing the patent application details.
    :raises ExternalApiError: If the USPTO API request fails.
    """
    params = {"publicationDocumentIdentifier": f"US{application_number}{kind_code}"}
    return fetch_from_uspto_api("publications", params)


def fetch_us_patent_grant_from_uspto_api(patent_number: str) -> dict[str, str]:
    """
    Fetches a granted US patent from the USPTO API.

    :param patent_number: The patent number to fetch.
    :return: A dictionary containing the patent grant details.
    :raises ExternalApiError: If the USPTO API request fails.
    """
    params = {"patentNumber": patent_number}
    return fetch_from_uspto_api("grants", params)


def fetch_from_uspto_api(endpoint: str, params: dict) -> dict[str, str]:
    """
    Helper function to fetch data from the USPTO API.

    :param endpoint: The API endpoint to call.
    :param params: The parameters to pass to the API call.
    :return: A dictionary containing the response data.
    :raises ExternalApiError: If the USPTO API request fails.
    """
    base_url = f"https://developer.uspto.gov/ibd-api/v1/application/{endpoint}"
    response = requests.get(base_url, params=params, timeout=60)
    if response.status_code == 200:
        return response.json()
    raise ExternalApiError(
        f"USPTO API request to {base_url} failed with status code {response.status_code}"
    )
