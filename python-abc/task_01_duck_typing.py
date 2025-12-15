#!/usr/bin/env python3
"""Shapes module using ABC and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Return the circle's area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the circle's perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle's perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape (duck typing)."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
