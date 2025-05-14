import pytest

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def test_divide_exception():
    with pytest.raises(ValueError):
        divide(10, 0)

def validate_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    return age

def test_validate_age():
    with pytest.raises(ValueError):
        validate_age(-20)
