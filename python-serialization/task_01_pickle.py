#!/usr/bin/env python3
"""Serialize and deserialize a custom object using the pickle module."""


import pickle


class CustomObject:
    """A simple custom class that supports pickling to/from a file."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to `filename` using pickle.

        Returns:
            None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None
        return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return an instance from `filename` using pickle.

        Returns:
            CustomObject instance on success, otherwise None.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
        except (OSError, EOFError, pickle.UnpicklingError, AttributeError):
            return None
        return None
