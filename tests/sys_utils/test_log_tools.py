"""
Unit tests for for log_tools.py ([TODO] minimal so far)
"""

import logging

from degel_python_utils import setup_logger


def test_setup_logger() -> None:
    """Test setup_logger enables logging and levels"""
    logger = setup_logger("my_app", logging.DEBUG)
    assert logger.isEnabledFor(logger.DEBUG)

    logger.setLevel(logger.INFO)
    assert logger.isEnabledFor(logger.INFO)
    assert not logger.isEnabledFor(logger.DEBUG)

    # Ensure custom levels exist
    assert hasattr(logger, "major")
    assert hasattr(logger, "minor")

    setup_logger("my_app", logger.MAJOR)
    assert logger.isEnabledFor(logger.MAJOR)
    assert not logger.isEnabledFor(logger.INFO)
