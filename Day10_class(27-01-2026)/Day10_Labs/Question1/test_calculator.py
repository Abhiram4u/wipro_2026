import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5
    assert 2 + 3 == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
