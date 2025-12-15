#!/usr/bin/python3
"""Defines the BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
