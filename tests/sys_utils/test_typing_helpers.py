"""
Unit tests for for typing_helpers.py ([TODO] minimal so far)
"""

from typing import Any, Callable

from degel_python_utils import ComparisonFunction


def example_comparison_func(a: Any, b: Any) -> bool:
    """Toy comparison function"""
    return a == b


def test_comparison_function_type_alias() -> None:
    """Test comparison function"""
    example_func: ComparisonFunction = example_comparison_func
    assert isinstance(example_func, Callable)
    assert example_func.__annotations__["a"] == Any
    assert example_func.__annotations__["b"] == Any
    assert example_func.__annotations__["return"] == bool
