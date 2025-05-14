import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4]

def test_length(sample_list):
    assert len(sample_list) == 4

def test_sum(sample_list):
    assert sum(sample_list) == 10

@pytest.fixture
def sample_dict():
    return {'name':"default_name", "password": "default_password"}

def test_login(sample_dict):
    assert sample_dict.get('name') == "default_name"
    assert sample_dict.get('password') == "default_password"
