"""
USPTO patent API
"""

import requests

from ..sys_utils.log_tools import setup_logger
from ..sys_utils.errors import ExternalApiError

logger = setup_logger(__name__)


def fetch_us_patent_application_from_uspto_api(
    patent_number: str, kind_code: str = "A1"
) -> dict[str, str]:
    """
    Fetches a US patent application from the USPTO API.

    :param patent_number: The patent number to fetch.
    :param kind_code: The kind code of the patent, default is "A1".
    :return: A dictionary containing the patent application details.
    :raises ExternalApiError: If the USPTO API request fails.
    """
    base_url = "https://developer.uspto.gov/ibd-api/v1/application/publications"
    params = {"publicationDocumentIdentifier": f"US{patent_number}{kind_code}"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        patents = response.json()
        return patents
    raise ExternalApiError(
        f"USPTO application request failed with status code {response.status_code}"
    )
