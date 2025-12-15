#!/usr/bin/python3
"""Defines a custom list class with a sorted display helper."""


class MyList(list):
    """A list subclass that can print its elements in ascending order."""

    def print_sorted(self):
        """Print a sorted version of the list without modifying it."""
        print(sorted(self))
