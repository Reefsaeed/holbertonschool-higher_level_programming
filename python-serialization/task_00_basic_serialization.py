#!/usr/bin/env python3
"""Basic JSON serialization/deserialization helpers for dictionaries."""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to `filename`."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON from `filename` and return it as a Python dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
