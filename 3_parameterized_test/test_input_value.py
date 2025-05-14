import pytest

def square(x):
    return x * x

@pytest.mark.parametrize("input, expected", [
    (2, 4),
    (-3, 9),
    (0, 0),
])
def test_square(input, expected):
    assert square(input) == expected
