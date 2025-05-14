# test_fetcher.py
import pytest
from unittest.mock import Mock
from fetcher import fetch_data

@pytest.fixture
def mock_requests_get(monkeypatch):
    mock_response = Mock()
    mock_response.json.return_value = {"data": "fake response"}

    def mock_get(*args, **kwargs):
        return mock_response

    monkeypatch.setattr('requests.get', mock_get)

def test_fetch_data(mock_requests_get):
    result = fetch_data("http://fakeurl.com")
    assert result == {"data": "fake response"}
