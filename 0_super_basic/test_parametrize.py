import pytest

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (5, 5, 10)
])
def test_addition_parametrize(x, y, expected):
    assert x + y == expected
