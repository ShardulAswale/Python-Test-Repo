"""Test suite for the `sample.py` module."""

import sample


def test_hello() -> None:
    """Ensure `hello()` returns the default greeting."""
    assert sample.hello() == "Hello, world!"


def test_greet() -> None:
    """Ensure `greet(name)` returns a personalized greeting."""
    assert sample.greet("Alice") == "Hello, Alice!"


def test_sum_values() -> None:
    """Ensure `sum_values(a, b)` returns the correctly formatted sum."""
    assert sample.sum_values(4, 5) == "Sum is 9"
