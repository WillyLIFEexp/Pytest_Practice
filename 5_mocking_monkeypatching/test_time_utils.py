import pytest
from datetime import datetime
import time_utils

class FixedDateTime(datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(2025, 1, 1, 12, 0, 0)  # fixed time: Jan 1, 2025, 12:00 PM

def test_is_past_deadline(monkeypatch):
    # Patch datetime in your target module (time_utils)
    monkeypatch.setattr(time_utils, "datetime", FixedDateTime)

    deadline = datetime(2024, 12, 31, 23, 59, 59)
    assert time_utils.is_past_deadline(deadline) is True

    future_deadline = datetime(2026, 1, 1, 0, 0, 0)
    assert time_utils.is_past_deadline(future_deadline) is False
