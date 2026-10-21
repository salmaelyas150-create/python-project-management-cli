
"""Provide JSON storage functions for the project management CLI."""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

FILES = {
    "users": DATA_DIR / "users.json",
    "projects": DATA_DIR / "projects.json",
    "tasks": DATA_DIR / "tasks.json",
}


def load_data(entity):
    """Load a collection of records from its JSON file."""
    if entity not in FILES:
        raise ValueError(f"Unknown data collection: {entity}")

    file_path = FILES[entity]
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        save_data(entity, [])
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError(
                f"{file_path.name} must contain a JSON list."
            )

        return data

    except json.JSONDecodeError as error:
        raise ValueError(
            f"{file_path.name} contains invalid JSON. "
            "Please repair the file before continuing."
        ) from error


def save_data(entity, records):
    """Save a collection of records to its JSON file."""
    if entity not in FILES:
        raise ValueError(f"Unknown data collection: {entity}")

    if not isinstance(records, list):
        raise ValueError("Records must be provided as a list.")

    file_path = FILES[entity]
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
        file.write("\n")
