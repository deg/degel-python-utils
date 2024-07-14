import requests

from ..sys_utils.log_tools import setup_logger

logger = setup_logger(__name__)


def fetch_us_patent_application_from_uspto_api(
    patent_number: str, kind_code: str = "A1"
) -> dict[str, str]:
    base_url = "https://developer.uspto.gov/ibd-api/v1/application/publications"
    params = {"publicationDocumentIdentifier": f"US{patent_number}{kind_code}"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        patents = response.json()
        return patents
    return {}
