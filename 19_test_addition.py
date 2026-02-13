import addition
import pytest

# to run tests: python3 -m pytest test_addition.py
# to run a specific test in the file: python3 -m pytest test_addition.py::test_add

def test_add():
    assert addition.add(4, 5) == 9


def test_sub():
    assert addition.sub(4, 5) == -1

