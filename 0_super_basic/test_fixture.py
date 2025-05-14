import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_fixture_sum(sample_data):
    assert sum(sample_data) == 6
