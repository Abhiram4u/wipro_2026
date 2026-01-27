from calculator_Q2 import subtract

def test_subtract_using_fixture(sample_numbers):
    a, b = sample_numbers
    assert a - b == 5
