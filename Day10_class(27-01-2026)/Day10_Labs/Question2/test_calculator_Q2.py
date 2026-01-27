# test_calculator_Q2.py

import pytest
from calculator_Q2 import add, divide

def setup_module(module):
    print("\nSetup before module")

def teardown_module(module):
    print("\nTeardown after module")

def setup_function(function):
    print("\nSetup before function")

def teardown_function(function):
    print("\nTeardown after function")

def test_add_using_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

