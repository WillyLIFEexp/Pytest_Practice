from math_util import multiply, is_even

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-1, 8) == -8

def test_is_even():
    assert is_even(5) == False 
    assert is_even(6) == True