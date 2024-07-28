"""Degel Python Utilities is a collection of useful Python helper functions that I've
used in various projects.

For now, it is still scattershot, but I expect it to grow and self-organize as I merge
in more projects.

"""

from .data.read_table import read_data_table
from .data.write_table import write_data_table
from .ip import parse_extended_patent_number
from .ip.uspto import (
    fetch_us_patent_application_from_uspto_api,
    fetch_us_patent_grant_from_uspto_api,
)
from .sys_utils.env import appEnv
from .sys_utils.errors import DegelUtilsError, ExternalApiError, UnsupportedError
from .sys_utils.file_system import append_to_filename
from .sys_utils.log_tools import setup_logger
from .sys_utils.typing_helpers import ComparisonFunction


__all__ = [
    "append_to_filename",
    "appEnv",
    "ComparisonFunction",
    "DegelUtilsError",
    "ExternalApiError",
    "fetch_us_patent_application_from_uspto_api",
    "fetch_us_patent_grant_from_uspto_api",
    "parse_extended_patent_number",
    "read_data_table",
    "setup_logger",
    "UnsupportedError",
    "write_data_table",
]
