# test_ecom_utils.py
import pytest
from ecom_utils import apply_discount

def test_apply_discount():
    assert apply_discount(100, 0.2) == 80
    assert apply_discount(50, 0) == 50
    assert apply_discount(50, 1) == 0

def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(100, 1.5)
