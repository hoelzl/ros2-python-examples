from math import isclose

from external_libraries.calculator import Calculator
import pytest


@pytest.fixture
def c():
    return Calculator()


def test_add(c):
    assert c.add(3, 5) == 8
    assert c.last_result == 8


def test_sub(c):
    assert c.sub(5, 3) == 2
    assert c.last_result == 2


def test_mul(c):
    assert c.mul(3, 4) == 12
    assert c.last_result == 12


def test_div(c):
    assert isclose(c.div(5, 2), 2.5)
    assert isclose(c.last_result, 2.5)


def test_pow(c):
    assert c.pow(2, 8) == 256
    assert c.last_result == 256


def test_store(c):
    c.pow(2, 8)
    c.store("my-result")
    # Overwrite the `c.last_result` attribute to make sure we are not using this
    # by chance.
    c.add(1, 2)

    assert c.add("my-result", 0) == 256
    assert c.add(0, "my-result") == 256


def test_unset_memory_reference(c):
    assert c.add("non-existing-var", 0) == 0
