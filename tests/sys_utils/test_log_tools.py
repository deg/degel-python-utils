"""
Unit tests for for log_tools.py ([TODO] minimal so far)
"""

import logging

from degel_python_utils import setup_logger


def test_setup_logger() -> None:
    """Test setup_logger enables logging and levels"""
    setup_logger("my_app", logging.DEBUG)
    logger = logging.getLogger("my_app")
    assert logger.isEnabledFor(logging.DEBUG)
    setup_logger("my_app", logging.INFO)
    assert logger.isEnabledFor(logging.INFO)
    assert not logger.isEnabledFor(logging.DEBUG)
