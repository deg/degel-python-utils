from typing import Self


class DegelUtilsError(Exception):
    """
    Base exception class for all degel_python_utils errors.
    """

    def __init__(self: Self, message: str = "An error occurred in degel_utils") -> None:
        super().__init__(message)


class ExternalApiError(DegelUtilsError):
    """
    Exception raised by calls to external APIs.
    """

    def __init__(
        self: Self, message: str = "An API error occurred in degel_utils"
    ) -> None:
        super().__init__(message)
