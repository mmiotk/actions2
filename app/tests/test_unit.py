import pytest
from calc import add, discount


def test_add():
    assert add(2, 3) == 5


def test_discount_half():
    assert discount(100, 50) == 50.0


def test_discount_invalid():
    with pytest.raises(ValueError):
        discount(100, 150)
