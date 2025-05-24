#Test suite for sample.py functions.

import sample

def test_hello() -> None:
    assert sample.hello() == "Hello, world!"


def test_greet() -> None:
    assert sample.greet("Alice") == "Hello, Alice!"


def test_sum_values() -> None:
    assert sample.sum_values(4, 5) == "Sum is 9"
