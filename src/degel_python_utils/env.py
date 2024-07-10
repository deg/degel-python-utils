from datetime import datetime
import os
import sys

from .log_tools import setup_logger

logger = setup_logger(__name__)
# pylint: disable=logging-format-interpolation


class AppEnv:
    """
    Manages environment variables in a controlled way.
    """

    def __init__(self):
        """Initialize state"""
        self.registered_vars = []

    def register_env_var(self, name: str, private: bool = False):
        """
        Register a variable, which we expect to find in the OS environment at runtime.

        [TODO]
        - We may want an option to name the variable different from the OS env name.

        Args:
            name (str): Variable name (both in the OS env and the program variable).
            private (bool, optional): Whether to obscure the value in logs.
        """
        value = os.environ.get(name)
        setattr(sys.modules[__name__], name, value)
        self.registered_vars.append({"name": name, "private": private})

    def show_env(self):
        """
        Show the program state and environment variables. Typically called at startup.
        Private variables will have their values obscured.
        """
        logger.info("================")
        logger.info(
            f"{__name__} environment at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        for var in self.registered_vars:
            var_name = var["name"]
            var_value = globals().get(var_name, None)
            if var["private"]:
                var_value = obscure_private(var_value, 4)
            logger.info(f"{var_name}: {var_value}")
        logger.info("================")

    def get_env_var(self, name: str) -> str | None:
        """
        Get the value of a registered environment variable.

        Args:
            name (str): The name of the environment variable.

        Returns:
            str | None: The value of the environment variable.
        """
        return globals().get(name, None)


def obscure_private(val: str, len_to_show: int) -> str:
    """
    Obscures part of a string, useful for hiding sensitive information in logs.

    Args:
        val (str): The value to obscure.
        len_to_show (int): The number of characters to show at the beginning and end
        of the string.
    Returns:
        str: The obscured string.
    """
    return f"{val[:len_to_show]}...{val[-len_to_show:]}" if val else ""
