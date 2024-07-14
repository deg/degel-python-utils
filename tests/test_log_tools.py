import logging
from degel_python_utils import setup_logger


def test_setup_logger() -> None:
    setup_logger("my_app", logging.DEBUG)
    logger = logging.getLogger("my_app")
    assert logger.isEnabledFor(logging.DEBUG)
    setup_logger("my_app", logging.INFO)
    assert logger.isEnabledFor(logging.INFO)
    assert not logger.isEnabledFor(logging.DEBUG)
