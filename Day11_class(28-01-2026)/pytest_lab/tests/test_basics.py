import pytest
import sys

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 3 == 1, "Subtraction result is incorrect"

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment():
    assert True

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True

@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert 2 * 2 == 5
