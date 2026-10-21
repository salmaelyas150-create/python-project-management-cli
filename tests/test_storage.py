
"""Test JSON storage functions."""

import json
import pytest

from utils import storage


def test_save_and_load_data(tmp_path, monkeypatch):
    """Check that records can be saved and loaded."""
    test_file = tmp_path / "users.json"
    monkeypatch.setitem(storage.FILES, "users", test_file)

    records = [
        {"id": "user-1", "name": "Alex", "email": "alex@example.com"}
    ]

    storage.save_data("users", records)
    assert storage.load_data("users") == records


def test_load_missing_file_creates_empty_list(tmp_path, monkeypatch):
    """Check that a missing file produces an empty collection."""
    test_file = tmp_path / "projects.json"
    monkeypatch.setitem(storage.FILES, "projects", test_file)

    assert storage.load_data("projects") == []
    assert json.loads(test_file.read_text(encoding="utf-8")) == []


def test_load_malformed_json_raises_error(tmp_path, monkeypatch):
    """Check that malformed JSON raises a clear error."""
    test_file = tmp_path / "tasks.json"
    test_file.write_text("{invalid json", encoding="utf-8")
    monkeypatch.setitem(storage.FILES, "tasks", test_file)

    with pytest.raises(ValueError, match="invalid JSON"):
        storage.load_data("tasks")


def test_unknown_collection_is_rejected():
    """Check that unknown collections are rejected."""
    with pytest.raises(ValueError, match="Unknown data collection"):
        storage.load_data("unknown")
