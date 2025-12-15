#!/usr/bin/env python3
"""Shapes via ABC and duck typing (area/perimeter + shape_info)."""

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
    """Circle defined by its radius."""

    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Return circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width, height):
        """Initialize rectangle dimensions."""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing (no isinstance checks)."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
